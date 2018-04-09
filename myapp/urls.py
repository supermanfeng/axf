from django.conf.urls import url

from myapp import views

app_name = 'myapp'

urlpatterns = [

    url(r'^home/', views.home, name='home'),
    url(r'^market$', views.market, name='market'),
    url(r'^market/(?P<typeid>\d+)/(?P<childcid>\d+)/(?P<sortrule>\d+)/$', views.marketwithparams, name='marketwithparams'),
    url(r'^cart/', views.cart, name='cart'),
    url(r'^myself/', views.myself, name='myself'),
    url(r'^register/',views.register,name='register'),
    url(r'^check_user/',views.check_user,name='check_user'),
    url(r'^login/',views.login, name='login'),
    url(r'^logout/',views.logout,name='logout'),
    url(r'^userinfo/',views.userinfo,name='userinfo'),
    url(r'^addtocart/',views.addtocart,name='addtocart'),
    url(r'^subtocart/',views.subtocart,name='subtocart'),
    url(r'^subcartgoods/',views.subcartgoods,name='subcartgoods'),
    url(r'^addcartgoods/',views.addcartgoods,name='addcartgoods'),
    url(r'^changecheck/',views.changecheck,name='changecheck'),
    url(r'^generateorder/',views.generateorder,name='generateorder'),
    url(r'^orderdetail/',views.orderDetail,name='orderDetail'),
    url(r'^pay/',views.pay,name='pay'),
    url(r'^notPayList/',views.notPayList,name='notPayList'),
    url(r'^notReceiveList',views.notReceiveList,name='notReceiveList'),




]
