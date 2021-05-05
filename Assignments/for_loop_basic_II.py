# 1. Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

testlist = [-1, 6, 9, 3]
def biggie_siaze(list):
    for x in range (0, len(list), 1):
        if list[x] > 0:
            list[x] = "big"
    return list

print(biggie_siaze(testlist))

# 2. Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

testlista = [-1,1,1,1]
testlistb = [1,6,-4,-2,-7,-2]
def count_positives(list):
    count = 0
    for x in range(0, len(list), 1):
        if list[x] > 0:
            count += 1
    list[len(list) -1] = count
    return list
print(count_positives(testlista))
print(count_positives(testlistb))

# 3. Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

testlista = [1,2,3,4]
testlistb = [6,3,-2]
def sum_total(list):
    sum = 0
    for i in range(0,len(list),1):
        sum = sum + list[i]
    return sum
print(sum_total(testlista))
print(sum_total(testlistb))

# 4. Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5

testlist = [1,2,3,4]
def average(list):
    sum = 0
    for x in range(0,len(list),1):
        sum = sum + list[x]
    return sum/len(list)
print(average(testlist))

# 5. Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

testlista = [37,2,1,-9]
testlistb = []
def length(list):
    return len(list)
print(length(testlista))
print(length(testlistb))

# 6. Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

testlista = [37,2,1,-9]
testlistb = []
def minimum(list):
    if len(list) == 0:
        return False
    else:
        min = list[0]
        for x in range(1, len(list),1):
            if list[x] < min:
                min = list[x]
        return min
print(minimum(testlista))
print(minimum(testlistb))

# 7. Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

testlista = [37,2,1,-9]
testlistb = []
def maximum(list):
    if len(list) == 0:
        return False
    else:
        max = list[0]
        for x in range(1, len(list),1):
            if list[x] > max:
                max = list[x]
        return max
print(maximum(testlista))
print(maximum(testlistb))

# 8. Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

testlist = [37,2,1,-9]
def ultimate_analysis(list):
    ultimate_dictionary = {
        'sumTotal': 0,
        'average': 0,
        'minimum': 0,
        'maximum': 0,
        'length': len(list)
    }
    for x in range(0,len(list),1):
        ultimate_dictionary['sumTotal'] = ultimate_dictionary['sumTotal'] + list[x]
        if list[x] > ultimate_dictionary['maximum']:
            ultimate_dictionary['maximum'] = list[x]
        if list[x] < ultimate_dictionary['minimum']:
            ultimate_dictionary['minimum'] = list[x]
    ultimate_dictionary['average'] = ultimate_dictionary['sumTotal']/len(list)
    return ultimate_dictionary
print(ultimate_analysis(testlist))

# 9. Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

testlist = [37,2,1,-9]
def reverse_list(list):
    for x in range (0,int(len(list)/2),1):
        temp = list[x]
        list[x] = list[len(list)-1-x]
        list[len(list)-1-x] = temp
    return list
print(reverse_list(testlist))


