string = input("Enter a string: ").split()


def capialize_first(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0][0].upper() + arr[0][1:])
    return result + capialize_first(arr[1:])


print(capialize_first(string))
print(f"{' '.join(capialize_first(string))}")
