#from文を使用したメインに変更
from sample.my_func import plus,minus
from sample.my_class import Account

result1 = plus(10,3)
result2 = minus(10,3)

print('10 + 3 =',result1)
print('10 - 3 =',result2)

account1 = Account('佐藤',1,1000)
#情報を表示する
account1.show_detail()