from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login


# Create your views here.
def logout_view(request):
    """
    注销用户
    :param request:
    :return:
    """
    logout(request)

    return HttpResponseRedirect(reverse('learning_logs:index'))


def register(request):
    """
    注册新用户
    :param request:
    :return:
    """
    if request.method != 'POST':
        # 显示空的注册表单
        form = UserCreationForm()

    else:
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录，再重定向至主页
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            # authenticated_user = authenticate(username=new_user.username, password=request.POST['password2'])
            # 其中request.POST['password1'] 是表单提交当中的Password， request.POST['password2']是表单当中的Password confirmation

            login(request, authenticated_user)

            return HttpResponseRedirect(reverse('learning_logs:index'))  # 参数为命名空间下的

    context = {'form': form}

    return render(request, "users/register.html", context)  # 参数2为路径
