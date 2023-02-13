from sample.my_class import students
#メイン処理
#人数を入力してリストを作成
stu = []
kazu = int(input("人数を入力してください"))
for i in range(kazu):#入力した人数の通り、繰り返す以下のを処理する
  print("----------------------")
  k_name = input("名前を入力")
  k_bango = int(input("学校番号を入力"))
  k_year = int(input("学年を入力"))
  #リストに追加
  addres = students(k_name,k_bango,k_year)
  stu.append(addres)

#会員表示
for add in stu:
  add.show()

#各学校の人数カウント
for add in stu:
  add.count_method()

#割合クラスメソッド呼び出し
students.wariai_method(kazu)

#人数と中学生の割合表示
students.kazu_print(kazu)