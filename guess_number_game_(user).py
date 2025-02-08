import random

def computer_guess():
  low = 1
  high = 100
  output = ""
  while output != "c":
    if low != high:
      guess_computer =  random.randint(low , high)
    else:
       guess_computer = low
    output = input(f"Is {guess_computer} too high (H) , too low (l) , or correct(C)?").lower()
    if output == "h":
      high = guess_computer - 1
    elif output == "l":
      low = guess_computer - 1
    else:
      print(f"Congratulations! {guess_computer} is a correct guess")
computer_guess()