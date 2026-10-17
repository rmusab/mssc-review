D=lambda x,y:sum([(a-b)**2 for a,b in zip(x,y)])
def stimr(x,k,s=1000000,l=300,e=1e-4,m=4,r=1):
 s=min(s,len(x));m=max(1,min(m,len(x)))
 def R(q):
  u=r+(q+1)*11400714819323198485
  def G(n):
   nonlocal u
   u=(u*1103515245+12345)%2147483648
   return u%n
  a=len(x)*q//m;b=len(x)*(q+1)//m;n=s*(q+1)//m-s*q//m;y=x[a:b];z=y[:n]
  [[j:=G(i+1),z.__setitem__(j,y[i]) if j<n else None] for i in range(n,len(y))]
  return z
 y=sum(map(R,range(m)),[]);u=r
 def G(n):
  nonlocal u
  u=(u*1103515245+12345)%2147483648
  return u%n
 c=sorted(y,key=lambda _:G(2147483648))[:k];a=[-1]*len(y);z=1
 def M(q):
  b=len(y)*q//m;d=len(y)*(q+1)//m
  def A(i):
   p=a[i]
   if p<0:return min(range(k),key=lambda j:D(y[i],c[j]))
   v=D(y[i],c[p]);g=p
   [[f:=D(y[i],c[j]),g:=j if f<v else g,v:=min(v,f)] for j in filter(lambda j:j!=p and h[p][j]<4*v,range(k))]
   return g
  v=[A(i) for i in range(b,d)];n=[sum([q==j for q in v]) for j in range(k)]
  f=[[sum([y[b+i][g] for i in range(len(v)) if v[i]==j]) for g in range(len(y[0]))] for j in range(k)]
  q=sum([v[i-b]!=a[i] for i in range(b,d)]);[a.__setitem__(i,v[i-b]) for i in range(b,d)]
  return [f,n,q]
 [[h:=list(map(lambda i:[D(c[i],c[j]) for j in range(k)],range(k))),v:=list(map(M,range(m))),n:=[sum([q[1][j] for q in v]) for j in range(k)],d:=[[sum([q[0][j][g] for q in v])/n[j] for g in range(len(y[0]))] if n[j] else y[G(len(y))] for j in range(k)],z:=sum([q[2] for q in v]) and (e<=0 or max([D(c[j],d[j]) for j in range(k)])>e*e),c:=d] for _ in range(l) if z]
 def F(q):return [min(range(k),key=lambda j:D(x[i],c[j])) for i in range(len(x)*q//m,len(x)*(q+1)//m)]
 return [c,sum(map(F,range(m)),[])]
