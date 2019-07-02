def solution(s):
	s_len = len(s)
	for j in reversed(range(1, s_len)):
		for i in range(s_len-j):
			if s[i:i+j+1] == s[i:i+j+1][::-1]:
				return j+1
	return 1