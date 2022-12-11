#アンパッキング
num_tuple = (10,20)
print(num_tuple)

x,y = num_tuple
print(x,y)

x,y = 10,20
print(x,y)

min,max = 0,100
print(min,max)
#短い代入は見やすくわかりやすいが、代入が多いと見にくくなる

i = 10
j = 20
tmp = i
i = j
j = tmp
#入れ替えるのに３行
print(i,j)


a = 100
b = 200
print(a,b)
a,b = b,a
print(a,b)
#入れ替えるのに２行　アンパッキングを使うと

chose_from_two = ('A','B','C')
answer = []
answer.append('A')
answer.append('c')

print(chose_from_two)
print(answer)
#タプルの使いかた、選択肢に間違って新しいものが入ることがない









  # TODO: write code...

