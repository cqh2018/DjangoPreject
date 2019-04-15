from django.shortcuts import render,HttpResponse
from django.utils.safestring import mark_safe
from utils import pagination

def index(request):
    from django.core.handlers.wsgi import WSGIRequest
    #封装了所有用户请求的信息
    print(request.environ)
    for k,v in request.environ.items():
        print(k,v)
    print(request.environ['HTTP_USER_AGENT'])
    return HttpResponse('ok')

LIST = []
for i in range(209):
    LIST.append(i)

def fenye(request):
    current_page = request.GET.get('p',1)
    current_page = int(current_page)
    page_obj = pagination.Page(current_page,len(LIST))
    data = LIST[page_obj.start:page_obj.end]
    page_str=page_obj.pag_str('/app03/fenye/')
    return render(request,'app03/fenye.html',{'li':data,'page_str':page_str})


