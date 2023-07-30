# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

# 2. Print the difference between the largest and smallest value:
print(max(numbers) - min(numbers))

# 3. Print True if the list contains a 2 next to a 2 somewhere.
subsequent_twos = False
index = 0
for number in numbers:
    if numbers[index] == 2 and numbers[index + 1] == 2:
        subsequent_twos = True
    index += 1
print(subsequent_twos)

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
total = 0
sum_after_six = 0
seen_six = False
for number in numbers:
    total += number
    sum_after_six += number
    if number == 6:
        seen_six = True
        sum_after_six = number
    elif seen_six and number == 7:
        total -= sum_after_six
        sum_after_six = 0
        seen_six = False
print(total)

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 
total_sum = 0
seen_thirteen = False
for num in numbers:
    total_sum += num
    if num == 13:
        seen_thirteen = True
        total_sum -= 13
    elif seen_thirteen and num != 13:
        total_sum -= num
        seen_thirteen = False
print(total_sum)