import shlex


# def cs_line(r:float):
#    """
#    计算面积与周长
#    :param r:半径
#    :return:面积与周长
#    """
#    return round(r*r*3.14),round(2*3.14*r)
# print(cs_line(2))
# def triangle(d,h):
#    return round(d*h/2,1)
# print(triangle(3,4))
# def namber(s):
#    """"
#   计算元音字母数
#    :param s: 输入的字母
#    :return: 元音数
#    """
#    total=0
#    for i in s:
#       if i in 'aeiouAEIOU':
#          total+=1
#    return total
# print(namber('asedfe'))
# def grade(s):
#     max_s=max(s)
#     min_s=min(s)
#     avg_s=sum(s)/len(s)
#     return max_s,min_s,avg_s
#
# s=[int(i) for i in input('输入数字：').split(',')]
# max_grade,min_grade,avg_grade=grade(s)
# print(max_grade,min_grade,avg_grade)
# s=('e,wr,e,wrw')
# print(s.split(','))
def jc(n):
    if n == 1 :
        return 1
    else:
        return jc(n-1)*n
print(jc(5))
def goods_price(*args,way=0,sroce=0,express=0.0):
    prise1=[goods[1]*goods[2] for goods in args]
    cost=sum(prise1)





