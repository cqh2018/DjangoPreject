from django.shortcuts import render,redirect,HttpResponse

# Create your views here.

from app01 import models
def orm(request):
    #创建
    models.UserInfo.objects.create(username = "root",password = "134",gender='1',user_type_id='1',user_group_id=1)
    # dic = {'username':'boco','password':'222'}
    # models.UserInfo.objects.create(**dic)
    # obj = models.UserInfo(username = "root",password = "131142")
    # obj.save()
    #查
    # result = models.UserInfo.objects.all()
    # result = models.UserInfo.objects.filter(username='root')
    # result = models.UserInfo.objects.filter(username='root',password='1342')
    # print(result)
    # for row in result:
    #     print(row.id,row.username,row.password)
    #删除
    # models.UserInfo.objects.filter(id=3).delete()
    #更新
    # models.UserInfo.objects.all().update(password='22222')
    return HttpResponse('orm')

def index(request):
    return render(request,'index.html')
def user_info(request):
    if request.method == 'GET':
        user_list = models.UserInfo.objects.all()
        group_list = models.UserGroup.objects.all()

        return render(request, 'user_info.html', {'user_list': user_list,'group_list':group_list})
    elif request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        models.UserInfo.objects.create(username=u,password=p)
        # user_list = models.UserInfo.objects.all()
        # return render(request, 'user_info.html', {'user_list': user_list})
        return redirect('/app01/user_info/')


def user_detail(request,nid):
    obj = models.UserInfo.objects.filter(id=nid).first()
    #取单条数据，如果不存在，直接报错
    # models.UserInfo.objects.get(id=nid)
    return render(request, 'user_detail.html', {'obj': obj})

def user_del(request,nid):
    models.UserInfo.objects.filter(id=nid).delete()
    #取单条数据，如果不存在，直接报错
    # models.UserInfo.objects.get(id=nid)
    return redirect('/app01/user_info/')
def user_edit(request,nid):
    if request.method == 'GET':
        obj = models.UserInfo.objects.filter(id=nid).first()
        return render(request,'user_edit.html',{'obj':obj})
    elif request.method == 'POST':
        # nid = request.POST.get('id')
        print(nid)
        u = request.POST.get('username')
        p = request.POST.get('password')
        models.UserInfo.objects.filter(id=nid).update(username=u,password=p)
        return redirect('/app01/user_info/')


def login(request):
    # models.UserGroup.objects.create(caption='dba')
    #
    # models.UserGroup.objects.filter(uid=1).update(caption='ceo1')
    obj=models.UserGroup.objects.filter(uid=1).first()
    obj.caption = 'ceooo'
    obj.save()
    if request.method == "GET":
        return render(request,'login.html')

    elif request.method == "POST":
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        obj = models.UserInfo.objects.filter(username=u,password=p).first()
        # obj = models.UserInfo.objects.filter(username=u,password=p).count()
        if obj:
            return  redirect('/app01/index/')
        else:
            return  render(request,'login.html')






