from django.shortcuts import render, redirect
from django.http import JsonResponse
from .form import Login_Form, SignUp_Form, New_Product
from .models import User_Model, Products, Cart
import json
import jwt
from jwt.exceptions import DecodeError
from Clothing_Brand.settings import SECRET_KEY, ALGORITHM
# Create your views here.


def Validator(func):
    def wrapper(request, *args, **kwargs):
        # Retrieve token from cookies
        token = request.COOKIES.get("AccessToken")
        if not token:
            return redirect("login")  # Redirect if no token exist
        try:
            # Decode the token
            decoded = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
            print("Decoded:", decoded)
            request.decoded = decoded  # Dynamically attach to the request object
        except jwt.ExpiredSignatureError:
            print("Token has expired")
            return redirect("login")
        except jwt.InvalidTokenError:
            print("Invalid token")
            return redirect("login")

        # Call the original view function
        return func(request, *args, **kwargs)
    return wrapper


def home(request):
    auth = False
    admin = False
    token = request.COOKIES.get("AccessToken")
    if token:
        decoded = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
        if decoded['isadmin']:
            admin = True
        auth = True
    return render(request, "Home.html", {"auth": auth, "admin": admin})


def aboutus(request):
    return render(request, "AboutUs.html")


@Validator
def cart(request):
    userid = request.decoded["userID"]
    username = User_Model.objects.get(user_id=userid).username
    cart_data = Cart.objects.filter(userID=userid)
    data = []
    for i in cart_data:
        product_data = Products.objects.get(product_id=i.productID)
        data.append({"product_id": int(i.productID), "product_name": product_data.product_name, "product_photo": product_data.photo,
                    "product_price": product_data.price, "quantity": i.quantity})
    data_length = len(data);
    return render(request, "Cart.html", {"username": username, "data": data,"data_length": data_length})


@Validator
def addtocart(request, id):
    if request.method == "POST":
        quantity = json.loads(request.body.decode("utf-8"))
        data = Products.objects.get(product_id=id)
        data.quantity -= int(quantity["quantity"])
        data.save()
        userid = request.decoded["userID"]
        try:
            data = Cart.objects.get(productID=id)
            data.quantity += int(quantity["quantity"])
            data.save()
        except Cart.DoesNotExist:
            Cart.objects.create(userID=userid, productID=id,
                                quantity=int(quantity["quantity"]))
    return JsonResponse({"message": "Successful"})


@Validator
def suits_page(request, id):
    data = Products.objects.get(product_id=id)
    quantities = list(range(1, int(data.quantity) + 1))
    return render(request, "Suits_page.html", {"data": data, "quantities": quantities})


def suits(request):
    data = Products.objects.filter(product_type=0)
    return render(request, "Suits.html", {"data": data})


@Validator
def polo_page(request, id):
    data = Products.objects.get(product_id=id)
    quantities = list(range(1, int(data.quantity) + 1))
    return render(request, "Polo_Page.html", {"data": data, "quantities": quantities})


def polo(request):
    data = Products.objects.filter(product_type=1)
    return render(request, "Polo.html", {"data": data})


def login(request):
    code = None
    login_form = Login_Form()
    signup_form = SignUp_Form()
    if request.method == "POST":
        if "login" in request.POST:
            login_form = Login_Form(request.POST)
            signup_form = SignUp_Form()
            if login_form.is_valid():
                username = login_form.cleaned_data["username"]
                password = login_form.cleaned_data["password"]
                try:
                    data = User_Model.objects.get(username=username)
                    if data.password == password:
                        response = redirect('/')
                        user_data = {"userID": data.user_id,
                                     "isadmin": data.isadmin}
                        token = jwt.encode(
                            user_data, key=SECRET_KEY, algorithm=ALGORITHM)
                        response.set_cookie("AccessToken", token)
                        return response
                    else:
                        code = 404
                except:
                    code = 403
        elif "signup" in request.POST:
            signup_form = SignUp_Form(request.POST)
            login_form = Login_Form()
            if signup_form.is_valid():
                username = signup_form.cleaned_data["username"]
                password = signup_form.cleaned_data["password"]
                email = signup_form.cleaned_data["email"]
                dob = signup_form.cleaned_data["birth_date"]
                gender = signup_form.cleaned_data["gender"]
                try:
                    User_Model.objects.get(username=username)
                    code = 401
                except:
                    User_Model.objects.create(
                        username=username, password=password, email=email, dob=dob, gender=gender)
                    code = 201

            else:
                code = 404
    else:
        login_form = Login_Form()
        signup_form = SignUp_Form()

    response = render(request, 'Login.html', {
        'login_form': login_form,
        'signup_form': signup_form,
        'code': code
    })
    return response


@Validator
def delete(request, id):
    cart_data = Cart.objects.get(productID=id)
    quantity = cart_data.quantity
    data = Products.objects.get(product_id=id)
    data.quantity += quantity
    data.save()
    cart_data.delete()
    return redirect("cart")


@Validator
def adminp(request):
    admin = request.decoded['isadmin']
    if admin:
        user_data = User_Model.objects.all()
        product_data = Products.objects.all()
        product_form = New_Product()
        return render(request, "Admin.html", {"product_form": product_form, "user_data": user_data, "product_data": product_data})
    else:
        return JsonResponse({"Message": "Dont have Access to this Page !"})


def new_product(request):
    print("New Product Here")
    if request.method == "POST":
        product_form = New_Product(request.POST)
        if product_form.is_valid():
            product_name = product_form.cleaned_data['product_name']
            price = product_form.cleaned_data['price']
            quantity = product_form.cleaned_data['quantity']
            description = product_form.cleaned_data['description']
            rating = product_form.cleaned_data['rating']
            photo = product_form.cleaned_data['photo']
            product_type = product_form.cleaned_data['product_type']
            Products.objects.create(
                product_name=product_name,
                price=price,
                quantity=quantity,
                description=description,
                rating=rating,
                photo=photo,
                product_type=product_type
            )
    return redirect("admin")


def delete_user(request, id):
    data = User_Model.objects.get(user_id=id)
    data.delete()
    return redirect("admin")


def delete_product(request, id):
    data = Products.objects.get(product_id=id)
    data.delete()
    return redirect("admin")


def logout(request):
    response = redirect("/")
    response.delete_cookie("AccessToken")
    return response
