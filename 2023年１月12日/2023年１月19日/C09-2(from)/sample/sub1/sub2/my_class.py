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