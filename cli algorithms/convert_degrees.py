# create a cli that converts a degree to either celsius from fahrenhiet or the reverse depending on what the user wants

import math

def firstQ():
  response = input('\nWould you like to convert Cel to Fah or Fah to Cel?\nCF or FC: ')

  switcher = {
    'CF': cel_to_fah,
    'FC': fah_to_cel
  }

  reaction = switcher.get(response.upper(), '\nInvalid choice for conversion!')

  if (type(reaction) == str):
    print(reaction)
    firstQ()
  else:
    reaction()

def cel_to_fah():
  # c / 5 * 9 + 32
  cel = int(input('\nPlease enter your celsius degree!: '))
  fah = math.ceil(((cel / 5) * 9) + 32)
  print(f'\nThe fahrenheit converted from your celsius ({cel}) is {fah}')
  again()

def fah_to_cel():
  # f - 32 * 5 / 9
  fah = int(input('\nPlease enter your fahrenheit degree!: '))
  cel = math.ceil(((fah - 32) * 5) / 9)
  print(f'\nThe celsius converted from your fahrenheit ({fah}) is {cel}')
  again()

def again():
  response = input('\nWould you like to convert another temperature?\n(Y/N): ').upper()

  if (response[0] == 'Y'):
    firstQ()
  else:
    return

firstQ()