from inputModification import *
from stringGeneration import *
from dnaFragmentSynthesis import *
from maxValue import *

items={}    #dictionary which has all required values stored at various processing stages
result={}   #final answer of 0/1 knapsack problem

#Calling function to take corresponding inputs
items=Input_Modification()

#Getting the mutiplication factor by which the initial arrays were processed
mul_factor = items["mul_factor"]

#Generating corresponding Ds,Dx compliment strands
items["Ds"],items["Dx"]=GenerateStrands(items)

#Generating corresponding connection codes
items["connection_code"]=ConnectionCode()

with open("strings.csv",'w') as tf:
    csvwriter=csv.writer(tf)
    csvwriter.writerow(['S.No','Weight','Value'])
    for i in range(len(Ds)):
        csvwriter.writerow([i+1,Ds[i],Dx[i]])

#Synthesizing all possible fragments        
selected = SynthesizeDnaFragments(items)
items ["selected_fragments"] = selected["selected_fragments"]
items ["selected_items"] = selected["selected_items"]

#Result of our processing
result=maxProfitItems(items)
print("Items included: " + str(result["items"]))
print("Maximum Profit: " + str(result["highest_profit"]))
print("Total Weight: " + str(result["highest_weight"]//mul_factor))
