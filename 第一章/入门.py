print('欢迎进入教务系统')
print()
print('''
#########使用指南########
#      1.添加信息       #
#      2.修改信息       #
#      3.删除信息       #
#      4.查询信息       #
#      5.查看学生信息    #
#      6.统计学生信息    # 
#      7.退出系统       #
########################
''')
print()
student_list={}
while True:
    i=int(input('请输入操作：'))
    match i:
        case 1:
            name=input('请输入姓名:')
            if name in student_list:
                print('学生信息已存在')
            else:
                math=input('请输入数学成绩：')
                chinese=input('请输入语文成绩：')
                english=input('请输入英语成绩:')
                student_list[name]={'数学':math,'语文':chinese,'英语':english}
                print('登记成功')
        case 2:
            name=input('请输入学生姓名：')
            if name in student_list:
                math = input('请输入新数学成绩：')
                chinese = input('请输入新语文成绩：')
                english = input('请输入新英语成绩:')
                student_list[name] = {'数学': math, '语文': chinese, '英语': english}
            else:
                print('没有此学生')
        case 3:
            name=input('请输入您要删除的学生姓名：')
            if name in student_list:
                del student_list[name]
                print('删除成功')
            else:
                print('未查询到此学生')
        case 4:
            name=input('请输入您要查询的学生姓名：')
            if name in student_list:
                print('学生信息为：',student_list[name])
            else:
                print('没有此学生')
        case 5:
            if student_list=={}:
                print('没有学生信息')
            else:
                for name in student_list:
                    print(name,student_list[name])
        case 6:
            if len(student_list)==0:
                print('暂无信息')
            else:
                count = len(student_list)
                math_max = 0
                chinese_max = 0
                english_max = 0
                math_name = ""
                chinese_name = ""
                english_name = ""
                for name,score in student_list.items():
                    math=int(score['数学'])
                    chinese=int(score['语文'])
                    english=int(score['英语'])
                    if math > math_max:
                        math_max=math
                        math_name = name
                    if chinese > chinese_max :
                        chinese_max=chinese
                        chinese_name=name
                    if english > english_max:
                        english_max=english
                        english_name=name
                print(f'数学最高分为：{math_name}{math_max}')
                print(f'语文最高分为：{chinese_name}{chinese_max}')
                print(f'英语最高分为：{english_name}{english_max}')
                math_min = 100
                chinese_min = 100
                english_min = 100
                math_name = ""
                chinese_name = ""
                english_name = ""
                for name, score in student_list.items():
                    math = int(score['数学'])
                    chinese = int(score['语文'])
                    english = int(score['英语'])
                    if math < math_min:
                        math_min = math
                        math_name = name
                    if chinese < chinese_min:
                        chinese_min = chinese
                        chinese_name = name
                    if english < english_min:
                        english_min = english
                        english_name = name
                print(f'数学最低分为：{math_name}{math_min}')
                print(f'语文最低分为：{chinese_name}{chinese_min}')
                print(f'英语最低分为：{english_name}{english_min}')
                math_sum = 0
                chinese_sum = 0
                english_sum = 0
                for name, score in student_list.items():
                    math = int(score['数学'])
                    chinese = int(score['语文'])
                    english = int(score['英语'])
                    math_sum += math
                    chinese_sum +=chinese
                    english_sum +=english
                    print('数学平均分为:',math_sum/count)
                    print('语文平均分为：',chinese_sum/count)
                    print('英语平均分为：',english_sum/count)