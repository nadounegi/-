class score:
  #クラス変数定義
  login_no = 100
  s_count = 0
  a_count = 0
  b_count = 0
  c_count = 0
  d_count = 0
  s_wari = 0


    #初期化 フィールド定義
  def __init__(self,in_name,in_gaku_no):
    self.login_no = score.no_method()
    self.name = in_name
    self.gaku_no = in_gaku_no
    self.tensu = score.score_method()

  #登録番号の連番処理 クラスメソッド
  @classmethod
  def no_method(cls):
    cls.login_no += 1
    return cls.login_no

  #評価カウント表示
  @classmethod
  def hyoka_print(cls):
    print("--------------------------------")
    print("S評価の人数",cls.s_count)
    print("A評価の人数",cls.a_count)
    print("B評価の人数",cls.b_count)
    print("C評価の人数",cls.c_count)
    print("D評価の人数",cls.d_count)
    print("S評価の割合",cls.swari_method(ninsu),"%")
    print("平均数：",cls.ave_method(ninsu),"です")

  #全員の成績の平均点を求め
  @classmethod
  def ave_method(cls,ninsu):
    cls.average = int(score.tensu/ninsu)
    return cls.average

  #評価を定義する

  def show(self):
    if 250 <= self.tensu <=300:
      hyoka = "S評価"
    elif 200 <= self.tensu <= 249:
      hyoka = "A評価"
    elif 199 <= self.tensu <= 150:
      hyoka = "B評価"
    elif 100 <= self.tensu <= 149:
      hyoka = "C評価"
    else:
      hyoka = "D評価"

    print("-----個人情報-------------")
    print("登録番号：",self.login_no)
    print("学籍番号：",gaku_no)
    print("名前：",name)
    print("成績：",self.tensu)
    print("評価：",hyoka)
   

#評価カウントダウン

  def hyoka_count(self):
    if 250 <= self.tensu <= 300:
      score.s_count += 1
    elif 200 <= self.tensu <= 249:
      score.a_count += 1
    elif 199 <= self.tensu <= 150:
      score.b_count += 1
    elif 100 <= self.tensu <= 149:
      score.c_count += 1
    else:
      score.d_count += 1

   
  #S評価の割合
  @classmethod
  def swari_method(cls,ninsu):
    cls.s_wari = int(cls.s_count/ninsu*100)
    return cls.s_wari

  #成績を求め
  @classmethod
  def score_method(cls):
    cls.tensu = int(java + python + arugo)
    return cls.tensu


#メイン処理
#配列の作成
stu = []
#キーボードから人数を入力
ninsu = int(input("人数を入力"))
#入力した人数の通り、繰り返し処理
for i in range(ninsu):
  print("----------------------------")
  gaku_no = int(input("学籍番号を入力"))
  name = input("名前を入力")
  java = int(input("Javaの点数を入力"))
  python = int(input("pythonの点数を入力"))
  arugo = int(input("アルゴリズムの点数を入力"))
#リストに追加,タブを気を付けて
  addres = score(name,gaku_no)
  stu.append(addres)

#個人情報表示
for add in stu:
  add.show()

#各評価をカウントダウン
for add in stu:
  add.hyoka_count()
#割合の表示
score.swari_method(ninsu)


#評価カウントダウン表示
score.hyoka_print()

