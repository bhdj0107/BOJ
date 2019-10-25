pr_count = int(input())
pr_list = []
for i in range(pr_count):
	pr_list.append([])
	pr_list[i].append(list(map(int, input().split())))
	pr_list[i].append(input())
	pr_list[i].append(input())




for i in range(pr_count):
	pt = 0
	cpt = 0
	l_stack = [0]
	stack = [pr_list[i][0][2]]
	for j in range(stack[0]):
		stack.append(pr_list[i][2][j])
	lpt_dict = {0:0}
	for _ in range(50000000):

		if cpt == pr_list[i][0][1]:
			ans = "Terminates"
			break

		if pr_list[i][1][cpt] == '+':
			lpt_dict[pt] += 1


		elif pr_list[i][1][cpt] == '-':
			lpt_dict[pt] -= 1

		elif pr_list[i][1][cpt] == '[':
			l_stack[0] += 1
			l_stack.append([cpt,pt,lpt_dict[pt]])

		elif pr_list[i][1][cpt] == ']':
			if lpt_dict[l_stack[l_stack[0]][1]] == l_stack[l_stack[0]][2]:
				ans = "Loops " + str(l_stack[l_stack[0]][0]) + " " + str(cpt)
				break
			elif lpt_dict[l_stack[l_stack[0]][1]] == 0:
				del l_stack[l_stack[0]]
				l_stack[0] -= 1
			else:
				cpt = l_stack[l_stack[0]][0] - 1

		elif pr_list[i][1][cpt] == '<':
			pt -= 1
			if pt == -1:
				pt = pr_list[i][0][0] - 1
			try:
				lpt_dict[pt] += 0
			except:
				lpt_dict[pt] = 0

		elif pr_list[i][1][cpt] == '>':
			pt += 1
			if pt == pr_list[i][0][0]:
				pt = 0
			try:
				lpt_dict[pt] += 0
			except:
				lpt_dict[pt] = 0

		elif pr_list[i][1][cpt] == ',':
			if stack[0] != 0:
				lpt_dict[pt] = ord(stack[1])
				del stack[1]
				stack[0] -= 1
			else:
				lpt_dict[pt] = 255

		cpt += 1
	print(ans)


