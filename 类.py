#对学生类的定义
class Student:
    def __init__(self, name,english,chinese,math ):
        self.name = name
        self.english = english
        self.chinese=chinese
        self.math = math
    def __str__(self):
        return f"姓名：{self.name} | 数学：{self.math},英语{self.english},语文：{self.chinese}"
    def change(self,english=None,math=None,chinese=None):
        if english is not None:
            self.english=english
        if math is not None:
            self.math=math
        if chinese is not None:
            self.chinese=chinese
# if __name__ == '__main__':
#     student1=Student("徐帅",150,150,150)
#     print(student1)
#     student1.change(english=125,math=145)
#     print(student1)
#     print(student1)

class Education:
    system_version=1.0
    system_name="教务管理系统"
    def __init__(self):
        self.student_list=[]

    def add_student(self):
        name=input('请输入学生姓名：')
        for i in self.student_list:
            if i.name==name:
                print('学生已存在')
                return
        chinese=int(input('请输入学生语文成绩='))
        math=int(input('请输入学生数学成绩='))
        english=int(input('请输入学生英语成绩='))
        if 0<=chinese<=150 and 0<=math<=150 and 0<=english<=150:
            student=Student(name,english,chinese, math)
            self.student_list.append(student)
            print('添加成功')
        else:
            print('成绩输入错误')
    def change(self):
        name = input('请输入学生姓名：')
        for i in self.student_list:
            if i.name==name:
                print(i)
                while True:
                    chinese = int(input('请输入修改的语文成绩='))
                    math = int(input('请输入修改数学成绩='))
                    english = int(input('请输入修改英语成绩='))
                    if 0 <= chinese <= 150 and 0 <= math <= 150 and 0 <= english <= 150:
                        i.change(english,math,chinese)
                        print(i)
                        print('修改成功')
                        break
                    else:
                        print('成绩输入错误')
                        continue
            else:
                print('未录入此学生')
    def delete (self):
        name=input('请输入要删除的学生：')
        for i in self.student_list:
            if i.name==name:
                self.student_list.remove(i)
                print('学生已删除')
                return
            else:
                print('未录入此学生')
                return

    def ask(self):
        name = input('请输入要查询的学生：')
        for i in self.student_list:
            if i.name==name:
                print(i)
                return
            else:
                print('未录入此学生')
    def display(self):
        for i in self.student_list:
            print(i)

    def funtion(self):
        print(f'欢迎使用教务管理系统{Education.system_version}')

        while True:
            print()
            print("""
            #########使用指南########
            #      1.添加信息       #
            #      2.修改信息       #
            #      3.删除信息       #
            #      4.查询信息       #
            #      5.查看学生信息    #
            #      6.退出系统       # 
            ########################
                    """)
            choice=input('请输入指令：')
            match choice:
                case '1':
                    self.add_student()
                case '2':
                    self.change()
                case '3':
                    self.delete()
                case '4':
                    self.ask()
                case '5':
                    self.display()
                case '6':
                    print('See you again')
                    break
                case _:
                    print('命令错误')

if __name__ == '__main__':
    example=Education()
    example.funtion()














