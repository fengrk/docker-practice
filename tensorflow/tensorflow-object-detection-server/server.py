# coding:utf-8

from io import BytesIO

import numpy as np
import requests
import tensorflow as tf
from PIL import Image
from flask import Flask, request, make_response
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util


class ObjectDetetion(object):
    # Path to frozen detection graph. This is the actual model that is used for the object detection.
    PATH_TO_CKPT = '/data/frozen_inference_graph.pb'

    # List of the strings that is used to add correct label for each box.
    PATH_TO_LABELS = '/tensorflow/models/research/object_detection/data/mscoco_label_map.pbtxt'

    NUM_CLASSES = 90

    def __init__(self):
        detection_graph = tf.Graph()
        with detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(self.PATH_TO_CKPT, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')

        label_map = label_map_util.load_labelmap(self.PATH_TO_LABELS)
        categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=self.NUM_CLASSES,
                                                                    use_display_name=True)
        self.category_index = label_map_util.create_category_index(categories)
        self.detection_graph = detection_graph
        self.sess = None

    @staticmethod
    def load_image_into_numpy_array(image):
        (im_width, im_height) = image.size
        return np.array(image.getdata()).reshape(
            (im_height, im_width, 3)).astype(np.uint8)

    def api(self, image):
        if self.sess is None:
            self.sess = tf.Session(graph=self.detection_graph)
            detection_graph = self.detection_graph
            # Definite input and output Tensors for detection_graph
            self.image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
            # Each box represents a part of the image where a particular object was detected.
            self.detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            # Each score represent how level of confidence for each of the objects.
            # Score is shown on the result image, together with the class label.
            self.detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
            self.detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
            self.num_detections = detection_graph.get_tensor_by_name('num_detections:0')

        # the array based representation of the image will be used later in order to prepare the
        # result image with boxes and labels on it.
        image_np = self.load_image_into_numpy_array(image)
        # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
        image_np_expanded = np.expand_dims(image_np, axis=0)
        # Actual detection.
        (boxes, scores, classes, num) = self.sess.run(
            [self.detection_boxes, self.detection_scores, self.detection_classes, self.num_detections],
            feed_dict={self.image_tensor: image_np_expanded})
        # Visualization of the results of a detection.
        vis_util.visualize_boxes_and_labels_on_image_array(
            image_np,
            np.squeeze(boxes),
            np.squeeze(classes).astype(np.int32),
            np.squeeze(scores),
            self.category_index,
            use_normalized_coordinates=True,
            line_thickness=8)

        return image_np


app = Flask(__name__)
api_obj = ObjectDetetion()


@app.route("/", methods=["POST", 'GET'])
def search_image():
    url = request.args.get("url") or request.form.get("url")
    if not url:
        response = make_response("OK", 200)
    else:
        try:
            # load image
            raw_image_response = requests.get(url=url, timeout=10)

            # object detection
            image = Image.open(BytesIO(raw_image_response.content))
            image_np = api_obj.api(image=image)
            new_image_obj = Image.fromarray(image_np)

            # response
            new_image_bytes = BytesIO()
            new_image_obj.save(new_image_bytes, 'JPEG')
            response = make_response(new_image_bytes.getvalue())
            response.headers['Content-Type'] = "image/jpeg"
        except Exception as e:
            print(e)
            response = make_response("error {}".format(e), 200)

    return response


################################################################
# server
################################################################
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
