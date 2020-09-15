"""
A algorithm that takes in a string of DNA (A, T, C, G) in any order
and then generate and return a nested array of the proper dna pairs
"""
import re

def start():
  question1()

def question1():
  dna_string = input("\nPlease input a DNA-like string (contains A, C, T, G) to be compiled into a DNA paired 2D array. Example: ATCG\nString: ")

  regex = re.compile("[^atcgACTG]", re.IGNORECASE)
  test = regex.search(dna_string)

  if test is not None:
    print("\nYou entered an invalid DNA string: {}".format(dna_string))
  elif test == None:    
    switch_dict = {
      "A": "T",
      "T": "A",
      "C": "G",
      "G": "C"
    }

    dna_2d = []

    for letter in dna_string.upper():
      if switch_dict.__contains__(letter):
        dna_2d.append([letter, switch_dict.get(letter)])

    print("\nYour DNA 2D array is:\n{}".format(dna_2d))

start()