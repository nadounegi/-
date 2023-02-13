class student: #クラスを定義
    def __init__(self,in_name,in_height,in_weight):
        self.name = in_name
        self.height = in_height
        self.weight = in_weight
   #表示メソッド
    def show_detail(self):
        print("名前",self.name)
        print("身長",self.height)
        print("体重",self.weight)
        
#内容を代入    
name = "佐藤"
height = 180
weight = 75
#インスタンスの生成
iti = student(name,height,weight)
#情報表示
iti.show_detail()