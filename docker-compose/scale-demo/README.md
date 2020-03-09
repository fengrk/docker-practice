# docker-compose scale 传参

本示例， 展示在 `docker-compose up --scale` 场景下， 如何向容器传递当前容器序号。

执行：

```
docker-compose down
chmod +x ./scale.sh 
./scale.sh
```

结果：

在 `demo.log` 文件中， 展示如下结果：

```
server-1
server-2
server-3
server-4
server-5
server-6
server-7
server-8
server-9
server-10

```

结果表明：
- 每个容器只会执行一次
- 每个容器可根据 `$HOSTNAME` 获知容器的序号
  