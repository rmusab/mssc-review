D=lambda a,b:sum([(a[i]-b[i])**2 for i in range(len(a))])
def mdeclust(x,k,p=150,t=1e-4,n=5000,l=300,a=3,r=1):
 m=2147483648
 def G(q=m):
  nonlocal r
  r=(r*1103515245+12345)%m
  return r%q
 def K(c):
  b=[];z=1;f=0
  def A():return [min(range(k),key=lambda j:D(v,c[j])) for v in x]
  def U(v):return [[sum([x[i][d] for i in range(len(x)) if v[i]==j])/sum([q==j for q in v]) for d in range(len(x[0]))] if j in v else c[j] for j in range(k)]
  [[v:=A(),f:=sum([D(x[i],c[v[i]]) for i in range(len(x))]),z:=v!=b,c:=U(v) if z and q<l-1 else c,b:=v] for q in range(l) if z]
  return [c,b,f]
 def H(s,b):
  c=[[D(s[i],b[j]) for j in range(k)] for i in range(k)];u=[0]*(k+1);v=[0]*(k+1);p=[0]*(k+1);w=[0]*(k+1)
  def R(i):
   p[0]=i;d=[1e999]*(k+1);z=[0]*(k+1)
   def B(j):
    q=w[j];p[j]=p[q]
    B(q) if q else None
   def Q(j):
    z[j]=1;q=p[j]
    [[w.__setitem__(h,j),d.__setitem__(h,c[q-1][h-1]-u[q]-v[h])] for h in range(1,k+1) if not z[h] and c[q-1][h-1]-u[q]-v[h]<d[h]]
    e,j=min([[d[h],h] for h in range(1,k+1) if not z[h]])
    [[[u.__setitem__(p[h],u[p[h]]+e),v.__setitem__(h,v[h]-e)] if z[h] else d.__setitem__(h,d[h]-e)] for h in range(k+1)]
    Q(j) if p[j] else B(j)
   Q(0)
  [R(i) for i in range(1,k+1)]
  return [s[p[j]-1] for j in range(1,k+1)]
 def I(s,v):return not sum([len({v[i] for i in range(len(v)) if s[i]==j})>1 for j in set(s)])
 P=[K(sorted(x,key=lambda _:G())[:k]) for _ in range(p)]
 def V():return sum([abs(P[i][2]-P[j][2]) for i in range(p) for j in range(i+1,p)])
 def S(i):
  q=[];z=1
  [[q:=sorted([j for j in range(p) if j!=i],key=lambda _:G())[:3],v:=[i]+q,z:=sum([I(P[v[g]][1],P[v[h]][1]) for g in range(4) for h in range(g+1,4)])>0 if e<a else 0] for e in range(a+1) if z]
  return q
 h=0
 def E(q):
  nonlocal h
  i=q%p;j=S(i);s=P[j[2]][0];b=H(P[j[0]][0],s);c=H(P[j[1]][0],s);f=.5+.3*G()/m;o=K([[b[g][d]+f*(c[g][d]-s[g][d]) for d in range(len(x[0]))] for g in range(k)]);z=o[2]<min([v[2] for v in P]);h=0 if z else h+(o[2]>=P[i][2]);P.__setitem__(i,o) if o[2]<P[i][2] else None
 [E(q) for q in range(n*p) if h<n and V()>t]
 b=min(P,key=lambda v:v[2])
 return b[:2]
