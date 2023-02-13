class students:
  kaiin_no = 100 #会員番号の初期値は１００にする

  #カウントの初期値
  count1 = 0
  count2 = 0
  count3 = 0
  #割合の初期値
  wariai = 0

#割合の計算の
  @classmethod #クラスメソッド
  def wariai_method(cls,kazu):
    cls.wariai = int(cls.count2/kazu*100)
    return cls.wariai
  

  #会員番号の登録を連番で行う
  @classmethod#クラスメソッドを行う
  def kain_method(cls):
    cls.kaiin_no += 1
    return cls.kaiin_no

  #クラス変数の表示 
  @classmethod #クラスメソッド
  def kazu_print(cls,kazu):
    print("--------------------")
    print('小学校の人数:',cls.count1)
    print('中学校の人数:',cls.count2)
    print('高校の人数:',cls.count3)
    print('中学校の割合:',cls.wariai_method(kazu),"%")

  #初期化 フィールド定義
  def __init__(self,in_name,in_bango,in_year):#コンストラクタ定義
    #クラスメソッドを呼び出して代入
    self.kaiin_no = students.kain_method()
    self.name = in_name
    self.bango = in_bango
    self.year = in_year 


#表示メソッド　 インスタンス
  def show(self):
    if self.bango == 1:
      gago = '小学校'
    elif self.bango == 2:
      gago = '中学校'
    else:
      gago = '高校'
    print("--------会員情報----------")
    print("会員番号：",self.kaiin_no)
    print("名前：",self.name)
    print("学校：",gago)
    print("学年：",self.year)
  

#各学校の人数カウントダウンメソッド
  def count_method(self):
    if self.bango == 1:
      students.count1 += 1
    elif self.bango == 2:
      students.count2 += 1
    else:
      students.count3 += 1