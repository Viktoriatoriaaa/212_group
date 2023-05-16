function1 = [1,2,3,'a','bc8?']
function2 = (1,2,3,'a','bc8?',7,8,9)
function3 = 788
function4 = '7f88'
a=0
d=0
c=0
t=0
b=0
S=str()
for m in str(function1):
    if m.isalpha():
        a+=1
    elif m.isdigit():
        d+=1

for v in function2:
    if type(v)==str:
        S+=v
c=len(S)

for j in str(function3):
     if int(j)%2 != 0:
          t+=1

for i in function4:
     if i.isalpha():
          b+=1
def function1(): print([1,2,3,'a','bc8?'], 'Это список, в котором ',a, 'букв', d, 'чисел')
def function2(): print((1,2,3,'a','bc8?',7,8,9),'Это кортеж, в котором ',c, 'символов')
def function3(): print(788,'Это число, в котором ',t, ' нечетных цифр')
def function4(): print('7f88','Это строка, в которой ',b, 'букв')

def simple_decore(fn):
     fn()

simple_decore(function1)
simple_decore(function2)
simple_decore(function3)
simple_decore(function4)
