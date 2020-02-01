# coding:utf-8
__author__ = 'rk.feng'

import json
import time
from concurrent import futures

import grpc
import jieba

import jieba_service_pb2
import jieba_service_pb2_grpc


class JiebaService(jieba_service_pb2_grpc.JiebaServiceServicer):

    def cut(self, request: jieba_service_pb2.CutRequest, context) -> jieba_service_pb2.CutReply:
        seg_list = jieba.lcut(sentence=request.sentence, use_paddle=request.use_paddle, cut_all=request.cut_all, HMM=request.HMM)
        return jieba_service_pb2.CutReply(seg_list=json.dumps([seg for seg in seg_list]))


def serve():
    # 启动 rpc 服务
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    jieba_service_pb2_grpc.add_JiebaServiceServicer_to_server(JiebaService(), server)
    server.add_insecure_port('[::]:10000')
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)  # one day in seconds
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
