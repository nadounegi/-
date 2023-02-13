class urihyoka:
    def __init__(self,in_tenban,in_name,in_uriaka,in_target):#クラスを定義
        self.tenban = in_tenban
        self.name = in_name
        self.uriaka = in_uriaka
        self.target = in_target
        self.complete = 0
  
    #情報を定義
    def display_method(self):
        print('店番',self.tenban)
        print('店名',self.name)
        print('売上額',self.uriaka)
        print('目標額',self.target) 
        print('達成率',self.complete,'%')

        
    #メソッド定義　評価
    def hyoka(self):
        if self.complete >= 100:
           print('優秀')
        elif 80 <= self.complete < 100:
            print('良好')
        elif 50 <= self.complete < 80:
            print('頑張りましょう')
        else:
             print('問題有り')
    
 #メソッド定義　達成率計算
    def comp(self):
        self.complete = int(self.uriaka/self.target*100)

#クラス型のリスト作成
urihyoka_list = []
#店舗数と店舗情報を入力
kazu = int(input("店舗数を入力"))
for i in range(kazu):
    k_tenban = int(input("店番を入力"))
    k_name = str(input("店名を入力"))
    k_uriaka = int(input("売上額を入力"))
    k_target = int(input("目標額を入力"))
    #リストに追加
    addres = urihyoka(k_tenban,k_name,k_uriaka,k_target)
    urihyoka_list.append(addres)

#達成率を計算し評価を表示
for add in urihyoka_list:
    print('-----お店の情報表示-----')
    add.comp()
    add.display_method()
    add.hyoka()
