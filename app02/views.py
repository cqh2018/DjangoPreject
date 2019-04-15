from django.shortcuts import render,HttpResponse,redirect
from app02 import models
# Create your views here.
def business(request):
    v = models.Business.objects.all()
    #<QuerySet [<Business: Business object (1)>, <Business: Business object (2)>, <Business: Business object (3)>, <Business: Business object (4)>]>
    v2 = models.Business.objects.all().values('id','caption')
    #<QuerySet [{'caption': '运维', 'id': 1}, {'caption': '开发', 'id': 2}, {'caption': '市场部', 'id': 3}, {'caption': '测试部', 'id': 4}]>
    v3 = models.Business.objects.all().values_list()
    #<QuerySet [(1, '运维', 'sa'), (2, '开发', 'sa'), (3, '市场部', 'sa'), (4, '测试部', 'sa')]>
    return render(request,'app02/business.html',{'v':v,'v2':v2,'v3':v3})


# def host(request):
#     v1 = models.Host.objects.filter(nid__gt=0)
#     for row in v1:
#         print(row.nid,row.ip,row.b)
#     v2 = models.Host.objects.filter(nid__gt=0).values('nid','hostname','b_id','b__caption')
#     for row in v2:
#         print(row['nid'],row['hostname'],row['b_id'],row['b__caption'])
#     v3 = models.Host.objects.filter(nid__gt=0).values_list('nid','hostname','b_id','b__caption')
#     return render(request, 'app02/host.html', {'v1': v1, 'v2': v2, 'v3': v3})
#     # return HttpResponse('host')

def host(request):
    if request.method == 'GET':
        v1 = models.Host.objects.filter(nid__gt=0)
        v2 = models.Host.objects.filter(nid__gt=0).values('nid','hostname','b_id','b__caption')
        v3 = models.Host.objects.filter(nid__gt=0).values_list('nid','hostname','b_id','b__caption')
        b_list = models.Business.objects.all()
        return render(request, 'app02/host.html', {'v1': v1, 'v2': v2, 'v3': v3,'b_list':b_list})
    elif request.method == 'POST':
        h = request.POST.get('hostname')
        i = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('b_id')
        models.Host.objects.create(hostname=h,ip=i,port=p,b_id=b)
        # return render(request, 'app02/host.html')
        return redirect('/app02/host')
def test_ajax(request):
    import json
    ret = {'status': True, 'error': None, 'data': None}
    try:
        h = request.POST.get('hostname')
        i = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('b_id')
        if len(h) > 5 and h:
            models.Host.objects.create(hostname=h, ip=i, port=p, b_id=b)
            # return HttpResponse('ok')
        else:
            ret['status']=False
            ret['error']='太短了'
    except Exception as e:
        ret['error']='请求错误'
    return HttpResponse(json.dumps(ret))

def edit_ajax(request):

    if request.method == 'POST':
        nid = request.POST.get('nid')
        h = request.POST.get('hostname')
        i = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('b_id')
        print(request.POST)
        models.Host.objects.filter(nid=nid).update(hostname=h,ip=i,port=p,b_id=b)
        return HttpResponse('ok')
    else:
        return HttpResponse('no')
def app(request):
    if request.method == 'GET':
        app_list = models.Aplication.objects.all()
        host_list = models.Host.objects.all()
        return render(request, 'app02/app.html', {'app_list': app_list, 'host_list': host_list})
    elif request.method == 'POST':
        app_name = request.POST.get('app_name')
        host_list = request.POST.getlist('host_list')
        print(app_name,host_list)
        obj = models.Aplication.objects.create(name=app_name)
        obj.r.add(*host_list)
        return HttpResponse('ok')
def ajax_add_app(request):
    import json
    ret = {'status': True, 'error': None, 'data': None}
    app_name = request.POST.get('app_name')
    host_list = request.POST.getlist('host_list')
    print(app_name,host_list)
    obj = models.Aplication.objects.create(name=app_name)
    obj.r.add(*host_list)
    return HttpResponse(json.dumps(ret))

def ajax_edit_app(request):
    import json
    ret = {'status': True, 'error': None, 'data': None}
    aid = request.POST.get('nid')
    appname = request.POST.get('app')
    host_list = request.POST.getlist('host_list')
    print(aid)
    print(request.POST)
    obj=models.Aplication.objects.get(id=aid)
    obj.name=appname
    obj.r.set(host_list)
    obj.save()
    return HttpResponse(json.dumps(ret))
def ajax_delete_app(request):
    import json
    ret = {'status': True, 'error': None, 'data': None}
    aid = request.POST.get('aid')
    host_list = request.POST.getlist('host_list')
    print(aid+'11')
    # print(request.POST)
    print(host_list)
    obj=models.Aplication.objects.filter(id=aid).delete()

    return HttpResponse(json.dumps(ret))












