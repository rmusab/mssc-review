D=lambda x,y:sum([(a-b)**2 for a,b in zip(x,y)])
P=lambda x,k,s:[x[i] for i in sorted(range(len(x)),key=lambda i:(i+s)*1103515245%2147483648)[:k]]
def forgy_kmeans(x,k,n=300,e=1e-4,s=1):
 c=P(x,k,s);p=1e999;b=[];z=1
 def A(c):return [min(range(k),key=lambda j:D(v,c[j])) for v in x]
 def U(c,a):return [[sum([v[h] for i,v in enumerate(x) if a[i]==j])/a.count(j) for h in range(len(x[0]))] if j in a else c[j] for j in range(k)]
 [[a:=A(c),f:=sum([D(v,c[a[i]]) for i,v in enumerate(x)]),z:=a!=b and (p==1e999 or p and 1-f/p>e),c:=U(c,a) if z and t<n-1 else c,p:=f,b:=a] for t in range(n) if z]
 return [c,a]
