# docker-jieba-service

## 结巴 proto

```
python -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I. jieba_service.proto
```

## 运行

```
chmod +x run.sh
./run.sh
```
