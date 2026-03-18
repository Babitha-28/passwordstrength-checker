password=input("Enter your password: ")
score=0

if len(password)>=6:
    score=score+1
if any(char.isdigit() for char in password):
      score=score+1
if any(char.isupper() for char in password):
    score=score+1
if score ==3:
     print("strong password")
elif score ==2:
     print("medium password")
else:
  print("weak password")

