import numpy
from scipy import stats

n = int(input())
x = list(map(int, input().split()))

mean = numpy.mean(x)
median = numpy.median(x)
mode = stats.mode(x)
 
print("%.1f" % mean)
print("%.1f" % median)
print(mode[0][0])