shopping_cart={}
def goods_price(card, way=0, sroce=0, express=0.0):
    total=0
    for item, s in card.items():
        cost = s['价格'] * s['数量']
        total += cost
    if total > 5000:
        if way <= total:
            total -= way
        if sroce // 100 <= total:
            total -= sroce // 100
    last_price = total + express
    return last_price
print('欢迎使用徐帅帮你买购物车系统')
print()
print("""
#####购物车系统菜单######
#     1.添加购物车     #
#     2.修改购物车     #
#     3.删除购物车     #
#     4.查询购物车     #
#     5.结算总价       #
#     6.退出系统       #     
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
                parse1=float(input('商品价格为:'))
                numb1=float(input('商品数量为:'))
                shopping_cart[name]={'价格':parse1,'数量':numb1}
                print('添加成功')
        case 2:
            name=input('请输入修改商品名称:')
            if name not in shopping_cart:
                print('商品不存在')
            else:
                parse_new=float(input('请输入新的价格：'))
                numb_new=float(input('请输入新的数量：'))
                shopping_cart[name]={'价格':parse_new,'数量':numb_new}
                print('修改成功')
        case 3:
            name = input('请输入删除商品名称:')
            if name in shopping_cart:
                del shopping_cart[name]
                print('删除成功')
            else:
                print('没有此商品:')
        case 4:
            name=input('请输入查询的商品:')
            if name in shopping_cart:
                print(shopping_cart[name])
            else:
                print('没有此商品:')
        case 5:
            if len(shopping_cart)==0:
                print('总价格为零')
            else:
                a=int(input('输入您的积分：'))
                b=int(input('输入您的优惠：'))
                c=int(input('请输入邮寄价格：'))
                print(goods_price(shopping_cart,sroce=a,way=b,express=c))
        case 6:
            print("再见")
            break

