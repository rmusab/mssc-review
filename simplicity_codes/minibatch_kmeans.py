D=lambda x,y:sum([(a-b)**2 for a,b in zip(x,y)])
def minibatch_kmeans(x,k,b=100,t=100,s=1):
 def R(n):
  nonlocal s
  s=(s*1103515245+12345)%2147483648
  return s%n
 c=[x[R(len(x))]]
 [[w:=[min([D(p,z) for z in c]) for p in x],u:=R(2147483648)/2147483648*sum(w),c.append(x[sum([sum(w[:i+1])<u for i in range(len(x))])])] for _ in range(k-1)]
 v=[0]*k
 [[m:=[x[R(len(x))] for _ in range(b)],a:=[min(range(k),key=lambda j:D(p,c[j])) for p in m],[[j:=a[i],v.__setitem__(j,v[j]+1),c.__setitem__(j,[(c[j][h]*(v[j]-1)+p[h])/v[j] for h in range(len(p))])] for i,p in enumerate(m)]] for _ in range(t)]
 return [c,[min(range(k),key=lambda j:D(p,c[j])) for p in x]]
