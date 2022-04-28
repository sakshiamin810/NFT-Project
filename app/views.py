from ast import Return
from urllib import request
from django.shortcuts import render,redirect
from .models import *


# Create your views here.
def IndexPage(request):
    return render(request,"app/index.html")
 
def activitypage(request):
    return render(request,"app/activity.html")

def articalpage(request):
    return render(request,"app/artical.html")

def blogpage(request):
    return render(request,"app/blog.html")

def chatpage(request):
    return render(request,"app/chat.html")

def collectionpage(request):
    return render(request,"app/collection.html")

def contactpage(request):
    return render(request,"app/contact.html")

def creatorepage(request):
    return render(request,"app/creatore.html")

def editprofilepage(request):
    return render(request,"app/edit-profile.html")

def faqpage(request):
    return render(request,"app/faq.html")

def headerpage(request):
    return render(request,"app/header.html")

def index2darkpage(request):
    return render(request,"app/index-2-dark.html")

def index2page(request):
    all_pro = product.objects.all()
    return render(request,"app/index-2.html",{'allpro':all_pro})

def index3darkpage(request):
    return render(request,"app/index-3-dark.html")

def index3page(request):
    return render(request,"app/index-3.html")


def index4darkpage(request):
    return render(request,"app/index-4-dark.html")

def index4page(request):
    return render(request,"app/index-4.html")

def indexdarkpage(request):
    return render(request,"app/index-dark.html")

def indexpage(request):
    return render(request,"app/index.html")

def itemdetailspage(request):
    return render(request,"app/item-details.html")

def loginpage(request):
    return render(request,"app/login.html")

def newsletterpage(request):
    return render(request,"app/newsletter.html")

def postdetailpage(request):
    return render(request,"app/post-detail.html")

def privacypage(request):
    return render(request,"app/privacy.html")

def profilepage(request):
    return render(request,"app/profile.html")

def rankingpage(request):
    return render(request,"app/ranking.html")

def registerpage(request):
    return render(request,"app/register.html")

def submitrequestpage(request):
    return render(request,"app/submit-request.html")

def walletpage(request):
    return render(request,"app/wallet.html")

def RegisterUser(request):
    img = request.FILES['img']
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    cpassword = request.POST['cpassword']

    if password == cpassword:
        newuser = User.objects.create(image=img,name=name,email=email,password=password)
        return render(request,"app/login.html")
    else:
        message = "Password and Cpassword is not Match"
        return render(request,"app/register.html")


def LoginUser(request):
    email = request.POST['email']
    password = request.POST['password']

    user = User.objects.get(email=email)
    if user:
        if user.password == password:
            request.session['name'] = user.name
            request.session['email'] = user.email
            request.session['password'] = user.password
            request.session['img'] = user.image.url
            return redirect('index2')
        else:
            message = "Password is wrong"
            return render(request,"app/login.html")
    else:
        message = "User doesnot exist"
        return render(request,"app/login.html")











