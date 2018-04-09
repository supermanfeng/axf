# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from myapp.models import MainWheel, MainNav, ContentThird, MainShop, MainShow, FoodType, Goods, User, Cart, Order


def home(request):
    wheels = MainWheel.objects.all()
    navs = MainNav.objects.all()
    contentthird = ContentThird.objects.all()
    mainshop = MainShop.objects.all()
    mainshop0 = mainshop[0]
    mainshop1_2 = mainshop[1:3]
    mainshop3_6 = mainshop[3:7]
    mainshop7_10 = mainshop[7:]
    mainshow = MainShow.objects.all()
    data = {
        'title': '爱鲜蜂',
        'wheels': wheels,
        'navs': navs,
        'contentthird': contentthird,
        'mainshop0': mainshop0,
        'mainshop1_2': mainshop1_2,
        'mainshop3_６': mainshop3_6,
        'mainshop7_10': mainshop7_10,
        'mainshow': mainshow,

    }

    return render(request, 'myapp/home/home.html', context=data)


def cart(request):
    username = request.session.get('username')
    if not username:
        return redirect(reverse('myapp:lgoin'))
    user = User.objects.filter(u_name=username).first()
    # 每一种商品对应着一个购物车,所以这里应该叫cartlist更合适
    goodsList = user.cart_set.filter(c_belong=False)

    data = {
        'title': '爱鲜蜂',
        'goodsList': goodsList
    }

    return render(request, 'myapp/cart/cart.html', context=data)


def market(request):
    return redirect(reverse('myapp:marketwithparams', kwargs={'typeid': '104749', 'childcid': '0', 'sortrule': "0"}))


def marketwithparams(request, typeid, childcid, sortrule):
    List = []
    foodtypes = FoodType.objects.all()
    goodlist = Goods.objects.filter(categoryid=typeid)
    child = foodtypes.filter(typeid=typeid).first().childtypenames
    chlids = child.split("#")
    for item in chlids:
        items = item.split(":")
        List.append(items)

    if childcid != "0":
        goodlist = goodlist.filter(childcid=childcid)

    if sortrule == "1":
        goodlist = goodlist.order_by("productnum")
    elif sortrule == "2":
        goodlist = goodlist.order_by("-productnum")
    elif sortrule == "3":
        goodlist = goodlist.order_by("-price")
    elif sortrule == "4":
        goodlist = goodlist.order_by("price")

    data = {
        'title': '爱鲜蜂',
        'foodtypes': foodtypes,
        'goodlist': goodlist,
        'List': List,
        'childcid': childcid,
        'typeid': typeid,

    }
    return render(request, 'myapp/market/market.html', context=data)


def myself(request):
    user = request.session.get('username')
    data = {

        'title': '爱鲜蜂'
    }

    if user:
        username = User.objects.get(u_name=user)
        data['username'] = username.u_name
        data['icon'] = username.u_icon.url

        data['islogin'] = 'login'
        not_pay_num = Order.objects.filter(o_user=username).filter(o_status=0).count()
        not_receive_num = Order.objects.filter(o_user=username).filter(o_status=1).count()
        print(not_pay_num)
        print(not_receive_num)
        data["not_pay"] = not_pay_num
        data["not_receive"] = not_receive_num

    return render(request, 'myapp/myself/myself.html', context=data)


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        icon = request.FILES['icon']
        password2 = passwordMD5(password)
        user = User()
        user.u_name = username
        user.u_password = password2
        user.u_email = email
        user.u_icon = icon
        user.save()
        response = redirect(reverse('myapp:myself'))
        request.session['username'] = username
        return response
    elif request.method == "GET":
        return render(request, 'myapp/myself/register.html')


def check_user(request):
    username = request.GET.get('username')
    user = User.objects.filter(u_name=username)
    data = {
        'title': '注册',
        'msg': '用户名可用',
        'status': '888'
    }

    if user.exists():
        data['msg'] = '用户名已存在'
        data['status'] = '900'

    return JsonResponse(data)


def passwordMD5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    passwordmd5 = md5.hexdigest()
    return passwordmd5


def login(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        usernames = User.objects.filter(isDelete=False).filter(u_name=user)
        if usernames.exists():
            pwd = passwordMD5(pwd)
            if pwd == usernames.first().u_password:
                request.session['username'] = user
                response = redirect(reverse('myapp:myself'))
                return response
            return HttpResponse('用户或密码错误')
    elif request.method == 'GET':

        return render(request, 'myapp/myself/login.html')


def logout(request):
    request.session.flush()
    return render(request, 'myapp/myself/myself.html')


def userinfo(request):
    if request.method == 'POST':
        username = request.session['username']
        users = User.objects.filter(u_name=username)
        if users.exists():
            user = users.first()
            password = request.POST.get('password')
            if password:
                password = passwordMD5(password)
                user.u_password = password
            icon = request.FILES['icon']

            if icon:
                user.u_icon = icon

            user.save()
        return redirect(reverse('myapp:myself'))
    elif request.method == 'GET':

        return render(request, 'myapp/myself/userinfo.html')


def addtocart(request):
    username = request.session.get('username')
    data = {
        'status': '200',
        'msg': '操作成功'

    }
    if not username:
        data['status'] = '302'
        data['msg'] = '用户不存在'
        return JsonResponse(data)

    user = User.objects.filter(u_name=username).first()
    goodsid = request.GET.get('goodsid')
    goods = Goods.objects.filter(pk=goodsid).first()
    cart_item = Cart.objects.filter(c_belong=False).filter(c_user=user).filter(c_goods=goods).first()
    if not cart_item:
        cart_item = Cart()

    else:
        cart_item.c_num = cart_item.c_num + 1

    cart_item.c_goods = goods
    cart_item.c_user = user
    cart_item.save()
    data['c_num'] = cart_item.c_num
    return JsonResponse(data)


def subtocart(request):
    username = request.session.get('username')
    data = {
        'status': '200',
        'msg': '操作成功',

    }

    if not username:
        data['status'] = '302'
        data['msg'] = '用户不存在'
        return JsonResponse(data)
    user = User.objects.filter(u_name=username).first()
    goodsid = request.GET.get('goodsid')
    goods = Goods.objects.filter(pk=goodsid).first()
    cart_item = Cart.objects.filter(c_belong=False).filter(c_goods=goods).filter(c_user=user).first()
    if cart_item:
        if cart_item.c_num == 1:

            cart_item.delete()
            data['c_num'] = '0'
            cart_item.save()

        else:
            cart_item.c_num = cart_item.c_num - 1
            cart_item.save()
            data['c_num'] = cart_item.c_num
    else:
        data['status'] = '202'
        data['msg'] = '操作数据不存在'

    return JsonResponse(data)


def subcartgoods(request):
    cartid = request.GET.get('cartid')
    cart_item = Cart.objects.filter(pk=cartid).first()
    data = {
        'status': '300',
        'msg': '操作成功',
    }
    if cart_item.c_num == 1:
        cart_item.delete()
        data['num'] = 0
    else:

        cart_item.c_num = cart_item.c_num - 1
        cart_item.save()
        data['num'] = cart_item.c_num

    return JsonResponse(data)


def addcartgoods(request):
    cartid = request.GET.get('cartid')
    cart_item = Cart.objects.filter(pk=cartid).first()
    data = {
        'status': '300',
        'msg': '操作成功',
    }

    cart_item.c_num = cart_item.c_num + 1
    cart_item.save()
    data['num'] = cart_item.c_num

    return JsonResponse(data)


def changecheck(request):
    cartid = request.GET.get('cartid')
    cart_item = Cart.objects.filter(pk=cartid).first()
    cart_item.c_select = not cart_item.c_select
    cart_item.save()
    data = {
        'status': '300',
        'msg': '修改成功',
    }

    data['is_select'] = cart_item.c_select
    return JsonResponse(data)


def generateorder(request):
    selects = request.GET.get('selects')
    select_list = selects.split('#')
    data = {
        'status': '200',
        'msg': '操作成功',
    }

    username = request.session.get('username')
    user = User.objects.get(u_name=username)
    order = Order()
    order.o_status = 0
    order.o_user = user
    order.save()
    for item in select_list:
        cart_item = Cart.objects.get(pk=item)

        cart_item.c_belong = True
        cart_item.c_order = order
        cart_item.save()
        data['order_num'] = order.id

    return JsonResponse(data)


def orderDetail(request):
    orderid = request.GET.get('orderid')
    user = request.session.get('username')
    username = User.objects.get(u_name=user)
    order = Order.objects.get(pk=orderid)
    goodsinfos = order.cart_set.all()
    data = {
        'user': username,
        'goodsinfos': goodsinfos,
        'orderid': orderid,

    }

    return render(request, 'myapp/market/order/order_detail.html', context=data)


def pay(request):
    orderid = request.GET.get('orderid')
    data = {

        'status': '200',
        'msg': '操作成功',
    }
    order = Order.objects.get(pk=orderid)
    order.o_status = 1
    order.save()

    return JsonResponse(data)


def notPayList(request):
    username = request.session.get("username")

    data = getOrders(username, 0)

    return render(request, 'myapp/market/order/order_list.html', context=data)


def notReceiveList(request):
    username = request.session.get("username")

    data = getOrders(username, 1)

    return render(request, 'myapp/market/order/order_list_not_receive.html', context=data)


def getOrders(username, status):
    if not username:
        return redirect(reverse("myapp:login"))
    user = User.objects.get(u_name=username)

    orderList = Order.objects.filter(o_user=user).filter(o_status=status)
    print(orderList)

    data = {
        "orderList": orderList,
    }
    return data
