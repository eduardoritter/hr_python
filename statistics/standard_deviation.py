#number = int(input())
#elements = list(map(int, input().split()))

elements, number = [10, 40, 30, 50,20] , 5

mean = sum(elements) / number

squared_distance = [(e - mean) ** 2 for e in elements]

#the power of 0.5 is the same as square root
print("%.1f" %(sum(squared_distance) / number ) ** 0.5)

""" 
   Solution using Python 3
"""

from statistics import pstdev

print("%.1f" % pstdev(elements))

