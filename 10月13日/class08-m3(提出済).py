from sys import stderr

bmi = 0
std = 0
class health:
    def __init__(self,in_height,in_weight,in_bango,in_bmi,in_std):
        self.height = in_height
        self.weight = in_weight
        self.bango = in_bango
        self.bmi = in_bmi
        self.std = in_std
    def show_detail(self):
        print("身長",self.height)
        print("体重",self.weight)
        print("診療番号",self.bango)
    def get_bmi(self):
        return self.weight/(self.height*self.height)
    def get_std(self):
        return (self.height*self.height)*22

#メイン
bango = int(input("診療番号を入力してください"))
height = float(input("身長を入力してください"))
weight = float(input("体重を入力してください"))
#インスタンス生成を行い実行する
check = health(height,weight,bango,bmi,std)
check.show_detail() 
bmi = check.get_bmi()
std = check.get_std()
print("BMI",int(bmi))
print("標準体重",int(std))