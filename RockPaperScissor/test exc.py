# Python 3

a = [1, 2, 3]
try:
    print("Second element = %d" % (a[5]))

    # Throws error since there are only 3 elements in array
    print("Fourth element = %d" % (a[3]))

except Exception as e:
    print(f"An error occurred :{e}", e)
    raise ("BaseException",e)
