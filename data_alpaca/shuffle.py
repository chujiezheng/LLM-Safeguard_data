import random
import json

#random.seed(42)
data = json.load(open('./alpaca_eval_original.json'))
random.Random(42).shuffle(data)
json.dump(data, open('./alpaca_eval.json', 'w'), indent=2)
