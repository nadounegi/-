'''
クラスを作成
ファイル名：class04.py
インスタンス変数の利用
'''
class Student:
    def __init__(self, in_name,in_math,in_eng,in_jpn):
        self.name = in_name
        self.math = in_math
        self.english = in_eng
        self.japanese = in_jpn
#インスタンスの生成
stu1 = Student('高野',90,60,70)
#情報表示
print('生徒名',stu1.name)
print('数学',stu1.math)
print('英語',stu1.english)
print('国語',stu1.japanese)
#インスタンス変数を直接変更する(通常はメソッドで行う)
stu1.japanese =75
print('変更後の国語',stu1.japanese)
