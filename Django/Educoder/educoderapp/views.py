from django.shortcuts import render, redirect, reverse

# Create your views here.
from educoderapp.models import BookInfo
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


# 导模块：一定要从包开始导


def hello(request):
    """

    :param request: 给定一个访问请求
    :return: 响应
    """
    return HttpResponse("Hello RichardLau_Cx")


def index(request):
    """
    查询所有图书信息，并渲染显示
    :param request:
    :return:
    """
    lists = BookInfo.objects.all()  # 返回所有已经存在的对象

    return render(request, 'educoder_app/index.html', {'book_list': lists})


def create(request):
    """
    跳转至添加书籍页面
    :param request:
    :return:
    """
    return render(request, 'educoder_app/create.html')


@csrf_exempt
def create_p(request):
    """
    获取POST请求中提交的数据，并且保存至MySQL数据库中
    :param request:
    :return:
    """
    book = BookInfo()
    book.b_title = request.POST.get('b_title')  # POST方法一般用来向目的服务器发出更新请求，并附有请求实体。
    book.b_pub_date = request.POST.get('b_pub_date')

    book.save()  # 把对象数据进行保存（存入数据库当中）

    # 转向到首页
    return redirect(reverse('educoder_app:index'))  # 针对命名空间操作
    # 跨站请求伪造（英语：Cross-site request forgery），也被称为 one-click attack 或者 session riding，通常缩写为 CSRF 或者 XSRF
    # reverse方法的作用是对已命名的URL进行反向解析 -HttpReponseDirect只支持hard coded urls(硬编码链接)


def delete(request, ID):
    """
    根据传入值，删除指定ID的书籍对象
    :param request:
    :param ID: 通过HTML页面上面，生成的数据对象来获取
    :return:重定向，反向解析至首页
    """
    book = BookInfo.objects.get(id=int(ID))  # 从数据库中，获取编号为ID的书籍对象
    book.delete()  # 删除书籍对象

    # 重定向至首页
    return redirect(reverse('educoder_app:index'))


def edit_d(request, ID):
    """
    获取当前编辑的书籍信息
    :param request:
    :param ID:
    :return: 渲染到edit.html页面
    """
    book = BookInfo.objects.get(id=int(ID))
    b_title = book.b_title
    # b_pub_date = book.b_pub_date.today().strftime("%Y-%m-%d")  # 此处获取为当天日期的字符串格式
    b_pub_date = book.b_pub_date.strftime("%Y-%m-%d")  # 此处获取为当天日期的字符串格式

    return render(request, 'educoder_app/edit.html', {'b_title': b_title, 'b_pub_date': b_pub_date, 'id': ID})


@csrf_exempt
def edit_s(request, ID):
    """
    将表单上面提交的信息，存入数据库
    :param request:
    :param ID:
    :return:
    """
    # book = BookInfo()
    book = BookInfo.objects.get(id=int(ID))
    book.b_title = request.POST.get('b_title')
    book.b_pub_date = request.POST.get('b_pub_date')  # 只要页面表单上需要提交的数据，就不能够省略
    # book.id = ID  # 如果是新实例化的对象，就要通过修改id，来实现对原数据的覆盖
    book.save()

    return redirect(reverse('educoder_app:index'))
