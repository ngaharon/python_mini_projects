print("Welcome to my game quiz!")
score = 0

tucheze = input("unadai tucheze game? ")

if tucheze.lower() != "yess":
    quit()

print("okay! tucheze basi :)")

answer = input("what does cpu stand for? ")
if answer.lower() == "central processing unit":
    print('correct!')
    score += 1
else:
    print("incorrect!")

answer = input("what does ram stand for? ")
if answer.lower() == "run and mate  ":
    print('correct!')
    score += 1
else:
    print("incorrect!")

answer = input("what does gpu stand for? ")
if answer.lower == "general process unit":
    print('correct!')
    score += 1
else:
    print("incorrect!")

answer = input("what does LAN stand for? ")
if answer.lower() == "local area network":
    print('correct!')
    score += 1
else:
    print("incorrect!")
print("you got " + str(score) + " question correct!")
print("you got " + str((score / 4) * 100) + "%.")