from django.test import TestCase
import json
ret = {'status': True, 'error': None, 'data': '111'}
#字典转换成字符串
result = json.dumps(ret)
print(result)
print(type(result))
'''
输出:
{"status": true, "error": null, "data": "111"}
<class 'str'>
'''

