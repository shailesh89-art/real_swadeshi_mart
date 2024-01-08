from django.shortcuts import render,redirect,HttpResponse
from .models import product_upload_database,login_details,cart_data,address_data
from django.contrib import messages 
import razorpay
from django.conf import settings

# Create your views here.
def index(request):
    
    return render(request,"index.html")  
def home(request):
    return render(request,"index.html") 
def jewellery(request):
    product=product_upload_database.objects.filter(product_type="Jewellery")
    return render(request,"second.html",{'product':product})
def electronic(request):
    product=product_upload_database.objects.filter(product_type="Electronic's")
    return render(request,"second.html",{'product':product})
def fashion(request):
    product=product_upload_database.objects.filter(product_type="Clothing's")
    return render(request,"second.html",{'product':product})
    
def seller_product_adding(request):
    return render(request,"seller_product_adding.html")
def product_add(request):
    if request.method=="POST":
        product_name=request.POST["product_name"]
        product_price=request.POST["product_price"]
        product_description=request.POST["product_description"]
        index_photo=request.FILES["index_photo"]
        left_side_photo=request.FILES["left_side_photo"]
        right_side_photo=request.FILES["right_side_photo"]
        up_photo=request.FILES["up_photo"]
        down_photo=request.FILES["down_photo"]
        product_for=request.POST["product_for"]
        product_type=request.POST["product_type"]
        seller_id=request.session.get('username')
        p=product_upload_database(product_name=product_name,product_price=product_price,product_description=product_description,index_photo=index_photo,left_side_photo=left_side_photo,right_side_photo=right_side_photo,up_photo=up_photo,down_photo=down_photo,product_for=product_for,product_type=product_type,seller_id=seller_id)
        p.save()
        
        return redirect(upload_success)
    else:
        return redirect(upload_fail)
        
def product_show(request):
    username=request.session.get('username')
    logg=request.session.get('logg')
    if username==username and logg=="admin":
        product=product_upload_database.objects.all().order_by('-id')
        return render(request,"product_show.html",{'product':product})
    else:
        
        return HttpResponse("only admins have the acees ")

def new_release(request): 
    product=product_upload_database.objects.all().order_by('-id')
    return render(request,"second.html",{'product':product})
        
# login section
def registration(request):
    return render(request,"registration.html")
def login_index(request):
    return render(request,"login.html")

# to store data 
def register(request):
    if request.method=="POST":
        logged_as=request.POST["logged_as"]
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        email=request.POST["email"]
        date_of_birth=request.POST["date-of-birth"]
        password=request.POST["password"]
        confirm_password=request.POST["confirmpassword"]
        contact=request.POST["contact"]
        checkbox_checked=request.POST["checkbox_checked"]
        gender=request.POST["gender"]
        try:    
            if password==confirm_password:
                     l=login_details(logged_as=logged_as,fname=fname,lname=lname,email=email,date_of_birth=date_of_birth,password=password,confirm_password=confirm_password,contact=contact,checkbox_checked=checkbox_checked,gender=gender)
                     l.save()
                     return redirect(registration_success)
            else:
                      return redirect(registration_fail)
        except:
            return render(request,"email_previously_used.html")
            
def login(request):
    count=0
    if request.method=="POST":
        email=request.POST["login_id"]
        password=request.POST["password"]
        logged_as=request.POST["logged_as"]
        data=login_details.objects.all()
        for i in data:
            if(i.email==email and i.password==password and i.logged_as==logged_as):
                count+=1
    if count==1:
        request.session["username"]=email #session start
        request.session["logg"]=logged_as
        return redirect(logged_page)
    else:
        return redirect(login_fail)
def logged_page(request):
    if request.session.get('username') is not None:
        if request.session.get('logg') is not None:
            return redirect(login_success)
    else:
        return redirect(login_fail)
    
def logout(request):
    del request.session["username"]#session close 
    return redirect(logout_logg)
def logout_logg(request):
    del request.session["logg"]
    return redirect(home)


#cart section 
def cart(request):
    if request.method=="POST":
        product_id=request.POST["id"]
        product_name=request.POST["product_name"]
        product_price=request.POST["product_price"]
        product_description=request.POST["product_description"]
        cart_index=request.POST["cart_index"]
        c1=cart_index[7:]
        user_id=request.COOKIES["csrftoken"]
        c1=cart_data(product_id=product_id,user_id=user_id,product_name=product_name,product_price=product_price,product_description=product_description,cart_index=c1)
        c1.save()
        return redirect(check_session)
def check_session(request):
    try:
        user_id=request.session.get("username")
        csrf_token=request.COOKIES["csrftoken"]
        u1=cart_data.objects.filter(user_id=csrf_token).update(user_id=user_id)
        return redirect(personal_cart)
    except:
        return redirect(personal_cart)
       

def personal_cart(request):
    
    user_id=request.COOKIES["csrftoken"]
    product_data=cart_data.objects.filter(user_id=user_id)
    if len(product_data)>=1:
        l1=len(product_data)
        l2=[]
        for i in product_data:
            l2.append(int(i.product_price))
        l3=sum(l2)
        
        return render(request,"cart1.html",{'product_data':product_data,'l1':l1,'l3':l3})
    else:
        user_id=request.session.get("username")
        product_data=cart_data.objects.filter(user_id=user_id)
    if len(product_data)>=1:
            l1=len(product_data)
            l2=[]
            for i in product_data:
                l2.append(int(i.product_price))
            l3=sum(l2)
            return render(request,"cart1.html",{'product_data':product_data,'l1':l1,'l3':l3})
    else:
        return redirect(cart_empty)
def forgot_password(request):
    return render(request,"forget.html")
def set_new_password(request):
    if request.method=="POST":
        login_id1=request.POST["login_id1"]
        logged_as=request.POST["logged_as"]
        birthday=request.POST["birthday"]
        new_password=request.POST["new_password"]
        confirm_password=request.POST["confirm_password"]
        data=login_details.objects.all()
        for i in data:
            if(i.email==login_id1 and i.date_of_birth==birthday and i.logged_as==logged_as):
                if (new_password==confirm_password):
                    login_details.objects.filter(email=login_id1).update(password=new_password,confirm_password=confirm_password)
                    return redirect(set_success)
            else:
                return redirect(fail_to_set_new_password)

def product_details_view(request):
    id = request.GET['id']   
    product_data=product_upload_database.objects.filter(id=id)
    return render(request,"product_details_view.html",{'product_data':product_data})

# login messages
def login_fail(request):
    message="login_fail"
    return render(request,"message.html",{'message':message})
def login_success(request):
    user_id=request.session.get("username")
    csrf_token=request.COOKIES["csrftoken"]
    u1=cart_data.objects.filter(user_id=csrf_token).update(user_id=user_id)
    message="login_success"
    return render(request,"message.html",{'message':message})
# upload messages
def upload_fail(request):
    message="upload_fail"
    return render(request,"message.html",{'message':message})
def upload_success(request):
    message="upload_success"
    return render(request,"message.html",{'message':message})
# registration messages
def registration_fail(request):
    message="registration_fail"
    return render(request,"message.html",{'message':message})
def registration_success(request):
    message="registration_success"
    return render(request,"message.html",{'message':message})
def fail_to_set_new_password(request):
    message="fail_to_set_new_password"
    return render(request,"message.html",{'message':message})
def set_success(request):
    message="set_success"
    return render(request,"message.html",{'message':message})

def remove_cart_product(request):
    if request.method=="POST":
        csrf_token=request.COOKIES["csrftoken"]
        d1=cart_data.objects.filter(user_id=csrf_token)
        id=request.POST["id"]
        product_id=request.POST["product_id"]
        
        if len(d1)>=1:
            cart_data.objects.filter(user_id=csrf_token,id=id,product_id=product_id).delete()
            return redirect(personal_cart)
        else:
            user_id=request.session.get("username")
            cart_data.objects.filter(user_id=user_id,id=id,product_id=product_id).delete()
            return redirect(personal_cart)

def customer_service(request):
    return render(request,"cutomer_service.html")
def login_detail(request):
    username=request.session.get('username')
    logg=request.session.get('logg')
    if username==username and logg=="admin":
        user_data=login_details.objects.all().order_by('-id')
        return render(request,"user_data_show.html",{'user_data':user_data})
    else:
        return HttpResponse("only admins have the acess")
def delete_user(request):
    id = request.GET['id'] 
    
    if id != "17" : 
        login_details.objects.filter(id=id).delete()
        return redirect(login_detail)

    else:
        return redirect(d2)

def d2(request):
       return HttpResponse("!!! you can not Delete the Main Admin And The Developer of the WEb site contact the owner of the site Email:ajinkyaawari0011@gmail.com   MOB:9359790413 !!! if you again try this then admin have block you from the site access !!! so be aware and don't do that again !!!")

def product_data_delete(request):
    id = request.GET['id']
    product_upload_database.objects.filter(id=id).delete()
    return redirect(product_show)
def cart_show(request):
    username=request.session.get('username')
    logg=request.session.get('logg')
    if username==username and logg=="admin":
        cart_data_show=cart_data.objects.all().order_by('-id')
        return render(request,"cart_data_show.html",{'cart_data_show':cart_data_show})
    else:
        return HttpResponse("only admin have access")
def cart_empty(request):
    return render(request,"cart_empty.html")
def personal_info(request):
    user=request.session.get("username")
    login_data=login_details.objects.filter(email=user)
    for i in login_data:
        gender=i.gender
    return render(request,"personal_info.html",{'login_data':login_data,'gender':gender})

def address_store(request):
    user_id=request.session.get("username")
    if request.method=="POST":
       fname=request.POST["fname"]
       mobile=request.POST["mobile"]
       pincode=request.POST["pincode"]
       locality=request.POST["locality"]
       address=request.POST["address"]
       city=request.POST["city"]
       state=request.POST["state"]
       landmark=request.POST["landmark"]
       alternate_mobile=request.POST["alternate_mobile"]
       address_location=request.POST["address_location"]
       
       a1=address_data(fname=fname,mobile=mobile,pincode=pincode,locality=locality,address=address,city=city,state=state,landmark=landmark,alternate_mobile=alternate_mobile,address_location=address_location,user_id=user_id)
       a1.save()
       return redirect(show_address)
def add_address(request):
    return render(request,"add_address.html")
def show_address(request):
    user_id = request.session.get("username")
    address = address_data.objects.filter(user_id=user_id)
    login_data = login_details.objects.filter(email=user_id)

    # Initialize gender with a default value
    gender = ""
    name = ""
    for i in login_data:
        gender = i.gender
        name = i.fname

    # Razorpay integration
    client = razorpay.Client(auth=(settings.KEY, settings.SECRET))
    product_data = cart_data.objects.filter(user_id=user_id)

    if len(product_data) >= 1:
        l1 = len(product_data)
        l2 = []
        for i in product_data:
            l2.append(int(i.product_price))
        l3 = sum(l2)

        payment = client.order.create({'amount': l3 * 100, 'currency': 'INR'})  # Specify the currency here
        context = {
            'address': address,
            'gender': gender,
            'name': name,
            'product_data': product_data,
            'l1': l1,
            'l3': l3,
            'payment': payment  # Include the payment dictionary here
        }

        cart_instance = cart_data.objects.first()
        cart_instance.razor_pay_order_id = payment['id']
        cart_instance.save()

        return render(request, "address_show.html", context)
    else:
        return render(request, "address_show.html", {'address': address, 'gender': gender, 'name': name})

def delete_address(request):
    id = request.GET['id']   
    address_data.objects.filter(id=id).delete()
    return redirect(show_address)

def seller_product_show(request):
    user_id=request.session.get("username")
    logg=request.session.get("logg")
    if logg == "seller":
            product=product_upload_database.objects.filter(seller_id=user_id)
            return render(request,"seller_product_show.html",{'product':product})

def deactivate_account(request):
    return HttpResponse("deactivate account function ")