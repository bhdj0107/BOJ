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
	l_stack = []
	stack = []
	for j in range(pr_list[i][0][2]):
		stack.insert(0,pr_list[i][2][j])
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
			t_cpt = cpt + 1
			t_pt = pt
			while(1):
				if pr_list[i][1][t_cpt] == ']':
					break
				elif pr_list[i][1][t_cpt] == '<':
					t_pt += 1
				elif pr_list[i][1][t_cpt] == '>':
					t_pt -= 1
			# l_stack 에 루프 시작점, 메모리 포인터 자리, 메모리 포인터의 값 자리, 기존 인풋 길이 삽입
			try:
				lpt_dict[t_pt] += 0
			except:
				lpt_dict[t_pt] = 0
			l_stack.insert(0,[cpt,t_pt,lpt_dict[t_pt], len(stack)])

		elif pr_list[i][1][cpt] == ']':

			if lpt_dict[l_stack[0][1]] == l_stack[0][2] and len(stack) == l_stack[0][3]:
				ans = "Loops " + str(l_stack[l_stack[0]][0]) + " " + str(cpt)
				break

			elif lpt_dict[l_stack[0][1]] == 0:
				del l_stack[0]
			else:
				cpt = l_stack[0][0] - 1

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
			if len(stack) != 0:
				lpt_dict[pt] = ord(stack[0])
				del stack[0]
			else:
				lpt_dict[pt] = 255

		cpt += 1

	print(ans)


