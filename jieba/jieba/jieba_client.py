# coding:utf-8
__author__ = 'rk.feng'

import json
import random
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
    count = 0
    flag = random.randint(5, 20)
    seg_list = None
    with open("/data.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            seg_list = jieba_cut(
                rpc_channel=channel,
                sentence=line,
                use_paddle=False,
                cut_all=True,
            )
            count += 1
            if count % flag == 0:
                print("result is {}".format(seg_list))

    if seg_list:
        print("result is {}".format(seg_list))


if __name__ == '__main__':
    run()
