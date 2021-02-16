# get marks, earnings
marks = float(input("Enter your mark: "))
earnings = float(input("Enter your earnings: "))

# compute and show destination
if marks >= 80 and earnings >= 500:
    print("You get to go to Europe.")
elif marks >= 80:
    print("You get to go to California.")
else:
    print("You stay home :(")
