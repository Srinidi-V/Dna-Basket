import random
import math
import csv

Ds=[]
Dx=[]
connection_code={}
letters=['A','T','G','C']

#This function defines the compliments for all letters
def Compliment(ch):
    if(ch=='T'):
        return 'A'
    elif(ch=='A'):
        return 'T'
    elif(ch=='G'):
        return 'C'
    elif(ch=='C'):
        return 'G'

#It finds the continuity of the strand passed as argument and returns continuity value & index    
def Continuity(strand):
    count=1
    maxi=0
    ch=strand[0]
    for y in range(1,len(strand)):
        if(ch==strand[y]):
            count+=1
        else:
            if(maxi<count):
                maxi=count
                index=y-1
            count=1
        ch=strand[y]
    if(count>maxi):
        maxi=count
        index=len(strand)-1
    return maxi,index

#This function replaces character where continuity occurs
def Mutate(strand,index):
    if(index!=len(strand)-1):
        temp=set((letters))-set((strand[index+1],strand[index]))
        char = ''.join(random.choices(list(temp), k = 1))
        strand=strand[:index]+char+strand[index+1:]
    else:
        strand=strand[:index]+Compliment(strand[index])
    return strand

#This generates Ds and Dx strands
def GenerateStrands(items): 
    for i,j in zip(items["weight"],items["value"]):
        strand = ''.join(random.choices(letters, k = i))
        maxi,index=Continuity(strand)
        while(maxi>2):
            strand=Mutate(strand,index)
            maxi,index=Continuity(strand) 
        Ds.append(strand)
        comp=''
        for k in range(math.ceil((i-j)/2),i-((i-j)//2)):
            comp=comp+Compliment(strand[k]) 
        Dx.append(comp)
    return Ds,Dx

#This generates connection codes
def ConnectionCode():
    for k1 in range(len(Ds)-1):
        for k2 in range(k1+1,len(Ds)):
            cc=''
            l1=len(Ds[k1])
            l2=len(Dx[k1])
            for x in range(math.ceil((l1-l2)/2) + l2,l1):
                cc=cc+Compliment(Ds[k1][x])
            l1=len(Ds[k2])
            l2=len(Dx[k2])
            for x in range(math.ceil((l1-l2)/2)):
                cc=cc+Compliment(Ds[k2][x])
            connection_code["D"+str(k1+1)+str(k2+1)]=cc
    return connection_code


