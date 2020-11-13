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

#Checks our two constraints as required
def Check_Constraint(weight,value,n):
    a = []
    for i in range(n):
        if (weight[i] >= value[i]) and ((weight[i] - value[i]) % 2 == 0):
            a.append(1)
        else:
            a.append(0)
    return a

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
    
    i = 2   #variable to keep track of the multiplier
    flag = 0    #check value
    
    #Checks for the two constraints of our problem
    check_array = Check_Constraint(weight,value,n)
    
    #If satisfied as given
    if Count(check_array):
        flag = 1
        final = {"weight":weight, "value":value, "maxWeight":max_weight}
        return final
    
    else:
        weight1 = weight
        while flag==0 and i<20:     #20 - being our own set upperbound for manipulation
            weight1 = [element * i for element in weight]
            max_weight1 = max_weight * i
            i = i + 1
            check_array = Check_Constraint(weight1,value,n)
            if Count(check_array):
                flag = 1
                final = {"weight":weight1, "value":value, "maxWeight":max_weight1}
                return final
            else:
                continue
        #In case it still doesnt satisfy, we give our last manipulated value
        weight1 = [element * i for element in weight]
        max_weight1 = max_weight * i
        final = {"weight":weight1, "value":value, "maxWeight":max_weight1}
        return final
        

print(Input_Modification())