# i=0
# while i<5:
#     name=input('请输入用户名：')
#     code=input("请输入密码：")
#     if name=="123" and code=="123":
#         print('登陆成功')
#         break
#     elif name=="133" and code=="456":
#         print('登陆成功')
#         break
#     elif name=="" or code=="":
#         print('用户名或密码为空')
#         continue
#     else:
#         i=i+1
#         print('密码或用户名错误')
# if i==5:
#     print('错误五次，已锁定')
# import random
# numb=random.randint(1,100)
# while True:
#     n=int(input('请输入数字：'))
#     if n==numb:
#         print('恭喜你，猜对了，666')
#         break
#     elif n>numb:
#         print('您猜的数大了')
#     elif n<numb:
#         print('您猜的数小了')
# total=0
# for i in range(1,1001):
#     if i%5==0:
#         total=i+total
# print(total)
# count_a=0
# count_j=0
# s="asdfghjkkdfsasdfghjkljjhgfdsadfghjkhgfdsadfghjkhgfdsasdfgh"
# for i in s:
#     if i=="a":
#         count_a+=1
#     elif i=="j":
#         count_j+=1
# numb_list = []
# for i in range(10):
#     n=int(input('请输入数字：'))
#     numb_list.append(n)
# numb_list.sort()
# print('您输入的数字为：',numb_list)
# print('最大值为：',numb_list[-1])
# print('最小值为：',numb_list[0])
# print('平均数为：',sum(numb_list)/len(numb_list))
# numb_list1=[27,34,23,45,32,55,46 ]
# numb_list2=[24,35,78,69,30,35,79,46]
# numb_list=numb_list1+numb_list2
# print(numb_list)
# numb_new=[]
# for numb in numb_list:
#     if numb not in numb_new:
#         numb_new.append(numb)
# numb_new.sort()
# print(numb_new)
# numb=[i**2 for i in range(1,21) if i%2==0]
# print(numb)
# list1=['w','a','r','t','m','c','g','o']
# list2=['r','p','h','j','l','q']
# list3=['w','s','a','d','x','v']
# new_list=[]
# for i in list1+list2+list3:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)
# list1=[i**2 for i in range(1,31) if i%3==0 or i%5==0]
# print(list1)/
# list3=[i for i in list2 if i>=0 ]
# print(list2[-1:5:-1])
# s='hello-world-hello-name'
# a=s.find('l')
# print(a)
# b=s.count('l')
# print(b)
# s1=s.upper()
# print(s1)
# s2=s.lower()
# print(s2)
# z=s.split('l')
# print(z)
# s.strip()
# q=s.replace('l','  ')
# print(q)
# print(s.startswith('l'))
# print(s.endswith('l'))
# print(s)
# mail=input('请输入邮箱：')
# if mail.count('@')==1 and mail.count('.')>=1:
#     print('邮箱正确')
# else:
#     print('邮箱错误')
# if  '.'in mail and mail.count('@')==1:
#     print('邮箱正确')
# list_1=[]
# s=input('请输入：')
# if s[::-1]==s :
#     print('是回文')
# else:
#     print('不是回文')
# for i in s[::-1].upper():
#     list_1.append(i)
# for i in list_1:
#    print(i)
t1=(12,34,356,354,4332,)
print(t1)
print(type(t1))
print(t1[2])
print(t1.count(12))
print(t1.index(4332))
t1=(666,)