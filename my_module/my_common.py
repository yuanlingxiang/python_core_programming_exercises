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


def my_commom_compare_obj(self, before_obj, after_obj, fault, obj):
    '''
    故障前后，对象比较
    单个对象比较：输出对象不同的属性值
    批量对象比较：输出不一致的对象
    :param self:
    :param before_obj: 字典类型，故障前对象的信息
    :param after_obj: 字典类型，故障后对象的信息
    :param fault: 故障动作
    :param obj: 对象名
    :return:bool值，True表示比较结果相同，False表示比较结果不相同
    '''
    if before_obj == after_obj:
        print u'%s故障前后，%s的信息未发生变化' % (fault, obj)
        return True
    else:
        print u'%s故障前后，%s存在不一致的属性， 如下：' % (fault, obj)
        print u'%s故障前:%s' % (obj, before_obj)
        print u'%s故障后:%s:' % (obj, after_obj)
        # 故障前后，对象属性逐个比较
        for obj_param, obj_param in zip(before_obj, after_obj):
            if before_obj[obj_param] != after_obj[obj_param]:
                print u'%s的属性:%s， 预期值：%s, 实际值：%s' % (obj, obj_param, before_obj[obj_param], after_obj[obj_param])
        return False


def my_common_print_all_compare_result(self, result_dict=None):
    '''
    故障前后，打印所有不一致的对象，并抛出异常
    :param self:
    :param 存放对象比较结果：result_dict:字典类型：{类型1：比较结果1, 类型2： 比较结果2}
    :return:None
    '''
    # 过滤掉所有故障前后，相同的对象
    for key, value in result_dict.items():
        if value == True:
            result_dict.pop(key)
    # 打印所有故障前后不一致的对象
    if not all(result_dict.values()):
        print '故障前后，不一致的对象有：', result_dict.keys()
        raise ValueError('故障前后，对象的信息不一致')




