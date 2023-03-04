# Question 1:
# You are required to complete the following two functions.
# 1. find_max: find the max value of an array of numbers.
# 2. find_position: find the first position of the target number inside an array of numbers. The position should be counted starting from 0, if you can't find the target, please return -1.
# Reminder: you cannot use those built-in functions like max() and index() to complete this assignment, please implement it by yourself.

def find_max(numbers):
  # Version 1
  max = numbers[0]
  for i in numbers[1:]:
    if i > max:
      max = i
  return max

  # # Version 2
  # return sorted(numbers, reverse=True)[0]

def find_position(numbers, target):
  position = -1
  for i, num in enumerate(numbers):
    if num == target:
      position = i
      break
  return position

print(find_max([1, 2, 4, 5]) ); # should print 5
print(find_max([5, 2, 7, 1, 6]) ); # should print 7
print(find_position([5, 2, 7, 1, 6], 5)) # should print 0 print(find_position([5, 2, 7, 1, 6], 7)) # should print 2 print(find_position([5, 2, 7, 7, 7, 1, 6], 7)) # should print 2 (the first one)
print(find_position([5, 2, 7, 1, 6], 8)) # should print -1