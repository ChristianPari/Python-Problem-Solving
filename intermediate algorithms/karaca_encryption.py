# Make a function that encrypts a given input with the following steps:
# Step 1: reverse the input
# Step 2: replace all vowels using the chart below
# a => 0 
# e => 1
# i => 2
# o => 2
# u => 3
# Step 3: add "aca" to the end of the word

def encrpyt(word):

  def convert_to_list(string):
    letters = []
    # this will "push" each letter into the letters list as a new index
    letters[:0] = string
    letters.reverse()
    return letters

  word_list = convert_to_list(word)

  for letter in word_list:
    idx = word_list.index(letter)
    if letter == "a":
      word_list[idx] = "0"
    elif letter == "e":
      word_list[idx] = "1"
    elif letter == "i" or letter == "o":
      word_list[idx] = "2"
    elif letter == "u":
      word_list[idx] = "3"

  converted = "".join(word_list)

  converted = converted + "aca"

  return converted

print(encrpyt("karaca"))