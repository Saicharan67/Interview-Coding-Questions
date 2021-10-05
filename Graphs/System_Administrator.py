Que - https://codeforces.com/contest/22/problem/C
  
Solution -

n,m,v=map(int,input().split())
if m<n-1 or m>(n-1)*(n-2)//2+1:
	print(-1)
	exit()
if v==1:
	print(1,2)
	t=[1]+[i for i in range(3,n+1)]
	s=1
	i,j=0,1
	k=len(t)
	while s<m and i<k-1:
		print(t[i],t[j])
		j+=1
		if j==k:
			i+=1
			j=i+1
		s+=1
else:
	print(1,v)
	t=[i for i in range(v,n+1)]+[i for i in range(2,v)]
	s=1
	i,j=0,1
	k=len(t)
	while s<m and i<k-1:
		print(t[i],t[j])
		j+=1
		if j==k:
			i+=1
			j=i+1
		s+=1
