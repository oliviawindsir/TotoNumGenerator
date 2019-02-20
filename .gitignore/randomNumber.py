
from random import shuffle

START_NUM = 1
END_NUM = 49

print("Hello 13 million~!\n")
print("Default - Press '6'\n")
print("System 7 - Press '7'\n")
print("System 8 - Press '8'\n")
print("System 9 - Press '9'\n")
systemType = int(input("\nWhich system are you buying?\n"))

uncalledNum = list(range(START_NUM, END_NUM+1))
selectedNum = []

for i in range(6): 
     pickedNum = random.choice(uncalledNum)
     selectedNum.append(pickedNum)
     uncalledNum.remove(pickedNum)
     print(pickedNum)
     print("\n")