a=100
if a>=0:
	print(a)
else:
	print(-a)

age=20
if age>=18:
	print('your age is:',age)
	print('adult')
else:
	print('your age is:',age)
	print('teenager')

newage=16
if newage>=18:
	print('adult!')
elif newage>=6:
	print('teenager')
else:
	print('kid')

s=input('input your year of birth:')
birth=int(s)
if birth<2000:
	print('00前')
else:
	print('00后')

height=1.75
weight=80.5
s=80.5/(1.75*1.75)
if s<18.5:
	print('过轻')
elif s<25:
	print('正常')
elif s<28:
	print('过重')
elif s<32:
	print('肥胖')
else:
	print('严重肥胖')
