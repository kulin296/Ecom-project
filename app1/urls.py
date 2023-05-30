from django.urls import path
from app1.views import *
urlpatterns = [
    path('first/',first),
    path('login/',login,name='login1'),
    path('logout/',logout,name='logout1'),
    path('register/',register,name='register1'),
    path('table/',tableview),
    path('',index,name='index'),
    path('product-all/',productall,name='productall'),
    path('product-filter/<int:id>/',productcategorywise,name='productfilter'),
    path('product-get/<int:id>/',singleproduct,name='productget1'),
    path('change-password',changepass,name='change'),
    path('profile',profile,name='profile1'),
    path('contact-us',contact,name='contact'),
    path('paymenthandler/',paymenthandler,name='paymenthandler'),
    path('buy-now/',buynow,name='buy'),
    path('razorpayView/',razorpayView,name='razorpayView'),
    path('successview/',successview,name="orderSuccessView"),
    path('order-list/',orderview,name="orderList"),
     path('myorders/',myorder,name='myorder')
] 