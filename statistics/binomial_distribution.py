from math import factorial

def combination(number_elements, combination_length):
    return factorial(number_elements) / (factorial(combination_length) * factorial(number_elements - combination_length))

ratio = 1.09 / (1.09 + 1)
number_children = 6
number_minimum_boys = 3

proportion = 0

for number_of_boys in range(number_minimum_boys, number_children + 1):
    proportion += combination(number_children, number_of_boys) * (ratio ** number_of_boys) * ((1 - ratio) ** (number_children - number_of_boys))

print("%.3f" % proportion)
