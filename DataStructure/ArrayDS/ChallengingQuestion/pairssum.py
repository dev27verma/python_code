def pair_sum(myList, sum):
    result = []
    for i in range(len(myList)):
        for j in range(i + 1, len(myList)):
            if myList[i] + myList[j] == sum:
                result.append(str(myList[i]) + "+" + str(myList[j]))
    return result


print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7))
