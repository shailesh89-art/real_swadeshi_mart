from django.db import models

# Create your models here.

class product_upload_database(models.Model):
    product_name=models.CharField(max_length=30)
    product_price=models.CharField(max_length=5)
    product_description=models.CharField(max_length=100)
    index_photo=models.FileField(upload_to="index_photo")
    left_side_photo=models.FileField(upload_to="left_side_photo")
    right_side_photo=models.FileField(upload_to="right_side_photo")
    up_photo=models.FileField(upload_to="up_photo")
    down_photo=models.FileField(upload_to="down_photo")
    product_for=models.CharField(max_length=30)
    product_type=models.CharField(max_length=30)
    seller_id=models.CharField(max_length=50,default="seller@gmail.com")

class login_details(models.Model):
    logged_as=models.CharField(max_length=20) 
    fname=models.CharField(max_length=30) 
    lname=models.CharField(max_length=30) 
    email=models.CharField(max_length=50,unique=True) 
    date_of_birth=models.CharField(max_length=50) 
    password=models.CharField(max_length=50) 
    confirm_password=models.CharField(max_length=50) 
    contact=models.CharField(max_length=50)
    checkbox_checked=models.CharField(max_length=10,default="on")
    gender=models.CharField(max_length=20,default="Male")
    
class  cart_data(models.Model):
    product_id=models.CharField(max_length=20,default=0)
    user_id=models.CharField(max_length=20,default=0)
    product_name=models.CharField(max_length=50,default=0)
    product_price=models.CharField(max_length=20,default=0)
    product_description=models.CharField(max_length=100,default=0)
    cart_index=models.FileField(max_length=50,default=0)
    
class address_data(models.Model):
    fname=models.CharField(max_length=20)
    mobile=models.CharField(max_length=15)
    pincode=models.CharField(max_length=7)
    locality=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=40)
    landmark=models.CharField(max_length=150)
    alternate_mobile=models.CharField(max_length=15)
    address_location=models.CharField(max_length=10)    
    user_id=models.CharField(max_length=50)
    
    
    
