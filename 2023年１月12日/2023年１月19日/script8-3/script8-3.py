import my_class
#インスタンス生成
students = [my_class.Student('佐藤',100,40,65),my_class.Student('丸山',64,98,79),
            my_class.Student('三村',48,87,92),my_class.Student('古川',83,81,74)]

namae = input('生徒名を入力')
flg = True

for stu in students:
    if namae  == stu.name:
        stu.show_detail()
        flg = False
        break
        
if flg:
    print('存在しません')