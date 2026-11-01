from ast import parse

shopping_cart={}
print('欢迎使用徐帅帮你买购物车系统')
print()
print("""
#####购物车系统菜单######
#     1.添加购物车     #
#     2.修改购物车     #
#     3.删除购物车     #
#     4.查询购物车     #  
#     5.退出系统       #
####################### 
""")



while True:
    i=int(input('请输入操作:'))
    match i:
        case 1:
            name=input('商品名称为:')
            if name in shopping_cart:
                print('商品已在购物车')
            else:
                parse1=input('商品价格为:')
                numb1=input('商品数量为:')
                shopping_cart[name]={'价格':parse1,'数量':numb1}
                print('添加成功')
        case 2:
            name=input('请输入修改商品名称:')
            if name not in shopping_cart:
                print('商品不存在')
            else:
                parse_new=input('请输入新的价格：')
                numb_new=input('请输入新的数量：')
                shopping_cart[i]={'价格':parse_new,'数量':numb_new}
                print('修改成功')
        case 3:
            name = input('请输入删除商品名称:')
            if name in shopping_cart:
                del shopping_cart[i]
                print('删除成功')
            else:
                print('没有此商品:')
        case 4:
            name=input('请输入查询的商品:')
            if name in shopping_cart:
                print(shopping_cart[i])
            else:
                print('没有此商品:')
        case 5:
            print("再见")
            break

