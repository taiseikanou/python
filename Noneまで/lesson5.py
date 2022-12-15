#if文
x = 0

if x < 0:
    print('negative')
elif x == 0:
    print('zero')
else:
    print('positive')


a = 5
b = 10

if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')

#Inとnotの使い所
y = [1,2,3]
x = 1
if x in y:
    print('in')

if 100 not in y:
    print('not in')

a = 1
b = 2
#この使い方はあまり好ましくない！＝を使った方がいい
if not a == b:
    print ('Not equl')
    

is_ok = True

if not is_ok:
    print('hello')


    

    
    
    

    