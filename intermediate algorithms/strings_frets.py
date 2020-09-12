"""
Write a function that gets a string number and a fret of a 6-string guitar in 'standard tuning' and return the corresponding note. For this challenge we use a 24 fret model.
"""

def string_fret(st, fr):
  notes = "C, C#/Db, D, D#/Eb, E, F, F#/Gb, G, G#/Ab, A, A#/Bb, B".split(", ")

  if (st < 1 or st > 6 or fr < 1 or fr > 24):
    return "Invalid input"

  # string lists created by slicing through the notes list
  strings = {}
  string1 = notes[4:] + notes[:4]
  string1 += string1
  string1.append(notes[4])
  strings["string1"] = string1

  string2 = notes[11:] + notes[:11]
  string2 += string2
  string2.append(notes[11])
  strings["string2"] = string2
  
  string3 = notes[7:] + notes[:7]
  string3 += string3
  string3.append(notes[7])
  strings["string3"] = string3

  string4 = notes[2:] + notes[:2]
  string4 += string4
  string4.append(notes[2])
  strings["string4"] =string4

  string5 = notes[9:] + notes[:9]
  string5 += string5
  string5.append(notes[9])
  strings["string5"] = string5

  string6 = notes[4:] + notes[:4]
  string6 += string6
  string6.append(notes[4])
  strings["string6"] = string6

  return_string = "string{}".format(st)
  
  return strings[return_string][fr]
  

print(string_fret(2, 10))