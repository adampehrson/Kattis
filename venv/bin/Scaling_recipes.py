cases = int(input())

for x in range(cases):
    data = list(map(int, input().split()))
    ingredients = []
    main_ingredient = None
    for y in range(data[0]):
        temp = input().split()
        if temp[-1] == "100.0":
            main_ingredient = temp
        ingredients.append(temp)

    main_ingredient_amount = float(main_ingredient[1])*(data[2]/data[1])

    for y in range(len(ingredients)):
        ingredients[y][1] = float(ingredients[y][2])*main_ingredient_amount/100

    print("Recipe # {}".format(x+1))
    for y in ingredients:
        print("{} {}".format(y[0], y[1]))

    print("----------------------------------------")