import json

with open("../recipes/block_ids.json") as f:
    all_item_data = json.load(f)

with open("../recipes/block_recipies.json") as f:
    block_recipes = json.load(f)

input = {"Redstone Comparator":4, "Ice":16476, "Oak Sign":1411, "Quartz Slab":130, "White Concrete":12, "Chest":6, "Redstone Dust":5, "Hopper":3, "Dropper":2, "Stone Button":2, "Dispenser":1, "Light Blue Wool":1, "Observer":1, "Piston":1, "Redstone Repeater":1, "Stone Pressure Plate":1, "Warped Fence":1, "Warped Planks":1}
# input = {"Piston":1}
item_names = {}
item_ids = {}
needed_resources = {}
useful_block_ids = {}
changes = []
# data = {}
# currentline = 0
# 
# with open("../data/Ice_Farm.txt") as f:
#     for line in f:
#         if currentline == 1:
#             chunks = line.split("'")
#             odd_chunks = chunks[1::2]
#             data["title"] = "".join(odd_chunks)
#         currentline += 1
# 
# print(data)

for item_data in all_item_data:
    item_names[item_data["displayName"]] = str(item_data["id"])
    item_ids[str(item_data["id"])] = item_data["displayName"]

for item_Name in input.keys():
    if "Concrete" in item_Name and "Powder" not in item_Name:
        changes.append([item_Name + " Powder", item_Name])
    print(changes)


for change in changes:
    if change[1] in input.keys():
        input[change[0]] = input.pop(change[1])

    
print(input)

def displayNameToId(input):
    for item_name in item_names:
        for key in input.keys():
            if item_name == key:
                useful_block_ids[key] = item_names[item_name]
    return useful_block_ids

useful_block_ids = displayNameToId(input)

def IdToDisplayName(input):
    output = {}
    for item_id, item_name in item_ids.items():
        for key in input.keys():
            if str(key) == str(item_id):
                # output[key] = item_name
                output[item_name] = input[key]
    return output



#looks at every item name in minecraft, and see if its in useful_block_ids.
for itemName, id in useful_block_ids.items():
    try:
        recipe = block_recipes[id]
        if "inShape" in recipe[0].keys():
            print("The item: ", itemName, "has the recipe", recipe[0]["inShape"])
            for row in recipe[0]["inShape"]:
                for item in row:
                    # print(item)
                    if item in needed_resources.keys():
                        needed_resources[item] += 1
                    else: 
                        needed_resources[item] = 1
        elif "ingredients" in recipe[0].keys():
            print("The item: ", itemName, "has the recipe", recipe[0]["ingredients"])
            for item in recipe[0]["ingredients"]:
                if item in needed_resources.keys():
                    needed_resources[item] += 1
                else: 
                    needed_resources[item] = 1
    except KeyError:
        print(f"{itemName} does not have a crafting recipe\n")
    

# print(needed_resources)
print(IdToDisplayName(needed_resources))

# If the term ingredients is returned then that means that its a crafting recipe that does not have a shape to it


