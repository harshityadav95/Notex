## Python Resources and List

- [Microsft Python for Beginners web Series](https://www.youtube.com/playlist?list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6)

```
"""class A:
	def s(self,a,b):
		return a+b
obj=A()
print(obj.s(1,1))
def f(a,b):
	return a+b
c=f(4,6)
print(c)
l=['apple',"orange",3,5,8]
print(l[3])
d={"3":'third',"4":'four'}
print(d["3"])"""

lst=[]
print("Hello")
n=int(input("Enter the number"))
print("the displayed value is ",n," and the string continous")
for i in range(n):
	ele=int(input())
	lst.append(ele)

for i in range(0,n-1):
	for j in range(0,n-1-i):
		if lst[j]>lst[j+1]:
			lst[j],lst[j+1]=lst[j+1],lst[j]

print(lst)


```

