class Student:
    def __init__(self,in_name,in_math,in_eng,in_jpn):#初期値を引数で受け取る
        self.name = in_name
        self.math = in_math
        self.english = in_eng
        self.japense = in_jpn

    def show_detail(self):#メソッド定義（表示する処理）
        print('生徒名',self.name)
        print('数学',self.math)
        print('英語',self.english)
        print('国語',self.japense)
#メソッド定義（合計と平均数を求める処理）
    def get_total_sore(self):
        return self.math + self.english + self.japanese
    def get_average_score(self):
        return self.get_total_sore()/3
