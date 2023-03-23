## Now let’s change our function to compare against an entire string
## instead of a single character. This function should accept a string
## and a substring to compare against. The number of occurrences of the
## second parameter within the first parameter string are returned.
## What this means is that we are checking the number of occurrences
## of the shorter string (second parameter) within the longer string
##(first parameter).

# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
  return len(word.split(x))-1
# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1
