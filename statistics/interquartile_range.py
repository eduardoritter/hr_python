from statistics import median

number = int(input())
elements = list(map(int, input().split()))
frequency = list(map(int, input().split()))

elem_fq = [elements[i] for i in range(number) for _ in range(frequency[i])]
elem_fq.sort()

middle = len(elem_fq)//2

lower = elem_fq[:middle]
upper = elem_fq[middle + (number % 2):]

print("%.1f" % (median(upper) - median(lower)))