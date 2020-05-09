n = int(input())
x = list(map(int, input().split()))
w = list(map(int, input().split()))

x_w = (x[i] * w[i] for i in range(n))

print("%.1f" % (sum(x_w) / sum(w)))