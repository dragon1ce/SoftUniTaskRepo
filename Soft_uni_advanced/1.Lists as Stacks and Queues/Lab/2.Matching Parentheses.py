entry = list(input())
l_pars = []
for index in range(len(entry)):
    if entry[index] == "(":
        l_pars.append(index)
    elif entry[index] == ")":
        start_index = l_pars.pop()
        end_index = index + 1
        print("".join(entry[start_index:end_index]))
