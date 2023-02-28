obj1 = {
    "stuff": 'foo',
    "data": {
        "val": {
            "thing": {
                "info": 'bar',
                "moreInfo": {
                    "evenMoreInfo": {
                        "weMadeIt": 'baz'
                    }
                }
            }
        }
    }
}


def collect_strings(obj):
    result_arr = []
    for key in obj:
        if type(obj[key]) is str:
            result_arr.append(obj[key])
        if type(obj[key]) is dict:
            result_arr += collect_strings(obj[key])
    return result_arr


print(collect_strings(obj1))
