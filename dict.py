#dict内部存放的顺序和key放入的顺序是没有关系的
#dict 查找和插入的速度极快，不会随着key的增加而变慢
#	  需要占用大量的内存，内存浪费多
# list则查找和插入的时间随着元素的增加而只能加  占用空间小，浪费内存很少
d={'faker':100,'uzi':99,'gogoing':95}
print(d['faker'])

#由于列表可变，不能做key值
# key=[1,2,3]
# d[key]='a list'

s=set([1,2,2,3,3])
s.add(4)
s.remove(3)
print(s)

