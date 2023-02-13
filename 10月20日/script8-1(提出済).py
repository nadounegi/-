class student:
    def __init__(self,in_name,in_math,in_eng,in_jpn):#初期値を引数で受け取る
        self.name = in_name
        self.math = in_math
        self.eng = in_eng
        self.jpn = in_jpn
    
    def show_detail(self):#情報を表示
        print('生徒名',self.name)
        print('数学',self.math)
        print('英語',self.eng)
        print('国語',self.jpn)
   

    #情報を入力
    #生徒１の情報を入力
name =input("名前を入力")
math = int(input("数学の点数を入力してください"))
eng = int(input("英語の点数を入力してください"))
jpn = int(input("国語の点数を入力してください"))



    #生徒２の情報を入力
name2 =input("名前を入力")
math2 = int(input("数学の点数を入力してください"))
eng2 = int(input("英語の点数を入力してください"))
jpn2 = int(input("国語の点数を入力してください"))
 #インスタンス生成
joho = student(name,math,eng,jpn)
joho2 = student(name2,math2,eng2,jpn2)
 #情報を表示  
joho.show_detail()

joho2.show_detail()




















































































