# Question 2:
# Complete the following functions by Python
# 1. count: return an object which shows the count of each character.
# 2. group_by_key: return an object which shows the summed up value of each key.
# Note:
# 1. The input format is different for these two functions.
# 2. In the second function, the input may have the same key but different values, the output should have each key only once.

def count(input):
  # Version 1
  count_object = {}
  input_set = sorted(set(input))
  for character in input_set:
    count_object[character] = 0
  for character in input:
    count_object[character] += 1
  return count_object

  # # Version 2
  # count_object = {}
  # input_set = sorted(set(input))
  # for character in input_set:
  #   count_object[character] = input.count(character)
  # return count_object

input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}

def group_by_key(input):
  count_object = {}
  for item in input:
    if item['key'] in count_object:
      count_object[item['key']] += item['value']
    else:
      count_object[item['key']] = item['value']
  return count_object

input2 = [
{'key': 'a', 'value': 3}, {'key': 'b', 'value': 1}, {'key': 'c', 'value': 2}, {'key': 'a', 'value': 3}, {'key': 'c', 'value': 5}
]
print(group_by_key(input2)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}