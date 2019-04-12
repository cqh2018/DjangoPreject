from django.shortcuts import render,redirect,HttpResponse
from cmdb import models


# Create your views here.



USER_DICT = {
    '1':{'name':'root1','email':'root@qq.com'},
    '2':{'name':'root2','email':'root@qq.com'},
    '3':{'name':'root3','email':'root@qq.com'},
    '4':{'name':'root4','email':'root@qq.com'},
    '5':{'name':'root5','email':'root@qq.com'},
    '6':{'name':'root6','email':'root@qq.com'},
}

# USER_LIST = {
#     {'name':'root'},
#     {'name':'root'},
#     {'name':'root'},
# }

def login(request):
    # 包含用户提交的所有信息
    # 获取用户提交方法
    # print(request.method)
    error_msg = ""
    if request.method == "POST":
        # 获取用户通过POST提交过来的数据
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        if user == 'root' and pwd == "123":
            # 去跳转到
            return redirect('/home')
        else:
            # 用户密码不配
            error_msg = "用户名或密码错误"
    return render(request,'login.html', {'error_msg': error_msg})

def detail(request,nid):
    # return HttpResponse(uid)
    # nid=request.GET.get('nid')
    detail_info = USER_DICT[nid]
    return render(request,'detail.html',{'detail_info':detail_info})

def index(request):

    return render(request,'index.html',{'user_dict':USER_DICT})
# def home(request):
#     USER_LIST = models.getUser()
#     if request.method == "POST":
#         # 获取用户提交的数据 POST请求中
#         u = request.POST.get('username')
#         e = request.POST.get('email')
#         g = request.POST.get('gender')
#         id = 5
#         temp = {'id':id,'username': u, 'email': e, "gender": g}
#         USER_LIST.append(temp)
#     return render(request, 'test/home.html', {'user_list':  USER_LIST})

def del_host(request):
    USER_LIST = models.getUser()

    print("响应del_host")
    if request.method == "POST":
        # 获取用户提交的数据 POST请求中
        nid = request.POST.get('nid')
        print("提交过来的nid"+nid)
        models.deleteUserById(int(nid))

        # e = request.POST.get('email')
        # g = request.POST.get('gender')
        # id = 5
        # temp = {'id':id,'username': u, 'email': e, "gender": g}
        return render(request, 'test/home.html', {'user_list': USER_LIST})
    else:
        USER_LIST = models.getUser()
        return render(request, 'test/home.html', {'user_list': USER_LIST})
        # USER_LIST.append(temp)

from django.views import View
class Home(View):
    def dispatch(self, request, *args, **kwargs):
        print('before')
        result = super(Home,self).dispatch(request, *args, **kwargs)
        print('after')
        print(result)
        return result

    def get(self,request):
        print("get")
        USER_LIST = models.getUser()
        return render(request, 'test/home.html', {'user_list': USER_LIST})
    def post(self,request):
        print("post")
        USER_LIST = models.getUser()
        if request.method == "POST":
            # 获取用户提交的数据 POST请求中
            u = request.POST.get('username')
            e = request.POST.get('email')
            g = request.POST.get('gender')
            id = 5
            temp = {'id': id, 'username': u, 'email': e, "gender": g}
            USER_LIST.append(temp)
        return render(request, 'test/home.html', {'user_list': USER_LIST})



# def login(request):
#     # string = """
#     # <form>
#     #     <input type='text' />
#     # </form>
#     #
#     # """
#     # f = open('templates/login.html', 'r', encoding='utf-8')
#     # data = f.read()
#     # f.close()
#     # return HttpResponse(data)
#     return render(request,'login.html')

# def home(request):
#     return HttpResponse('<h1>CMDB</h1>')

# 主机管理
# 防火墙
# 。。。
