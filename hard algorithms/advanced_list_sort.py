"""
Create a function that takes a list of numbers or strings and returns a list with the items from the original list stored into sublists. Items of the same value should be in the same sublist.

Examples

advanced_sort([2, 1, 2, 1]) ➞ [[2, 2], [1, 1]]

advanced_sort([5, 4, 5, 5, 4, 3]) ➞ [[5, 5, 5], [4, 4], [3]]

advanced_sort(["b", "a", "b", "a", "c"])➞ [["b", "b"], ["a", "a"], ["c"]]
"""

def advanced_sort(data):
  elm_dict = list(dict.fromkeys(data))
  print(elm_dict)

  new_list = []
  
  for i in range(0, elm_dict.__len__()):
    new_list.append([])

  for elm in elm_dict:
    idx = elm_dict.index(elm)
    for elm2 in data:
      if elm == elm2:
        new_list[idx].append(elm)
  
  return new_list
  

print(advanced_sort([1, 2, 1, 2])) # [[2, 2], [1, 1]]
print(advanced_sort([2, 1, 2, 1])) # [[2, 2], [1, 1]]
print(advanced_sort(["b", "a", "b", "a", "c"])) # [["b", "b"], ["a", "a"], ["c"]]