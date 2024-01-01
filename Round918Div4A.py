iterations=int(input())
for i in range(0, iterations):
    problem=input().split()
    problemcopy=problem
    i=problem[0]
    problem.remove(i)
    if i in problem:
        problem.remove(i)
        print(problem[0])
    else:
        print(int(i))
