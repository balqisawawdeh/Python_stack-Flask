#Biggie Size
def Biggie():
    biggie_size=[-1, 3, 5, -5]
    i=0
    while i<len(biggie_size):
        if biggie_size[i]>0:
            biggie_size[i]="big"
        i=i+1
        print(biggie_size)
print(Biggie())

#Count Positives
count_positives=[1,6,-4,-2,-7,2]
print(count_positives)
count=0
for j in range(len(count_positives)):
    if count_positives[j]> 0:
        count_positives[-1]=count
        count=count+1
    print(j,":",count,":",count_positives[-1])
print(count_positives)

#Sum Total
SumList=[1,2,3,4]
sum2=0
for x in range(0,len(SumList)):
    sum2=sum2 + SumList[x]
    print(sum2)

#Average
SumList=[1,2,3,4]
Avg=0
sum2=0
for y in range(len(SumList)):
    sum2=sum2 +SumList[y]
    Avg=sum2/len(SumList)
    print(Avg)

#Length
length=[37,2,1,-9]
print(len(length))
length2=[]
print(len(length2))

#Minimum
def Minimum():
    Min=[37,2,1,-9]
    if len(Min)>0:
        print ("min value element : ", min(Min))
    else:
        return False
print(Minimum())

#Maximum
def Maximum():
    Max=[37,2,1,-9]
    if len(Max)>0:
        print ("Max value element : ", max(Max))
    else:
        return False
print(Maximum())

#Ultimate Analysis
def DicList():
    DicList=[37,2,1,-9]
    if len(DicList)>0:
        sumTotal=0
        average=0
        for y in range(len(DicList)):
            sumTotal=sumTotal +DicList[y]
            average=sumTotal/len(DicList)
        print(sumTotal,average,min(DicList),max(DicList),len(DicList))
print(DicList())

#Reverse
# def Reverse():
#     DicList=[37,2,1,-9]

#     DicList.reverse()
#     print(DicList)
# print(Reverse())
def reverse_2(DictList):
    a=0
    med=len(DictList)/2
    for i in range (len(DictList)-1,int(med),-1):
        temp=DictList[a]
        DictList[a]=DictList[i]
        DictList[i]=temp
        a+=1
        print(DictList)
reverse_2([37,2,1,-9])
