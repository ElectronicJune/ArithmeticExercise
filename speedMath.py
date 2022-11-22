import random
rounds = 0
operators = [" + "," - "," * "," / "]
difficulty = int(input("difficulty 1-10 : "))
score = 0
while True :
    rounds+=1
    i = random.randrange(0,4)
    if i==0:
        #addition
        num1=random.randrange(-(10**difficulty),10**difficulty)
        num2=random.randrange(-(10**difficulty),10**difficulty)
        ans = num1+num2
    elif i==1:
        #subtraction
        num1=random.randrange(-(10**difficulty),10**difficulty)
        num2=random.randrange(-(10**difficulty),10**difficulty)
        ans=num1-num2
    elif i==2:
        #multiplication
        num1=random.randrange(-(10**difficulty),10**difficulty)
        num2=random.randrange(-13,13)
        ans=num1*num2
    else :
        #division
        ans=random.randrange(-(10**difficulty),difficulty*4)
        num2=random.randrange(2,10)
        num1=ans*num2
    
    respond= int(input(f"{rounds}) {num1} {operators[i]} {num2} = "))
    if respond!=ans :
        print(f"wrong! answer is {ans}.")
        break
    score+=i+1
score*= 2**(difficulty)
print(f"game over\nscore: {score}")

while True :        
    pass
        
