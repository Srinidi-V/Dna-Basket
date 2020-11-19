#Counts for the number of items satisfying the two imposed constraints
def Count(a):
    count = 0
    for i in range(len(a)):
        if a[i]==1:
            count = count + 1
    if count == len(a):
        return 1
    else:
        return 0

#Computing item numbers
def Item_Numbers(n):
    l=[]
    for i in range(n):
        l.append(i+1)
    return l

#Checks our two constraints as required
def Check_Constraint(weight,value,n):
    a = []
    for i in range(n):
        if (weight[i] > value[i]) and ((weight[i] - value[i]) % 2 == 0):
            a.append(1)
        else:
            a.append(0)
    return a

#Function to check when the weight>value constraint is first satisfied
def Check_First_Satisfy(weight,value,n):
    count = 0
    for i in range(n):
        if (weight[i] > value[i] and weight[i]-value[i]>1):
            count = count + 1
    if count == n :
        return 1
    else:
        return 0

#Main function to collect and manipulate inputs
def Input_Modification():
    #Number of items
    n = int(input("Number of items:"))

    weight = []     #List containing respective weights of items
    value = []      #List containing respective values of items
    
    #Obtaining values from user
    for i in range(n):
        weight.append(int(input("Weight of " + str(i+1) + " : ")))
        value.append(int(input("Value of " + str(i+1) + " : ")))
    
    #Maximum capacity of the bag
    max_weight = int(input("Enter the maximum weight allowed: "))
    
    item_num = Item_Numbers(n)
    
    i = 2   #variable to keep track of the multiplier
    flag = 0    #check value
    
    #Checks for the two constraints of our problem
    check_array = Check_Constraint(weight,value,n)
    
    #If satisfied as given
    if Count(check_array):
        flag = 1
        final = {"item_numbers":item_num, "weight":weight, "value":value, "max_weight":max_weight}
        return final
    
    else:
        weight1 = weight
        weight_first_satisfy = []   #Incase of strings that dont satisfy despite above 20 iterations
        track = 0   #First weight array that satisfies weight>value condition
        item_track = 0  #stores the corresponding i value
        while flag==0 and i<20:     #20 - being our own set upperbound for manipulation
            weight1 = [element * i for element in weight]
            max_weight1 = max_weight * i
            track=Check_First_Satisfy(weight1,value,n)
            #Storing first weight array that satisfies the weight>value condition just in case required
            if (track == 1) and (item_track == 0):
                weight_first_satisfy = weight1
                item_track = i
            i = i + 1
            check_array = Check_Constraint(weight1,value,n)
            if Count(check_array):
                flag = 1
                final = {"item_numbers":item_num, "weight":weight1, "value":value, "max_weight":max_weight1}
                return final
            else:
                continue
        #In case it still doesnt satisfy, we give our first weight>value satisfying array
        max_weight1 = max_weight * item_track
        final = {"item_numbers":item_num, "weight":weight_first_satisfy, "value":value, "max_weight":max_weight1}
        return final,item_track
        