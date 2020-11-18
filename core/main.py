# -*- coding: utf-8 -*-
# @Author    : Evescn
# @time      : 2020/11/17 11:50
# @File      : main.py
# @Software  : PyCharm

import json
import threading
import paramiko
from conf import setting


def list_group():
    """
    显示当前主机分组函数，显示当前系统上的主机分组
    :return:
    """
    print('\033[1;33m Host Managemet Tools\033[0m')
    file = '%s/conf/host_group.json' % setting.BASE_DIR
    # print(file)
    setting.trans_logger.info(file)

    num = 0
    group_list = []
    with open(file, mode='r') as f:

        all_group_list = json.load(f)

        for i in all_group_list:
            print('%s: %s' % (num, i))
            num += 1
            group_list.append(i)

        return group_list, all_group_list


def show_common():
    """
    显示信息，进入分组后，显示可以执行操作
    :return:
    """
    print()
    common_msg = """
    exce common
    put source_file destination_file
    get source_file destination_file
    ... 
    
    quit: 返回上一层，重新选择分组
    """
    print('\033[1;32m %s\033[0m' % common_msg)

    return None


def ssh_common(host, username, password, common):
    """
    执行普通命令，如：ls. pwd 等
    :param host: 主机IP
    :param username: 用户名
    :param password: 密码
    :param common: 命令
    :return:
    """
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # print('%s %s %s' %(host, username, password))
    setting.access_logger.info('%s' % common)
    setting.trans_logger.info('%s' % common)

    ssh.connect(hostname=host, port=22, username=username, password=password)

    stdin, stdout, stderr = ssh.exec_command(common)

    res, err = stdout.read(), stderr.read()
    result = res if res else err

    print('\033[1;31m ------ %s ------ \033[0m' % host)
    print(result.decode())

    return None


def file_common(host, username, password, common):
    """
    上传文件函数，执行上线文件功能
    :param host: 主机IP
    :param username: 用户名
    :param password: 密码
    :param common: 执行的命令
    :return:
    """
    transport = paramiko.Transport((host, 22))
    transport.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    # print(common.split()[0])
    source_file = common.split()[1]
    destination_file = common.split()[2]
    # print('%s %s' % (source_file, destination_file))
    setting.access_logger.info('%s %s' % (source_file, destination_file))

    try:
        if common.split()[0] == 'put':
            source_file = "%s/db/%s" % (setting.BASE_DIR, source_file)
            sftp.put(source_file, destination_file)
            print("\033[1;31m ------ %s ------ \033[0m" % host)
            print("%s 上传成功，保存为 %s" %(source_file, destination_file))
        elif common.split()[0] == 'get':
            destination_file = "%s/db/%s" % (setting.BASE_DIR, destination_file)
            sftp.get(source_file, destination_file)
            print("\033[1;31m ------ %s ------ \033[0m" % host)
            print("%s 下载成功，保存为 %s" %(source_file, destination_file))
        else:
            print('命令错误')
            setting.trans_logger.error('命令错误')
    except BaseException as e:
        print(e)
        setting.trans_logger.error(e)

    return None


def exec_common(host_list, common):
    """
    识别用户命令，执行命令
    :param host_list: 需要执行命令的主机列表
    :param common: 执行的命令
    :return:
    """
    file = '%s/conf/password.json' % setting.BASE_DIR
    setting.access_logger.info(file)

    with open(file, mode='r') as f:
        t_objs = []
        host_info_list = json.load(f)

        for host in host_list:
            username = host_info_list[host]['name']
            password = host_info_list[host]['password']

            if common.split()[0] == 'put' or common.split()[0] == 'get':
                func = file_common
            else:
                func = ssh_common
            t = threading.Thread(target=func, args=(host, username, password, common))
            t.start()
            t_objs.append(t)

        for t in t_objs:
            t.join()

    return None


def start():
    """ 执行管理工具 """
    while True:
        group_list, all_group_list = list_group()

        choice = int(input(">> ").strip())

        try:
            host_list = []
            for host, ip in all_group_list[group_list[choice]].items():
                print('%s. %s' % (host, ip))
                host_list.append(ip)

            while True:
                show_common()
                choice = input(">> ").strip()

                if choice == 'quit':
                    break
                else:
                    exec_common(host_list, choice)

        except BaseException as e:
            print(e)


if __name__ == '__main__':
    start()
