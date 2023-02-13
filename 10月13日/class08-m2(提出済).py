class student:
    def __init__(self,in_name,in_height,in_weight):
        self.name = in_name
        self.height = in_height
        self.weight = in_weight
    #クラスを定義
    def show_detail(self):
        print("名前",self.name)
        print("身長",self.height)
        print("体重",self.weight)
#メイン処理
for i in range(3):
    name = input("名前を入力")
    height = float(input("身長を入力"))
    weight = int(input("体重を入力"))

#インスタンスの生成
    iti = student(name,height,weight)  
    iti.show_detail()