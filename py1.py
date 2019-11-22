
"""empty_dict = {} # Pythonic

grades = { "Joel" : 80, "Tim" : 95 }
joels_grade = grades["Joel"]
print(joels_grade)
try:
    kates_grade = grades["Kate"]
except KeyError:
    print ("no grade for Kate!")

   
joel_has_grade = "Joel" in grades
kate_has_grade = "Kate" in grades
print(kate_has_grade)


joels_grade = grades.get("Joel", 0)
kates_grade = grades.get("Kate", 0) #dict.get(key, default = None)
#default − This is the Value to be returned in case key does not exist.

print(kates_grade)
print(joels_grade)

no_ones_grade = grades.get("adsi") # default default is None
print(no_ones_grade)
grades["Tim"] = 99
grades["Kate"] = 100
num_students = len(grades)
print(num_students)
# replaces the old value # adds a third entry
# equals 3
# less Pythonic
# dictionary literal
# equals 80
# True # False
# equals 80 # equals 0
"""

tweet = {
"user" : "joelgrus",
"text" : "Data Science is Awesome",
"retweet_count" : 100,
"hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}
tweet_keys = tweet.keys() # list of keys tweet_values = tweet.values() # list of values
tweet_values = tweet.values() # list of values
print(tweet_keys, tweet_values)

print("-------------------------------")
tweet_items = tweet.items() # list of (key, value) tuples
print(tweet_items)

print("user" in tweet_keys)
"user" in tweet
"joelgrus" in tweet_values
# True, but uses a slow list in
# more Pythonic, uses faster dict in
# True

from collections import defaultdict
dd_list = defaultdict(list)
dd_list[2].append(1)
print(dd_list)
dd_dict = defaultdict(dict)
dd_dict["Joel"]["City"] = "Seattle"
dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1
# list() produces an empty list # now dd_list contains {2: [1]}
# dict() produces an empty dict
# { "Joel" : { "City" : Seattle"}}
# now dd_pair contains {2: [0,1]}"""

# lecture d'un ficihier 
 filenames = glob.glob('*.txt')
 # On crée un dict complétement vide
 d = {}
 for file in filenames:
     #a chaque fois qu'on ouvre un fichier
     with open(file, 'r') as f:
         # on rajoute une clé a notre dictionnaire, elle va prendre le nom de notre fichier
         d[file] = f.read().splitlines()

print(d)