from django.shortcuts import render
from django.http import HttpResponse 
from .models import *
# Create My views here.
def home(request):
    if "email" in request.session:
        return render(request,"myapp/index.html")
    else:
        return render(request,"myapp/login.html")

def login(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "chairman":
            cid = chairman.objects.get(User_id = uid)
            context = {
                        "uid" : uid,
                        "cid" : cid,
            }
            return render(request,"myapp/index.html",context)
        else:
            pass
                
    elif request.POST:
        print("submit button hit ")
        p_email = request.POST['email']
        p_password = request.POST['password']
        print("======> Email = ",p_email)
        try:
            uid = User.objects.get(email = p_email)
            print("===> uid Object",uid)
            if uid.password == p_password:
                if uid.role=="Chairman":
                    cid = chairman.objects.get(user_id = uid)
                    request.session['email'] = uid.email
                    print(cid)
                    context = {
                        "uid" : uid,
                        "cid" : cid,
                    }
                    return render(request,"myapp/index.html",context)
                else:
                    pass
            else:
                print("===> invalid password")
                context = {
                "e_msg" : "Invalid Password"
            }
            return render(request,"myapp/login.html",context)
            # get data from database - validation query
        except:   
                context = {
                    "e_msg" : "Invalid email or Password"}
        return render(request,"myapp/login.html",context)
    
    else:
        print("only page refresh")
    return render(request,"myapp/login.html")


def logout(request):
    if "email" in request.session:
        del request.session['email']
        return render(request,"myapp/login.html")
    else:
        return render(request,"myapp/login.html") 