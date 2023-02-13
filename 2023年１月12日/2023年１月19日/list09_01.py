# ---　関数を定義している部分　ここから---#
def plus(x=0,y=0):
  return x + y #戻り値　ｘ+ｙ

def minus(x=0,y=0):
  return x - y #戻り値　ｘ-ｙ
#--- ここまで ----------#

#--- クラスを定義している部分 ここから----#
class Account:
  def __init__(self,name,no,balance):#フィールド定義
    self.__name = name
    self.__no = no
    self.__balance = balance
  
  def show_detail(self):#情報表示
    print('口座名義',self.__name)
    print('口座番号',self.__no)
    print('残高',self.__balance)
#------ここまで----------------------------#

#--------関数やクラスを利用している部分 ここから----------------#
#関数を呼び出し、利用する
result1 = plus(10,3)  
result2 = minus(10,3)

print('10 + 3 =',result1)
print('10 - 3 =',result2)

#クラスを呼び出し、利用する
account1 = Account('佐藤',1,1000)
#情報を表示する
account1.show_detail()
#------ここまで----------------------------#
