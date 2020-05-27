# docker-compose v3 版本中限制容器资源

本示例， 展示在docker-compose v3 版本下, 如何限制容器资源。

执行：

```
docker-compose down
chmod +x ./start.sh 
./start.sh
```

结果：

```
py-demo_1  | start container
py-demo_1  | memory len: 1000000
py-demo_1  | memory len: 2000000
py-demo_1  | start container
py-demo_1  | memory len: 1000000
py-demo_1  | memory len: 2000000
py-demo_1  | start container
py-demo_1  | memory len: 1000000
py-demo_1  | memory len: 2000000
py-demo_1  | start container
py-demo_1  | memory len: 1000000
py-demo_1  | memory len: 2000000

```

结果表明：docker-compose v3 下, 配合 `docker-compose --compatibility  up` 可以限制容器使用资源.

  