from django.db import models


# Create your models here.
# 定义书籍模型类
class BookInfo(models.Model):
    """
    此类里面的数据，同时联系着数据库
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # id 为默认主键
    b_title = models.CharField(max_length=20)  # 专业书的名称
    b_pub_date = models.DateField()  # 发布日期
    b_read = models.IntegerField(default=0)  # 阅读量
    b_comment = models.IntegerField(default=0)  # 评论量
    is_Delete = models.BooleanField(default=False)  # 逻辑删除


