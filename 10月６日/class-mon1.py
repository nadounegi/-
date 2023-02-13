class animal:
  def __init__(self,in_kind,in_name,in_weight,in_age):
    self.kind = in_kind
    self.name = in_name
    self.weight = in_weight
    self.age = in_age

  def show_detail(self):
    print("種類",self.kind)
    print("名前",self.name)
    print("体重",self.weight)
    print("年齢",self.age)

  def set_weight(self,in_wei):
    self.weight = in_wei

#メイン処理
kind = input("種類を入力")
name = input("名前を入力")
weight = int(input("体重を入力"))
age = int(input("年齢を入力"))

#インスタンスの生成
iti = animal(kind,name,weight,age)

#情報表示
iti.show_detail()
weight2 = int(input("変更体重を入力"))
iti.set_weight(weight2)

#情報表示
iti.show_detail()
ni = animal(kind,name,weight,age)
#情報表示
ni.show_detail()
ni.set_weight(weight2)
#情報表示
ni.show_detail()