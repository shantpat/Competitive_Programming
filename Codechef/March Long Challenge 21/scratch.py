T = int(input())

for t in range(T):
	N, K = map(int, input().split())
	String = list(input())
	counter = 0
	for i in range(N//2):
		if String[i] != String[N-i-1]:
			counter += 1


	print('Case #'+str(t+1)+':',abs(K-counter))