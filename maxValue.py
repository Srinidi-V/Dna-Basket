from stringGeneration import *

#This dictionary stores the highest profit items list, profit value, weight value
final_items={}

#Function to find the profit obtained from every item list
def findProfit(item_list,items):
    added_value=''
    for item in item_list:
        item_value=items["Dx"][item-1]
        for ch in item_value:
            added_value=added_value+Compliment(ch)
    return added_value        

#Function to find which subset gives the highest profit
def maxProfitItems(items):
    max_value=0
    item_nos=[]
    for item_list in items["selected_items"]:
        value=findProfit(item_list,items)
        if(len(value)>max_value):
            max_value=len(value)
            item_nos=item_list
        
    final_items["items"]=item_nos
    final_items["highest_profit"]=max_value
    final_items["highest_weight"]=len(''.join(items["selected_fragments"][items["selected_items"].index(item_nos)]))
    
    return final_items