x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

x[1][0] = 15
print(x)

students[0]['last_name'] = 'Bryant'
print(students[0])

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z[0]['y'] = 30
print(z)

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterate_dictionary(some_list):
    for a_dict in some_list:  # This will start to look at all the indexs of some_list
        display_str = ""  # This creates an empty string for our later output
        for a_key in a_dict.keys():  # This will start to look at all the keys withing the indexs in some list
            # This will add to our empty string the sting of The Key and its Value. we format it like this so it adds all the items correctly as a string.
            display_str += f"{a_key} - {a_dict[a_key]}, "
        # What is happening here is that we added a comma and space to the end of our stings. This is funny looking so we are removing them. We did this by saying the String is now equal to itself slicing two off the end.
        display_str = display_str[:len(display_str) - 2]
        print(display_str)


iterate_dictionary(students)


def iterateDictionary2(key_name, some_list):
    for index in some_list:  # This will look into each index of Some_list
        # This will print out the key name of the index that we are currently looking in of Some_list
        print(index[key_name])


iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    for key in some_dict.keys(): #this will look at each key in the given dictonary
        print(len(some_dict[key]), key.upper()) #This will print of the length of the list within the key, and then capatilize it.
        for i in some_dict[key]: #This will go through each item in the key that were currently looking at ang print each one out individually.
            print(i)
printInfo(dojo)