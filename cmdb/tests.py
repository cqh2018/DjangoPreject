from django.test import TestCase

# Create your tests here.

import os

file_path = os.path.join('cmdb','1.jpg')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR,'1.jpg')
print(file_path)
print(BASE_DIR)
print(os.path)
