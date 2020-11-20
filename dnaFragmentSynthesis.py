#Function to generate all subsets to find all possible combinations of strings
def StringCombinations(l): 
    base = [] 
    lists = [base] 
    for i in range(len(l)): 
        orig = lists[:]
        new = l[i]
        for j in range(len(lists)):
            lists[j] = lists[j] + [new]
        lists = orig + lists
    return lists   

#Combine list items into one string - generating a continuous strand of dna
def DnaCombine(dna_f):
    dna_combined_fragments = []
    for i in dna_f:
        l = len(i)
        s=''
        for j in range(l):
            s = s + i[j]
        dna_combined_fragments.append(s)
    return dna_combined_fragments

#Function to remove any empty subset formed
def RemoveEmptyFragment(l1):
    temp = []
    for i in l1:
        l = len(i)
        if l!=0:
            temp = temp + [i]
    return temp

#Function to filter out dna strands with weights greater than given capacity     
def GelElectrophoresis(dna,selected_items,items):
    temp_comb = DnaCombine(dna)
    weight = items["max_weight"]
    result = []
    result1 = []
    for i in range(len(temp_comb)):
        if len(temp_comb[i]) <= weight:
            result.append(temp_comb[i])
            result1.append(selected_items[i])
    final = {"selected_f": result , "selected_i" : result1 }
    return final

#Function to create all possible combination fragments and filter out unnecessary ones
def SynthesizeDnaFragments(items):
    
    #Taking required inputs for futher manipulation
    l1 = items["item_numbers"] 
    l2 = items["Ds"]
    
    #Taking all possible combinations
    item_combination = StringCombinations(l1)
    dna = StringCombinations(l2)
    
    #Remove empty fragment if formed
    dna_f = RemoveEmptyFragment(dna)
    item_combination_1 = RemoveEmptyFragment(item_combination)
    item_combination = item_combination_1
    
    #Performing gel electrophoresis and remove fragments whose weight is greater than the max capacity
    intermediate_selected = GelElectrophoresis(dna_f,item_combination,items)
    dna_combined_fragments = intermediate_selected["selected_f"]
    item_combination = intermediate_selected["selected_i"]
    
    #contains all processed, selected values
    selected_list= {"selected_fragments" : dna_combined_fragments, "selected_items" : item_combination}
    return selected_list
