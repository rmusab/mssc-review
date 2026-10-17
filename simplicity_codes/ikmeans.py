D=lambda x,y:sum([(a-b)**2 for a,b in zip(x,y)])
def ikmeans(x,k,l=200,e=10,t=1e-4,r=1):
 u=r
 def G(n):
  nonlocal u
  u=(u*1103515245+12345)%2147483648
  return u%n
 c=sorted(x,key=lambda _:G(2147483648))[:k];a=[-1]*len(x);z=[0]*len(x);s=[0]*k;R=[0]*k;p=q=-1;v=1;n=0
 def A(i,j,h):
  nonlocal n
  if h and z[i] and D(x[i],c[a[i]])>R[a[i]]:z[i]=0
  if z[i]:return a[i]
  d=[D(x[i],y) for y in c];b=sorted(range(k),key=lambda j:d[j])[:2]
  if j>1 and abs(d[b[0]]-d[b[1]])>s[b[0]]+s[b[1]]:z[i]=1;n+=1
  return b[0]
 [[h:=e>0 and i>0 and (i+1)%e==0,q:=i+1 if h else q,n:=0,o:=a,a:=[A(j,i,h) for j in range(len(x))],R:=[max([D(x[g],c[j]) for g in range(len(x)) if a[g]==j] or [0]) for j in range(k)],d:=[[sum([x[i][g] for i in w])/len(w) for g in range(len(x[0]))] if (w:=[i for i in range(len(x)) if a[i]==j]) else x[G(len(x))] for j in range(k)],s:=[D(c[j],d[j])**.5 for j in range(k)],c:=d,p:=i+1 if n else p,v:=(e>0 and sum(z) and p>=q) or not(a==o or t>0 and max(s)<=t)] for i in range(l) if v]
 return [c,[min(range(k),key=lambda j:D(y,c[j])) for y in x]]
