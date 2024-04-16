guesssec = 89

guess = int(input("Guess a number: "))

while guess != guesssec:
      guess = int(input("Guess a number: "))
      if guess > guesssec:
            print("Too Low")
            guess = int(input("Guess a number: "))
      elif guess < guesssec:
               print("Too High")
               guess = int(input("Guess a number: "))
      else:
             break
print(f"Good The number Was {guesssec}!")