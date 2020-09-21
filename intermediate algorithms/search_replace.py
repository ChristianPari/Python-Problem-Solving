"""
Using a function that takes in parameters for a string, a word to find and a word to replace the found word, replace the found word with the second word and return the new string.

Case sensitive so if the word being replaced is Title Cased, the replacing word should follow suite.
"""

import re

def myReplace(st, before, after):
  st = st.split(' ')
  found_idx = st.index(before)

  if (re.match('[A-Z]', before[0]) != None):
    after = str.capitalize(after)
  
  st.remove(before)
  st.insert(found_idx, after.lower())
  st = ' '.join(st)
  return st

print(myReplace('A quick brown fox jumped over the lazy dog', 'jumped', 'Leaped'))