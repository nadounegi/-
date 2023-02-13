#引数無のインスタンス変数の初期化
class Student:
    def __init__(self,in_name='',in_math=0,in_eng=0,in_jpn=0):
        self.name = in_name
        self.math = in_math
        self.english = in_eng
        self.japanese = in_jpn       
#インスタンスの生成
stu1 = Student('高野',90,60,70)
print(type(stu1))