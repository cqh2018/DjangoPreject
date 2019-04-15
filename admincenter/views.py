from django.shortcuts import render

from django.http import StreamingHttpResponse

# Create your views here.
def downloadTest(request):
    def file_iterator(file_name, chunk_size=512):#用于形成二进制数据
        with open(file_name,'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
    the_file_name ="D:\\涉敏日志金库审批日志.xls"#要下载的文件路径
    response =StreamingHttpResponse(file_iterator(the_file_name))#这里创建返回
    response['Content-Type'] = 'application/vnd.ms-excel'#注意格式
    response['Content-Disposition'] = 'attachment;filename="模板.xls"'#注意filename 这个是下载后的名字
    return response

def index(request):
    return render(request,'admincenter/download.html')

