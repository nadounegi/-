'''
ファイル名：class02.py
クラス型のクラス変数の定義
インスタンスの生成を行い
実行結果を見てみる
'''
#引数無のインスタンス変数の初期化
class Student:
    def __init__(self):
        self.name = ''
        self.math = 0
        self.english = 0
        self.japanese = 0
#インスタンスの生成
stu1 =Student()
print(type(stu1))