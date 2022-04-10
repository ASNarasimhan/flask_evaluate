import json, uuid
from random import randint

# Opening JSON file
# f = open('static/TPAMI2022_Viz/OBQA_vizSentences.json')
 
# returns JSON object as
# a dictionary
# data = json.load(f)
 
# Iterating through the json # list
#for i in data['10']:
#    print(i)


#print(data["11"])

#print(data.items()) #prints keys and values
# print(data.keys()) #prints keys
# print(data.values()) #prints values
#print([value for value in data.values()][2])

# print(data['ID']['concepts']['imgPath']['sentence'][0])

# Closing file
# f.close()

x = uuid.uuid4()
print(x)

def random_question():
    with open('static/TPAMI2022_Viz/OBQA_vizSentences.json') as fp:
        data = json.load(fp)
        random_index = randint(0, len(data)-1)
        print(random_index)
        print(([key for key in data.keys()][random_index], [value for value in data.values()][random_index]))
        dict_data = dict([value for value in data.values()][random_index])
        print(dict_data["sentence"])
        fp.close()
        return [value for value in data.values()][random_index]

print(random_question())