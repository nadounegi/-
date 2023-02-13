class student:
    def __init__(self,in_name,in_height,in_weight):
        self.name = in_name
        self.height = in_height
        self.weight = in_weight
    #表示メソッド
    def display_method(self):
        print("名前",self.name)
        print("身長",self.height)
        print("体重",self.weight)
    #名前を判定する 名前で検索するときに利用する
    def if_name_method(self,if_name):
        if if_name == self.name:
            self.display_method()
            return True
        else:
            return False   
    
    def set_weight(self,in_weight):
        self.weight = in_weight       
    def set_height(self,in_height):
        self.height = in_height 

            
#5人の学生の情報を入力   
student_list=[]
for i in range(5): 
    name = str(input("名前を入力してください"))
    height = int(input("身長を入力してください"))
    weight = int(input("体重を入力してください"))
#一人分の情報をリストに追加（全て5人）
addres=student(name,height,weight)
student_list.append(addres)
#リストの全ての情報を表示
name_f =input("検索したい名前を入力")
for i in range(5):
    if(student_list[i].if_name_method(name_f)):
        # weight2 = int(input("変更体重を入力"))
        # addres.set_weight(weight2)
        # height2 = int(input("変更身長を入力"))
        # addres.set_height(height2)
        # addres.display_method(name_f)
        # addres.display_method(weight2)
        # addres.display_method(height2)
        in_chan = int(input("身長を変更（１）：　体重を変更（２）："))
        in_data = int(input("変更する値＝＞"))
        student_list[i].data_change_method(in_chan,in_data)
        student_list[i].display_method()
        break
    elif i==2:
        print("名前がありません")
