# 遇到BUG
1. in() got an unexpected keyword argument 'template_name'
2. 部署至Heroku服务器之后，导航栏无法实现下来功能

# BUG解决
1. 作者使用的Django是版本是1.11，但是，在Django2.0中内置登陆视图不再是函数，而是类，位置在django.contrib.auth.views.LoginView


# 配置信息

* 超级用户

1. Username：admin
2. Email address：2409608770@qq.com
3. Password：admin

# Notice 
1. 当Django项目无法正常运行时，通过重新生成符合各配置版本信息的虚拟环境来解决
