#! usr/bin/env/python
# -*- coding:utf-8 -*-

'''this is useage module'''

from time import sleep, ctime
import threading

def my_common_create_lun(self, arg1=None, arg2=None, arg3=None, arg4='512KB', arg5=None):
    '''
    :param self:
    :param arg1:
    :param arg2:
    :param arg3:
    :param arg4:
    :param arg5:
    :return:
    '''
    params = dict(arg1=arg1, arg2=arg2, arg3=arg3, arg4=arg4, arg5=arg5)
    # 处理为None的参数
    param_deal(self, params)
    return params


def param_deal(self, params):
    '''
    过滤为None的参数
    :param self:
    :param params: 字典类型
    :return: 返回待下发给对象的参数
    '''
    for param in params.keys():
        if params[param] == None:
            params.pop(param)
    return params


def my_common_kill_process(self, process_name, wait_time=3):
    '''
    杀进程
    :param process_name:
    :param time: 等待进程复位时间
    :return:
    '''
    print 'kill -9： %s! %s' % (process_name, ctime())
    sleep(wait_time)


def my_common_kill_process_with_thread(self, process_list=None):
    '''
    多线程杀进程
    :param self:
    :param process_list:进程列表
    :return:
    '''
    # 线程列表
    threads = []
    try:
        process_num = len(process_list)
    except TypeError:
        raise (u'process_list不能为空')

    # 创建线程
    for process_name in process_list:
        t = threading.Thread(target=my_common_kill_process, args=(self, process_name,))
        threads.append(t)

    # 启动线程
    for i in range(process_num):
        threads[i].start()

    # 等待线程结束
    for i in range(process_num):
        threads[i].join()

    # 主线程
    print 'end:%s' % ctime()








