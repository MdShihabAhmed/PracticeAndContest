direction = dict()
direction["N"] = "S"
direction["S"] = "N"
direction["E"] = "W"
direction["W"] = "E"
direction["NE"] = "SW"
direction["SW"] = "NE"
direction["SE"] = "NW"
direction["NW"] = "SE"

d = input()
print(direction[d])