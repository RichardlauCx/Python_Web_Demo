from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Topic(models.Model):
    """
    用户学习的主题
    """
    # 默认主键id，会自动生成
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)  # 是否公开主题
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # 若执行删除，将以级联的方式进行

    def __str__(self):
        """
        返回模型（主题名）的字符串表示
        :return: test
        """
        return self.text


class Entry(models.Model):
    """
    学到的有关某个主题领域的具体知识（条目）
    """

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  # 外键实例，删除是以级联的方式
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)  # 自动添加当前时间戳

    class Meta:
        verbose_name_plural = 'entries'  # 详细的多个条目名

    def __str__(self):
        """
        返回模型的字符串表示（界面上的显示）
        :return: 对应对象实例的描述信息
        """
        if len(self.text[:]) <= 50:  # TODO 待测试
            return self.text

        else:
            return self.text[:50] + "..."
