import datetime

from django.db import models

"""
create  table user(
id  int  primary key  auto_increment,
email varchar(100),
username varchar(64),
password varchar(128),
phone varchar(11),
is_delete int(1)
)

"""

"""
约束

模型 字段 ,字段类型
约束(选项,参数)
primary_key  表示主键  一个模型里必须有主键,如果没有设置主键,django会自动帮我们生成一个id的主键
unique   唯一约束  创建约束 ,给字段创建唯一索引
null  空值约束  django里面所有字段默认不允许为null
default  默认值约束 
         外键约束
索引         

db_index = True 表示该字段是索引字段
"""

"""
# 当我们去修改该记录的时间赋值给字段 (每次更新该模型的数据记录最后一次更新时间)
DatetimeField(auto_now=True)
# auto_now_add 把第一次创建该条记录的时候会赋当前的时间
DatetimeField(auto_now_add=True)

DateFiled

"""


# django框架会自动帮我们创建主键
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100, name='mail', unique=True)
    username = models.CharField(max_length=64, null=False)
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=11)
    is_delete = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now=True)

    class Meta:
        # 模块名+ 类名 修改表的名称
        db_table = 'user'
        # 默认的排序字段
        # 默认按升序进行排序    -表示按降序排序
        ordering = ['-create_date', '-username']
        managed = True


#  string  list  hash  set  zset
# decimal(7,2)
class GroupInfo(models.Model):
    title = models.CharField(max_length=255)
    img = models.CharField(max_length=100)
    # max_digits 表示数字长度(整数位数+ 小数位数 = 长度) decimal_places 表示小数的位数
    # 现价
    current_price = models.DecimalField(max_digits=7, decimal_places=2)
    # 原价
    original_price = models.DecimalField(max_digits=7, decimal_places=2)
    # 对应数据库的int类型
    count = models.IntegerField()
    # 假删除
    is_delete = models.BooleanField()

    #     元信息
    class Meta:
        db_table = 'group_info'


class BaseModel(models.Model):
    create_date = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Test(BaseModel):
    name = models.CharField(max_length=100, db_index=True)
    age = models.CharField(max_length=100)

    class Meta:
        db_table = 't_test'
        # 索引  django1.11新增属性
        indexes = [models.Index(fields=['name'], name='idx_test_name')]
        # admin 后台显示模型的名称
        verbose_name = '测试'
        # 复数形式 中文是没有单复数的
        verbose_name_plural = verbose_name
