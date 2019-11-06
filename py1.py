""""for i in [1, 2, 3, 4, 5]: print(i)
for j in [1, 2, 3, 4, 5]: print(j)
print(i + j)

print (i)
print ("done looping")"""

empty_dict = {} # Pythonic

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

tweet = {
"user" : "joelgrus",
"text" : "Data Science is Awesome",
"retweet_count" : 100,
"hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}
tweet_keys = tweet.keys() # list of keys tweet_values = tweet.values() # list of values
tweet_values = tweet.values() # list of values
print(tweet_keys, tweet_values)