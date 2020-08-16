from django.contrib import admin

# Register your models here.
from .models import Topic, Entry
# from models import Topic, Entry  # 不可取，同时上面的语句指明，已经很规范啦


admin.site.register(Topic)  # 为管理网站注册模型：Topic
admin.site.register(Entry)  # 为管理网站注册模型：Entry

