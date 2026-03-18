text=input("Enter your text:").lower()

positive_words=["happy","good","great","excellent","love"]
negative_words=["sad","bad","angry","hate","worst"]

score=0
for word in positive_words:
    if word in text:
        score=score+1
for word in negative_words:
    if word in text:
        score=score-1
if score>0:
    print("😁 positive")
elif score<0:
    print("😒negative")
else:
    print("😐 neutral")

