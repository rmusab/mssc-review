D=lambda x,y:sum([(a-b)**2 for a,b in zip(x,y)])
def bigmeans_inner(x,k,s=100,t=100,l=300,e=1e-4,r=1):
 def G(n):
  nonlocal r
  r=(r*1103515245+12345)%2147483648
  return r%n
 def S():return sorted(x,key=lambda _:G(2147483648))[:s]
 def P(y,c):
  c=list(filter(lambda z:z is not None,c))
  if not c:c=[y[G(len(y))]]
  def N(_):
   d=list(map(lambda p:min(map(lambda z:D(p,z),c)),y));u=G(2147483648)/2147483648*sum(d)
   return y[sum([sum(d[:i+1])<u for i in range(len(y))])]
  [c.append(N(_)) for _ in range(k-len(c))]
  return c
 def K(y,c):
  p=1e999;b=[];z=1
  def A(c):return list(map(lambda v:min(range(k),key=lambda j:D(v,c[j])),y))
  def U(a):
   def C(j):
    i=list(filter(lambda i:a[i]==j,range(len(y))))
    return list(map(lambda h:sum(map(lambda i:y[i][h],i))/len(i),range(len(y[0])))) if i else None
   return list(map(C,range(k)))
  [[a:=A(c),f:=sum(map(lambda i:D(y[i],c[a[i]]),range(len(y)))),z:=a!=b and (p==1e999 or p and 1-f/p>e),c:=U(a) if z and i<l-1 else c,p:=f,b:=a] for i in range(l) if z]
  return [list(map(lambda j:c[j] if j in a else None,range(k))),f]
 c=[None]*k;o=1e999
 [[y:=S(),n:=K(y,P(y,c)),c:=n[0] if n[1]<o else c,o:=min(o,n[1])] for _ in range(t)]
 return [c,list(map(lambda p:min(range(k),key=lambda j:D(p,c[j])),x))]
