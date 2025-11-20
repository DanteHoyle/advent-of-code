import json
import pprint


def json_sum_without_counting_red(json_obj: dict | list) -> int:
    sum = 0

    if isinstance(json_obj, dict):
        json_obj = [json_obj]

    for obj in json_obj:
        if isinstance(obj, int):
            sum += obj
            continue
        if isinstance(obj, str):
            continue
        if isinstance(obj, list):
            sum += json_sum_without_counting_red(obj)
            continue
        for k, v in obj.items():
            if isinstance(v, int):
                sum += v
            elif isinstance(v, (list, dict)):
                sum += json_sum_without_counting_red(v)
            else:
                print('v is unknown type:', v, type(v))
    return sum

with open('input.txt') as f:
    input_text = f.read()

input_json = json.loads(input_text)


for item in input_json:
    print(json_sum_without_counting_red(item))
