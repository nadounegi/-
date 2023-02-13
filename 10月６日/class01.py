'''
クラスを作成
ファイル名：class01.py
クラス型のクラス変数の定義のみ
実行は出来ません。
'''

class Student:
    def __init__(self):
        self.name = ''
        self.math = 0
        self.english = 0
        self.japanese = 0
#インスタンス変数の指定（None)
class Student:
    def __init__(self):
        self.name = None
        self.math = None
        self.english = None
        self.japanese = None

#初期値を引数で受け取る
class Student:
    def __init__(self,in_name,in_math,in_eng,in_jpn):
        self.name = in_name
        self.math = in_math
        self.english = in_eng
        self.japanese = in_jpn
#引数に初期値を設定する
class Student:
    def __init__(self,in_name='',in_math=0,in_eng=0,in_jpn=0):
        self.name = in_name
        self.math = in_math
        self.english = in_eng
        self.japanese = in_jpn       