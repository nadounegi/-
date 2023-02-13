class Student:
    def __init__(self, in_name,in_math,in_eng,in_jpn):
        self.name = in_name
        self.math = in_math
        self.english = in_eng
        self.japanese = in_jpn
#情報の表示メソッド
    def show_detail(self):
        print('生徒名',self.name)
        print('数学',self.math)
        print('英語',self.english)
        print('国語',self.japanese)
#合計点を返すメソッド
    def get_total_score(self):
        return self.math + self.english + self.japanese
#数学の点数を変更するメソッド    
    def set_math(self,new_math):
        self.math = new_math
#インスタンス生成を行い実行する
stu1 = Student('高野',90,60,70)
#情報表示メソッドの呼び出し
stu1.show_detail()
#1行開業の為のprint関数
print()
#数学の点数を変更するメソッドの呼び出し
stu1.set_math(80)
#再度情報表示メソッドの呼び出し
stu1.show_detail()

ts1 = stu1.get_total_score()
print('合計点',ts1)