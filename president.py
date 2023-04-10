import json

# file syntax:
# line 1: #presidents:[(<name>:<party>:<state>);...]
# line 2: #hobbies:[(<name>:<hobby>);...]
with open("presidents.txt", "r") as f:
    presidents = f.readline()
    hobbies = f.readline()
    # print(presidents)
    # print(hobbies)

presidentsJSON = dict()

# presidents will be saved as a json structure with the syntax:
# [{"<name>":{"party":<party>, "state":<state>, "hobby": [<hobby1>, <hobby2>, ...]}, ...}, ...]
presidents = presidents.replace("#presidents:[", "").replace("]", "").replace("(", "").replace(")", "").split(";")
for pr in presidents:
    pr = pr.split(":")
    presidentsJSON[pr[0]] = {"party": pr[1], "state": pr[2], "hobby": []}

hobbies = hobbies.replace("#hobby:[", "").replace("]", "").replace("(", "").replace(")", "").split(";")
for h in hobbies:
    h = h.split(":")
    presidentsJSON[h[0]]["hobby"].append(h[1])

with open("presidents.json", "w") as f:
    json.dump(presidentsJSON, f, indent=4)

def filterKeys(dikt, func):
    keys = list()
    for key, value in dikt.items():
        if func(key, value):
            keys.append(key)
    return keys

def printList(lst):
    string = "\n"
    for i in lst:
        string += (i + "\n")
    return string


republicans = filterKeys(presidentsJSON, lambda key, val: val["party"] == "Republican")
print(f"========== 2a ========== {printList(republicans)}")
republicans.sort()
print(f"========== 2b ========== {printList(republicans)}")


notdemocrats = filterKeys(presidentsJSON, lambda key, val: val["party"] != "Democratic")
# print(f"Non-democrat presidents: {printList(notdemocrats)}")
print(f"Non-democrat presidents and their hobbies:")
for pres in notdemocrats:
    hobby = presidentsJSON[pres]["hobby"]
    party = presidentsJSON[pres]["party"]
    for hobi in hobby:
        print(f"{party}:{hobi}")
    # print(f"{pres} -> {presidentsJSON[pres]['hobby']}, {presidentsJSON[pres]['party']}")
