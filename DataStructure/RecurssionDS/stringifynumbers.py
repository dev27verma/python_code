obj1 = {
    "num": 1,
    "test": [],
    "data": {
        "val": 4,
        "info": {
            "isRight": True,
            "random": 22
        }
    }
}


def stringify_numbers(obj):
    for key in obj:
        if type(obj[key]) is int:
            obj[key] = str(obj[key])
        if type(obj[key]) is dict:
            obj[key] = stringify_numbers(obj[key])
    return obj


print(stringify_numbers(obj1))
