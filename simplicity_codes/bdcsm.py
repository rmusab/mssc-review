D=lambda x,y:sum([(a-b)**2 for a,b in zip(x,y)])
P=lambda x,k,s:[x[i] for i in sorted(range(len(x)),key=lambda i:(i+s)*1103515245%2147483648)[:k]]
def K(x,c,n):
 def U(c):
  a=[min(range(len(c)),key=lambda j:D(p,c[j])) for p in x]
  return [[sum([p[h] for i,p in enumerate(x) if a[i]==j])/a.count(j) for h in range(len(x[0]))] if j in a else c[j] for j in range(len(c))]
 [(c:=U(c)) for _ in range(n)]
 return c
def bdcsm(x,k,q=0,n=100,s=1):
 q=q or (127359*k*k+639)//640
 b=[x[i:i+q] for i in range(0,len(x)-len(x)%q,q)] or [x]
 c=[v for i,z in enumerate(b) for v in K(z,P(z,k,s+i),n)]
 c=K(c,P(c,k,s+len(b)),n)
 return [c,[min(range(k),key=lambda j:D(p,c[j])) for p in x]]
