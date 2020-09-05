def stutter(word):
    stut = word[:2] + "..."
    stuts = stut + " " + stut + " "
    ending = word + "?"
    return(stuts + ending)


stutter("hey")
