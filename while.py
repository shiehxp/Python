# sum=0
# n=99
# while n>0:
# 	sum=sum+n
# 	n=n-2
# 	print(sum)

#break 提前结束循环
# n=1
# while n<=100:
# 	if n>10:
# 		break
# 	print(n)
# 	n=n+1
# 	print('end')

#利用continue跳过某些循环
n=0
while n<10:
	n=n+1
	if n%2 ==0:
		continue
	print(n)