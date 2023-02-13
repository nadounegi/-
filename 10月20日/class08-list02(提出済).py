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
    #名前を判定する
    def if_name_method(self,if_name):
        if if_name == self.name:
            self.display_method()
            return True
        else:
            return False   
            
#3人の学生の情報を入力   
student_list=[]
for i in range(3): 
    name = str(input("名前を入力してください"))
    height = float(input("身長を入力してください"))
    weight = int(input("体重を入力してください"))
#一人分の情報をリストに追加（全て3人）
addres=student(name,height,weight)
student_list.append(addres)
#リストの全ての情報を表示
name_f =input("検索したい名前を入力")
for i in range(3):
    if(student_list[i].if_name_method(name_f)):
        break
        #student_list[i].display_method()
        
    elif i==2:
        print("名前がありません")
