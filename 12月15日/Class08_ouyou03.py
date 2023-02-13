class gakuseki:
    def __init__(self,in_no,in_name,in_score,in_bango):
        self.no = in_no
        self.name = in_name
        self.score = in_score
        self.bango = in_bango

    def kyoka(self):
        if self.bango == 1:
            jyugyo = "JAVA"
        elif self.bango == 2:
            jyugyo = "Python"
        elif self.bango == 3:
            jyugyo = "アルゴリズム"
        else:
            print("エラー")

        print("名前：",self.name)
        print("学籍番号:",self.no)
        print("教科",jyugyo)
        
    def hyoka()