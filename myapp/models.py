# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class BaseModel(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=200)
    trackid = models.CharField(max_length=32)

    class Meta:
        abstract = True


class MainWheel(BaseModel):
    class Meta:
        db_table = 'axf_wheel'


class MainNav(BaseModel):
    class Meta:
        db_table = 'axf_nav'


class ContentThird(BaseModel):
    class Meta():
        db_table = 'axf_mustbuy'


class MainShop(BaseModel):
    class Meta():
        db_table = 'axf_shop'


class MainShow(BaseModel):
    categoryid = models.CharField(max_length=32)
    brandname = models.CharField(max_length=100)
    img1 = models.CharField(max_length=200)
    childcid1 = models.CharField(max_length=32)
    productid1 = models.CharField(max_length=32)
    longname1 = models.CharField(max_length=200)
    price1 = models.CharField(max_length=100)
    marketprice1 = models.CharField(max_length=100)
    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=32)
    productid2 = models.CharField(max_length=32)
    longname2 = models.CharField(max_length=200)
    price2 = models.CharField(max_length=100)
    marketprice2 = models.CharField(max_length=100)
    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=32)
    productid3 = models.CharField(max_length=32)
    longname3 = models.CharField(max_length=200)
    price3 = models.CharField(max_length=100)
    marketprice3 = models.CharField(max_length=100)

    class Meta():
        db_table = 'axf_mainshow'


class FoodType(models.Model):
    typeid = models.CharField(max_length=32)
    typename = models.CharField(max_length=100)
    childtypenames = models.CharField(max_length=200)
    typesort = models.CharField(max_length=32)

    class Meta:
        db_table = 'axf_foodtypes'


class Goods(models.Model):
    productid = models.CharField(max_length=32)
    productimg = models.CharField(max_length=200)
    productname = models.CharField(max_length=100)
    productlongname = models.CharField(max_length=200)
    isxf = models.BooleanField(default=False)
    pmdesc = models.CharField(max_length=100)
    specifics = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    marketprice = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=32)
    childcid = models.CharField(max_length=32)
    childcidname = models.CharField(max_length=100)
    dealerid = models.CharField(max_length=32)
    storenums = models.CharField(max_length=32)
    productnum = models.CharField(max_length=32)

    class Meta:
        db_table = "axf_goods"


class User(models.Model):
    u_name = models.CharField(max_length=32, unique=True)
    u_password = models.CharField(max_length=32)
    u_email = models.CharField(max_length=64)
    u_icon = models.ImageField(upload_to='icons')
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = 'axf_user'


class Order(models.Model):
    o_create_time = models.DateTimeField(auto_created=True, auto_now=True)
    """
        0 订单生成但是未支付
        1 订单支付但未发货
        2 订单支付且已发货
        3 订单已发货且已收货
        4 订单已收货但未评价
        5 已收货已评价
        6 已收货又退货
        7 售后
        ...
    """
    o_status = models.IntegerField(default=0)
    o_user = models.ForeignKey(User, on_delete=models.CASCADE, )


class Cart(models.Model):
    c_num = models.IntegerField(default=1)
    c_select = models.BooleanField(default=True)
    # False 代表属于购物车，True代表属于订单表
    c_belong = models.BooleanField(default=False)
    c_order = models.ForeignKey(Order, null=True, default=None, on_delete=models.CASCADE, )
    c_user = models.ForeignKey(User, on_delete=models.CASCADE, )
    c_goods = models.ForeignKey(Goods, on_delete=models.CASCADE, )
