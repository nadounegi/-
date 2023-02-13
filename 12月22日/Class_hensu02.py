class bank:
    #初期化

#パスワードを４桁にする
    pw_keta = 4 
#口座番号の初期値は21000
    bango = 21000

    def __init__(self,in_bango,in_name,in_yokikn,in_pw):#コンストラクタ定義
        self.bango = in_bango
        self.name = in_name
        self.yokikn = in_yokikn
        self.pw = in_pw
    
#口座番号連番
    @classmethod
    def bango_method(cls):
        cls.bango +=1
        return cls.bango



#入金処理(メソッド定義)
    def ryokin(self,in_money):
        self.money = in_money

    
       
















#メイン処理
#配列作成
user_list = []
#２０人の配列定義
ninsu = 20
for i in range(ninsu):
    #処理番号
    no = int(input("処理番号を入力"))
    if no == 1:
        #新規登録
        def account_method(self):
            self.pw = int(input("パスワードを入力"))
            self.name = input("名前を入力")    
            self.yokikn = int(input("預金額を入力"))

        #パスワード
        def password(self):
            while len(self.pw) != 4:
                print("もう一回入力")
    elif no == 2:
         #入金処理
        def ryokin_method(self):
            self.money = int(input("金額を入力"))
            self.yokikn += self.money
    elif no == 3:
         #出金処理
        def syukin_method(self):
            self.money = int(input("金額を入力"))
            self.yokikn -= self.money
    elif no == 4:


    else:
         print("")

    #新規登録
   
   
    
   




        