D=lambda a,b:sum([(a[i]-b[i])**2 for i in range(len(a))])
def drsmeans(x,k,m=10000,h=-1,l=300,t=1e-4,r=1):
 n=len(x);q=2147483648
 def G(a=q):
  nonlocal r
  r=(r*1103515245+12345)%q
  return r%a
 def I(w):
  z=[i for i in range(len(w)) if w[i]<=0];v=[int(i in z) for i in range(len(w))] if z else [1/a for a in w];s=sum(v)
  return [a/s for a in v]
 def R(w):
  a=G()*sum(w)/q;s=0;z=[i for i in range(len(w)) if (s:=s+w[i])>a]
  return z[0]
 def K(c):
  b=[];z=1;f=1e999
  def A():return list(map(lambda v:min(range(k),key=lambda j:D(v,c[j])),x))
  def U(v):return [[sum([x[i][d] for i in range(n) if v[i]==j])/sum([a==j for a in v]) for d in range(len(x[0]))] if j in v else c[j] for j in range(k)]
  [[v:=A(),g:=sum([D(x[i],c[v[i]]) for i in range(n)]),e:=1-g/f if f<1e999 and f>0 else 1e999,z:=v!=b and (t<=0 or e>t),c:=U(v),b:=v,f:=g] for _ in range(l) if z]
  v=A()
  return [c,v,sum([D(x[i],c[v[i]]) for i in range(n)])]
 h=max(1,min(h if h>0 else n//100,n-1));p=[1] if n<2 else I(list(map(lambda i:sorted([D(x[i],x[j])**.5 for j in range(n) if j!=i])[h-1],range(n))))
 w=p[:];v=[]
 [[a:=[i for i in range(n) if i not in v],j:=R(w) if sum(w)>0 else a[G(len(a))],v.append(j),w.__setitem__(j,0)] for _ in range(k)]
 c,a,f=K([x[i] for i in v])
 def E(_):
  nonlocal c,a,f
  v=[[i,j,D(c[i],c[j])**.5] for i in range(k) for j in range(i+1,k)];g=v[R(I([z[2] for z in v]))];j=g[G(2)];w=list(map(lambda y:min([D(y,c[i]) for i in range(k) if i!=j]),x));w=[p[i]*w[i] for i in range(n)];s=[z[:] for z in c];s[j]=x[R(w if sum(w)>0 else p)];z=K(s);c,a,f=z if z[2]<f else [c,a,f]
 [E(i) for i in range(m) if k>1]
 return [c,a]
