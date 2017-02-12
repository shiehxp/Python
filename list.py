#这是list
classmates=['xiepeng','skt','faker']
print(classmates)
print(len(classmates))

classmates.append('marin')
print(classmates[-1])

classmates.insert(1,'bang')
print(classmates)

classmates.pop()
print(classmates)

classmates.pop(0)
print(classmates)

#这是一个元祖，不能改变，下标一样使用
classmate=('haha','heh','xixi','heihei')
print(classmate)

L=[
	['apple','google','microsoft'],
	['java','python','ruby','php'],
	['adam','bateman','ironman']
]
#获取apple
print(L[0][0])
#获取python
print(L[1][1])
#获取ironman
print(L[2][2])