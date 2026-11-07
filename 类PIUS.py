class Goods:
    def __init__(self,price,name,number):
        self.price=price
        self.name=name
        self.number=number
    def __str__(self):
        return f'商品名称：{self.name} | 商品价格:{self.price} | 商品数量:{self.number}'
    def change(self,price,number):
        self.price=price
        self.number=number

class Shoppingcar:
    system_version=1.0
    system_name="购物车系统"
    def __init__(self):
        self.shopping_list=[]
    def add_shopping_car(self):
        name=input('请输入商品名称：')
        for i in self.shopping_list:
            if i.name==name:
                print('商品已存在')
                return
        price=int(input('请输入价格：'))
        number=int(input('请输入数目：'))
        if price> 0 and number>0:
                s=Goods(price,name,number)
                self.shopping_list.append(s)
                print('添加成功')
    def change(self):
        name = input('请输入要修改商品名称：')
        for i in self.shopping_list:
            if i.name==name:
                while True:
                    price = int(input('请输入价格：'))
                    number = int(input('请输入数目：'))
                    if price > 0 and number > 0:
                        i.change(price,number)
                        print('修改成功')
                        break
                    else:
                        print('格式错误')
                        continue
            else:
                print('没有此商品')
    def delete (self):
        name = input('请输入要删除商品名称：')
        for i in self.shopping_list:
            if i.name == name:
                self.shopping_list.remove(i)
                print("删除成功")
            else:
                print('没有查找到此商品')
    def show(self):
        name = input('请输入商品名称：')
        for i in self.shopping_list:
            if i.name == name:
                print(i)
            else:
                print('没有此商品')
    def display(self):
        for i in self.shopping_list:
            print(i)
    def run (self):
        print(f'欢迎使用购物车系统{self.system_version}')
        print()
        print("""
      #####购物车系统菜单######
      #     1.添加购物车     #
      #     2.修改购物车     #
      #     3.删除购物车     #
      #     4.查询购物车     #
      #     5.展示购物车     #
      #     6.退出系统       #     
      ####################### 
      """)
        print()
        while True:
           choice=input('请输入操作：')
           match choice:
               case '1':
                   self.add_shopping_car()
               case '2':
                   self.change()
               case '3':
                   self.delete()
               case '4':
                   self.show()
               case '5':
                   self.display()
               case '6':
                   print('See you later!')
                   break
               case _ :
                   print('操作失误')
                   continue

if __name__ == '__main__':
    shopping_car=Shoppingcar()
    shopping_car.run()





