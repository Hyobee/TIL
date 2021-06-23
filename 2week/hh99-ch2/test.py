import sys
a, b = map(int,sys.stdin.readline().split())

H = int(a)
M = int(b)

if M >= 45:
	print(H, M-45)
else:
	if H==0:
		print(23, M+60-45)
	else:
		print(H-1, M+60-45)