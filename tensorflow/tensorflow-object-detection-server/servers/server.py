#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import shutil
import uuid

from flask import Flask, request, make_response, Response, redirect, send_file

import numpy as np
import os
import tarfile
import tensorflow as tf

from PIL import Image

from object_detection.utils import label_map_util

from object_detection.utils import visualization_utils as vis_util


class ObjectDetetion(object):
    # What model to download.
    MODEL_NAME = 'faster_rcnn_nas_coco_2017_11_08'
    MODEL_FILE = '/root/models/faster_rcnn_nas_coco_2017_11_08.tar.gz'
    DOWNLOAD_BASE = 'http://download.tensorflow.org/models/object_detection/'

    # Path to frozen detection graph. This is the actual model that is used for the object detection.
    PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'

    # List of the strings that is used to add correct label for each box.
    PATH_TO_LABELS = os.path.join('/root/servers/data', 'mscoco_label_map.pbtxt')

    NUM_CLASSES = 90

    def __init__(self):
        tar_file = tarfile.open(self.MODEL_FILE)
        for file in tar_file.getmembers():
            file_name = os.path.basename(file.name)
            if 'frozen_inference_graph.pb' in file_name:
                tar_file.extract(file, os.getcwd())

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

    @staticmethod
    def load_image_into_numpy_array(image):
        (im_width, im_height) = image.size
        return np.array(image.getdata()).reshape(
            (im_height, im_width, 3)).astype(np.uint8)

    def api(self, image):
        detection_graph = self.detection_graph
        with detection_graph.as_default():
            with tf.Session(graph=detection_graph) as sess:
                # Definite input and output Tensors for detection_graph
                image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
                # Each box represents a part of the image where a particular object was detected.
                detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
                # Each score represent how level of confidence for each of the objects.
                # Score is shown on the result image, together with the class label.
                detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
                detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
                num_detections = detection_graph.get_tensor_by_name('num_detections:0')

                # the array based representation of the image will be used later in order to prepare the
                # result image with boxes and labels on it.
                image_np = self.load_image_into_numpy_array(image)
                # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
                image_np_expanded = np.expand_dims(image_np, axis=0)
                # Actual detection.
                (boxes, scores, classes, num) = sess.run(
                    [detection_boxes, detection_scores, detection_classes, num_detections],
                    feed_dict={image_tensor: image_np_expanded})
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


def create_guid():
    return str(uuid.uuid1()).lower()


def get_md5(string):
    import hashlib
    hash_md5 = hashlib.md5(string.encode('utf-8'))
    return hash_md5.hexdigest()
    

# 实例化Flask服务器
app = Flask(__name__)
manager = None


class UrlToImageFile(object):
    def __init__(self):
        import requests
        self.client = requests

    def save_large_file(self, url, file_name):
        r = self.client.get(url, stream=True)
        if r.status_code == 200:
            with open(file_name, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)

    def save_file(self, url, file_name):
        r = self.client.get(url, stream=True)
        if r.status_code == 200:
            with open(file_name, 'wb') as f:
                f.write(r.content)


def save_image(image_np):
    try:
        _id = get_md5(create_guid())
        image_id_ = "/root/servers/" + _id + ".jpg"
        im = Image.fromarray(image_np)
        im.save(image_id_)
        return send_file(image_id_, mimetype='image/jpeg')
    except Exception as e:
        return str(e), 404
    except:
        return "XXXX", 404


@app.route("/api", methods=["POST", 'GET'])
def search_image():
    url = request.args.get("url") or request.form.get("url")
    if not url:
        response = make_response("OK", 200)
    else:
        try:
            tmp_file_name = create_guid() + ".jpg"
            UrlToImageFile().save_file(url, tmp_file_name)
            image = Image.open(tmp_file_name)
            api = ObjectDetetion()
            image_np = api.api(image)
            return save_image(image_np)
        except Exception as e:
            print(e)
            response = make_response("error {}".format(e), 200)

    return response


################################################################
# server测试
################################################################
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)

