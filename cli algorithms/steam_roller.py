"""
Flatten a nested array. You must account for varying levels of nesting.
"""

import json

def start():
  question1()

def question1():
  lst_string = input("\nPlease enter an list that you would like to have flattened!\nList: ")

  try:

    lst = json.loads(lst_string)

    print(lst)
    
    flatten_list(lst)

  except:
    print("\nPlease enter a list!\nYou entered: {}".format(lst_string))
    question1()


def flatten_list(lst):
  flattened = []
  for elm in lst:
    for item in elm:
      flattened.append(item)

  print("\nYour flattened list is:\n{}".format(flattened))

start()