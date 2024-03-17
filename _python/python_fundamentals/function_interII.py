#1 Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ]
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
#1
x[1]=[15,8,9]
print(x)
#2
#students[0]=[{'first_name':  'Michael', 'last_name' : 'Bryant'}]
def change_LastName(students):
    students[0]['last_name']="Bryant"
    return students
print(change_LastName(students))
#3
sports_directory['soccer']=['Andres', 'Ronaldo', 'Rooney']
print(sports_directory)
#4
z[0]={'x': 10, 'y': 30}
print(z)


#2 Iterate Through a List of Dictionaries
students_Dict = {
    "std1": {'first_name':  'Michael', 'last_name' : 'Jordan'},
    "std2": {'first_name' : 'John', 'last_name' : 'Rosales'},
    "std3": {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    "std4":{'first_name' : 'KB', 'last_name' : 'Tonel'}
}

stds_to_update = {'std1', 'std2', 'std3','std4'}
for std in stds_to_update:
    std = "{std1} {std2} {std3} {std4}".format(std1 = 'first_name - Michael, last_name - Jordan',
                                               std2 = 'first_name - John, last_name - Rosales',
                                               std3 = 'first_name - Mark, last_name - Guillen',
                                               std4 = 'first_name - KB, last_name - Tonel')
    print(std)
print(students_Dict)

#3 iterateDictionary2(key_name, some_list)
List = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'}
]
def iterateDictionary2(key_name, students):
    for x in range(0,len(List)):
        print(List[x][key_name])
iterateDictionary2('first_name',List)

#4 Iterate Through a Dictionary with List Values
dict = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for key,list_values in some_dict.items():
        print(len(key),key)
        for item in list_values:
            print(item)
printInfo(dict)





