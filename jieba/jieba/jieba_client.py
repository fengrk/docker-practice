# coding:utf-8
__author__ = 'rk.feng'

import json

import grpc

import jieba_service_pb2
import jieba_service_pb2_grpc


def jieba_cut(rpc_channel, sentence: str, cut_all: bool = False, HMM: bool = True, use_paddle: bool = False) -> [str]:
    """ """
    # 调用 rpc 服务
    stub = jieba_service_pb2_grpc.JiebaServiceStub(rpc_channel)
    response = stub.cut(jieba_service_pb2.CutRequest(
        sentence=sentence,
        use_paddle=use_paddle,
        cut_all=cut_all,
        HMM=HMM
    ))
    return json.loads(response.seg_list)


def run():
    # 连接 rpc 服务器
    channel = grpc.insecure_channel('jieba:10000')

    # 调用 rpc 服务
    seg_list = jieba_cut(
        rpc_channel=channel,
        sentence="今天天气很好",
        use_paddle=False,
        cut_all=True,
    )

    print("jieba client received: {}".format(seg_list))


if __name__ == '__main__':
    run()
