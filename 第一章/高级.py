
# total=10000
# numb=int(input('输入密码='))
# if numb==123456789:
#     a=int(input('取款金额='))
#     if a<=total:
#        print('取款成功',f' 您的余额为={total-a}')
#     else:
#        print('余额不足')
# else:
#     print('密码错误')
# s=int(input('你的成绩为='))
# if s>=60:
#     print('合格')
# else:
#     print('不合格')
# numb=int(input('数字为='))
# if numb>0:
#     print('正数')
# elif numb==0:
#     print('0')
# else:
#      print("负数")
# numb=int(input('数字为='))
# if numb % 2==0:
#     print('偶数')
# else:
#     print('奇数')
# numb=int(input('请输入您的成绩='))
# if numb>85:
#     print('优秀')
# elif 60<numb<85:
#     print('良好')
# else:
#     print('不及格')
# f=int(input('本月消耗度数为='))
# if f<=2880:
#     cost=f*0.4883
#     print(f'费用为={cost}')
# elif f>2880 and f<=3000:
#     cost=f*0.5383
#     print(f'费用为={cost}')
# else:
#     cost=f*0.7883
#     print(f'费用为={cost}')
# a=int(input('请输入数字='))
# b=int(input('请输入数字='))
# c=input('请输入符号：')
# match c:
#     case "*":
#         print(f'{a}*{b}=',a*b)
#     case "/"if b!=0:
#         print(f'{a}/{b}=',a/b)
#     case "+":
#         print(f'{a}+{b}=',a+b)
#     case "-":
#         print(f'{a}-={b}=',a-b)
#     case _:
#         print('错误')
# O=input('请进行下一步操作：')
# match O:
#     case '上'|'w'|'W':
#         print('前进')
#     case "下"|"s"|"S":
#         print("后退")
#     case"左"|"a"|"A":
#         print("向左")
#     case'右'|'D'|'d':
#         print('向右')
#     case" "|'跳跃':
#         print('跳')
#     case'j'|"攻击":
#         print('发动攻击')
#     case'esc'|'ESC'|"退出":
#         print("退出游戏")
# i=0
# while i<10:
#     print('徐帅爱打飞机')
#     i+=1
# else:
#     print('完毕')
# total=0
# i=1
# while i<100:
#     if i%2!=0:
#         total+=i
#     i+=1
# print(f'奇数和为：{total}')
# total=0
# for i in range(1,101,2):
#     total+=i
# else:
#     print("和为=",total)
# m=int(input('长度为='))
# n=int(input('宽度为='))
# for j in range(n):
#     for i in range(m):
#         print("*",end="  ")
#     print()
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{j}x{i}={i*j}',end='\t')
#     print()
# h=int(input('请输入高度='))
# for i in range(1,h+1):
#     for j in range(1,h+1):
#         print(f'{j}',end='  ')
#     print()
# s=int(input('请输入大小：'))
# for i in range(1,s+1):
#     for j in range(1,s+1):
#         if (i+j)%2!=0:
#             print('*',end='  ')
#         else:
#             print('+',end='  ')
#     print()
# while True:
#     name=input('请输入用户名：')
#     code=input("请输入密码：")
#     if name=="" or code=="":
#         print('用户名或密码为空')
#         continue
#     elif name=='123' and code=='123':
#         print('登陆成功')
#         break
#     elif name=='124' and code=='124':
#         print('登陆成功')
#         break
#     else:
#         print('密码或用户名错误')














