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

    def get_total_score(self):#合計を計算する
        return self.math + self.eng + self.jpn

    def get_average_score(self):#平均数を計算する
        return self.get_total_score/3


    #情報を入力
name =input("名前を入力")
math = int(input("数学の点数を入力してください"))
eng = int(input("英語の点数を入力してください"))
jpn = int(input("国語の点数を入力してください"))
print()
#インスタンス生成
joho = student(name,math,eng,jpn)
#情報を表示
joho.show_detail()
#合計＆平均数
total =joho.get_total_score()
ave = joho.get_average_score()

#合計＆平均数を出力
print("合計値",total)
print("平均数",ave)
