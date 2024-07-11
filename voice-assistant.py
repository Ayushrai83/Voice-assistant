import pyttsx3
import random
import pickle
import csv
x=0 #pointer
engine = pyttsx3.init()#voice assistant feature
engine.say('hello sir')
engine.say('Amazon in your service')
engine.runAndWait()
engine.say('i am your voice assistant , Amazon. I have various in built functions and can help you in some tasks. ')
engine.runAndWait()


engine.say('Enter command, do you want to open a file, play a game, listen to a joke or want to stop')
engine.runAndWait()
n=int(input("Enter command, do you want to open a file-1, play a game-2, listen to a joke-3 or want to stop-4: "))
while x!=1:

    if n==1:
        engine.say('enter command, text file, binary file or csv file')
        engine.runAndWait()
        
        a=int(input("enter command, text file-1, binary file-2, csv file-3: "))
        if a==1:#text file
            
            engine.say('enter file name')
            engine.runAndWait()
            b=input("enter file name: ")
            file=open(b,"a+")

            engine.say('do you want to write or read ')
            engine.runAndWait()
            c=input("do you want to write(w) or read(r): ")
            if c=="r":
                file=open(b,"r+")

                str1=file.read()
                print(str1)

                engine.say(str1)
                engine.runAndWait()
                file.close()
                

            elif c=="w":
                file=open(b,"a+")
                str2=input("enter data: ")
                file.write(str2)
                file.close()
                
            else:
                print("Thank you!")
                

            


        elif a==2:#binary file
            engine.say('enter file name')
            engine.runAndWait()
            b1=input("enter file name: ")
            file1=open(b1,"ab+")
            engine.say('do you want to write or read ')
            engine.runAndWait()
            c1=input("do you want to write(w) or read(r): ")
            if c1=="r":
                file1=open(b1,"rb+")
                str3=pickle.load(file1)
                print(str3)
                engine.say(str3)
                engine.runAndWait()
                file1.close()
                            
            elif c1=="w":
                str4=input("enter data: ")
                pickle.dump(str4,file1)
                file1.close()
                
            else:
                print("Thank you!")

        elif a==3:#csv file
            engine.say('enter file name')
            engine.runAndWait()
            b2=input("enter file name: ")
            file2=open(b2,"a+")
            engine.say('do you want to write or read ')
            engine.runAndWait()
            c2=input("do you want to write(w) or read(r): ")
            if c2=="r":
                file2=open(b2,"r+")
                creader=csv.reader(file2)
                for i in creader:
                    print(i)
                file2.close()
                
                
            elif c2=="w":
                file2=open(b2,"a+")
                data=input("enter data: ")
                cwriter=csv.writer(file2)
                cwriter.writerow(data)
                
                file2.close()
                
            else:
                print(" Thank you!")

        else:
            print("please type 1,2 or 3")
            


    elif n==2:
        engine.say("what game do you want to play?")
        engine.runAndWait()
        print("what game do you want to play?")
        engine.say("roll a dice, rock paper scissors or guess a number ")
        engine.runAndWait()
        game=int(input("roll a dice-1, rock paper scissors-2, guess a no.-3: " ))

        if game==1:#rolling a dice
            engine.say("press r for roll and s for stop ")
            engine.runAndWait()
            
            roll=input("press r for roll and s for stop: ")
            m=0
            while roll=="r" :
                roll1=random.randrange(1,7)
                print(roll1)
                engine.say(roll1)
                engine.runAndWait()
                m=roll1
                while roll1==6:
                    roll1=random.randrange(1,7)
                    print(roll1)
                    engine.say(roll1)
                    engine.runAndWait()
                    m+=roll1
                if m>=18:
                    engine.say("oh no, your move is cancelled")
                    engine.runAndWait()
                    print("oh no, your move is cancelled") 
                else:
                    engine.say("move")
                    engine.say(m)
                    engine.say("spaces")
                    engine.runAndWait()
                    print("move",m,"spaces\n")
                engine.say("wanna roll again? print r")
                engine.runAndWait()    
                roll=input("wanna roll again? print r: ")
            else:
                print("ok thanks!")
            
        elif game==2:# rock,paper and scissors
                comp=0
                you=0
                s=0
                engine.say("how many turns 3,5,10 or 15 ?")
                engine.runAndWait()
                turn=int(input("how many turns 3,5,10 or 15?: "))
                while turn>you and turn>comp:
                    
                    n=input("rock(r),paper(p)or scissors(s)?: ")
                    a=random.randrange(1,4)

                    if a==1:
                        print("rock")

                    elif a==2:
                        print("paper")

                    else:
                        print("scissors")

                    if (n=="r" and a==1) or (n=="p" and a==2) or (n=="s" and a==3):
                        print("draw")
                        s+=1
                        print("you-",you  ,"computer-",comp, "\n" )

                    elif (n=="r" and a==3) or (n=="p" and a==1) or (n=="s" and a==2):
                        print("you got one point")
                        s+=1
                        you+=1
                        print("you-",you  ,"computer-",comp, "\n" )

                    elif (n=="r" and a==2) or (n=="p" and a==3) or (n=="s" and a==1):
                        print("computer got one point")
                        s+=1
                        comp+=1
                        print("you-",you  ,"computer-",comp, "\n" )
                    else:
                        print("bad call. try again")

                if you>comp:
                    engine.say("you win")
                    engine.runAndWait()
                    
                    print("you win")
                    print("you-",you)
                    print("computer-",comp)
                else:
                    engine.say("computer wins")
                    engine.runAndWait()
                    
                    print("computer wins")
                    print("you-",you)
                    print("computer-",comp)

                

        elif game==3:#guessing a random no.
                    
                upper=int(input("enter upper range: "))
                lower=int(input("enter lower range: "))

                random= random.randint(lower,upper)
                engine.say("guess the number: ")
                engine.runAndWait()
                    
                no= int(input("guess the no.: "))
                if no==random:
                    engine.say("congratulations you win,the number was")
                    engine.runAndWait()

                    engine.say(random)
                    engine.runAndWait()
                    print("congrats you win,the no. was",random)
                else:
                    engine.say("sorry it was not the number chosen by the computer. The number was")
                    engine.runAndWait()

                    engine.say(random)
                    engine.runAndWait()
                    
                    print("sorry it was not the no. chosen by the computer. The no. was",random)

                
    elif n==3:#jokes

        jo=random.randint(1,4)
        if jo==1:
            engine.say("did you hear about the mathematician who's afraid of negative numbers ?") 
            engine.runAndWait()

            engine.say("he will stop at nothing to avoid them. haha") 
            engine.runAndWait()


            print("did you hear about the mathematician who's afraid of negative numbers? he will stop at nothing to avoid them")


        elif jo==2:
            engine.say("Hear about the new restaurant called Karma ?") 
            engine.runAndWait()

            engine.say("There’s no menu: You get what you deserve. haha") 
            engine.runAndWait()

            
            print("Hear about the new restaurant called Karma?There’s no menu: You get what you deserve.")

        elif jo==3:
            engine.say("Did you hear about the claustrophobic astronaut ?") 
            engine.runAndWait()

            engine.say("He just needed a little space. haha") 
            engine.runAndWait()
            print("Did you hear about the claustrophobic astronaut?He just needed a little space.")

        else:
            engine.say("Why don’t scientists trust atoms") 
            engine.runAndWait()

            engine.say("Because they make up everything. haha") 
            engine.runAndWait()
            print("Why don’t scientists trust atoms? Because they make up everything.")


    else:
        x=1
        break

    engine.say('Enter command, do you want to open a file, play a game, listen to a joke or want to stop')
    engine.runAndWait()
    n=int(input("Enter command, do you want to open a file-1, play a game-2, listen to a joke-3 or want to stop-4: "))
    

engine.say('Thank you')
engine.runAndWait()
print("Thank you")







