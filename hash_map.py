# Hash maps pair values (right) with keys (left)
# Ex:
# France:Paris
# Pakistan:Islamabad
# Japan:Tokyo
#
# Once they map data to a key, CANNOT change the key
# Keys must be an immutable data type
# Use tuples as keys instead of lists
# In python, hash maps are called dictionaries, but most people refer to them as hash maps

# First step is Initializing
city_map = {} # OR city_map = dict()
cities = ['Calgary', 'Vancouver', 'Toronto'], ['New York City', 'Austin', 'Seattle'], ['London', 'Manchester']
city_map['Canada'] = [] # have to initialize the key before assigning a value to it, otherwise you will get an error
city_map['USA'] = []
city_map['England'] = []

# Assigning values to keys
city_map['Canada'] += cities[0]
city_map['USA'] += cities[1]
city_map['England'] += cities[2]

# defaultdict has all keys already initialized
# This is another way to achieve the above:
# from collections import defaultdict
# city_map = defaultdict(list)
# cities = ["Calgary", "Vancouver", "Toronto"]
# city_map["Canada"] += cities

# 3 methods for retrieving data
# hashmap.keys() # This method returns all keys from the dictionary in the form of a list
# hashmap.values() # returns all values in the form of a list
# hashmap.items() # returns a list with all of the key value pairs in tuples

# Example Problem: Leetcode 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. you can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
# the original letters exactly once.
# Example 1:
# Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
# Example 2:
# Input: strs = [""]
# Output: [[""]]

from collections import defaultdict
anagram_map = defaultdict(list)
result = []

for s in strs:
    sorted_s = tuple(sorted(s))
    anagram_map[sorted_s].append(s)

for value in anagram_map.values():
    result.append(value)

return result

# Leetcode 1

prevMap = {} # val : index

for i, n in enumerate(nums):
    diff = target-n
    if diff in prevMap:
        return [prevMap[diff], i]
    prevMap[n] = i