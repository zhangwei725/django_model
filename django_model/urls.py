from django.conf.urls import url
from django.contrib import admin

from model01 import views as v1
from model02 import views as v2
from homework import views as hw

# 二级路由
# 路由  映射 url地址(path)----> 视图函数(控制层)
urlpatterns = [
    url('admin/', admin.site.urls),
    url('index/', v1.index),
    url('all/', v2.find_all),
    url('add/', v2.add),
    url('filter/', v2.find_filter),
    url('order/', v2.find_order),
    url('values/', v2.find_values),
    url('group/', v2.find_group),
    url('annotate/', v2.find_annotate),
    url('raw/', v2.find_raw),
    url('chained/', v2.find_chained),
    url('f/', v2.find_f),
    url('get/', v2.find_get),
    url('save/', v2.save1),
    url('create/', v2.create),
    url('bulk/', v2.bulk_create),
    url('update/', v2.update),
    url('update1/', v2.update1),
    url('emps/', hw.emp_list),
    url('shops/', hw.shops),

]
