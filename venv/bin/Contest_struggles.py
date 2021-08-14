problems = list(map(int, input().split()))
difficulties = list(map(int, input().split()))

total_problems = problems[0]
solved = problems[1]
unsolved = problems[0] - problems[1]

total_difficulty_solved = solved * difficulties[1]
total_difficulty_unsolved = difficulties[0]*total_problems - total_difficulty_solved
difficulty_unsolved = total_difficulty_unsolved / unsolved

if 0 <= difficulty_unsolved <= 100:
    print(difficulty_unsolved)
else:
    print("impossible")


