from statistics import median

number = int(input())
elements = list(map(int, input().split()))
elements.sort()

middle = number//2

lower = elements[:middle]
upper = elements[middle + (number % 2):]

print(int(median(lower)))
print(int(median(elements)))
print(int(median(upper)))

""" 
   Solution using Python 3.8
"""

from statistics import quantiles

elements = [3, 7, 8, 5, 12, 14, 21, 13, 18]

for q in quantiles(elements):
    print(q)
 