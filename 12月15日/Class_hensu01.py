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
  def kazu_print(cls):
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

#メイン処理
#人数を入力してリストを作成
stu = []
kazu = int(input("人数を入力してください"))
for i in range(kazu):#入力した人数の通り、繰り返す以下のを処理する
  print("----------------------")
  k_name = input("名前を入力")
  k_bango = int(input("学校番号を入力"))
  k_year = int(input("学年を入力"))
  #リストに追加
  addres = students(k_name,k_bango,k_year)
  stu.append(addres)

#会員表示
for add in stu:
  add.show()

#各学校の人数カウント
for add in stu:
  add.count_method()

#割合クラスメソッド呼び出し
students.wariai_method(kazu)

#人数と中学生の割合表示
students.kazu_print()