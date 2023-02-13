class kenko:
  #登録番号を初期値100にする
  no = 100

#登録番号連番　メソッド
  @classmethod
  def no_method(cls):
    cls.no += 1
    return cls.no

# インスタンス生成の初期化定義
  def __init__(self,in_name,in_height,in_weight):
    self.no = kenko.no_method()
    self.name = in_name
    self.height = in_height
    self.weight = in_weight

#情報表示
  def show_method(self):
    print("---------------------------")
    print("登録番号:",self.no)
    print("名前:",self.name)
    print("身長:",self.height)
    print("体重:",self.weight)

#名前判定
  def name_check_method(self,if_name):
    if if_name == self.name:
      return True
    else:
      return False

#身長変更　メソッド
  def change_height_method(self,new_height):
    self.height = new_height

#隊中変更メソッド
  def change_weight_method(self,new_weight):
    self.weight = new_weight

#メイン処理
#配列作成
kenko_list = []
sw = 0
#処理番号を入力
process_no = int(input('1:新規登録、2:身長の変更、3:体重の変更、4:終了　=>'))
#新規登録
if process_no == 1:
  print("-----新規登録-----")
  k_name = input("名前を入力")
  k_height = int(input("身長を入力"))
  k_weight = int(input("体重を入力"))

  #リストに追加
  addres = kenko(k_name,k_height,k_weight)
  kenko_list.append(addres)
