from inputModification import *
from stringGeneration import *
from dnaFragmentSynthesis import *

items={}
Ds=[]
Dx=[]
connection_code={}

items=Input_Modification()
Ds,Dx=GenerateStrands(items)
connection_code=ConnectionCode()
"""
with open("strings.csv",'w') as tf:
    csvwriter=csv.writer(tf)
    csvwriter.writerow(['S.No','Weight','Value'])
    for i in range(len(Ds)):
        csvwriter.writerow([i+1,Ds[i],Dx[i]])"""
items["Ds"] = Ds
items["Dx"] = Dx
items["connection_code"] = connection_code


selected = SynthesizeDnaFragments(items)
items ["selected_fragments"] = selected["selected_fragments"]
items ["selected_items"] = selected["selected_items"]
print(items)