length = int(input())
sen = input()
num = []
op = []
for i in range(length):
	if (bool(i%2)):
		op.append(sen[i])
	else:
		num.append(int(sen[i]))

bracket = [0 for _ in range(len(op))]

field = []
field.append(num)
field.append(bracket)
field.append(op)

def calculate(n1, n2, op):
	if (op == '+'):
		return n1 + n2
	if (op == '-'):
		return n1 - n2
	if (op == '*'):
		return n1 * n2

def make_bracket(pointer, field):
	if (pointer >= len(num) - 1):
		#곱셈 처리 총 계산
		print(field[0])
		print(field[1])
		print(field[2])
	else:
		make_bracket(pointer + 1, field)
		field[0][pointer] = calculate(field[0][pointer],field[0][pointer+1],field[2][pointer])
		field[1][pointer] += 1
		make_bracket(pointer + 2, field)


make_bracket(0, field)