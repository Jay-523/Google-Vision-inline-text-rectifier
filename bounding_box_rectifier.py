def find_dsu(i,p):
  if p[i] == i:
    return i
  else:
     p[i] = find_dsu(p[i],p)
     return p[i]
def get_charht(bbox):
  ht = 0
  for i in bbox:
    ht+=(i[3]-i[1])/2
  ht/=len(bbox)
  return ht
def unite(x,y, p, r):
  x = find_dsu(x, p)
  y = find_dsu(y,p)
  if r[x] > r[y]:
    p[y] = x
  elif r[y] > r[x]:
    p[x]=  y
  else:
    p[x] = y 
    r[x]+=1

char_ht = get_charht(boxes)
char_ht
thres = char_ht/2


for i in range(len(cent)):
  for j in range(i+1,len(cent)):
    if(marked[j] == 1):
      continue
    else:
      dist = np.abs(cent[i][1] - cent[j][1])
      if dist < thres:
        marked[j] = 1
        unite(i,j,parent,rank)
print(parent)
lines = dict()
for i in range(len(parent)):
  if(parent[i] in lines.keys()):
    lines[parent[i]].append(boxes[i]) 
  else:
    lines[parent[i]] = [boxes[i]]

def customsort(l):
  return l[1]
for i in lines:
  lines[i].sort(key = customsort)
  for j in lines[i]:
    print(j[-1])
  print('='*100)