# find longest word in a string inputted by user

def find_longest():
  string = input('\nEnter a phrase and I will return to you the londest word from that phrase!\nphrase: ')
  string_lst = string.split()
  longest = None
  for idx, word in enumerate(string_lst):
    if (idx + 1) < len(string_lst):
      if len(word) > len(string_lst[idx + 1]):
        longest = word
      else:
        longest = string_lst[idx + 1]
  print(f'\nThe longest word found was: {longest}')

find_longest()