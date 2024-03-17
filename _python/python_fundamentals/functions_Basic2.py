#Countdown
def count_down():
    for i in range (5,0,-1):
        print(i)
a()

#print_and_return
def print_and_return():
    list =[2,1]
    print(list[0])
    return list[1]
print_and_return()

#first_plus_length
def first_plus_length():
    list=[1,2,3,4,10]
    sum = list[0]+len(list)
    return sum
print(first_plus_length())

#Values Greater than Second
def greater():
    list=[5,2,3,2,1,4]
    low=0
    high=len(list)
    s=list[1]
    for i in range(low,high):
        if list[i]>s:
            list2=[]
            list2.append(list[i])
            list2=list2
            print(len(list2))
            print(list2)
        else:
            if len(list)<2:
                False 
greater()

#This Length, That Value
def length_value(size,value):
    list=[]
    list=[size,value]
    print(list)
    for i in range (0,len(list)):
        new_list=[value]*size
    print (new_list)
print(length_value(4,7))
print(length_value(6,2))
print(length_value(10,1))
