class student:#クラスを定義
    def __init__(self,in_name,in_kaiin,in_bango,in_year):# 初期化
        self.name = in_name
        self.kaiin = in_kaiin
        self.bango = in_bango
        self.year = in_year

    def gakusei(self):#表示メソッド
        if self.bango == 1:
            gako = "小学校"
        elif self.bango == 2:
            gako = "中学校"
        elif self.bango == 3:
           gako = "高校"

        print('名前',self.name)
        print('会員番号',self.kaiin)
        print('学年',self.year)
        print('学校',gako)
  
    
    
    
#メイン処理
# データを入力してリストを作成  
def count_method(gono:list,c:int):
        c1 = 0
        c2 = 0
        c3 = 0

        for i in range(c):
            if gono[i] == 1:
                c1 += 1
            elif gono[i] == 2:
                c2 += 1
            else:
                c3 += 1
        return c1,c2,c3   

count1 = 0
count2 = 0
count3 = 0
gako_no =[]
kodomo_list =[] 

ninsu = int(input("人数を入力"))
for i in range(ninsu):
    k_name = str(input("名前を入力"))
    k_kaiin = int(input("会員番号を入力"))
    K_year = int(input("学年を入力"))
    K_bango = int(input("学校番号を入力"))
    gako_no.append(K_bango)
    kodomo_list.append(student(k_name,k_kaiin,K_year,K_bango)) 


count1,count2,count3 = count_method(gako_no,ninsu)
for ad in kodomo_list:
    ad.gakusei()
    
waritu = int(count2/ninsu*100)
print("---------")
print("小学校の人数", count1)
print("中学校の人数",count2)
print("高校の人数",count3)
print("中学校の％",waritu,"%")
