from django.contrib import admin
from django.urls import path,include
from  .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
 path('',views.index,name="index"),
 path('jewellery',views.jewellery,name="jewellery"),
 path('electronic',views.electronic,name="electronic"),
 path('fashion',views.fashion,name="fashion"),
 path('home',views.home,name="home"),
 path ('seller_product_adding',views.seller_product_adding,name="seller_product_adding"),
 path ('product_add',views.product_add,name="product_add"),
 path('product_show',views.product_show,name="product_show"),
 path('new_release',views.new_release,name="new_release"),
 path('registration',views.registration,name="registration"),
 path('login_index',views.login_index,name="login_index"),
 path('register',views.register,name="register"),
 path('login',views.login,name="login"),
 path('logged_page',views.logged_page,name="logged_page"),
 path('logout',views.logout,name="logout"),
 path('logout_logg',views.logout_logg,name="logout_logg"),
 path('cart',views.cart,name="cart"),
 path('personal_cart',views.personal_cart,name="personal_cart"),
 path('forgot_password',views.forgot_password,name="forgot_password"),
 path('set_new_password',views.set_new_password,name="set_new_password"),
 path('product_details_view',views.product_details_view,name="product_details_view"),
 
 
 path('login_fail',views.login_fail,name="login_fail"),
 path('login_success',views.login_success,name="login_success"),
 path('registration_fail',views.registration_fail,name="registration_fail"),
 path('registration_success',views.registration_success,name="registration_success"),
 path('upload_fail',views.upload_fail,name="upload_fail"),
 path('upload_success',views.upload_success,name="upload_success"),
 path('set_success',views.set_success,name="set_success"),
 path('fail_to_set_new_password',views.fail_to_set_new_password,name="fail_to_set_new_password"),
 
 
 path('remove_cart_product',views.remove_cart_product,name="remove_cart_product"),
 path('customer_service',views.customer_service,name="customer_service"),
 path('login_detail',views.login_detail,name="login_detail"),


path('delete_user',views.delete_user,name="delete_user"),
path('product_data_delete',views.product_data_delete,name="product_data_delete"),
path('cart_show',views.cart_show,name="cart_show"),
path('check_session',views.check_session,name="check_session"),

path('cart_empty',views.cart_empty,name="cart_empty"),
path('personal_info',views.personal_info,name="perssonal_info"),

path('d2',views.d2,name="d2"),


path('add_address',views.add_address,name="add_address"),
path('address_store',views.address_store,name="address_store"),
path('show_address',views.show_address,name="show_address"),
path('delete_address',views.delete_address,name="delete_address"),

path('seller_product_show',views.seller_product_show,name="seller_product_show")


 
 
 
 
 

]

