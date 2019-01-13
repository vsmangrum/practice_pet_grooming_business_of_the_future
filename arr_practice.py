import random
import collections


# this is how you make an array

# the first is an empty array
# the second is how you make a list with items already in it
# the third is putting a in the array 3 times

a_arr = []
b_arr = ['item 1', 'item 2', 'item 3']
c_arr = ['a'] * 3

print('Part 1 :')
print('====================')
print(a_arr)
print(b_arr)
print(c_arr)
print()

# to add an item to a list that has already been created we use the ".append(<item>)" function call
# the ".append()" call only adds item to the END of the list

a_arr.append(1)
a_arr.append(2)
a_arr.append(3)

print("Part 2:")
print('====================')
print(a_arr)
print()

# to remove an item from an array we can one of several possibilities
# the first way is to do the ".pop()"  function call
# like ".append()" it only pops the item from END of the list

a_arr.pop()

print("Part 3:")
print('====================')
print(a_arr)
print()

# OR you could the ".remove()" function


print("Part 4:")
print('====================')
print('Array before ".remove("item 2":)')
print(b_arr)
print('Array after:')
b_arr.remove('item 2')
print(b_arr)
print()


# i am now going to make an array with random number values and sort it
# using the ".sort()" function call

temp_arr = [random.randint(0, 1000) for x in range(10)]
print(temp_arr)
temp_arr.sort()
print(temp_arr)
print()


# the ".Counter()" function comes with the "collections" library
# it is used to see how many times an element is within an array
big_arr = [random.randint(0,1000) for y in range(300)]

cnt_arr = collections.Counter()
for every in big_arr:
    cnt_arr[every] += 1

print(big_arr)
print(cnt_arr)
print()


john_arr = [1, 2, 3, 4, 5, 6, 7, 8]

print(john_arr[1])
random.shuffle(john_arr)

print(john_arr)



