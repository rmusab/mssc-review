def birch(x,k,b=50,l=200,t=.5,m=500,q=1.5):
 def D(a,b):return sum([(a[1][i]/a[0]-b[1][i]/b[0])**2 for i in range(len(a[1]))])
 def A(a,b):return [a[0]+b[0],[a[1][i]+b[1][i] for i in range(len(a[1]))],a[2]+b[2],a[3]]
 def V(a):return (max(0,2*(a[0]*a[2]-sum([v*v for v in a[1]]))/(a[0]*(a[0]-1))))**.5 if a[0]>1 else 0
 def C(n):return [sum([e[0] for e in n[1]]),[sum([e[1][i] for e in n[1]]) for i in range(len(n[1][0][1]))],sum([e[2] for e in n[1]]),n]
 def S(n):
  e=n[1];p=max([[D(e[i],e[j]),i,j] for i in range(len(e)) for j in range(i+1,len(e))]);a=[n[0],[]];c=[n[0],[]]
  [(a if i==p[1] or i!=p[2] and D(v,e[p[1]])<D(v,e[p[2]]) else c)[1].append(v) for i,v in enumerate(e)]
  return [a,c]
 def I(n,e,t):
  if n[0]:
   if not n[1]:n[1].append(e)
   else:
    i=min(range(len(n[1])),key=lambda j:D(n[1][j],e));z=A(n[1][i],e)
    if V(z)<=t:n[1][i]=z
    else:n[1].append(e)
   return S(n) if len(n[1])>l else [n]
  i=min(range(len(n[1])),key=lambda j:D(n[1][j],e));z=I(n[1][i][3],e,t);n[1][i:i+1]=[C(v) for v in z]
  return S(n) if len(n[1])>b else [n]
 def B(y,t):
  r=[1,[]]
  def J(p):
   nonlocal r
   z=I(r,[1,p[:],sum([v*v for v in p]),None],t);r=z[0] if len(z)<2 else [0,[C(v) for v in z]]
  [J(p) for p in y]
  return r
 def L(n):return [n] if n[0] else sum([L(e[3]) for e in n[1]],[])
 def X(r):
  z=L(r)
  return z[0][1] if len(z)==1 else [C(n) for n in z]
 def H(y,t):
  r=B(y,t);n=sum([len(v[1]) for v in L(r)])
  [[t:=t*q,r:=B(y,t),n:=sum([len(v[1]) for v in L(r)])] for _ in range(20) if n>m]
  return [r,t]
 def P(x,e):return sum([(x[i]-e[1][i]/e[0])**2 for i in range(len(x))])
 n=min(len(x),10000);y=[x[i*(len(x)-1)//max(1,n-1)] for i in range(n)];f=[];d=t
 [[z:=H(y,d),f:=X(z[0]),d:=z[1]/2 if len(f)<k else z[1]] for _ in range(20) if len(f)<k]
 f=[];g=[]
 [[z:=H(x,d),f:=X(z[0]),g:=f if len(f)>len(g) else g,d:=z[1]/2 if len(f)<k else z[1]] for _ in range(5) if len(g)<k]
 f=g;g=[[i] for i in range(len(f))]
 def W(a,b):return min([D(f[i],f[j]) for i in a for j in b])
 [[z:=min([[W(g[i],g[j]),i,j] for i in range(len(g)) for j in range(i+1,len(g))]),g[z[1]].extend(g[z[2]]),g.pop(z[2])] for _ in range(len(f)-k)]
 h=[0]*len(f);[[h.__setitem__(i,j) for i in g[j]] for j in range(k)]
 a=[h[min(range(len(f)),key=lambda j:P(p,f[j]))] for p in x]
 c=[[sum([x[i][d] for i in v])/len(v) for d in range(len(x[0]))] for j in range(k) for v in [[i for i in range(len(x)) if a[i]==j]]]
 return [c,a]
