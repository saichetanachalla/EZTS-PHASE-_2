def solution(s):
	pair = []
	for ch in s:
		if ch == '(':
			pair.append(')')
		elif ch == '[':
			pair.append(']')
		elif ch == '{':
			pair.append('}')
		elif pair[-1] == ch:
			pair.pop()
	    else:
			return False
	return True


s1 = "()"
# output = True
s2 = "()[]{}"
# output = True
s3 = "{]"
# output = False
s4 = "([)]"
# output = False

print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4))