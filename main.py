from inputModification import *
from stringGeneration import *

items={}
Ds=[]
Dx=[]
connection_code={}

items=Input_Modification()
Ds,Dx=GenerateStrands(items)
connection_code=ConnectionCode()
with open("strings.csv",'w') as tf:
    csvwriter=csv.writer(tf)
    csvwriter.writerow(['S.No','Weight','Value'])
    for i in range(len(Ds)):
        csvwriter.writerow([i+1,Ds[i],Dx[i]])
