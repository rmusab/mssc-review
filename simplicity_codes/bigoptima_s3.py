D=lambda x,y:sum([(a-b)**2 for a,b in zip(x,y)])
def bigoptima_s3(x,k,a=50,b=150,p=10,t=100,w=4,l=300,e=1e-4,r=1):
 def W(q):
  u=r+q*11400714819323198485
  def G(n):
   nonlocal u
   u=(u*1103515245+12345)%2147483648
   return u%n
  def S(n):return sorted(x,key=lambda _:G(2147483648))[:n]
  def P(y,c):
   c=[z for z in c if z is not None]
   if not c:c=[y[G(len(y))]]
   def N(_):
    d=[min([D(p,z) for z in c]) for p in y];v=G(2147483648)/2147483648*sum(d)
    return y[sum([sum(d[:i+1])<v for i in range(len(y))])]
   [c.append(N(_)) for _ in range(k-len(c))]
   return c
  def K(y,c):
   h=1e999;b0=[];z=1
   def A(c):return [min(range(k),key=lambda j:D(v,c[j])) for v in y]
   def U(a):
    def C(j):
     i=[i for i in range(len(y)) if a[i]==j]
     return [sum([y[i][h] for i in i])/len(i) for h in range(len(y[0]))] if i else c[j]
    return [C(j) for j in range(k)]
   [[a0:=A(c),f:=sum([D(y[i],c[a0[i]]) for i in range(len(y))]),z:=a0!=b0 and (h==1e999 or h and 1-f/h>e),c:=U(a0) if z and i<l-1 else c,h:=f,b0:=a0] for i in range(l) if z]
   return [[c[j] if j in a0 else None for j in range(k)],f]
  def F(y,c):return sum([min([D(v,z) for z in c]) for v in y])
  c=[None]*k;v=[]
  [[s:=a+G(b-a+1),y:=S(s),c:=P(y,c),o:=F(y,c),[[y:=S(s),n:=K(y,P(y,c)),v.append(s) if n[1]<o else None,c:=n[0] if n[1]<o else c,o:=min(o,n[1])] for _ in range(p)]] for _ in range(t)]
  return [P(y,c),v]
 z=list(map(W,range(w)));v=[s for q in z for s in q[1]]
 s=int(sum(v)/len(v)+.5) if v else (a+b+1)//2
 u=r+w*11400714819323198485
 def G(n):
  nonlocal u
  u=(u*1103515245+12345)%2147483648
  return u%n
 y=sorted(x,key=lambda _:G(2147483648))[:s]
 def F(c):return sum([min([D(v,z) for z in c]) for v in y])
 c=min(map(lambda q:[q[0],F(q[0])],z),key=lambda q:q[1])[0]
 return [c,list(map(lambda p:min(range(k),key=lambda j:D(p,c[j])),x)),s]
