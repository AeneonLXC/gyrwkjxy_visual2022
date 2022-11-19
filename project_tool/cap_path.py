# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 15:03:40 2022

@TwinkelStar: 李星辰
@Email: xingchenziyi@163.com   
 
# ----------------------------------------------
#
#             captrue path file
#               Coding By lxc
#                  获取文档路径
#
#          LAST_UPDATE: Sat Nov 19 15:03:40 2022
#
# ----------------------------------------------

"""
import os

def capPath():
    #   获取当前工作目录
    path = os.getcwd()
    #   获取项目路径
    list_project = os.listdir(path)
    list_project.pop(0)
    #将各个项目分割
    web = []
    for i in range(len(list_project)):
        web.append(list_project[i].split("-"))
        
    return web
    #web列表格式
    # web = [['number100', '神龙尊者', '张三', '李四', '王五']
    #       ['number99', '至高之拳', '赵六', '天七', '高八']]

