import random
print("Hello World!")

ans = input("Print again? ")

while ans != "":
    oNum = random.randint(1,100)
    print(f"Hell{oNum * 'o'} World!")
    ans = input("Print again? ")


