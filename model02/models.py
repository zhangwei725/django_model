import time

from django.db import models


class Emp(models.Model):
    emp_id = models.AutoField(primary_key=True)
    login_name = models.CharField(max_length=64, unique=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100, unique=True)
    role = models.CharField(max_length=10, name='role')
    join_date = models.DateTimeField(auto_now_add=True)
    emp_status = models.BooleanField(default=True)
    age = models.IntegerField(default=1)

    def __str__(self):
        return self.login_name

    class Meta:
        db_table = 'emp'


class Goods(models.Model):
    # 商品的ID
    goods_id = models.AutoField(primary_key=True)
    # 商品的图片地址
    goods_img = models.CharField(max_length=100)
    # 商品的名称
    goods_name = models.CharField(max_length=100)
    # 商品信息
    goods_info = models.CharField(max_length=255)
    # 商品价格
    goods_price = models.DecimalField(max_digits=7, decimal_places=2)
    # 商品的状态 False表示未删除  True表示删除
    goods_status = models.BooleanField(default=False)

    class Meta:
        db_table = 'goods'
