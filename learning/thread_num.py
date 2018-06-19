# -*- encoding:utf-8 -*-

import threading

def thread_fun(num):
    for n in range(0,int(num)):
        print ("I come from %s, num: %s" %( threading.current_thread().getName(),n))

def main(thread_num):
    thread_list = list()
    # 创建线程对象
    for i in range(0,thread_num):
        thread_name = "thread_%s" %i
        thread_list.append(threading.Thread(target = thread_fun,name= thread_name,args= (20,)))

    # 启动所有线程
    for thread in thread_list:
        thread.start()

    # 主线程中等待所有子线程完成
    for thread in thread_list:
        thread.join()

if __name__ == "__main__":
    main(3)