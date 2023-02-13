import sample.sub1.sub2.my_func
import sample.sub1.sub2.my_class

result1 = sample.sub1.sub2.my_func.plus(10,3)
result2 = sample.sub1.sub2.my_func.minus(10,3)

print('10 + 3 =',result1)
print('10 - 3 =',result2)

account1 = sample.sub1.sub2.my_class.Account('佐藤',1,1000)
#情報を表示する
account1.show_detail()