def ranku (in_ave):
    if 100 >=in_ave >=80:
        hyoka = 'A'
    elif 70 >= in_ave >=79:
        hyoka = 'B'
    elif 60 >= in_ave >= 69:
        hyoka = 'C' 
    elif 0 >= in_ave >= 59:
        hyoka = 'D' 
    return hyoka    
i = 0
for i in range (5):#五人分の処理
    in_x = int(input('国語の点数を入力してください'))
    in_y = int(input('英語の点数を入力してください'))
    in_z = int(input('数学の点数を入力してください')) 
    if 0<=in_x<=100 and 0<=in_y<=100 and  0<=in_z<=100:
        score_sum =in_x+in_y+in_z
        score_ave =int(score_sum/3)
        pinjia= ranku(score_ave)
    print("3教科の平均点は",score_ave,"点なので、評価は",pinjia ,"評価です")