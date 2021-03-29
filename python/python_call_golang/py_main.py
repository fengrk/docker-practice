# coding:utf-8
__author__ = 'rk.feng'

import ctypes


class GoApi:
    def __init__(self, lib):
        self.lib = lib

    @classmethod
    def from_dll(cls, dll_file: str) -> 'GoApi':
        return cls(ctypes.CDLL(dll_file))

    def go_hello(self, name: str) -> str:
        self.lib.go_hello.restype = ctypes.c_char_p

        return getattr(self.lib, "go_hello")(ctypes.c_char_p(name.encode("utf-8"))).decode("utf-8")

    def go_call_count(self) -> int:
        return getattr(self.lib, "go_call_count")()


if __name__ == '__main__':
    so_file = "./go_api.so"
    go_api = GoApi.from_dll(so_file)
    print(f"call count: {go_api.go_call_count()}")
    print(f"call count: {go_api.go_call_count()}")
    print(f"call count: {go_api.go_hello('python')}")
    print(f"call count: {go_api.go_call_count()}")
    print(f"call count: {go_api.go_hello('golang')}")
    print(f"call count: {go_api.go_call_count()}")
