# docker-jieba-service

# 1. 结巴服务

## 1.1 结巴 proto

```
python -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I. jieba_service.proto
```

