import json
a=0
b=0
# a=int(input('请输入a='))
# b=int(input('请输入b='))
# c=a+b
# print("输出a+b=",c)

#----------------------------------------------------函数--------------------------
#def function():  函数定义

def fun2(name,age):
      print('name is:'+name+'\n'+"age=",age)

#调用方式1：
fun2('hdn',22)    
#调用方式2：

fun2(name='hdb',age=11)

      #函数使用默认 形参 定义函数

def fun3(work,time=10):
      print('i work locate:%s;work Time is:%d' % (work,time))

fun3('zmkg')

fun_list=list(range(11,21,2))
f_list2=list(range(21,31,2))   

def fun4(list_f):
      mm=0
      if 13 in fun_list:
            mm=list_f.remove(13)
      nn=list_f.pop()
      print('the mm=',mm,'\n','the list=',list_f,'\n','the nn=',nn)

fun4(fun_list)

print('查看函数fun4是否修改列表的值；；；现在fun_list=',fun_list)

print('\n','\n')
      #------------------------------------
   
fun4(f_list2[:])

print('查看函数fun4是否修改列表的值；；；现在f_list=',f_list2)

#--------------------------------------------------------------传递任意多值

#def function(*name)    使用函数function时  参数可以是任意多个
      
#def function(home,*name)    使用函数function时  参数可以是任意多个

#def funciton(home,**person)  **person是一个字典；调用举例： function(myHome,bb="hjl",mm='zxy',dd='hdc')    bb="hjl",mm='zxy',dd='hdc'就是**person的实例化






#---------------------------------------------------------文件操作----------------------------------

with open('/home/hdb/HDB_tempt/0—文档/tBox_Arm.txt')  as filename:
      lines=filename.readlines()    #将所有行 保存到 lines中
      for in_line in filename:
            print(1)    #逐行打印



for lline in lines:
      print(lline)
