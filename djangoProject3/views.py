# -*- ecoding: utf-8 -*-
# @ModuleName: views
# @Function: 
# @Author: MysteriousKnight
# @Email: xingchenziyi@163.com
# @Time: 2022-11-18 22:15
from django.shortcuts import render
import os


def index(request):
    path = "C:\\Users\\23608\\Desktop\\web"
    list_project = os.listdir(path)
    list_project.pop(0)
    web = []
    for i in range(len(list_project)):
        web.append(list_project[i].split("-"))
    view_str = []
    view_img = []

    for i in range(len(web)):
        view_str.append([
            ["<a href='https://www.lxcearthnet.xyz/visual2022/" + str(web[i][0]) + "/index.html'" + "class='btn "
                                                                                                   "btn-block "
                                                                                                   "btn-while "
                                                                                                   "text-truncate "
                                                                                                   "rounded-0 py-2 "
                                                                                                   "d-none "
                                                                                                   "d-lg-block' "
                                                                                                   "style='z-index: "
                                                                                                   "1000;' "
                                                                                                   "target='_blank'>"
            + str(web[i][1]) +"-"+ str(web[i][0][6:]) + "号" + "</a>"], ["img/vision/index" + str(web[i][0][6:]) + ".jpg"]])
        print(web[i][0][6:])
    return render(request, 'index.html', {"view_str": view_str})

# def runoob(request):
#     views_str = "<a href='https://www.runoob.com/'>点击跳转</a>"
#     return render(request, "runoob.html", {"views_str": views_str})
#
# {{ views_str|safe }}

# def index(request):
#     path = os.getcwd()
#     list_project = os.listdir(path)
#     context = {}
#     context['work'] = 'Hello World++++!'
#     num = []
#     for i in range(100):
#         context[str("a") + str(i)] = 'C++' + str(i)
#         num.append(i)
#
#     return render(request, 'index.html', {"num": context})
