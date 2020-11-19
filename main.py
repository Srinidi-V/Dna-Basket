from inputModification import *
from stringGeneration import *
from dnaFragmentSynthesis import *
from maxValue import *

items={}
result={}

items,mul_factor=Input_Modification()
items["Ds"],items["Dx"]=GenerateStrands(items)
items["connection_code"]=ConnectionCode()

"""with open("strings.csv",'w') as tf:
    csvwriter=csv.writer(tf)
    csvwriter.writerow(['S.No','Weight','Value'])
    for i in range(len(Ds)):
        csvwriter.writerow([i+1,Ds[i],Dx[i]])"""
        
selected = SynthesizeDnaFragments(items)
items ["selected_fragments"] = selected["selected_fragments"]
items ["selected_items"] = selected["selected_items"]

result=maxProfitItems(items)
print("Items included: " + str(final_items["items"]))
print("Maximum Profit: " + str(final_items["highest_profit"]))
print("Total Weight: " + str(final_items["highest_weight"]//mul_factor))
