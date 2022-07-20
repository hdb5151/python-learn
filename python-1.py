import json
import requests

if True:
    print(1)
else:
    print(2)
print("hello world")

#response=requests.get('https://randomuser.me/api/?results=10')
#data=response.json()

name = '郝大彬'
print(name)

h_age = 23

print('the person\'s name is %s,his age=%d' % (name, h_age))
"""
a=input("输入一个数 a")
b=input("输入一个数 b")
c=int(a)+int(b)
print("a+b="+str(c))
"""
r = range(10)  #range 3种形式    range(stop):创建一个[0,stop]之间的整数序列，步长是1;
#  range(start，stop)创建一个[start,stop]之间的整数序列，步长是1;
#  range(srart,stop,step)创建一个[start,stop]之间的整数序列，步长是step;
print(list(r))

print(2 in r)
print(3 not in r)

m_1a = 6
m_1b = 9
print(m_1b, m_1a)
m_1a, m_1b = m_1b, m_1a  #数据互换
print(m_1b, m_1a)
m2_sum = 0

for m_2a in range(2, 11, 2):
    m2_sum += m_2a
print(m2_sum)

for _ in range(3):
    print("fuck")
if m_1a > 10:
    #
    print("somthing")
#
"""列表（list）创建方式"""
#使用[]创建
list1 = ['hello', 'world', 112]
print(list1)

#使用内置函数list()创建
list2 = list(["hello", "world", 113])
print(list2)

#----------------------列表.索引--------------------------#
# 1、list.index(list[n])      在list列表中索引 元素 list[n]..n取值0~N-1;;或0=-N~-1
#2、list.index(lins[n],start_num,end_num) 在list列表中的start_num~end_num之间索引 元素 list[n]
print(list1[0], list2[2])
list3 = list(["ni", 0, "hao", 1, 'the', 3, 'fuch'])
print(list3.index(1))  #查找索引
print(list3.index("ni", 0, 4))  #[0]~[4]之间查找

#----------------------列表.切片--------------------------#  注意：切片 会生产一个新的列表
# list[start:stop:step] 如果不写 则默认为1

list4 = [10, 20, 0, 40, 50, 60, 7, 0, 80, 90]

print(list4[1:6:])  #默认步长为1
print(list4[1:6:2])  #步长为2
print(list4[:6:2])  #默认start为第一个元素

print(id(list4))
list4_1 = list4[1::2]
print(list4_1)  #默认stop为最后一个元素

#print 类似于c语言printf 格式输出

print("list4_1地址==%d" % (id(list4_1)))
#-------------------------------in /// not in-----------------------#

print(88 in list4)  #false    88不在list4

print(10 not in list4)  #false      10在list4

#-------------------------------列表.增加-----------------------#

#append()   在列表的末尾添加一个元素            不生产新对象
list4.append(90)
print(list4)

#extend()   在列表的末尾至少添加一个元素
list4.extend(list3)
print(list4)

#insert()   在列表的任意位置添加一个元素
list4.insert(1, 99)  #在索引是1的位置上添加元素 99
print(list4)

#切片       在列表的任意位置添加至少一个元素
list5 = ['hello', 'world', 'fine']
list5_1 = [1, 2, 3, 4, 5]
print(id(list5))
list5[1:] = list5_1
print(id(list5), list5)

list5[1:1:] = list5_1  #在index 1 的后面插入list5_1
print(list5)

#-------------------------------列表.删除-----------------------#
#remove()   一次删除一个元素；；重复元素只删除第一个，无返回值。。。；；元素不存在着 抛出ValueError...

#pop()      删除一个指定索引位置上的元素；返回，被删除的那个元素；指定索引不存在 跑出ValueError;; 不指定索引，则删除列表中最后一个元素

#切片       一次至少删除一个元素
list6 = list(range(0, 100, 10))
print(list6)
print('list6 address is %d' % (id(list6)))
list6_1 = list6[2:3:]  #使用切片删除一个切片时会产生一个新的列表，但是下面的这个表示不会产生新列表
list6[2:3:] = []  #这种切片方式不会产生新的列表
print(list6_1)
print('list6_1 address is %d' % (id(list6_1)))
print('list6 address is %d' % (id(list6)))
#clear()    清空列表

#del        删除列表

#-------------------------------列表.修改-----------------------#

list7 = list(range(0, 10, 2))
print(list7)

list7[0] = 100
print(list7)

# 使用切片 进行多修改

list7[2:4:] = [11, 22]  #相当于list7[2]=11   list7[3]=22
print(list7)

#-------------------------------列表.排序-----------------------#

#sort（） 进行升序排序， 如果sort(reverse=True) 则进行降序排序。。。。不会产生新的列表对象

list8 = list(range(12, 0, -1))

print(list8)
list8.sort()
print("升序排序：", list8)

list8.sort(reverse=True)
print("降序排序：", list8)

#-----------使用内置函数 sorted 则会产生一个新的列表对象。。。

list8_1 = sorted(list8)
print('使用内置函数sorted 进行升序排序，生成一个新的列表', list8_1)

list8_2 = sorted(list8_1, reverse=True)
print('使用内置函数sorted 进行降序排序，生成一个新的列表', list8_2)

#------------列表表达式-------------------------------------------#

list9 = [i for i in range(1, 10)]
print(list9)

list9_1 = [i for i in range(1, 11, 2)]
print(list9_1)

list9_2 = [i * 2 for i in range(1, 11, 2)]
print(list9_2)

#=============================================字典=================================#

#--------------------字典.创建------------------#
dict1 = {'name': 'hdb', 'age': 10}
print(dict1)
print(type(dict1))

dict2 = dict(name='jiangnan', age=18)
print(dict2)

#--------------------字典.获取------------------#
dict3 = dict(num1=1, num2=2, num3=3, num4=4, num5=5)
print(dict3)
#1、使用[key]进行获取value值.. 如果key不存在时会抛出一个valueError
print("dict3['num3']=", dict3['num3'])

#2使用  dict.get(key),  如果key不存在 则返回none
print("num[4]=", dict3.get('num4'))

#--------------------字典.判断------------------#
print('num1' in dict3)

if dict3['num1'] == 2:
    print('字典判断：', False)
elif dict3['num2'] == 2:
    print("字典判断：", True)

#--------------------字典.删除------------------#
print('字典.删除')
del dict3['num1']  #删除指定的键值对
print(dict3)

#dict3.clear()    清空字典

#--------------------字典.增加，修改------------------#
print('字典.增加，修改')

print(dict3)

dict3['num6'] = 6  #增加 ’num':6

print(dict3)

dict3['num6'] = 666  #修改 ’num':666
print(dict3)

#--------------------字典.获取视图------------------#
print('字典.获取视图  dict.keys(),dict.value(),dict.items()')

#获取字典中 所有的 keys
dict_key = dict3.keys()
print(dict_key)
print(type(dict_key))
print(type(list(dict_key)))

#获取字典中 所有的 value
##
#
#
#

#获取字典中 所有的 键值对 使用items

dict_items = dict3.items()
print(dict_items)

#--------------------字典.生成式------------------#
print('字典.生成式')

dict4_key = ['n1', 'n2', 'n3', 'n4', 'n5', 'n7']
dict4_value = list(range(1, 10))

dict4 = {
    dict4_key: dict4_value
    for dict4_key, dict4_value in zip(dict4_key, dict4_value)
}
print(dict4)

#------------------------字典.嵌套------------------------#
#------列表中嵌套字典
print('列表中嵌套字典')
dict5_1 = dict(n1=1, n2=2, n3=3, n4=4, n5=5)
dict5_2 = dict(m1=1, m2=2, m3=3, m4=4, m5=5)
dict5_3 = dict(l1=1, l2=2, l3=3, l4=4, l5=5)

list_dict5 = list([dict5_1, dict5_2, dict5_3])

print("列表中嵌套字典", list_dict5)

#------字典中嵌套列表
print('字典中嵌套列表')

d_list1 = list(range(1, 10))
d_list2 = list(range(11, 20))

dict6 = dict(ten=d_list1, twen=d_list2)
print('字典中嵌套列表', dict6)

#------字典中嵌套字典
print('字典中嵌套字典')

dict7 = {
    "dict7_1": {
        "na": 'hh',
        'age': 33,
        'state': 'good'
    },
    'dict7_2': 'what',
    'dict7_3': {
        "name": "the world",
        "age": "long age"
    }
}

print(type(dict7['dict7_1']['na']))

#=========================================元组=========================================== 
#------------------------元组.创建------------------------#
# -- 元组为不可变序列， 创建完成后不可以进行增，删，改，查。 
# -- 元组中包含可变序列元素（列表或字典）时，可以对该元素进行增，删，改，查。 但是指向的位置不可更改

#------元组 创建--1
tuple_t=('python','ni',1,'hao')

#------元组 创建--2  使用内置函数创建
tuple_t2=tuple(('python','ni',1,'hao'))

#------元组  只包含一个元组的元素需要使用逗号和小括号
tuple_t3=(10,)

#=========================================集合=========================================== 

#------------------------集合.创建------------------------#
# -- 集合相当于没有 value 的字典

#------集合 创建--1
set_t={'hello','world',77}

#------集合 创建--2 使用内置函数
set_t2=set({'hello','world',77})
set_t3=set(range(6))
set_t4=set([1,2,3,'45'])

#------------------------集合.操作方法------------------------#
# 集合的判断操作：-> in 或 not in

#------集合元素的新增操作：
# --> 调用add()方法，一次增加一个元素
set_t.add(100)

# --> 调用updata()一次至少添加一个元素
set_t2.update({1,2,3})  # 添加集合
set_t2.update([5,6,7])  # 添加队列

#------集合元素的删除操作：
# --> remove()方法，一次删除一个指定元素，如果元素不存在 则抛出KeyError

# --> discard()方法， 一次删除一个指定元素，如果元素不存在 不抛出错误

# --> pop()方法，一次只删除一个任意元素。 不能带参

# --> clear()  清空集合

#------------------------集合.关系------------------------#
#------ 两个集合是否相同（元素相同，就相同）

#------ 一个集合是两一个集合的子集，可调用方法 issubset()判断
print(set_t2.issubset(set_t))

#------ 一个集合是另一个集合的超集，可调用方法issuperset()
print(set_t2.issuperset(set_t))

#------ 两个集合是否没有交集， 可调用方法 isdisjoin() 进行判断
print(set_t2.isdisjoin(set_t))

#------ 求两个集合"交集"的方法： intersection()
set_t4=set_t3.intersection(set_t)

#------ 求两个集合"并集"的方法： union()
set_t4=set_t3.union(set_t)

#------ 求两个集合差集的方法： difference()