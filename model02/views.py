from django.shortcuts import render
from django.http import HttpResponse

# 查询
from model02.models import Goods, Emp

"""

# 当我们掉用方式方法的时候底层帮我们去转化成相应sql语句去执行

1>查询所有
SQL : SELECT  * FROM 表名 
ORM : 模型名称.objects.all()

2>控制行
SQL : SELECT  * FROM  表名  WHERE 条件
ORM : 模型类名.objects.filter(条件)
3>控制列
SQL :  SELECT  列名 别名,列名 别名  FROM  表名

ORM :  模型类名.objects.values(*args)



4>排序
sql :
    SELECT  * FROM 表名  
    where 条件
    order by 字段

ORM : 模型类名.objects.order_by(排序字段)
5>分组函数查询
SQL :  SELECT   AVG(列名)  
       FROM  表名  
       
ORM :    模型类名.objects.aggregate(别名=分组函数(属性))  
         字典对象  
#      分组查询
    
    
6>关联查询
7>分页查询
"""


def add(request):
    goods = Goods(goods_img='https://ws1.sinaimg.cn/large/0065oQSqgy1fwgzx8n1syj30sg15h7ew.jpg', goods_name='小甜甜',
                  goods_info='不要998,只要198,小甜甜带回家,白天么么哒,晚上啪啪啪~!', goods_price='198.0', goods_status=1)
    goods.save()
    return HttpResponse('添加数据')


def find_all(request):
    # [模型对象,模型对象]
    # 查询表里面所有的数据
    # 返回的是一个QuerySet对象(可以理解是一个列表,列表里面的每一个元素都是一个模型对象)
    goods = Goods.objects.all()
    return HttpResponse('查询所有')


def find_filter(request):
    # [模型对象实例]
    # **kwargs
    # WHERE goods_status=1
    # 限定符 __
    goods = Goods.objects.filter(goods_status=1)
    return HttpResponse('过滤行')


# 排序
def find_order(request):
    goods = Goods.objects.all().order_by('-goods_id', 'goods_price')
    for good in goods:
        print(good.goods_id)
    return HttpResponse('排序')


# 过滤列
def find_values(request):
    # [{'key':值},{}]
    goods = Goods.objects.all().values('goods_id', 'goods_name', 'goods_img')
    return HttpResponse('过滤列')


from django.db.models import Min, Max, Sum, Avg, Count, Q, F


# 分组函数 AVG MIN MAX COUNT SUM
def find_group(request):
    # 查询价格最低的商品信息
    # 返回的是字典对象
    goods = Goods.objects.all().aggregate(Min('goods_price'))
    goods = Goods.objects.all().aggregate(Max('goods_price'))
    goods = Goods.objects.all().aggregate(sum=Sum('goods_price'))
    print(goods['sum'])

    return HttpResponse('分组函数')


# 分组   group by

# SELECT  SUM(GOODS_PRICE)
#     FROM  goods
# group by  goods_status

def find_annotate(request):
    # 查询价格最低的商品信息
    # 返回的是字典对象
    # Goods.objects.values(属性).annotate(分组函数)
    goods = Goods.objects.values('goods_status').annotate(sum=Sum('goods_price'),
                                                          avg=Avg('goods_price'),
                                                          count=Count('*'))
    return HttpResponse('分组统计')


# SELECT  DISTINCT  goods_status FROM GOODS
def find_raw(request):
    # 如果模型查询的api不够用的 你可以使用原生sql
    # [模型对象,模型对象]
    sql = 'SELECT * FROM goods g WHERE  g.goods_status=1 order by g.goods_price desc '
    goods = Goods.objects.raw(sql).distinct('goods_status')
    for good in goods:
        print(good.goods_price)
    return HttpResponse(r'原生SQL支持')


# AND  &
# OR   |
# not  ~  取反
# 链式编程

def find_chained(request):
    # 所谓的懒加载就是,当我们执行完返回QuerySet对象的方法时,只会给我们生产sql语句,并不会去执行数据库的查询
    # 当我们从QuerySet对象中获取数据的时候才回去执行数据库操作
    # WHERE login_name='jiaojiao'  AND  phone=1
    q = Q(login_name='jiaojiao') & Q(phone=1)
    # and操作
    qs = Emp.objects.filter(Q(login_name='jiaojiao') & Q(phone=1)).order_by('-join_date')
    # 或的操作
    qs = Emp.objects.filter(Q(login_name='jiaojiao') | Q(phone=1)).order_by('-join_date')
    # 取反操作
    qs = Emp.objects.filter(~Q(login_name='jiaojiao') | ~Q(phone=1)).order_by('-join_date')
    qs = Emp.objects.filter(q).order_by('-join_date')
    return HttpResponse('链式编程---懒加载')


# SELECT age+1 FROM emp
# 字符串住家++??
def find_f(request):
    # 支持四则运算
    emp = Emp.objects.filter(emp_id=1).update(age=F('age') + 1)
    return HttpResponse('链式编程---懒加载')


# ======= 不返回QuerySet对象=======

def find_get(request):
    # get 方法
    # 注意事项  该方法只能返回一条记录
    # 如果查询的结果集中多余一条记录.该方法直接抛出异常    MultipleObjectsReturned
    # 如果查询的结果集为空  该方法也会直接抛出异常 DoesNotExist
    try:
        good = Goods.objects.get(goods_id=1)
        # good = Goods.objects.get(goods_name='hahahah')
        # good = Goods.objects.get(goods_status=1)
    except Goods.DoesNotExist as dne:
        print(dne)
    except Goods.MultipleObjectsReturned as mor:
        print(mor)

    # 建议使用安全的方法 推荐写法
    # goods = Goods.objects.filter(goods_name='hahahah')
    # if goods:
    #     good = goods.first()

    # Goods.objects.count() 统计条数

    # SELECT  COUNT(*)  FORM  GOODS
    print(Goods.objects.filter(goods_status=1).count())
    return HttpResponse('get方法')


# 限定符

# 保存方法

def save1(request):
    try:
        emp = Emp(login_name='马云', phone='10000', email='11111@163.com', role='1')
        emp.save()
    except Exception as e:
        pass
    return HttpResponse('添加数据')


# 添加数据(尽量少用)
def create(request):
    try:
        emp = Emp.objects.create(login_name='马化腾', phone='10000', email='1111@163.com', role='1')
    except Exception as e:
        pass
    return HttpResponse('添加数据')


def bulk_create(request):
    try:
        emp_list = [Emp(login_name=f'test{i}', phone='10000', email=f'11111111{i}@163.com', role='1') for i in
                    range(1001, 20001)]
        emp_list = Emp.objects.bulk_create(emp_list, batch_size=1000)
    except Exception as e:
        pass
    return HttpResponse('批量添加')


# save()  更新操作
# update_fields
# 如果是更新操作 建议使用update_fields
# 默认情况下django会修改所有的字段
# 建议使用save做更新操作的时候指定更新字段

def update(request):
    try:
        # 获取客服端传递数据
        emp_id = request.GET.get('id', 0)
        login_name = request.GET.get('name')
        emp_list = Emp.objects.filter(emp_id=emp_id)
        emp = emp_list.first() if emp_list else None
        if emp:
            emp.login_name = login_name
            emp.save(update_fields=['login_name'])
    except:
        return HttpResponse('修改失败')
    return HttpResponse('添加添加')


# 通过objects的update方法
#  UPDATE `emp` SET `login_name` = '凉凉', `phone` = '112' WHERE `emp`.`emp_id` = 1
def update1(request):
    try:
        Emp.objects.filter(emp_id=1).update(login_name='凉凉', phone=112)
    except:
        return HttpResponse('修改失败')
    return HttpResponse('添加添加')


