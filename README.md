# evescn_hosts_management_tools

> Python 使用的Python 3.6版本

## 主机批量管理工具

- 实现了简单的查询主机信息等命令： ls、 pwd、ifconfig 等
- 实现了批量从主机组中下载文件信息，保存地址统一为：```db``` 目录下
- 实现了从 ```db``` 目录下 批量上传某个文件，到主机组中


## 代码目录结构

```
├─bin # 执行文件目录
│      start.py  # 程序入口
│      __init__.py
│
├─conf # 配置文件
│     host_group.json # 主机组文件，可以按照实际情况修改
│     password.json # 主机信息文件，保存了主机用户名和密码
│     setting.py # 配置文件，保存了日志等定义
│     __init__.py
│
├─core # 主要程序逻辑都在这个目录里
│     logger.py # 日志记录模块
│     main.py # 主要逻辑交互程序
│     __init__.py
│
├─db # 文件上传下载的地方
│      1.py # 保存的数据信息，从服务器上下载获得
│      host_group.json # 保存的文件信息，测试上传到服务器文件
│      __init__.py
│
└─log # 日志记录
        access.log # 日志
        transactions.log # 日志
        __init__.py

```

## 程序流程图

![](主机批量管理工具.png)

##  程序启动

> 使用的依赖为：os, sys, json, threading, paramiko, logging

```
pip3 install json, threading, paramiko, logging
python bin/start.py
```

## 执行程序

```
0: web
1: backend
2: NFS
>> 3
list index out of range

 Host Managemet Tools
0: web
1: backend
2: NFS
>> 0
1. 192.168.3.132
2. 192.168.3.161
3. 192.168.3.191

 
    exce common
    put source_file destination_file
    get source_file destination_file
    ... 
    
    quit: 返回上一层，重新选择分组
    
>> quit
 Host Managemet Tools
0: web
1: backend
2: NFS
>> 

 Host Managemet Tools
0: web
1: backend
2: NFS
>> 2
1. 192.168.3.52

    exce common
    put source_file destination_file
    get source_file destination_file
    ... 
    
    quit: 返回上一层，重新选择分组

>> ls

 ------ 192.168.3.52 ------ 
1.json
1.py
1.sh
2.sh
5ee2e73fab246.png
a
bky
elastalert
elastalert.tar.gz
file.txt
Python-3.6.0.tgz
redis-5.0.5.tar.gz
sp
test_images


 
    exce common
    put source_file destination_file
    get source_file destination_file
    ... 
    
    quit: 返回上一层，重新选择分组

>> get 1.py test.py

 ------ 192.168.3.52 ------ 
1.py 下载成功，保存为 D:\evescn\python14\day9\eve_hosts_management_tools/db/test.py

 
    exce common
    put source_file destination_file
    get source_file destination_file
    ... 
    
>> put 1.py /root/test.py

 ------ 192.168.3.52 ------ 
D:\evescn\python14\day9\eve_hosts_management_tools/db/1.py 上传成功，保存为 /root/test.py

 
    exce common
    put source_file destination_file
    get source_file destination_file
    ... 
    
    quit: 返回上一层，重新选择分组

>> ls

 ------ 192.168.3.52 ------ 
1.json
1.py
1.sh
2.sh
5ee2e73fab246.png
a
bky
elastalert
elastalert.tar.gz
file.txt
Python-3.6.0.tgz
redis-5.0.5.tar.gz
sp
test_images
test.py


 
    exce common
    put source_file destination_file
    get source_file destination_file
    ... 
    
    quit: 返回上一层，重新选择分组

```