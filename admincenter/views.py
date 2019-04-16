from django.shortcuts import render,HttpResponse

from django.http import StreamingHttpResponse

from openpyxl import Workbook, load_workbook
from openpyxl.writer.excel import save_virtual_workbook, ExcelWriter
import time
# Create your views here.

def download(request):
    strtime = request.POST.get('strtime')
    endtime = request.POST.get('endtime')
    from admincenter import tests
    exportSenseLog = tests.ExportSenseLog()
    startStr = strtime
    endStr = endtime
    print(endStr)
    print(type(endStr))
    the_file_name = "download//t_sens_.xlsx"
    title = (
        'logid', 'logname', 'account', 'acctype', 'systemid', 'accesstype', 'dip', 'clientip', 'url', 'optypeid',
        'logtime',
        'opcontent', 'dataname', 'datarange', 'datalevel', 'pingju', 'pingjutype', 'hbasession')
    exportSenseLog.exportExcel(startStr, endStr, the_file_name, title)
    import json
    ret = {'status': True, 'error': None, 'data': None}
    return HttpResponse(json.dumps(ret))

def downloadTest(request):
    def file_iterator(file_name, chunk_size=512):  # 用于形成二进制数据
        with open(file_name, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
    the_file_name = "download//t_sens_.xlsx"
    response = StreamingHttpResponse(file_iterator(the_file_name))  # 这里创建返回
    response['Content-Type'] = 'application/vnd.ms-excel'  # 注意格式
    # response['Content-Disposition'] = 'attachment;filename="testeser.xls"'#注意filename 这个是下载后的名字
    response['Content-Disposition'] = 'attachment;filename="t_sens_log.xlsx"'  # 注意filename 这个是下载后的名字
    return response


def index(request):
    return render(request,'admincenter/download.html')


