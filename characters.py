mylist = [{"name": "Tsuna", "show": "Katekyo Hitman Reborn", 
"like": True},
{"name": "Naruto", "show": "Naruto", 
"like": False},
{"name": "Ichigo", "show": "Bleach", 
"like": False},
{"name": "Sakura", "show": "Naruto", 
"like": False},
{"name": "Hibari", "show": "Katekyo Hitman Reborn", 
"like":  True},
{"name": "Gokudara", "show": "Kateyo Hitman Reborn",
"like": True}
]
def myFunc(e):
    return e["name"]
mylist.sort(key=myFunc)
print(mylist)
