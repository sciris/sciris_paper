'''
Figure out which files in Covasim use the most Sciris
'''

import os
import sciris as sc

folder = '/home/cliffk/idm/covasim/covasim'
os.chdir(folder)
wc = sc.runcommand('wc -l *.py')
gn = sc.runcommand('gn "sc\."')

wclines = wc.splitlines()
wcdata = dict()
for line in wclines:
    if line:
        count,name = line.split()
        wcdata[name] = int(count)


gndata = sc.ddict(int)
gnlines = gn.splitlines()
for line in gnlines:
    if ':' in line:
        name, _ = line.split(':', 1)
        if name in wcdata:
            gndata[name] += 1

df = sc.dataframe(columns=['name', 'lines', 'sciris'])
for k,v in gndata.items():
    row = [k, wcdata[k], v]
    df.appendrow(row)

df['ratio'] = df.sciris/df.lines*100
df = sc.dataframe(df.sort_values('ratio'))

df.appendrow(['total', df.lines.sum(), df.sciris.sum(), df.sciris.sum()/df.lines.sum()*100])
print(df)