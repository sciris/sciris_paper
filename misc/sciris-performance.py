'''
Time Sciris dicts
'''

import sciris as sc


n = int(1e6)
S = sc.objdict()
G = sc.objdict()

count = 0
with sc.timer() as S.nd:
    for i in range(n):
        key = str(i)
        count += i

G.nd = S.nd

di = {}
with sc.timer() as S.di:
    for i in range(n):
        key = str(i)
        di[key] = i

od = sc.odict()
with sc.timer() as S.od:
    for i in range(n):
        key = str(i)
        od[key] = i

ob = sc.objdict()
with sc.timer() as S.ob:
    for i in range(n):
        key = str(i)
        ob[key] = i
    
count = 0
with sc.timer() as G.di:
    for i in range(n):
        key = str(i)
        count += di[key]

count = 0
with sc.timer() as G.od:
    for i in range(n):
        key = str(i)
        count += od[key]

count = 0
with sc.timer() as G.ob:
    for i in range(n):
        key = str(i)
        count += ob[key]



sc.heading('Set')

st = sc.objdict({k:v.total for k,v in S.items()})
sd = sc.objdict({k:v-st.nd for k,v in st.items()})
sr = sc.objdict({k:v/sd.di for k,v in sd.items()})

print('Diffs')
print(sd)
print('Ratios')
print(sr)

sc.heading('Get')

gt = sc.objdict({k:v.total for k,v in G.items()})
gd = sc.objdict({k:v-gt.nd for k,v in gt.items()})
gr = sc.objdict({k:v/gd.di for k,v in gd.items()})

print('Diffs')
print(gd)
print('Ratios')
print(gr)