from django.shortcuts import reverse, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404

from .tools import check_topic_owner, check_topic_public
from .forms import Topic_Form, Entry_Form
from .models import Topic, Entry


# Create your views here.


def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')


# @login_required
def topics(request):
    """显示所有的主题"""

    # topic_all = Topic.objects.filter(owner=request.user).order_by('date_added')
    topic_all = Topic.objects.order_by('date_added')
    context = {'topics': topic_all}  # 通过字典的键，来引用列表值

    return render(request, 'learning_logs/topics.html', context)


# @login_required
def topic(request, topic_id):
    """
    显示单个主题，以及所有的条目
    :param request: 服务器请求
    :param topic_id: 主题id
    :return:
    """

    # topic_single = Topic.objects.get(id=topic_id)
    topic_single = get_object_or_404(Topic, id=topic_id)

    # 确认请求的主题，是否属于当前用户
    # check_topic_owner(request, topic_single)
    check_topic_public(request, topic_single)
    entries = topic_single.entry_set.order_by('-date_added')  # 减号指定按照降序排序
    context = {'topic': topic_single, 'entries': entries}  # 数据环境字典

    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """
    添加一个新主题
    :param request:
    :return:
    """
    if request.method != 'POST':  # 相当于可能是GET请求
        # 未提交数据：创建一个空表单
        form = Topic_Form()

    else:
        # POST 提交了数据，对数据进行处理
        form = Topic_Form(request.POST)

        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user  # 当前用户为新添所有者
            new_topic.save()

            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}

    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """
    在特定的主题当中，添加新条目
    :param topic_id:
    :param request:
    :return:
    """
    topic = Topic.objects.get(id=topic_id)  # 获取主题对象

    if request.method != 'POST':  # 相当于可能是GET请求
        # 未提交数据：创建一个空表单
        form = Entry_Form()

    else:
        # POST 提交了数据，对数据进行处理
        form = Entry_Form(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.owner = request.user
            new_entry.save()

            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}

    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """
    编辑既有的条目
    :param request:
    :param entry_id:
    :return:
    """
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    # check_topic_owner(request, topic)
    check_topic_public(request, topic)

    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单
        form = Entry_Form(instance=entry)

    else:
        # POST提交的数据，对数据进行处理
        form = Entry_Form(instance=entry, data=request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}

    return render(request, 'learning_logs/edit_entry.html', context)


@login_required
def whether_public(request, topic_id):
    """
    调整主题是否为公开
    :param request:
    :return:
    """
    public = request.POST.get("public")  # 接收到的是字符串形式
    topic = Topic.objects.get(id=topic_id)  # 获取主题对象
    # print(type(public))  <class 'str'>

    if public == "True":
        public_s = "public"
        public = True

    else:
        public_s = "private"
        public = False

    topic.public = public
    topic.save()  # 保存模型对象
    # print(topic.public)

    # topic_single = Topic.objects.get(id=topic_id)
    topic_single = get_object_or_404(Topic, id=topic_id)

    check_topic_public(request, topic_single)
    entries = topic_single.entry_set.order_by('-date_added')  # 减号指定按照降序排序
    context = {'topic': topic_single, 'entries': entries, 'public_s': public_s}  # 数据环境字典

    return render(request, 'learning_logs/topic.html', context)


