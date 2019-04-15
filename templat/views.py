from django.shortcuts import render

# Create your views here.

def template1(request):
    user_list = [1,2,3,4]

    return render(request,'templat/template1.html',{'u':user_list})
def template2(request):
    name = 'root'

    return render(request,'templat/template2.html',{'name':name})
def template3(request):
    status = '已删除'

    return render(request,'templat/template3.html',{'status':status})
def template4(request):
    name = 'LLSkdKLD'
    return render(request,'templat/template4.html',{'name':name})



