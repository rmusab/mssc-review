D=lambda a,b:sum([(a[i]-b[i])**2 for i in range(len(a))])
P=lambda a,b:sum([a[i]*b[i] for i in range(len(a))])
def big_clust(x,k,l=50,r=1):
 n=len(x);d=len(x[0]);m=2147483648
 def G(q=m):
  nonlocal r
  r=(r*1103515245+12345)%m
  return r%q
 def C(v):return [v[i*d:(i+1)*d] for i in range(len(v)//d)]
 def O(c,z):
  a=list(map(lambda v:min(range(len(c)),key=lambda j:D(v,c[j])),z));g=[[0]*d for _ in c]
  [[g[a[i]].__setitem__(q,g[a[i]][q]+2*(c[a[i]][q]-z[i][q])) for q in range(d)] for i in range(len(z))]
  return [sum([D(z[i],c[a[i]]) for i in range(len(z))]),sum(g,[])]
 def A(c,z):
  w=[min([D(v,q) for q in c]) for v in z]
  def F(y):
   q=[i for i in range(len(z)) if D(z[i],y)<w[i]]
   return [sum([w[i] for i in range(len(z)) if i not in q])+sum([D(z[i],y) for i in q]),[sum([2*(y[j]-z[i][j]) for i in q]) for j in range(d)]]
  return F
 def L(F,z,e,it,s,u,ga=1):
  s=s[:];u=u[:];f,g=F(z);a=g[:];b=0;v=[f];q=1;o=1;nn=0;mc=max(7,len(s));nf=1;ng=1;nit=0;st=0;Y=[[z[:],f,g[:]]];inew=0 if len(s)>=mc else len(s);gamma=ga;tmp=[];ib=0;ir=0;nres=1;nress=0;ncres=-1;neps=0;pw=1e300;iterm=0
  def C():return [s[inew:]+s[:inew],u[inew:]+u[:inew]] if len(s)==mc and inew else [s[:],u[:]]
  def Z(x,y):
   nonlocal inew
   if len(s)<mc:s.append(x);u.append(y);inew=len(s)%mc
   else:s[inew]=x;u[inew]=y;inew=(inew+1)%mc
  def V(A,b):
   n=len(b);A=[i[:] for i in A];be=max(4e-16,max([abs(A[i][i]) for i in range(n)] or [0]),max([abs(A[i][j]) for i in range(n) for j in range(i+1,n)] or [0])/max(n,1));de=4e-16*max(be,1)
   def E(k):
    r=max(abs(A[k][k]),max([abs(A[k][j]) for j in range(k+1,n)] or [0])**2/be,de);A[k][k]=r
    def J(j):
     g=A[k][j];A[k][j]=g/r;[A[i].__setitem__(j,A[i][j]-A[k][i]*g) for i in range(k+1,j+1)]
    [J(j) for j in range(k+1,n)]
   [E(k) for k in range(n)];x=[0]*n
   [x.__setitem__(i,b[i]-sum([A[j][i]*x[j] for j in range(i)])) for i in range(n)];[x.__setitem__(i,x[i]/A[i][i]) for i in range(n)];[x.__setitem__(i,x[i]-sum([A[i][j]*x[j] for j in range(i+1,n)])) for i in range(n-2,-1,-1)]
   return x
  def Q(A,b,t):
   x=b[:];r=range(len(x)) if not t else range(len(x)-1,-1,-1)
   [x.__setitem__(i,(x[i]-sum([A[j][i]*x[j] for j in range(i)]))/A[i][i] if not t else (x[i]-sum([A[i][j]*x[j] for j in range(i+1,len(x))]))/A[i][i]) for i in r]
   return x
  def K(t=[]):
   S,U=C();S+=([t[0]] if t else []);U+=([t[1]] if t else []);m=len(S);rp=[P(S[i],U[j]) for j in range(m) for i in range(j+1)];np=[P(U[i],U[j]) for j in range(m) for i in range(j+1)];R=[[rp[j*(j+1)//2+i] if i<=j else 0 for j in range(m)] for i in range(m)];N=[[np[max(i,j)*(max(i,j)+1)//2+min(i,j)] for j in range(m)] for i in range(m)];D=[R[i][i] for i in range(m)]
   return [S,U,R,N,D]
  def B(g):
   S,U,R,N,D=K(tmp)
   if not S:return [-j for j in g]
   q=Q(R,[P(i,g) for i in S],0);h=[D[i]*q[i]+gamma*sum([N[i][j]*q[j] for j in range(len(q))])-gamma*P(U[i],g) for i in range(len(q))];r=Q(R,h,1)
   return [gamma*(sum([U[i][j]*q[i] for i in range(len(q))])-g[j])-sum([S[i][j]*r[i] for i in range(len(r))]) for j in range(len(g))]
  def R(g,t=[]):
   S,U,A,N,D=K(t)
   if not S:return [-j for j in g]
   M=[[N[i][j]-A[i][j]-A[j][i]+(D[i] if i==j else 0) for j in range(len(S))] for i in range(len(S))];b=[P(U[i],g)-P(S[i],g) for i in range(len(S))];q=V(M,b)
   return [-g[j]+sum([(U[i][j]-S[i][j])*q[i] for i in range(len(S))]) for j in range(len(g))]
  def T(g,y,a,h,b,Q):
   H=lambda z:[-i for i in Q(z)]
   if nn==0:
    u=[y[i]-g[i] for i in range(len(g))];p=P(Q(g),u)-h;q=P(u,H(u));l=1 if p>0 else 0;l=min(1,max(0,p/q)) if q>0 else l
    return [[l*y[i]+(1-l)*g[i] for i in range(len(g))],l*h]
   p=[g[i]-a[i] for i in range(len(g))];r=[y[i]-a[i] for i in range(len(g))];P1=P(p,H(p));R1=P(r,H(r));PR=P(p,H(r));rp=P(p,H(a))-b;rr=P(r,H(a))+h-b;pq=R1-2*PR+P1;qq=pq+PR+rr-P1-rp;l1=0;l2=0;go=0
   if P1>0 and R1>0:
    t=rr/R1;z=PR/R1;w=P1-PR*z
    if w:l1=(t*PR-rp)/w;l2=-t-l1*z;go=l1*(l1-1)<0 and l2*(l1+l2-1)<0
   if not go:
    l1=0;l2=min(1,max(0,-rr/R1)) if R1>0 else (1 if h<=b else 0);w=(l2*R1+2*rr)*l2;t=min(1,max(0,-rp/P1)) if P1>0 else (1 if b>=0 else 0);z=(t*P1+2*rp)*t
    if z<w:w=z;l1=t;l2=0
    if pq and qq*(qq-pq)<0 and R1+2*rr-qq*qq/pq<w:l1=qq/pq;l2=1-l1
   if l1==0 and l2*(l2-1)<0 and -rp-l2*PR>0 and P1>0:l1=min(1-l2,(-rp-l2*PR)/P1)
   t=1-l1-l2
   return [[l1*g[i]+l2*y[i]+t*a[i] for i in range(len(g))],l2*h+t*b]
  def I(p):
   d=max(P(p,p)**.5,1e-300);t=min(1,1000/d);r=[[max(abs(y[1]-f+P(y[2],[z[i]-y[0][i] for i in range(len(z))])),1e-4*D(z,y[0])),P(y[2],p)] for y in Y if D(y[0],z)>0];w=P(a,p)
   if r:
    h,j=max(r,key=lambda x:t*x[1]-x[0]);v=max([x[1]-x[0] for x in r])
    if q and v>w/2 and t*j-h>w*t*(1-t/2):
     v=1-j/w;c=max(0,v*v+2*h/w)**.5;v=v+c;v=-2*h/(w*v) if j>=0 and v else v;t=min(1.95,max(0,v))
    if not q:
     r=[x for x in r if x[0]<x[1]-w]
     if r:
      h,j=max(r,key=lambda x:t*x[1]-x[0]);t=h/(j-w) if t*j-h>w*t and j!=w else t
   return min(max(t,1e-12),1000/d)
  def J(l,r,fl,fr,w):
   z=(fr-fl)/(-w*r) if w*r else 1;q=2*(1-z)
   return max((1-.5/.52)*r,r/q) if l==0 and q>1 else (l+r)/2
  def W(p,w):
   nonlocal nf,ng
   t=I(p);l=0;r=t;fl=f;fr=f;ft=max(v[-10:]);n=0;done=0;y=z;fy=f;gy=g;h=0;ok=0
   def E(_):
    nonlocal t,l,r,fl,fr,n,done,y,fy,gy,h,ok,nf,ng
    y=[z[i]+t*p[i] for i in range(len(z))];fy,gy=F(y);nf+=1;ng+=1;pd=P(gy,p);h=max(abs(f-fy+t*pd),1e-4*t*t*P(p,p))
    if fy<=ft-.48*t*w:l=t;fl=fy
    else:r=t;fr=fy
    if fy>ft and r-l>=1e-13 and nn and n<20:t=J(l,r,fl,fr,w)
    else:
     ok=fy<=ft-.24*t*w and (t>=1e-12 or h>0);done=ok or pd-h>=-.4800000000001*w or r-l<1e-13 or n>=20;t=t if done else J(l,r,fl,fr,w)
    n+=1
   [E(i) for i in range(21) if not done and nf<500]
   return [y,fy,gy,t,h,ok]
  def E(_):
   nonlocal z,f,g,a,b,q,s,u,v,o,nn,mc,st,Y,inew,gamma,tmp,ib,ir,nres,nress,ncres,neps,pw,iterm,nit
   p=B(a) if q else R(a);d=P(a,p)
   if d+2e-16*max(P(a,a)*P(p,p),0)**.5>0:
    nres+=1
    if nres==1:s=[];u=[];inew=0;gamma=1;tmp=[];a=g[:];b=0;q=1;nn=0;ncres+=1;return 1
    o=0;iterm=-1;return 0
   nres=0;nit+=1
   if -d<1e-12*P(a,a):p=[p[i]-1e-12*a[i] for i in range(len(a))];d-=1e-12*P(a,a)
   w=-d+2*b
   if w<=1000*e and s and mc<15:s,u=C();mc+=1;inew=len(s)
   o=not s or w>e or .5*P(a,a)+b>1e3
   if not o:return 0
   if nf>=max(500,it):o=0;iterm=4;return 0
   if nit>=it:o=0;iterm=5;return 0
   neps=neps+1 if not q and abs(w-pw)<=2e-16 else 0;pw=w
   if neps>20:o=0;iterm=-4;return 0
   dn=max(P(p,p),0)**.5
   if dn and 1000/dn<=1e-12:
    nress+=1
    if nress==1:s=[];u=[];inew=0;gamma=1;tmp=[];a=g[:];b=0;q=1;nn=0;ncres+=1;return 1
    o=0;iterm=-1;return 0
   nress=0
   y,fy,gy,t,h,ok=W(p,w);sv=[y[i]-z[i] for i in range(len(z))];uv=[gy[i]-g[i] for i in range(len(g))];Y=(Y+[[y[:],fy,gy[:]]])[-2:];old=a[:]
   if ok:
    st=st+1 if abs(f-fy)<=1e-8 else 0;z=y;f=fy;g=gy;a=gy;b=0;v.append(f);q=1;nn=0;o=st<10;c=P(sv,uv);ib=3
    if c>0:
     gamma=c/max(P(uv,uv),2e-16);gamma=max(.01,min(100,gamma)) if not s else max(2e-13,gamma)
     if -P(p,uv)-P(old,sv)<-2e-16:Z(sv,uv);tmp=[];ib=1
     else:tmp=[sv,uv];ib=2
   else:
    a,b=T(g,gy,a,h,b,B if nn==0 else R);q=0;ir=3
    if -P(p,uv)-P(old,sv)<-2e-16:
     if nn==0 or len(s)<mc:Z(sv,uv);ir=1
     elif P(a,R(a,[sv,uv]))-P(a,R(a))>=0:Z(sv,uv);ir=1
    tmp=[];nn+=1
   return 1
  [E(i) for i in range(it) if o and nf<500]
  s,u=C();return [z,f,s,u,gamma]
 def SL(Q,z,e,h,H):
  s=[];u=[];ga=1;f=H(z)[0];w=[z[:],f];a=0;o=1
  def E(_):
   nonlocal z,s,u,ga,w,a,o
   b=min(len(y),max(len(y)//50,1000));v=sorted(range(len(y)),key=lambda _:G())[:b];q=L(Q([y[i] for i in v]),z,e,10,s,u,ga);z,s,u,ga=q[0],q[2],q[3],q[4];f=H(z)[0];a=0 if f<w[1] else a+1;w=[z[:],f] if f<w[1] else w;o=a<=10
  [E(i) for i in range(h) if o]
  return w
 def U(v,t):
  z=[];[z.append(a) for a in v if not z or min([D(a,b) for b in z])>t]
  return z
 def sample():return x if n<=100000 else [x[i] for i in sorted(range(n),key=lambda _:G())[:max(n//50,10000)]]
 y=sample();c=[[sum([v[j] for v in y])/len(y) for j in range(d)]];base=O(c,y)[0];m1=min(n,500) if n*d<=10000000 else 200;g1=100;g2=50 if n*d<1000000 else 20
 def S(q):
  nonlocal c,y,m1,g1
  m1=max(m1-50,200 if n*d<=10000000 else 100) if n*d>1000000 else m1;g1=max(g1-10,10);a=list(map(lambda v:min(range(len(c)),key=lambda j:D(v,c[j])),y));w=[D(y[i],c[a[i]]) for i in range(len(y))];v=sum([sorted([i for i in range(len(y)) if a[i]==j],key=lambda i:w[i],reverse=True)[:max(1,sum([a[i]==j for i in range(len(y))])*m1//len(y))] for j in range(q-1) if sum([a[i]==j for i in range(len(y))])>1],[]);v=sorted(v,key=lambda i:sum([min(0,D(y[i],y[j])-w[j]) for j in range(len(y)) if w[i]<4*w[j]]))[:max(1,g1*len(v)//100)];v=[[sum([y[i][h] for i in z])/len(z) for h in range(d)] if z else y[j] for j in v for z in [[i for i in range(len(y)) if w[j]<4*w[i] and D(y[j],y[i])<w[i]]]];t=1e-5*base/q;v=U(v,.1*t);v=[SL(lambda b:A(c,b),z,1,1,A(c,y)) for z in v];v=sorted(v,key=lambda z:z[1])[:max(1,g2*len(v)//100)];v=U([z[0] for z in v],.1*t);v=[SL(lambda b:lambda z:O(C(z),b),sum(c+[z],[]),1e-3 if q%5==0 else 1e3,min(50,l),lambda z:O(C(z),y)) for z in v];c=C(min(v,key=lambda z:z[1])[0]);y=sample()
 [S(q) for q in range(2,k+1)]
 a=list(map(lambda v:min(range(k),key=lambda j:D(v,c[j])),x))
 return [c,a]
