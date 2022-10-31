print("WELLCOME")
print("SNAKE WATER GUN GAME")
print("Enter Input with First Capital letter")
import random
def Processing():
    c_p = 0
    c_val = 0
    u_val = 0
    Draw=0
    i=1

    while(i<=10):
        value = ["Snake", "Water", "Gun"]
        val = random.choice(value)
        #print(val)
        inp = input("Enter your Player : ")
        if inp == "Snake" or inp == "Gun" or inp == "Water":
            if val == "Snake":
                if inp == "Water":
                    print("Computer got 1 Point")
                    c_val = c_val + 1
                elif inp == "Gun":
                    print("You got 1 Point")
                    u_val = u_val + 1
                elif inp == "Snake":
                    #print(f"Both are Equal \nComputer Enter {val}  and got 0 Point \nYou Entered {inp} and you also got 0 Point")
                    print("Draw")
                    Draw=Draw+1
            elif val == "Gun":
                if inp == "Snake":
                    print("Computer got 1 Point")
                    c_val = c_val + 1
                elif inp == "Water":
                    print("You got 1 Point")
                    u_val = u_val + 1
                elif inp == "Gun":
                    #print(f"Both are Equal \nComputer Enter {val}  and got 0 Point \nYou Entered {inp} and you also got 0 Point")
                    print("Draw")
                    Draw = Draw + 1
            elif val == "Water":
                if inp == "Gun":
                    print("Computer got 1 Point")
                    c_val = c_val + 1
                elif val == "Snake":
                    print("You got 1 Point")
                    u_val = u_val + 1
                elif inp == "Water":
                    #print(f"Both are Equal \nComputer Enter {val}  and got 0 Point \nYou Entered {inp} and you also got 0 Point")
                    print("Draw")
                    Draw = Draw + 1
        else:
            print("You Enter Wrong Input")
        c_p = c_p + 1
        i = i + 1
        # now result
    if c_p<=10:
        print("F I N A L    R E S U L T")
        print("Computer win and got", c_val, "Points") if c_val>u_val else print("You win and got", u_val,"Points")
    print("Computer got  ",c_val, "Points")
    print("You got  ", u_val, "Points")
    print("Draws are : ",Draw)

# Here Program Start
if __name__ == '__main__':
    Processing()





