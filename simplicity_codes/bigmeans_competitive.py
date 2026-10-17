D=lambda x,y:sum([(a-b)**2 for a,b in zip(x,y)])
def bigmeans_competitive(x,k,s=100,t=100,w=4,l=300,e=1e-4,r=1):
 def W(q):
  u=r+q*11400714819323198485
  def G(n):
   nonlocal u
   u=(u*1103515245+12345)%2147483648
   return u%n
  def S():return sorted(x,key=lambda _:G(2147483648))[:s]
  def P(y,c):
   c=[z for z in c if z is not None]
   if not c:c=[y[G(len(y))]]
   def N(_):
    d=[min([D(p,z) for z in c]) for p in y];v=G(2147483648)/2147483648*sum(d)
    return y[sum([sum(d[:i+1])<v for i in range(len(y))])]
   [c.append(N(_)) for _ in range(k-len(c))]
   return c
  def K(y,c):
   p=1e999;b=[];z=1
   def A(c):return [min(range(k),key=lambda j:D(v,c[j])) for v in y]
   def U(a):
    def C(j):
     i=[i for i in range(len(y)) if a[i]==j]
     return [sum([y[i][h] for i in i])/len(i) for h in range(len(y[0]))] if i else None
    return [C(j) for j in range(k)]
   [[a:=A(c),f:=sum([D(y[i],c[a[i]]) for i in range(len(y))]),z:=a!=b and (p==1e999 or p and 1-f/p>e),c:=U(a) if z and i<l-1 else c,p:=f,b:=a] for i in range(l) if z]
   return [[c[j] if j in a else None for j in range(k)],f]
  c=[None]*k;o=1e999
  [[y:=S(),n:=K(y,P(y,c)),c:=n[0] if n[1]<o else c,o:=min(o,n[1])] for _ in range(t)]
  return [c,o]
 c=min(map(W,range(w)),key=lambda z:z[1])[0]
 return [c,list(map(lambda p:min(range(k),key=lambda j:D(p,c[j])),x))]
