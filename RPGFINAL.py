# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 22:34:25 2021

@author: Prakhar Bhatnagar
"""


import random

print('''

█████████████████████████████████████████████
█▄─▀█▄─▄█▄─▄▄─█▄─▀█▀─▄█▄─▄▄─█─▄▄▄▄█▄─▄█─▄▄▄▄█
██─█▄▀─███─▄█▀██─█▄█─███─▄█▀█▄▄▄▄─██─██▄▄▄▄─█
▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀

█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█
██─▄─▄██─▄▄▄█─██▄─█
▀▄▄▀▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀
      _,.
    ,` -.)
   ( _/-\\-._
  /,|`--._,-^|            ,
  \_| |`-._/||          ,'|
    |  `-, / |         /  /     
    |     || |        /  /
     `r-._||/   __   /  /
 __,-<_     )`-/  `./  /
'  \   `---'   \   /  /
    |           |./  /
    /           //  /
\_/' \         |/  /
 |    |   _,^-'/  /
 |    , ``  (\/  /_
  \,.->._    \X-=/^
  (  /   `-._//^`
   `Y-.____(__}
    |     {__)
          ()
''')


print("It's the 16th century, the world seems to be in a turmoil... ever since the formation of the mysterious crevices, humanity ceases to exist. As the last remaining 'Knight Of Oblivion' will you be the glimmer of hope and shine bright or get consumed by the void of this dark world?.........")

print('''
    〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓
    /                                                                       /
   /               "YOUR CHOICES AFFECT THE PATH OF THE GAME"              /                                   
  /                                                                       /  
 〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓
''')

input("Press Enter to continue...")

########################################################################################################################################

#SCENE - 1

print(''' D-Day, date of departure....
                            +&-
                          _.-^-._    .--.
                       .-'   _   '-. |__|
                      /     |_|     \|  |      
                     /               \  |
                    /|     _____     |\ |
                     |    |==|==|    |  |
 |---|---|---|---|---|    |--|--|    |  |
 |---|---|---|---|---|    |==|==|    |  |
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
''')

print('''
Richard :- and so, the day has arrived young one...
'''
)

def S1a():
    c1 = str(input('''(a) Yes, it seems so teacher... thankyou for everything until now
(b) *remain silent* 
'''))

    if c1 == "a":
        print("Richard:- now now, i dont remember my disciple being so formal, i guess our company ends here kid... stay alive out there for me, here take this. Go, make a new identity that the world shall remember.... *Obtained 1x gold charm*")
    elif c1 == "b":
        print("Richard:-nervous kid? did not expect that from you, but oh well, its only natural, i guess this is where we depart... stay safe out there. i wont disturb you...")
    else:
        print("*PLEASE USE ONE OF THE APPROPRIATE OPTIONS*")
        S1a()

c1 = str(input('''(a) Yes, it seems so teacher... thankyou for everything until now
(b) *remain silent* 
'''))

if c1 == "a":
    print("Richard:- now now, i dont remember my disciple being so formal, i guess our company ends here kid... stay alive out there for me, here take this. Go, make a new identity that the world shall remember.... *Obtained 1x gold charm*")

elif c1 == "b":
    print("Richard:-nervous kid? did not expect that from you, but oh well, its only natural, i guess this is where we depart... stay safe out there. i wont disturb you...")

else:
    print("*PLEASE USE ONE OF THE APPROPRIATE OPTIONS*")
    S1a()
        
print('''Obtained 1x knight armour set, 1x erithrium sword
and with that ... you say your farewells to your only caretaker and mentor since birth, your inner self does not want to go, but warriors like you have no choice but to steel their emotions... for your objective may take everything away from you''')

input("press enter to continue")

########################################################################################################################################

#SCENE - 2

print("You depart on your journey by road and stop to eat in between, killing small monsters here and there that serve no match for you. On the road, you meet a young advanturer of your age and ask for directions, turns out, the adventurer also wanted to go to same area, he offered to travel alongside you for the journey, you accept it and decide not to question his motives")

print('''                                             
                                                  ░░░░░░░░░░░░            
          ▓▓▒▒▒▒▒▒▒▒▒▒                    ░░    ░░░░░░░░░░░░░░░░          
          ░░▓▓▓▓▓▓▓▓▓▓                    ░░    ░░░░░░░░░░░░░░░░          
          ░░██░░░░██░░                    ░░    ░░░░██░░░░██░░░░          
          ░░░░░░░░░░░░                    ░░    ░░░░░░░░░░░░░░░░          
            ░░░░░░░░                      ░░        ░░░░░░░░              
        ░░░░░░░░░░░░░░▒▒                  ░░    ░░░░░░░░░░░░░░░░          
      ▒▒░░░░░░░░░░▒▒░░░░░░                ░░  ▓▓▓▓░░░░░░░░░░░░▓▓▓▓▒▒▒▒▒▒  
    ░░░░  ░░▒▒░░░░░░░░  ▒▒░░            ▓▓▓▓▓▓▓▓  ░░░░░░░░░░░░  ▒▒▓▓▓▓▓▓▒▒
  ░░▒▒    ░░░░░░░░░░░░    ░░░░            ░░▓▓    ░░░░░░░░░░░░  ░░▓▓░░▒▒░░
  ░░      ░░░░▒▒░░░░░░      ░░            ░░      ▓▓▓▓▓▓▓▓▓▓▓▓  ▒▒▓▓▓▓▒▒░░
          ░░░░░░░░▒▒░░                    ▓▓      ▓▓▓▓▓▓▓▓▓▓▓▓    ░░░░▒▒  
          ░░▒▒    ░░░░                            ▓▓▓▓    ▓▓▓▓            
          ░░░░    ░░░░                            ▓▓▒▒    ▓▓▓▓            
          ▒▒░░    ░░░░                            ░░░░    ░░░░            
          ░░░░    ▒▒░░                            ░░░░    ░░░░            
          ░░░░    ░░░░                            ░░░░    ░░░░        
''')

input("press enter to continue...")

print("After hours on foot, both of you are finally able to board a horse carriage, you start checking your equipment, this seems like a good time to talk to your new subordinate.")


def S2a():
    c2 = str(input('''choose your path:-
                   (a) *start the conversation yourself*
                   (b) *Question the adventuer in a stern way(-1 fraternity)
                   (c) *remain silent*(because perhaps you are socially awkward
'''))
    if c2 == "a":
        print(''' You: phew. finally some rest huh.
              Adventurer: mhm. *nods head*
              You: so what is an adventuer doing this route? perhaps a quest contract?
              Adventurer: Ah, its not like that, i have my reasons, lets just say this is something i need to find there, oh, i forgot to introduce myself, i am Holland, 'Sam Holland' a lifelong adventurer, and you would be?''')
    elif c2 == "b":
        print(''' You: about time adventurer...*points sword* WHO ARE YOU? why are you here and what the heck do you want from me?! and you better not be playing games.
    Adventurer: WOAH WOAH!! calm down sir, what is your problem!! i am just an adventurer going same way because i have my reasons! put the sword down. i will go alone if you dont want to be together, this is insane!!
    You: *sheathes sword* i am sorry, i had to keep my guard open
    Adventurer: yeah... figured it out... *sigh* i am Holland, 'Sam Holland', and you would be?''')
    elif c2 == "c":
        print('''*awkward silence ._.*
    Adventurer: Person? of few words huh?)
    You:.......
    Adventurer: Name is Holland, 'Sam Holland' an Adventurer at your care, you would be?
''')
    else:
     print("*PLEASE USE ONE OF THE APPROPRIATE OPTIONS*")
     input("press enter to continue....")
     S2a()

c2 = str(input('''choose your path:-
(a) *start the conversation yourself*
(b) *Question the adventuer in a stern way(-1 fraternity)
(c) *remain silent*(because perhaps you are socially awkward
'''))

if c2 == "a":
        print(''' You: phew. finally some rest huh.
              Adventurer: mhm. *nods head*
              You: so what is an adventuer doing this route? perhaps a quest contract?
              Adventurer: Ah, its not like that, i have my reasons, lets just say this is something i need to find there, oh, i forgot to introduce myself, i am Holland, 'Sam Holland' a lifelong adventurer, and you would be?''')

elif c2 == "b":
        print(''' You: about time adventurer...*points sword* WHO ARE YOU? why are you here and what the heck do you want from me?! and you better not be playing games.
Adventurer: WOAH WOAH!! calm down sir, what is your problem!! i am just an adventurer going same way because i have my reasons! put the sword down. i will go alone if you dont want to be together, this is insane!!
You: *sheathes sword* i am sorry, i had to keep my guard open
Adventurer: yeah... figured it out... *sigh* i am Holland, 'Sam Holland', and you would be?''')

elif c2 == "c":
        print('''*awkward silence ._.*
Adventurer: Person? of few words huh?)
You:.......
Adventurer: Name is Holland, 'Sam Holland' an Adventurer at your care, you would be?
''')

else:
     print("*PLEASE USE ONE OF THE APPROPRIATE OPTIONS*")
     input("press enter to continue....")
     S2a()
     
name = str(input("Enter the name you would like to go by... : -"))

print("\nSam: Nice to meet you", name , "I will be in your care.....")

input("Press enter to continue:-")


print('''▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░    ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒        ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▒▒░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓              ▓▓▓▓▒▒▒▒▓▓▓▓▒▒▒▒              ▒▒▓▓▓▓▒▒▒▒▒▒▓▓▒▒▒▒▓▓▒▒░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒  ▓▓▓▓▓▓▓▓▓▓  ▒▒▒▒▓▓▓▓▒▒▒▒▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓  ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓▒▒░░▒▒▒▒▒▒░░░░▒▒░░░░▒▒▒▒▒▒▒▒▓▓  ▓▓▒▒▓▓▒▒▓▓  ▓▓▓▓▒▒▒▒▓▓▓▓▒▒▒▒  ▓▓▒▒▓▓▒▒▓▓  ▓▓▓▓▓▓▓▓▒▒▓▓▓▓▒▒░░▒▒▒▒▒▒░░░░▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒░░▒▒░░░░░░▒▒▒▒▒▒▓▓▓▓▒▒  ▓▓▒▒▓▓▒▒▓▓  ▓▓▒▒▓▓▓▓▓▓▒▒▓▓▓▓  ▓▓▒▒▓▓▒▒▓▓  ▓▓▓▓▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒░░▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒░░▒▒▓▓░░▒▒▒▒▒▒░░░░░░▒▒▒▒░░▒▒▒▒▓▓▒▒▒▒▓▓  ▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▒▒▒▒▓▓▓▓▒▒▒▒  ▓▓▓▓▓▓▓▓▓▓  ▒▒▓▓▓▓░░▒▒▓▓░░▒▒▒▒▒▒░░░░░░▒▒▒▒░░▒▒▒▒▓▓▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▓▓▒▒▓▓▒▒▓▓▓▓▒▒▒▒██▒▒▒▒░░░░░░▒▒▒▒▓▓▓▓▒▒              ▒▒▓▓▒▒▓▓▒▒▒▒▓▓▓▓              ▓▓▒▒▒▒▓▓▒▒▓▓▒▒▓▓▓▓▒▒▒▒██▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓▓▓▓▒▒██▒▒▒▒▒▒░░▒▒▒▒▓▓▒▒▒▒▓▓▓▓▒▒▓▓▓▓▓▓▒▒▒▒▒▒▓▓▒▒▒▒▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▒▒▒▒▓▓▒▒▒▒▓▓▓▓▒▒██▒▒▒▒▒▒░░▒▒▒▒▓▓▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒░░▓▓▒▒▒▒▒▒░░▓▓▒▒██▒▒▒▒░░▓▓░░▓▓░░▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒▓▓▓▓▒▒▒▒▓▓▓▓▒▒▒▒▓▓▓▓▓▓▒▒▓▓▓▓▒▒▒▒░░▒▒▒▒▒▒▒▒░░▓▓▒▒██▒▒▒▒░░▓▓░░▓▓░░▒▒▒▒▒▒▒▒
▒▒▒▒▓▓▓▓▒▒░░▒▒▓▓▒▒▒▒▓▓██▓▓▒▒░░▓▓▒▒░░░░▓▓                                                    ▓▓▓▓▒▒░░▒▒▓▓▒▒▒▒▓▓██▓▓▒▒░░▓▓▒▒░░░░▓▓▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▓▓██▒▒▒▒░░▓▓▒▒░░▒▒▒▒                      ░░░░░░░░░░░░                  ░░▒▒░░░░░░▒▒▒▒▒▒▓▓██▒▒▒▒░░▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓░░▒▒▓▓▒▒▓▓▒▒▒▒░░                      ▓▓▓▓▓▓▓▓▓▓▓▓                    ░░▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓░░▒▒▓▓▒▒▓▓▒▒▒▒░░▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓▒▒▒▒██░░▒▒▒▒░░▒▒                      ▓▓▓▓▓▓▓▓▓▓▓▓                      ▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓▒▒▒▒██░░▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▒▒██▓▓██░░░░░░▒▒▒▒▒▒    ▓▓▒▒▒▒▓▓▒▒▒▒▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▒▒▓▓▒▒▒▒▓▓    ▒▒▒▒▒▒▓▓▒▒▓▓▒▒██▓▓██▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░░░▒▒░░▒▒▒▒▒▒▒▒    ▓▓▒▒▒▒▓▓▒▒▒▒▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▒▒▓▓▒▒▒▒▓▓    ▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓░░░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░░░▒▒▓▓░░░░▒▒▒▒▒▒▒▒▒▒    ▓▓▒▒▒▒▓▓▒▒▒▒▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▒▒▓▓▒▒▒▒▓▓    ▒▒▒▒▒▒▒▒▓▓░░░░▒▒██░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
  ▒▒  ▒▒  ▒▒  ▓▓▓▓▒▒░░▒▒██░░  ▒▒  ▒▒  ▒▒    ▓▓▒▒▒▒▓▓▒▒▒▒▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▒▒  ▒▒▓▓▓▓▒▒░░▒▒██░░▒▒  ░░  ▒▒  ▒▒  ▒▒  
                      ██▓▓                  ▓▓▒▒▒▒▓▓▒▒▒▒▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓    ░░░░░░░░░░░░░░                  ▓▓▓▓      ░░              
  ▒▒  ▒▒  ▒▒  ▒▒  ▒▒  ██▓▓▒▒  ▒▒  ▒▒  ▒▒    ▓▓▒▒▒▒▓▓▒▒▒▒▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓  ▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒  ▒▒  ▒▒  ▒▒██▓▓  ▒▒  ▒▒  ▒▒  ▒▒  ▒▒  
                      ██▓▓                  ▓▓▒▒▒▒▓▓▒▒▒▒▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓                ██▓▓                      
  ▒▒  ▒▒  ▒▒  ▒▒  ▒▒  ████▒▒  ▒▒  ▒▒  ▒▒    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒  ▒▒  ▒▒  ▒▒████  ▒▒  ░░  ▒▒  ▒▒  ▒▒  
▒▒▓▓▒▒▓▓▒▒▓▓▒▒▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒▓▓▒▒▓▓▒▒▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓
''')

print("after hours of travels full of adversity and accompanying another group from between te journey, you finally arive at a nearby village at night and decide to rest there until next day.... As soon as you were going to sleep, The party invites u to have an all-night camp fire with the bard... Perhaps sleeping would be more beneficial?")

def S2b():
    c3 = str(input('''
(a) Join the party
(b) Sleep
'''))
    if c3 == "a":
        print("After a fun time and a highly deprivative sleep, you get ready to start the day feeling quite dizzy, Turns out sleep was the better option after all... (-20 endurance)")
    elif c3 == "b":
        print("After a good ol' sleep, a refreshed you is ready to start the day, unfortunately, your team feels they are on the verge of collapsing")
    else:
        print("Type a valid option")
        S2b()    
        
c3 = str(input('''
(a) Join the party
(b) Sleep
'''))

if c3 == "a":
    print("After a fun time and a highly deprivative sleep, you get ready to start the day feeling quite dizzy, Turns out sleep was the better option after all... (-20 endurance)")

elif c3 == "b":
    print("After a good ol' sleep, a refreshed you is ready to start the day, unfortunately, your team feels they are on the verge of collapsing")

else:
    print("Type a valid option")
    S2b()

input("press enter to continue")

print('''\nThe spirit of sports is high in the air...
You wake up to see a joyful Sam playing cricket with the village kids, you decide to join in too as both Sam and you exchange a sorrowful glare.... being aware that this is perhaps the last 'normal' thing they are going to experience in ther journey.....''')

input("press enter to start minigame #1...")

########################################################################################################################################    

#Minigame #1

def cont():
    q=input('Do You Want to play again? (yes/no):').lower()
    if q=='yes':
        main()
    elif q=='no':
        print("\nBYE")
        print("▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂")
    else:
        print('''
              ❌ Invalid Input ❌ 
              Please try again''')
        cont()
 
def main():
    print('''\n{NOTE} THERE WILL BE TWO GAMES INVOLVED. If you will press NO
          After the completion of first game then you will be allowed to play
          the second one


    ┃▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔┃
    ┃                              Rules:-                                  ┃
    ┃                                                                       ┃
    ┃ 1.You can only enter '1' and '2' for the toss                         ┃
    ┃ 2. You can enter numbers from 1 to 10 while batting or bowling        ┃
    ┃                                                                       ┃
    ┃       `IF YOU DON'T FOLLOW THESE RULES THE GAME RESTARTS'             ┃
    ┃                                                                       ┃
    ┃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁┃
''')
    def toss():
        x=input('CHOOSE ---> (odd/eve):').lower()
        y=int(input('CHOOSE FOR THE TOSS---> (1/2):'))
        if y>2:
            print('u are only allowed to use 1 and 2.')
            toss()
        z=random.randint(1,2)
        print('sam has played',z,'for the toss')
        if x=='eve':
            if ((y+z)%2)==0:
                print('you have won the toss')
                a=input('what do u want?(bat/bowl)').lower()
                if a=='bat':
                    bat1()
                elif a=='bowl':
                    bat2()
                else:
                    print('invalid input.The game will restart')
                    toss()
            else:
                x=random.choice(['bat','bowl'])
                if x=='bat':
                    print('sam chooses to bat!')
                    bat2()
                elif x=='bowl':
                    print('sam chooses to bowl!')
                    bat1()
        elif x=='odd':
            if ((y+z)%2)==0:
                y=random.choice(['bat','bowl'])
                if y=='bat':
                    print('sam chooses to bat!')
                    bat2()
                elif y=='bowl':
                    print('sam chooses to bowl!')
                    bat1()
                
            else:
                print('You have won the toss')
                a=input('what do u want?(bat/bowl)').lower()
                if a=='bat':
                    bat1()
                elif a=='bowl':
                    bat2()
                else:
                    print('invalid input.The game will restart')
                    toss()
        else:
             print('invalid input.The game will restart')
             toss()
 
    def bat1():  
        print('sam is bowling')
        total = 0
        while (True):
 
            match = random.randint(1, 10)
            Sam = random.randint(1, 10)
            player = int(input("Play your shot: "))
            if player>10:
                print('You Arent allowed to play any number more than 10.The game will restart now')
                toss()
            print("Sam plays: ", Sam)
            total = total + player
 
            if (Sam == player):
                print("Number Matched! ..OUT!!!")
                print("\nYour total runs =", total)
                break
 
        print('sam needs ', total+1, 'Runs to WIN!')
 
        print('It is Sams time to bat.')
        ctotal = 0
        while (True):
 
            cmatch = random.randint(1, 10)
            Sam = random.randint(1, 10)
            player = int(input("Put your ball: "))
            
            if player>10:
                print('You Arent allowed to play any number more than 10.The game will restart now')
                toss()
            print("Sam plays: ", Sam)
            ctotal = ctotal + Sam
            
 
            if (Sam == player):
                print('''
          〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓
            Number Matched! ..OUT!!!
          〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓
                      ''')
                print("Sam's total runs =", ctotal)
                
                if ctotal>total:
                    print(''''
            ︻︻︻︻︻︻︻
              YOU LOSE! 
            ︼︼︼︼︼︼︼
            Sam: Ha! I still got it! damn, i am just too good (^-^)
          You: .....
          Sam: just kidding, it was a nice match, good game.
          but u better give me a treat to be fair ._.
          You: alright...
          *Lost 5 coins*
                          ''')
                elif total>ctotal:
                    print('''
            ︻︻︻︻︻︻︻
              YOU WIN!
            ︼︼︼︼︼︼︼
             Sam: Ah well, looks like this adventurer needs more refining (^-^') 
         Good game''', name, ''' don't you expect me to lose the next time!!
         here.. take this as a token
         *obtained Sharp longsword 1x*
         ▬▬ι═══════ﺤ
         i am sure you can use this better.
                          ''')
                else:
                    print('''
           ︻︻︻︻︻︻︻
               TIE!
           ︼︼︼︼︼︼︼ 
            Sam: That was exhillarating!! , let us make sure to settle this even score next time!
                          ''')
                break
            
    def bat2():
        print('It is Sams time to bat.')
        ctotal = 0
        while (True):
 
            cmatch = random.randint(1, 10)
            Sam = random.randint(1, 10)
            player = int(input("put your ball: "))
            
            if player>10:
                print('You Arent allowed to play any number more than 10.The game will restart now')
                toss()
            print("Sam plays: ", Sam)
            ctotal = ctotal + Sam
            
            if (Sam == player):
                print('''
         〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓
           Number Matched! ..OUT!!!
         〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓
                      ''')
                print("Sam's total runs =", ctotal)
                break
 
        print('sam is bowling')
        total = 0
        while (True):
 
            cmatch = random.randint(1, 10)
            Sam = random.randint(1, 10)
            player = int(input("Play your shot: "))
            
            if player>10:
                print('u arent allowed to play any number more than 10.The game will restart now')
                toss()
            print("Sam plays: ", Sam)
            total = total + player
 
            if (Sam == player):
                print("Number Matched! ..out!!!")
                print("Your total runs =", total)
                if ctotal>total:
                    print('''
          ︻︻︻︻︻︻︻
            YOU LOSE! 
          ︼︼︼︼︼︼︼
          Sam: Ha! I still got it! damn, i am just too good (^-^)
          You: .....
          Sam: just kidding, it was a nice match, good game.
          but u better give me a treat to be fair ._.
          You: alright...
          *Lost 5 coins*
                          ''')
                elif total>ctotal:
                    print('''
         ︻︻︻︻︻︻︻
           YOU WIN!
         ︼︼︼︼︼︼︼
         Sam: Ah well, looks like this adventurer needs more refining (^-^') 
         Good game''', name, ''' don't you expect me to lose the next time!!
         here.. take this as a token
         *obtained Sharp longsword 1x*
         i am sure you can use this better.
                          ''')
                else:
                    print('''
          ︻︻︻︻︻︻
             TIE!
          ︼︼︼︼︼︼ 
          Sam: That was exhillarating!! , let us make sure to settle this even score next time!
                          ''')
                break           
 
    
 
 
 
 
    toss()
    cont()
main()
    
    
input("Press Enter to continue..")

########################################################################################################################################
  
#Scene - 4

print('''********************************************************************************
*                    /   \              /'\       _                              *
*\_..           /'.,/     \_         .,'   \     / \_                            *
*    \         /            \      _/       \_  /    \     _                     *
*     \__,.   /              \    /           \/.,   _|  _/ \                    *
*          \_/                \  /',.,''\      \_ \_/  \/    \                   *
*                           _  \/   /    ',../',.\    _/      \                  *
*             /           _/m\  \  /    |         \  /.,/'\   _\                 *
*           _/           /MMmm\  \_     |          \/      \_/  \                *
*          /      \     |MMMMmm|   \__   \          \_       \   \_              *
*                  \   /MMMMMMm|      \   \           \       \    \             *
*                   \  |MMMMMMmm\      \___            \_      \_   \            *
*                    \|MMMMMMMMmm|____.'  /\_            \       \   \_          *
*                    /'.,___________...,,'   \            \   \        \         *
*                   /       \          |      \    |__     \   \_       \        *
*                 _/        |           \      \_     \     \    \       \_      *
*                /                               \     \     \_   \        \     *
*                      ,      ,                                                  *
        ____/~\    ~O                                                            *
    ,;~( )_  )'' /~()'-{---                                                      * 
       )/  |(     /~)                                                            *
       ~    ~     ~ ~                                                            *
             ~O                                                                  *
            /()-|                                                                *
            /~)                                                                  *
            ~ ~                                 \     \      \   \__      \      *
*                                                  \     \_     \     \      \   *
*                                                   |      \     \     \      \  *
*                                                    \            |            \ *
 *********************************************************************************
 ''')

input()

print(''' You can only come to the morning through shadows...
You try and comprehend these words while a lair hundreds of times the size of you stand before you...
intimidating, yet exciting every single hair in your body.
''')

input()

print('''
The entrance is filled with hordes of goblins and orcs, Sam shares a shivering glare as you bot walk towards the horrid entrance....
  ''')

print("Suddenly, you both notice a seperate path winding around the lair towards the back.")
print('''
You: I do not think we can handle the entrance.
Sam: Please don't tell me you are considering the other path as an option....
You: .....
Sam: Too much for being scared! *you sense the hesitation in his voice*
I ain't an adventurer for nothing. Cmon''', name,'''.... the choice is simple, be brave or spend an eternity on an unknown route
''')

def S4a():
    c4 = str(input('''
(a) Rush the entrance
(b) Go down the unknown path
'''))

    if c4 == "a":
        print('''
    You: *sigh* Yeah... you are right.... I was just too scared, I guess
    Sam: Exactly! I knew you were smart enough.
    *You enter the domain hiding and sneaking reaching the very entrance, "it is time..." you say to yourself as you move forward with a step.
    when suddenly an uncanny sound suddenly starts echoing throughout...
    *An arrow narrowly misses your head by an inch*
    ''')
        input()
        print('''
          Sam: IT'S A TRAP!!! *same shouts as you both scurry your way to the nearest corner, you see a surge of monsters rushing to your side
          You: This is not good!*You evade more arrows*
          Sam: YEAH, GI-.....
          *You stare at your companion... now out of life,an arrow through his chest.*
          At this point.... there remains nothing but you accepting the undoubtful death that awaits you as you get surrounded.
          You: I am sorr-.... te-acher......
           ''')
        print('''
             
    ┃▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔┃
    ┃                                                                       ┃
    ┃               "YOU DIED.... BE CAREFUL WITH YOUR CHOICES."            |                                   
    ┃                                                                       ┃
    ┃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁┃
     ''')
     
    elif c4 == "b":
        print('''
          You: No. I'd rather be safe than sorry, you are not thinking straight sam.
          Sam:.....*sighs* FINE. It is not the time to debate. Just... promise me we will come back if we observe anything strange''', name)
        print('''You: Bet.''')
        print('''
          Both prepare and go for the heavy journey. hours of work turns into days, eventually weeks. weeks, of camping, hunting, gathering, but on the positive side, the loot was not too bad either, but above all, it was safe and played a major role in boosting confidence.
          You can't help but wonder what would have happened if you just rushed the entrance, how would it be??''')
    else:
        print("*PLEASE USE ONE OF THE APPROPRIATE OPTIONS*")
        S4a()

c4 = str(input('''
(a) Rush the entrance
(b) Go down the unknown path
'''))

if c4 == "a":
    print('''
    You: *sigh* Yeah... you are right.... I was just too scared, I guess
    Sam: Exactly! I knew you were smart enough.
    *You enter the domain hiding and sneaking reaching the very entrance, "it is time..." you say to yourself as you move forward with a step.
    when suddenly an uncanny sound suddenly starts echoing throughout...
    *An arrow narrowly misses your head by an inch*
    ''')
    input()
    print('''
          Sam: IT'S A TRAP!!! *same shouts as you both scurry your way to the nearest corner, you see a surge of monsters rushing to your side
          You: This is not good!*You evade more arrows*
          Sam: YEAH, GI-.....
          *You stare at your companion... now out of life,an arrow through his chest.*
          At this point.... there remains nothing but you accepting the undoubtful death that awaits you as you get surrounded.
          You: I am sorr-.... te-acher......
           ''')
    print('''
             
    ┃▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔┃
    ┃                                                                       ┃
    ┃               "YOU DIED.... BE CAREFUL WITH YOUR CHOICES."            |                                   
    ┃                                                                       ┃
    ┃▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁┃
     ''')
     
     
elif c4 == "b":
    print('''
          You: No. I'd rather be safe than sorry, you are not thinking straight sam.
          Sam:.....*sighs* FINE. It is not the time to debate. Just... promise me we will come back if we observe anything strange''', name)
    print('''You: Bet.''')
    print('''
          Both prepare and go for the heavy journey. hours of work turns into days, eventually weeks. weeks, of camping, hunting, gathering, but on the positive side, the loot was not too bad either, but above all, it was safe and played a major role in boosting confidence.
          You can't help but wonder what would have happened if you just rushed the entrance, how would it be??''')

else:
    print("*PLEASE USE ONE OF THE APPROPRIATE OPTIONS*")
    S4a()

input("press enter to continue....")

print('''
Sam: LIGHT! I SEE LIGHT AHEAD! *he exclaimes in happiness)
*Your face brightens up. There is finally some relief.*
Sam: thank you''', name, ''' You were right after all...
You: Save it sam. it will only get harder from here... (knowing well, that THIS is where it truly begins)''')

input("press enter to continue....")

########################################################################################################################################

#Scene-5

print(r"""
██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████████████████████
██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        ▒▒          ▒▒      ▓▓▓▓▓▓▓▓▓▓██████████████████████████████████████
██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓██████████████████████████████████████
██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██      ░░        ▒▒    ▓▓▓▓▓▓▓▓▓▓▓▓██████████████████████████████████████
██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓██████████████████████████████████████
██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████████████████████████████
██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████████████████████████████
██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓██████████████████████████████████████
██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒▓▓▓▓▓▓▓▓██████████████████████████████████████
██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒████████████████████▒▒▓▓▓▓▓▓▓▓██████████████████████████████████████
██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒████████████████████▒▒▓▓▓▓▓▓▓▓██████████████████▓▓▓▓▓▓████▓▓▓▓▓▓████
██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒████████████████████▒▒▓▓▓▓▓▓▓▓██████████████████████████████████████
██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▒▒████████████████████▒▒▓▓▓▓▓▓▓▓██████████████████▓▓██▓▓██▓▓▓▓████████
██████████████▓▓▓▓▓▓██▓▓██▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▒▒████████████████████▒▒▓▓▓▓▓▓▓▓██████████████████████████████████████
██████████████▓▓▓▓▓▓▓▓██▓▓██▓▓▓▓████▓▓▓▓▓▓▓▓▒▒████████████████████▒▒▓▓▓▓▓▓▓▓████████████████▓▓██▓▓██▓▓▓▓▓▓▓▓▓▓████
██████████████▓▓▓▓▓▓██▓▓████▓▓▓▓████▓▓██▓▓▓▓▒▒███████████████ o ██▒▒▓▓▓▓▓▓▓▓██████████████████████▓▓██████████████
██████████████▓▓▓▓▓▓▓▓██▓▓██▓▓▓▓██████▓▓▓▓▓▓▒▒████████████████████▒▒▓▓▓▓▓▓▓▓████████████▓▓▓▓██▓▓▓▓▓▓██████████████
██████████████▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▒▒████████████████████▒▒▓▓▓▓▓▓▓▓██████████████████████████████████████
██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒████████████████████▒▒▓▓▓▓▓▓▓▓██████████████████████████████████████
██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒████████████████████▒▒▓▓▓▓▓▓▓▓██████████████████████████████████████
██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒████████████████████▒▒▓▓▓▓▓▓▓▓██████████████████████████████████████
██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓██████████████████████████████████████
██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓██████████████████████████████████████
██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓██▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓██████████████████████████████████████
████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓██████████████████████████████████████
██████████████▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓████▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒████████████████████████████████████████

""")                    

input()

print('''
      Upon entering onto the strange source of light, you are struck with immense aw.
      Lying before you is an abandoned yet mysterious chamber... you can see the cobwebs and dust lying around. But... Why are the flames still running!
      Sam immediately eyes a silver door in the right of the chamber while u unpack for some rest
     ''')

input()

print('''
*Sam touches the door and in less than a second, a thick sheet of fog covers the room.*
You: What is Happening Sam!! Are you alright?! *you shout as the fog settles down a bit, but with a loud poof, on the place of Sam, there stand two aura eminating beings... a wizard wearing a blue robe and brown sandals and... a wolf?....''' )

input("press enter to continue...")

print(r"""\
                                                      _,-'|
                                                   ,-'._  |
                                         .||,      |####\ |
                                        \.`',/     \####| |
                                        = ,. =      |###| |
                                        / || \    ,-'\#/,'`.
                                          ||     ,'   `,,. `.
                                          ||____,' , ,;' \| |
                                          ||\    _/|/'   _| |
                                          ||/,-''  | >-'' _,\\
                                          ||'      ==\ ,-'  ,'
                                          ||       |  V \ ,|
                          '     '         ||       |    |` |
                          |\---/|    *****************************
                         /  , , |
                    __.-'|  / \ /
           __ ___.-'        ._O|
        .-'  '        :      _/
       / ,    .        .     |
      :  ;    :        :   _/
      |  |   .'     __:   /
      |  :   /'----'| \  |
      \  |\  |      | /| |
       '.'| /       || \ |
       | /|.'       '.l \\_
       || ||                         
       

""")

input()

print('''
Wizard: Hello warrior''', name, '''It seems you are finally here...
You: Wha- HOW do you know my name?? and where is-
Wizard: Patience young one... *chuckles* your friend is safe as of now, trapped but safe, The door had a self trapping mechanism, just.. dont blame me, i tried to come her faster.¯\_(ツ)_/¯
''')

def S5a():
    c5 = str(input('''
(a) "Who are you?"
(b) "YEAH... like i have to listen to what YOU have to say!" *agressive stance*))
(c) *remain silent*
'''))
    if c5 == "a":
        print("oh, how foolish of me to confuse you so", name,"forgive this old man for not greeting you and introducing myself, i was in quite a hurry as you might have figured.")
    elif c5 == "b":
        print("Oh my my! Do not even think of doing what you are thinking little", name, "Not to mention i am invincible while we are here...")
        input()
        print('''
    Wolf: Woof!
    You: .... *sheathes sword*
    Wizard: That's better.''')
    elif c5 == "c":
        print('''
    Wizard: I understand your confusion, little''', name, ''' but you needn't be afraid, I am just an old man who wishes good for humanity, well i guess a proper introduction would help....''')
    else:
        print("*PLEASE USE ONE OF THE APPROPRIATE OPTIONS*")
        S5a()

input()

c5 = str(input('''
(a) "Who are you?"
(b) "YEAH... like i have to listen to what YOU have to say!" *agressive stance*))
(c) *remain silent*
'''))

if c5 == "a":
        print("oh, how foolish of me to confuse you so", name,"forgive this old man for not greeting you and introducing myself, i was in quite a hurry as you might have figured.")

elif c5 == "b":
        print("Oh my my! Do not even think of doing what you are thinking little", name, "Not to mention i am invincible while we are here...")
        input()
        print('''
Wolf: Woof!
You: .... *sheathes sword*
Wizard: That's better.''')

elif c5 == "c":
        print('''
    Wizard: I understand your confusion, little''', name, ''' but you needn't be afraid, I am just an old man who wishes good for humanity, well i guess a proper introduction would help....''')

else:
        print("*PLEASE USE ONE OF THE APPROPRIATE OPTIONS*")        
        S5a()

input("press enter to continue")

print('''
      Wizard: My name is montegno, I am one who forsees everything down from a point, I know everything, yet I know nothing of the world....
      this is my companion, galantro*pointing at the wolf*
      Wolf: Woof!''')

input()

print(''' Wizard: We couldn't help but notice the peple who put their lives on stake to remove the shackles off humanity...
      Wizard;; Well, in simple words, you can say that I am a 'Gatekeeper' of what lies behind.     
      and so you must pass my test to move on, to know that a fate can be entrusted to you, if you win, i will give you something necessary to complete your journey for good, and if you don't, you must be sent back...
      You: So,I... have to fight you?''' )

input()      

print('''Wizard: oh no, not at all, just answer 3 riddles of mine, i am a fan of intellect over strength you see.
      You: Seems easy, will that really answer if i am ready?
      Wizard: Maybe I already know? More than anything this old man wants to have some fun...Ready or not, here they come.''')

########################################################################################################################################################################

#minigame2

input("Press enter to start Minigame #2...")

print(r"""\
                    ____ 
                  .'* *.'
               __/_*_*(_
              / _______ \
             _\_)/___\(_/_ 
            / _((\- -/))_ \
            \ \())(-)(()/ /
             ' \(((()))/ '
            / ' \)).))/ ' \
           / _ \ - | - /_  \
          (   ( .;''';. .'  )
          _\"__ /    )\ __"/_
            \/  \   ' /  \/
             .'  '...' ' )
              / /  |  \ \
             / .   .   . \
            /   .     .   \
           /   /   |   \   \
         .'   /    b    '.  '.
     _.-'    /     Bb     '-. '-._ 
 _.-'       |      BBb       '-.  '-. 
(________mrf\____.dBBBb.________)____)
                      
                
""")
        
guess = 0

while True:
    print("Wizard: Here comes the first one! 'I’m tall when I’m young and I’m short when I’m old. What am I?'")
    print("\n*Type your guess, or type 'help1', help2', or 'I give up' below.*")
    
    answer = input()
    guess += 1

    if "candle" in answer:
        print("\nWizard: That's right!!")
        print("It took you " + str(guess) + " guesses. Not too shabby... But how about this one?")
        break

    elif answer == "help1":
        print("\nI give light")

    elif answer == "help2":
        print("\nI'm made of wax.")

    elif answer.upper() == "I GIVE UP":
        print("\nThe answer was candle!")
        break

    else:
        print("""
        〓〓〓〓〓〓〓〓〓〓
           Try again!
        〓〓〓〓〓〓〓〓〓〓
                  """)
        
        guess = 0

while True:
    print("What is full of holes but still holds water")
    print("\nType your guess, or type 'help1', help2', or 'I give up' below.")
    
    answer = input()
    guess += 1

    if "sponge" in answer: 
        print("\nWizard: That's right!!")
        print("It took you " + str(guess) + " guesses. Not too bad huh...My final one is going to require some thoughts, You better be prepared")
        break

    elif answer == "help1":
        print("\nI have yellow colour")

    elif answer == "help2":
        print("\nI'm found in the kitchen")

    elif answer.upper() == "I GIVE UP":
        print("\nThe answer was sponge!")
        break

    else:
        print("""
        〓〓〓〓〓〓〓〓〓〓
           Try again!
        〓〓〓〓〓〓〓〓〓〓
                  """)
        
        guess = 0

while True:
    print(" What is black when it’s clean and white when it’s dirty?")
    print("\nType your guess, or type 'help1', help2', or 'I give up' below.")
    
    answer = input()
    guess += 1

    if "black board" in answer:
        print("\nWizard: That's right!!")
        print("It took you " + str(guess) + " guesses. That's what i was expecting... Welll done...")
        break

    elif answer == "help1":
        print("\nI am used to study")

    elif answer == "help2":
        print("\nMy best friend is a chalk")

    elif answer.upper() == "I GIVE UP":
        print("\nThe answer was blackboard!")
        break
    
    else:
        print("""
        〓〓〓〓〓〓〓〓〓〓
           Try again!
        〓〓〓〓〓〓〓〓〓〓
                  """)

print('''
Wizard: Good''',name, ''', Good! you really have passed the test.
You: I have?
Wizard: That's correct! I knew You were ready beforehand anyway and was going to let you pass no matter what you did.
You: -_-....
Wizard: What??
You: You... could have just let me pass through.....''')

input()

print('''Wizard: Well, that ruins the fun doesn't it? Oh, I almost forgot take these before you run out annoyed.
*Obtained 1x Elixir of the elite and 1x Diamond key
Wizard: Drink the elixir, as promised,  it will help you out and get stronger
You: what about this key??''')

input()

print('''Wizard: You will know with time.. NOW OFF YOU GO!
You: wait-
*You get kicked out and the wizard and the wolf are nowhere to be seen, You are half glad about it and forget it as soon as you find Sam confused lying on the ground''')

##########################################################################################################################################################################

#Scene 6

input()

print('''
After all this effort, The finale seems awfully close, Sam comes alive, safe but traumatized. And you with your newly found artifact, are ready to go full on for the journey but sam calls you out to say something to you...
Sam: um.. I did not want to disturb yesterday but i am afraid I have to go now ''', name, '''
You: wait... You don't mean-
Sam: Yes i do and you need to understand that i will be nothing but a burden, It was nice meeting you brother, but unfortunately, I still have another mission in hand that i must commit to...''')

input()

print('''You: I... understand, thanyou for everything until now Sam.
Sam: I feel the same.... let us hope that the threads of fate re-unite us once again. Till then, farewell my friend
You: Let us hope indeed, see you later.
*And with that the characters went their own way... what was it that sam had to do? why did he go? Perhaps that is be a tale for another time., Putting the sadness away, you comprehend the responsibility and front of you, and by the end of the day, arrive at a big crevice, possibly the biggest to exist, its evident, that this is the place...

''')

input()

print("""
            ,-.
       ___,---.__          /'|`\          __,---,___
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.
  ,'        |           ~'\     /`~           |        `.
 /      ___//              `. ,'          ,  , \___      \
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |
|   /          /\_  `   .    |    ,      _/\          \   |
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /
 \  \           | `._   `\\  |  //'   _,' |           /  /
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'
     ``       /     \    ,='/ \`=.    /     \       ''
             |__   /|\_,--.,-.--,--._/|\   __|
             /  `./  \\`\ |  |  | /,//' \,'  \
            /   /     ||--+--|--+-/-|     \   \
           |   |     /'\_\_\ | /_/_/`\     |   |
            \   \__, \_     `~'     _/ .__/   /
             `-._,-'   `-._______,-'   `-._,-')
         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓▓▓▓▓▓▓▓▓██████████
         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓████  ████▓▓▓▓▓▓▓▓██    ░░██       
         ▓▓▓▓▓▓▓▓▓▓▓▓████      ████▓▓▓▓▓▓██████████
         ▓▓▓▓▓▓▓▓▓▓████          ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓
         ▓▓▓▓▓▓▓▓████              ████▓▓▓▓▓▓▓▓▓▓▓▓
         ▓▓▓▓▓▓████                  ████▓▓▓▓▓▓▓▓▓▓
         ▓▓▓▓████                      ████▓▓▓▓▓▓▓▓
         ▓▓████                          ████▓▓▓▓▓▓
         ████                              ████▓▓▓▓
         ▓▓████░░                      ░░████▓▓▓▓▓▓
         ▓▓▓▓████░░                  ░░████▓▓▓▓▓▓▓▓
         ▓▓▓▓▓▓████░░              ░░████▓▓▓▓▓▓▓▓▓▓
         ▓▓▓▓▓▓▓▓████░░          ░░████▓▓▓▓▓▓▓▓▓▓▓▓
         ▓▓▓▓▓▓▓▓▓▓████░░      ░░████▓▓▓▓▓▓▓▓▓▓▓▓▓▓
         ▓▓▓▓▓▓▓▓▓▓▓▓████░░  ░░████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓████░░████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


After a minute of rest, you approach the door only to see a strange logo carved on it with a diamond socket below, you suddenly feel thankful to the crazy wizard and put the item in the slot
""")

input()

print('''
The door opened with a huge bang and you are introduced with an eerie hallway full of lanterns and crossways, almost like a maze, with your strengthened body and heightened senses, you walk ahead.... )
????: WHO IS IT WHO DARES TO ENTER MY DOMAIN!!
''')

input()

print("""
      
██████████████████████▒▒░░░░░░░░▒▒████████████████████████████░░░░░░░░░░░░████████████████████████████░░░░░░░░░░▓▓██
████████████████████░░░░░░░░░░░░░░░░██████████████████████▓▓░░░░░░░░░░░░░░░░██████████████████████▓▓░░░░░░░░░░░░░░▒▒
██████████████████░░░░░░░░░░░░░░░░░░░░████████████████████░░░░░░░░░░░░░░░░░░░░████████████████████░░░░░░░░░░░░░░░░░░
▒▒▓▓▓▓▒▒▓▓▓▓▓▓▓▓▒▒░░░░░░░░    ░░░░░░░░▒▒▓▓██▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░    ░░░░░░░░▒▒▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒▒▒░░░░░░░░░░  ░░░░░░
▒▒░░▒▒░░░░░░░░▒▒▒▒░░░░░░░░    ░░░░░░░░▒▒░░░░░░░░▒▒░░▒▒░░▒▒░░░░░░  ░░  ░░░░░░░░▒▒▒▒▒▒░░░░░░░░▒▒░░▒▒░░░░░░  ░░  ░░░░░░
░░  ▒▒▓▓██▓▓▒▒░░░░░░░░░░░░    ░░░░  ░░░░░░▒▒▓▓██▓▓▒▒▒▒▒▒░░░░░░░░░░    ░░░░  ░░░░░░▒▒▓▓██▓▓▒▒░░▒▒░░░░░░░░  ░░  ░░░░░░
░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░  ░░░░░░░░░░  ░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░  ░░  ░░░░░░░░  ░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░  ░░  ░░░░░░░░░░  
░░░░░░▓▓██▓▓▒▒░░░░  ░░            ░░  ░░░░░░▓▓██▓▓▒▒▒▒░░░░  ░░    ░░      ░░  ░░░░▒▒▓▓██▓▓▒▒░░░░░░  ░░    ░░        
░░░░░░▓▓██▓▓▒▒░░░░  ░░            ░░  ░░░░░░▓▓██▓▓▒▒▒▒░░░░░░░░            ░░  ░░░░▒▒▓▓██▓▓▒▒░░░░░░░░░░    ░░      ░░
░░░░░░▓▓██▓▓▒▒░░░░  ░░            ░░  ░░░░░░▓▓██▓▓▒▒▒▒░░░░░░                ░░░░░░▒▒▓▓██▓▓▒▒░░░░░░░░      ░░      ░░
░░░░░░▓▓██▓▓▒▒░░░░  ░░            ░░  ░░░░░░▓▓██▓▓▒▒▒▒░░░░░░                ░░░░░░▒▒▓▓██▓▓▒▒░░░░░░░░      ░░      ░░
░░░░░░▓▓██▓▓▒▒░░░░  ░░  ░░    ░░    ░░░░░░░░▓▓██▓▓▒▒▒▒░░░░░░    ░░    ░░    ░░░░░░▒▒▓▓██▓▓▒▒░░░░░░░░          ░░  ░░
░░░░░░▓▓██▓▓▒▒░░░░      ░░    ░░    ░░░░░░░░▓▓██▓▓▒▒▒▒░░░░░░  ░░░░    ░░    ░░░░░░▒▒▓▓██▓▓▒▒░░░░░░░░  ░░░░░░  ░░  ░░
░░░░▒▒▓▓██▓▓▒▒░░░░▒▒░░    ░░░░      ░░░░░░░░▓▓██▓▓▒▒▒▒░░░░░░  ░░  ░░░░      ░░░░░░▒▒▓▓██▓▓▒▒░░░░░░░░      ░░░░    ░░
░░░░▒▒▓▓██▓▓▒▒░░░░▒▒                ░░░░░░░░▓▓██▓▓▒▒▒▒░░░░░░      ░░        ░░░░░░▒▒▓▓██▓▓▒▒░░░░░░░░      ░░      ░░
░░░░░░▓▓██▓▓▒▒░░░░░░                ░░░░░░░░▓▓██▓▓▒▒▒▒░░░░░░                ░░░░░░▒▒▓▓██▓▓▒▒░░░░░░░░              ░░
░░░░░░▓▓██▓▓▒▒░░░░░░                ░░░░░░░░▓▓██▓▓▒▒▒▒░░░░░░      ░░        ░░░░░░▒▒▓▓██▓▓▒▒░░░░░░░░      ░░      ░░
░░░░░░▓▓██▓▓▒▒░░░░▒▒██▒▒▒▒  ▒▒▒▒██▒▒▒▒░░░░░░▓▓██▓▓▒▒▒▒░░░░▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒██▒▒░░░░▒▒▓▓██▓▓▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒
░░░░░░▓▓██▓▓▒▒░░░░                    ░░░░░░▓▓██▓▓▒▒▒▒░░░░                    ░░░░▒▒▓▓██▓▓▒▒░░░░░░                  
░░░░▒▒▓▓██▓▓▒▒░░░░                    ░░░░░░▓▓██▓▓▒▒▒▒░░░░                    ░░░░▒▒▓▓██▓▓▒▒░░░░░░                  
░░░░▒▒▓▓██▓▓▒▒▒▒░░░░  ░░    ░░    ░░░░░░░░░░▓▓██▓▓▒▒▒▒░░░░░░  ░░          ░░░░░░░░▒▒▓▓██▓▓▒▒▒▒░░▒▒░░░░    ░░    ░░░░
░░░░░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░▒▒▓▓██▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓██▓▓▒▒░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓██▓▓▒▒░░▒▒░░░░░░░░░░░░░░░░░░░░
░░░░░░▒▒░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒░░▒▒░░░░▒▒▒▒▒▒░░▒▒░░░░░░░░░░░░░░░░░░░░▒▒░░▒▒▒▒░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░
░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░▒▒░░░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░
░░▒▒░░░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░
░░▒▒░░░░░░░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░
    

       
""")

input()

print('''
*Heavy screeching intensifying*
????: FUNNY HOW HUMANS WALK INTO THEIR GRAVE
You: Are you just going to hide behind and say things to make you sound cool??
????: I am Xenork, leader of the race, you guys call 'demons'. Why does a bug approach my domain.''')

input()

print('''You: Why you ask... why? You took EVERYTHING out of ordinary human life, due to your actions, Hundreds of Thousands Lost their loved ones... and you ask why?
Xenork: The purpose of my entire existence is to 'purify' lower races
You: ... I have nothing to say to a stash of dirt, it wont be long until this 'lower race' wipes your existence.
''')

input("Press enter to continue...")

print(r'''/
                           __.--|~|--.__                               ,,;/;
                         /~     | |    ;~\                          ,;;;/;;'
                        /|      | |    ;~\\                      ,;;;;/;;;'
                       |/|      \_/   ;;;|\                    ,;;;;/;;;;'
                       |/ \          ;;;/  )                 ,;;;;/;;;;;'
                   ___ | ______     ;_____ |___....__      ,;;;;/;;;;;'
             ___.-~ \\(| \  \.\ \__/ /./ /:|)~   ~   \   ,;;;;/;;;;;'
         /~~~    ~\    |  ~-.     |   .-~: |//  _.-~~--,;;;;/;;;;;'
        (.-~___     \.'|    | /-.__.-\|::::| //~     ,;;;;/;;;;;'
        /      ~~--._ \|   /          `\:: |/      ,;;;;/;;;;;'
     .-|             ~~|   |  /V""""V\ |:  |     ,;;;;/;;;;;' \
    /                   \  |  ~`^~~^'~ |  /    ,;;;;/;;;;;'    ;
   (        \             \|`\._____./'|/    ,;;;;/;;;;;'      '\
  / \        \                             ,;;;;/;;;;;'     /    |
 |            |                          ,;;;;/;;;;;'      |     |
|`-._          |                       ,;;;;/;;;;;'              \
|             /                      ,;;;;/;;;;;'  \              \__________
(             )                 |  ,;;;;/;;;;;'      |        _.--~
 \          \/ \              ,  ;;;;;/;;;;;'       /(     .-~_..--~~~~~~~~~~
 \__         '  `       ,     ,;;;;;/;;;;;'    .   /  \   / /~
 /          \'  |`._______ ,;;;;;;/;;;;;;'    /   :    \/'/'       /|_/|   ``|
| _.-~~~~-._ |   \ __   .,;;;;;;/;;;;;;' ~~~~'   .'    | |       /~ (/\/    ||
/~ _.-~~~-._\    /~/   ;;;;;;;/;;;;;;;'          |    | |       / ~/_-'|-   /|
(/~         \| /' |   ;;;;;;/;;;;;;;;            ;   | |       (.-~;  /-   / |
|            /___ `-,;;;;;/;;;;;;;;'            |   | |      ,/)  /  /-   /  |
 \            \  `-.`---/;;;;;;;;;' |          _'   |T|    /'('  /  /|- _/  //
   \           /~~/ `-. |;;;;;''    ______.--~~ ~\  |u|  ,~)')  /   | \~-==//
     \      /~(   `-\  `-.`-;   /|    ))   __-####\ |a|   (,   /|    |  \
       \  /~.  `-.   `-.( `-.`~~ /##############'~~)| |   '   / |    |   ~\
        \(   \    `-._ /~)_/|  /############'       |X|      /  \     \_\  `\
        ,~`\  `-._  / )#####|/############'   /     |i|  _--~ _/ | .-~~____--'
       ,'\  `-._  ~)~~ `################'           |o| ((~>/~   \ (((' -_
     ,'   `-.___)~~      `#############             |n|           ~-_     ~\_
 _.,'        ,'           `###########              |g|            _-~-__    (
|  `-.     ,'              `#########       \       | |          ((.-~~~-~_--~
`\    `-.;'                  `#####"                | |           "     ((.-~~
  `-._   )               \     |   |        .       |  \                 "
      `~~  _/                  |    \               |   `---------------------
        |/~                `.  |     \        .     |  O    __.---------------
         |                   \ ;      \             |   _.-~
         |                    |        |            |  /  |
          |                   |         |           |/')
        
        ''')

def a11():
    c6 = str(input('''
(a) front stab
(b) slash
'''))
    if c6 == "a":
        print('''
Xenork: Decent damage but can, you take this!''')
    elif c6 =="b":
        print('''
Xenork: Decent damage but can, you take this!''')
    else:
        print("TYPE A VALID INPUT!!")
        a11()
        
c6 = str(input('''
(a) front stab
(b) slash
'''))

if c6 == "a":
    print('''
Xenork: Decent damage but can, you take this!''')

elif c6 =="b":
    print('''
Xenork: Decent damage but can, you take this!''')
else:
    print("Type a vaild input!!")
    a11()
        
input()

def a12():
    c7 = str(input('''
(a) block
(b) evade'''))

    if c7 == "a":
        print("Xenork: saved by an inch but you wont keep it again by that shabby movement")
    elif c7 =="b":
        print("Xenork: saved by an inch but you wont keep it again by that shabby movement")
    else:
        print("TYPE A VALID OPTION!!")
        a12()
        
c7 = str(input('''
(a) block
(b) evade'''))

if c7 == "a":
    print("Xenork: saved by an inch but you wont keep it again by that shabby movement")
elif c7 =="b":
    print("Xenork: saved by an inch but you wont keep it again by that shabby movement")
else:
    print("TYPE A VALID OPTION!!")
    a12()
input()

def a13():
    c8 = str(input('''
(a) fire blast
(b) lightning chain
'''))

    if c8 == "a":
        print("It- burns.... YOU!")
    elif c8 == "b":
        print("It- burns.... YOU!")
    else:
        print("TYPE A VALID OPTION!!")
        a13()
        
c8 = str(input('''
(a) fire blast
(b) lightning chain
'''))

if c8 == "a":
    print("It- burns.... YOU!")
elif c8 == "b":
    print("It- burns.... YOU!")
else:
    print("TYPE A VALID OPTION!!")
    a13()
    
input()

def a14():
    c9 = str(input('''*Heavy Physical sweep approaching:*
(a) evade
(b) Take cover'''))

    if c9 == "a":
        print("CRITICAL DAMAGE SUFFERED!!")
    elif c9 == "b":
        print("Successfully blocked!!")
    else:
        print("TYPE A VALID OPTION!!")
        a14()
        
c9 = str(input('''*Heavy Physical sweep approaching:*
(a) evade
(b) Take cover'''))

if c9 == "a":
    print("CRITICAL DAMAGE SUFFERED!!")
elif c9 == "b":
    print("Successfully blocked!!")
else:
    print("TYPE A VALID OPTIONs!!")
    a14()
        
print("Xenork: This is- not right... my body..")

def a15():
    c10 = str(input('''Choose the final move type!
(a) Magic
(b) Use erithrium sword
'''))

    if c10 == "a":
        print("You burn all your mana and body for the final strike to end it all and summon an array of magic missiles, The last thing Lord Xenork sees are your burning eyes displaying the agony of the entire humanity....")
    elif c10 == "b":
        print("You burn all your mana and body for the final strike to end it all and set ablaze your sword and strike your mightiest slash, The last thing Lord Xenork sees are your burning eyes displaying the agony of the entire humanity....")
    else:
        print("TYPE A VALID OPTION!!")
        a15()
        
c10 = str(input('''Choose the final move type!
(a) Magic
(b) Use erithrium sword
'''))

if c10 == "a":
    print("You burn all your mana and body for the final strike to end it all and summon an array of magic missiles, The last thing Lord Xenork sees are your burning eyes displaying the agony of the entire humanity....")
elif c10 == "b":
     print("You burn all your mana and body for the final strike to end it all and set ablaze your sword and strike your mightiest slash, The last thing Lord Xenork sees are your burning eyes displaying the agony of the entire humanity....")
else:
    print("TYPE A VALID OPTION!!")
    a15()

print('''
Xenork: Y-You humans... YOU KNOW NOTHING! if i dont purify your existence, someone else will, someone greater than me, you people never stand a chance
You: We will see about that Xenork.... your devilish existence ends here...''')

input()

print('''Xenork: heh, such confidence huh... what was your name again mortal?...
You: ''', name, ''' remember it, I stand not for myself but for everyone that came before me.''')

input()

print('''
.......
......
Xenork:I-.....
.....
......
''')

input("press enter to continue....")

print("""
                            +&-
                          _.-^-._    .--.
                       .-'   _   '-. |__|
                      /     |_|     \|  |
                     /               \  |
                    /|     _____     |\ |
                     |    |==|==|    |  |
 |---|---|---|---|---|    |--|--|    |  |
 |---|---|---|---|---|    |==|==|    |  |
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
""")

print('''
Richard: It has been a month since.... Everytime i remember it, i can be nothing but grateful ''', name, ''', it pains me that no one really knows it was you who actually did put end to it all...
You: It is how it should be Teacher... knowing it will only attract attention and problems for everyone. And after all I did not do anything for the fame of it. ('^-^)) ''')

input()
      
print('''Richard: I know you did not but... well, the wish is yours i suppose. What matters is that you and everyone is finally in a better place.
You: It does seem so. But.... I can never drive away the feeling that this is not the end.... [That something much bigger is on the way.... and it might not just be me alone enough to help out humanity.....]
''')

input("PRESS ENTER TO END THE RPG AND OPEN THE CREDITS")
    

########################################################################################################################################

from tkinter import*
root=Tk()
root.geometry("1212x658")
root.title("Final Window")
root.config(background="silver")
root.resizable(0,0)

def Sta():
    Sta=Toplevel(root)
    Sta.title("Student1")
    Sta.resizable(0,0)
    Sta1=Label(Sta,text="Name",font=('Verdana',12),relief="solid",width="20",height="2",bg="darkturquoise")
    Sta1.grid(row=1,column=1)    
    
    Sta2=Label(Sta,text="Shikhar",font=('Verdana',12),relief="solid",width="20",height="2",bg="white")
    Sta2.grid(row=1,column=2)    
    
    Sta3=Label(Sta,text="Surname",font=('Verdana',12),relief="solid",width="20",height="2",bg="white")
    Sta3.grid(row=2,column=1)    
    
    Sta4=Label(Sta,text="Kulshrestha",font=('Verdana',12),relief="solid",width="20",height="2",bg="darkturquoise")
    Sta4.grid(row=2,column=2)    
    
    Sta5=Label(Sta,text="Roll No ",font=('Verdana',12),relief="solid",width="20",height="2",bg="darkturquoise")
    Sta5.grid(row=3,column=1)    
    
    Sta6=Label(Sta,text="40",font=('Verdana',12),relief="solid",width="20",height="2",bg="white")
    Sta6.grid(row=3,column=2)    
    
    Sta7=Label(Sta,text="Class ",font=('Verdana',12),relief="solid",width="20",height="2",bg="white")
    Sta7.grid(row=4,column=1)    
    
    Sta8=Label(Sta,text="XI",font=('Verdana',12),relief="solid",width="20",height="2",bg="darkturquoise")
    Sta8.grid(row=4,column=2)    
    
    Sta9=Label(Sta,text="Section",font=('Verdana',12),relief="solid",width="20",height="2",bg="darkturquoise")
    Sta9.grid(row=5,column=1)    
    
    Sta10=Label(Sta,text="A2",font=('Verdana',12),relief="solid",width="20",height="2",bg="white")
    Sta10.grid(row=5,column=2)    
    
    Sta11=Label(Sta,text="Subject",font=('Verdana',12),relief="solid",width="20",height="2",bg="white")
    Sta11.grid(row=6,column=1)    
    
    Sta12=Label(Sta,text="CS",font=('Verdana',12),relief="solid",width="20",height="2",bg="darkturquoise")
    Sta12.grid(row=6,column=2)    
    
    Sta13=Label(Sta,text="Contributions",font=('Verdana',12),relief="solid",width="20",height="5",bg="darkturquoise")
    Sta13.grid(row=7,column=1)    
    
    Sta14=Label(Sta,text="1) RPG Main Content \n 2) Pictorial Art \n 3) Conceptualisation \n 4) Debugging",font=('Verdana',12),relief="solid",width="20",height="5",bg="white")
    Sta14.grid(row=7,column=2)
        
def Stb():
    Stb=Toplevel(root)
    Stb.title("Student2")
    Stb.resizable(0,0)    
    Stb1=Label(Stb,text="Name",font=('Verdana',12),relief="solid",width="20",height="2",bg="Forestgreen")
    Stb1.grid(row=1,column=1)    
    
    Stb2=Label(Stb,text="Prakhar",font=('Verdana',12),relief="solid",width="20",height="2",bg="white")
    Stb2.grid(row=1,column=2)    
    
    Stb3=Label(Stb,text="Surname",font=('Verdana',12),relief="solid",width="20",height="2",bg="white")
    Stb3.grid(row=2,column=1)    
    
    Stb4=Label(Stb,text="Bhatnagar",font=('Verdana',12),relief="solid",width="20",height="2",bg="Forestgreen")
    Stb4.grid(row=2,column=2)    
    
    Stb5=Label(Stb,text="Roll No.",font=('Verdana',12),relief="solid",width="20",height="2",bg="Forestgreen")
    Stb5.grid(row=3,column=1)    
    
    Stb6=Label(Stb,text="28",font=('Verdana',12),relief="solid",width="20",height="2",bg="white")
    Stb6.grid(row=3,column=2)    
    
    Stb7=Label(Stb,text="Class",font=('Verdana',12),relief="solid",width="20",height="2",bg="white")
    Stb7.grid(row=4,column=1)    
    
    Stb8=Label(Stb,text="XI",font=('Verdana',12),relief="solid",width="20",height="2",bg="Forestgreen")
    Stb8.grid(row=4,column=2)    
    
    Stb9=Label(Stb,text="Section",font=('Verdana',12),relief="solid",width="20",height="2",bg="Forestgreen")
    Stb9.grid(row=5,column=1)    
    
    Stb10=Label(Stb,text="A2",font=('Verdana',12),relief="solid",width="20",height="2",bg="white")
    Stb10.grid(row=5,column=2)    
    
    Stb11=Label(Stb,text="Subject",font=('Verdana',12),relief="solid",width="20",height="2",bg="white")
    Stb11.grid(row=6,column=1)   
    
    Stb12=Label(Stb,text="CS",font=('Verdana',12),relief="solid",width="20",height="2",bg="Forestgreen")
    Stb12.grid(row=6,column=2)    
    
    Stb13=Label(Stb,text="Contributions",font=('Verdana',12),relief="solid",width="20",height="5",bg="Forestgreen")
    Stb13.grid(row=7,column=1)    
    
    Stb14=Label(Stb,text="1) Mini games \n 2) Idealization \n 3)Debuggingn \n 4)Evaluation of RPG ",font=('Verdana',12),relief="solid",width="20",height="5",bg="white")
    Stb14.grid(row=7,column=2)    

def Li():
    Li=Toplevel(root)
    Li.title("Student3")
    Li.resizable(0,0)    
    Li1=Label(Li,text="Name",font=('Verdana',12),relief="solid",width="22",height="2",bg="orangered")
    Li1.grid(row=1,column=1)    
    
    Li2=Label(Li,text="Utkarsh",font=('Verdana',12),relief="solid",width="22",height="2",bg="white")
    Li2.grid(row=1,column=2)    
    
    Li3=Label(Li,text="Surname",font=('Verdana',12),relief="solid",width="22",height="2",bg="white")
    Li3.grid(row=2,column=1)
    
    Li4=Label(Li,text="Sharma",font=('Verdana',12),relief="solid",width="22",height="2",bg="orangered")
    Li4.grid(row=2,column=2)    
    
    Li5=Label(Li,text="Roll No.",font=('Verdana',12),relief="solid",width="22",height="2",bg="orangered")
    Li5.grid(row=3,column=1)    
    
    Li6=Label(Li,text="51",font=('Verdana',12),relief="solid",width="22",height="2",bg="white")
    Li6.grid(row=3,column=2)    
    
    Li7=Label(Li,text="Class",font=('Verdana',12),relief="solid",width="22",height="2",bg="white")
    Li7.grid(row=4,column=1)    
    
    Li8=Label(Li,text="XI",font=('Verdana',12),relief="solid",width="22",height="2",bg="orangered")
    Li8.grid(row=4,column=2)    
    
    Li9=Label(Li,text="Section",font=('Verdana',12),relief="solid",width="22",height="2",bg="orangered")
    Li9.grid(row=5,column=1)    
    
    Li10=Label(Li,text="A2",font=('Verdana',12),relief="solid",width="22",height="2",bg="white")
    Li10.grid(row=5,column=2)    
    
    Li11=Label(Li,text="Subject",font=('Verdana',12),relief="solid",width="22",height="2",bg="white")
    Li11.grid(row=6,column=1)    
    
    Li12=Label(Li,text="CS",font=('Verdana',12),relief="solid",width="22",height="2",bg="orangered")
    Li12.grid(row=6,column=2)    
    
    Li13=Label(Li,text="Contributions",font=('Verdana',12),relief="solid",width="22",height="5",bg="orangered")
    Li13.grid(row=7,column=1)    
    
    Li14=Label(Li,text="1) tkinter interface \n 2) Mini Game Idealization \n 3) Debugging \n 4) Logistics",font=('Verdana',12),relief="solid",width="22",height="5",bg="white")
    Li14.grid(row=7,column=2)    

def IF():
    IF=Toplevel(root)
    IF.title("if statement")
    IF.resizable(0,0)
    
    IF1=Label(IF,text="Introduction\n (if Statement)",font=('Verdana',12),relief="solid",width="20",height="10",bg="plum")
    IF1.grid(row=1,column=1)
    
    IF2=Label(IF,text="It simply states that if something is true, \nPython should perform the steps that \nfollow and do nothing in case the \ncondition evaluates to false.",font=('Verdana',12),relief="solid",width="40",height="10",bg="white")
    IF2.grid(row=1,column=2) 

def ifelse():
    ifelse=Toplevel(root)
    ifelse.title("if-else statement")
    ifelse.resizable(0,0)
    
    ifelse1=Label(ifelse,text="Introduction\n (if-else Statement)",font=('Verdana',12),relief="solid",width="20",height="10",bg="orchid")
    ifelse1.grid(row=1,column=1)
    
    ifelse2=Label(ifelse,text="An if else Python statement evaluates whether \nan expression is true or false. If a condition is\n true, the “if” statement executes. Otherwise, the \n“else” statement executes. ... Conditional statements allow \nyou to control the flow of your program more \neffectively. ",font=('Verdana',12),relief="solid",width="50",height="10",bg="white")
    ifelse2.grid(row=1,column=2)

def nestifelifelse():
    nestifelifelse=Toplevel(root)
    nestifelifelse.title("Nested if-elif-else statement")
    nestifelifelse.resizable(0,0)
    
    nestifelifelse1=Label(nestifelifelse,text="Introduction\n (Nested if-elif-else statement)",font=('Verdana',12),relief="solid",width="30",height="10",bg="orchid")
    nestifelifelse1.grid(row=1,column=1)
    
    nestifelifelse2=Label(nestifelifelse,text="It allows us to check for multiple expressions. \nIf the condition for if is False , it checks the \ncondition of the next elif block and so on. If \nall the conditions are False , the body of \nelse is executed.",font=('Verdana',12),relief="solid",width="45",height="10",bg="white")
    nestifelifelse2.grid(row=1,column=2)

def whileloop():
    whileloop=Toplevel(root)
    whileloop.title("While Loop")
    whileloop.resizable(0,0)
    
    whileloop1=Label(whileloop,text="Introduction\n (While Loop)",font=('Verdana',12),relief="solid",width="20",height="10",bg="orchid")
    whileloop1.grid(row=1,column=1)
    
    whileloop2=Label(whileloop,text=" A while loop is a control flow statement \nthat allows code to be executed repeatedly based \non a given Boolean condition.",font=('Verdana',12),relief="solid",width="50",height="10",bg="white")
    whileloop2.grid(row=1,column=2)
    
def Welc():
    Welc=Toplevel(root)
    Welc.title("WELCOME!")
    Welc.resizable(0,0)
    Welc=Label(Welc,text="Click! \n On the small buttons on the\n border of the window to view\n all the statements and functions\n we have used in our project.",font=('Verdana',12),relief="solid",width="30",height="10",bg="orangered")
    Welc.grid(row=1,column=1)

def defkey():
    defkey=Toplevel(root)
    defkey.title("def keyword")
    defkey.resizable(0,0)
    
    defkey1=Label(defkey,text="Introduction\n (def Keyword)",font=('Verdana',12),relief="solid",width="20",height="10",bg="orchid")
    defkey1.grid(row=1,column=1)
    
    defkey2=Label(defkey,text="In Python, defining the function works as follows. \ndef is the keyword for defining a function. \nThe function name is followed by parameter(s) in (). \nThe colon : signals the start of the function body, \nwhich is marked by indentation.",font=('Verdana',12),relief="solid",width="50",height="10",bg="white")
    defkey2.grid(row=1,column=2)

def Binop():
    Binop=Toplevel(root)
    Binop.title("While Loop")
    Binop.resizable(0,0)
    
    Binop1=Label(Binop,text="Introduction\n (While Loop)",font=('Verdana',12),relief="solid",width="20",height="10",bg="orchid")
    Binop1.grid(row=1,column=1)
    
    Binop2=Label(Binop,text="An operator can be termed as binary depending \nupon the number of operands it takes. A \nunary operator takes only one operand\n and a binary operator takes two operands.",font=('Verdana',12),relief="solid",width="40",height="10",bg="white")
    Binop2.grid(row=1,column=2)
 
def arithop():
    arithop=Toplevel(root)
    arithop.title("Arithmetic Operators")
    arithop.resizable(0,0)
    
    arithop1=Label(arithop,text="Introduction\n (Arithmetic Operators)",font=('Verdana',12),relief="solid",width="40",height="7",bg="orchid")
    arithop1.grid(row=1,column=1)
    
    arithop2=Label(arithop,text="They are used to perform mathematical \noperations like addition, subtraction, \nmultiplication and division.",font=('Verdana',12),relief="solid",width="40",height="7",bg="white")
    arithop2.grid(row=1,column=2)
    
    arithop3=Label(arithop,text="()",font=('Verdana',12),relief="solid",width="40",height="3",bg="white")
    arithop3.grid(row=2,column=1)
    
    arithop4=Label(arithop,text="Parentheses",font=('Verdana',12),relief="solid",width="40",height="3",bg="orchid")
    arithop4.grid(row=2,column=2)
    
    arithop5=Label(arithop,text="**",font=('Verdana',12),relief="solid",width="40",height="3",bg="orchid")
    arithop5.grid(row=3,column=1)
    
    arithop6=Label(arithop,text="Exponentiation",font=('Verdana',12),relief="solid",width="40",height="3",bg="white")
    arithop6.grid(row=3,column=2)
    
    arithop7=Label(arithop,text="-",font=('Verdana',12),relief="solid",width="40",height="3",bg="white")
    arithop7.grid(row=4,column=1)
    
    arithop8=Label(arithop,text="Negation",font=('Verdana',12),relief="solid",width="40",height="3",bg="orchid")
    arithop8.grid(row=4,column=2)
    
    arithop9=Label(arithop,text="/",font=('Verdana',12),relief="solid",width="40",height="3",bg="orchid")
    arithop9.grid(row=5,column=1)
    
    arithop10=Label(arithop,text="Division",font=('Verdana',12),relief="solid",width="40",height="3",bg="white")
    arithop10.grid(row=5,column=2)
    
    arithop11=Label(arithop,text="//",font=('Verdana',12),relief="solid",width="40",height="3",bg="white")
    arithop11.grid(row=6,column=1)
    
    arithop12=Label(arithop,text="Integer division",font=('Verdana',12),relief="solid",width="40",height="3",bg="orchid")
    arithop12.grid(row=6,column=2)
    
    arithop13=Label(arithop,text="*",font=('Verdana',12),relief="solid",width="40",height="3",bg="orchid")
    arithop13.grid(row=7,column=1)
    
    arithop14=Label(arithop,text="Multiplication",font=('Verdana',12),relief="solid",width="40",height="3",bg="white")
    arithop14.grid(row=7,column=2)
    
    arithop15=Label(arithop,text="%",font=('Verdana',12),relief="solid",width="40",height="3",bg="white")
    arithop15.grid(row=8,column=1)
    
    arithop16=Label(arithop,text="Modulus",font=('Verdana',12),relief="solid",width="40",height="3",bg="orchid")
    arithop16.grid(row=8,column=2)
    
    arithop17=Label(arithop,text="+",font=('Verdana',12),relief="solid",width="40",height="3",bg="orchid")
    arithop17.grid(row=9,column=1)
    
    arithop18=Label(arithop,text="Addition",font=('Verdana',12),relief="solid",width="40",height="3",bg="white")
    arithop18.grid(row=9,column=2)
    
    arithop19=Label(arithop,text="-",font=('Verdana',12),relief="solid",width="40",height="3",bg="white")
    arithop19.grid(row=10,column=1)
    
    arithop20=Label(arithop,text="Subtraction",font=('Verdana',12),relief="solid",width="40",height="3",bg="orchid")
    arithop20.grid(row=10,column=2) 
    
def Sc1():
    Sc1=Toplevel(root)
    Sc1.title("Scene1!")
    Sc1.resizable(0,0)
    Sc1=Label(Sc1,text="Departure of protagnist",font=('Verdana',12),relief="solid",width="30",height="10",bg="orangered")
    Sc1.grid(row=1,column=1)

def Sc2():
    Sc2=Toplevel(root)
    Sc2.title("Scene2!")
    Sc2.resizable(0,0)
    Sc2=Label(Sc2,text="Protagonist meets an adventurer \nand makes a trusty companion",font=('Verdana',12),relief="solid",width="30",height="10",bg="greenyellow")
    Sc2.grid(row=1,column=1)
    
def Sc3():
    Sc3=Toplevel(root)
    Sc3.title("Scene3!")
    Sc3.resizable(0,0)
    Sc3=Label(Sc3,text="They arrive and rest at a \nnearby village and have some \nfun before the setting storm",font=('Verdana',12),relief="solid",width="30",height="10",bg="steelblue")
    Sc3.grid(row=1,column=1)
    
def Sc4():
    Sc4=Toplevel(root)
    Sc4.title("Scene4!")
    Sc4.resizable(0,0)
    Sc4=Label(Sc4,text="They arrive at the lair \nand are met with some \nhuge problems",font=('Verdana',12),relief="solid",width="30",height="10",bg="bisque")
    Sc4.grid(row=1,column=1)
    
def Sc5():
    Sc5=Toplevel(root)
    Sc5.title("Scene5!")
    Sc5.resizable(0,0)
    Sc5=Label(Sc5,text="A strange figure offers help \nas the end comes near",font=('Verdana',12),relief="solid",width="30",height="10",bg="hotpink")
    Sc5.grid(row=1,column=1)
    
def Sc6():
    Sc6=Toplevel(root)
    Sc6.title("Scene6!")
    Sc6.resizable(0,0)
    Sc6=Label(Sc6,text="The final scene.  Upon entering \nthe crevice, the protagonist \nmeets the root of it all",font=('Verdana',12),relief="solid",width="30",height="10",bg="limegreen")
    Sc6.grid(row=1,column=1)
    
def Relaop():
    Relaop=Toplevel(root)
    Relaop.title("Relational Operators")
    Relaop.resizable(0,0)
    
    Relaop1=Label(Relaop,text="Introduction\n (Relational Operators)",font=('Verdana',12),relief="solid",width="40",height="7",bg="lime")
    Relaop1.grid(row=1,column=1)    

    Relaop2=Label(Relaop,text="They are used for comparing two expressions \nand result in either Teur or False.",font=('Verdana',12),relief="solid",width="40",height="7",bg="white")
    Relaop2.grid(row=1,column=2)
    
    Relaop3=Label(Relaop,text="<",font=('Verdana',12),relief="solid",width="40",height="3",bg="white")
    Relaop3.grid(row=2,column=1)
    
    Relaop4=Label(Relaop,text="Less than",font=('Verdana',12),relief="solid",width="40",height="3",bg="lime")
    Relaop4.grid(row=2,column=2)
    
    Relaop5=Label(Relaop,text=">",font=('Verdana',12),relief="solid",width="40",height="3",bg="lime")
    Relaop5.grid(row=3,column=1)
    
    Relaop6=Label(Relaop,text="Greater than",font=('Verdana',12),relief="solid",width="40",height="3",bg="white")
    Relaop6.grid(row=3,column=2)
    
    Relaop7=Label(Relaop,text="<=",font=('Verdana',12),relief="solid",width="40",height="3",bg="white")
    Relaop7.grid(row=4,column=1)
    
    Relaop8=Label(Relaop,text="less than equal to",font=('Verdana',12),relief="solid",width="40",height="3",bg="lime")
    Relaop8.grid(row=4,column=2)
    
    Relaop9=Label(Relaop,text=">=",font=('Verdana',12),relief="solid",width="40",height="3",bg="lime")
    Relaop9.grid(row=5,column=1)
    
    Relaop10=Label(Relaop,text="greater than equal to",font=('Verdana',12),relief="solid",width="40",height="3",bg="white")
    Relaop10.grid(row=5,column=2)
    
    Relaop11=Label(Relaop,text="!=,<>",font=('Verdana',12),relief="solid",width="40",height="3",bg="white")
    Relaop11.grid(row=6,column=1)
    
    Relaop12=Label(Relaop,text="not equal to",font=('Verdana',12),relief="solid",width="40",height="3",bg="lime")
    Relaop12.grid(row=6,column=2)
    
    Relaop13=Label(Relaop,text="==",font=('Verdana',12),relief="solid",width="40",height="3",bg="lime")
    Relaop13.grid(row=7,column=1)
    
    Relaop14=Label(Relaop,text="equal to",font=('Verdana',12),relief="solid",width="40",height="3",bg="white")
    Relaop14.grid(row=7,column=2)
    
def dummy():
    dummy=Toplevel(root)
    dummy.title("WELCOME!")
    dummy.resizable(0,0)
    
def Legend():
    Legend=Toplevel(root)
    Legend.title("THANK YOU")
    Legend.resizable(0,0)
    Legend1=Label(Legend,text="Biblography", font=('Verdana', 12), relief="solid", width="30", height="2", bg="maroon1")
    Legend1.grid(row=1,column=1)
   
    Legend3=Label(Legend,text="1)https://stackoverflow.com/", font=('Verdana', 12), relief="solid", width="30", height="2", bg="white")
    Legend3.grid(row=2,column=1)
        
    Legend5=Label(Legend,text="2) https://www.programiz.com/", font=('Verdana', 12), relief="solid", width="30", height="2", bg="white")
    Legend5.grid(row=3,column=1)
    
    Legend7=Label(Legend,text="3) https://github.com/", font=('Verdana', 12), relief="solid", width="30", height="2", bg="white")
    Legend7.grid(row=4,column=1)
    
    Legend9=Label(Legend,text="4) https://www.geeksforgeeks.org/", font=('Verdana', 12), relief="solid", width="30", height="2", bg="white")
    Legend9.grid(row=5,column=1)
        
    Legend11=Label(Legend,text="5) https://wwww.dummies.com/", font=('Verdana', 12), relief="solid", width="30", height="2", bg="white")
    Legend11.grid(row=6,column=1)
    
    Legend13=Label(Legend,text="6) https://www.w3schools.com/", font=('Verdana', 12), relief="solid", width="30", height="2", bg="white")
    Legend13.grid(row=7,column=1)
    
    Legend14=Label(Legend,text="7) https://www.javatpoint.com/", font=('Verdana', 12), relief="solid", width="30", height="2", bg="white")
    Legend14.grid(row=8,column=1)
    
    Legend14=Label(Legend,text="8) Preeti Arora Book", font=('Verdana', 12), relief="solid", width="30", height="2", bg="white")
    Legend14.grid(row=9,column=1)
    
def Tq():
    Tq=Toplevel(root)
    Tq.title("Thank You!")
    Tq.resizable(0,0)
    Tq1=Label(Tq,text="Thank You!\n For Seeing our project\n We Hope you like it. ", font=('Showcard Gothic', 36), relief="solid", width="35", height="10", bg="mediumseagreen")
    Tq1.grid(row=1,column=1)

def Spt():
    Spt=Toplevel(root)
    Spt.title("Thank You!")
    Spt.resizable(0,0)
    Spt1=Label(Spt,text="Thank You Ma'am for \nall the hardwork You did! \nAnd Big Thanks to Parikshit Saini. ", font=('Showcard Gothic', 20), relief="solid", width="30", height="10", bg="mediumseagreen")
    Spt1.grid(row=1,column=1)

def prjsum():
    prjsum=Toplevel(root)
    prjsum.title("Project Summary")
    prjsum.resizable(0,0)
    
    prjsum1=Label(prjsum,text="Introduction", font=('Verdana', 16), relief="solid", width="30", height="8", bg="coral")
    prjsum1.grid(row=1,column=1)
    
    prjsum2=Label(prjsum,text="Our Project is based on a RPG Game or \nA role-playing game which is a genre \nof video game where the gamer controls a \nfictional character (or characters) that \nundertakes a quest in an imaginary world", font=('Verdana', 16), relief="solid", width="50", height="8", bg="ivory")
    prjsum2.grid(row=1,column=2)
    
    prjsum3=Label(prjsum,text="Plot", font=('Verdana', 16), relief="solid", width="30", height="8", bg="ivory")
    prjsum3.grid(row=2,column=1)
    
    prjsum4=Label(prjsum,text="It's the 16th century, the world seems to\n be in a turmoil... ever since the formation \nof the mysterious crevices, humanity ceases to exist. As \nthe last remaining 'Knight Of Oblivion' will you be \nthe glimmer of hope and shine bright or get consumed\n by the void of this dark world?", font=('Verdana', 16), relief="solid", width="50", height="8", bg="coral")
    prjsum4.grid(row=2,column=2)
    
    prjsum5=Label(prjsum,text="No. of Scenes", font=('Verdana', 16), relief="solid", width="30", height="3", bg="coral")
    prjsum5.grid(row=3,column=1)
    
    prjsum6=Label(prjsum,text="6", font=('Verdana', 16), relief="solid", width="50", height="3", bg="ivory")
    prjsum6.grid(row=3,column=2)
    
    prjsum7=Label(prjsum,text="Extra addition", font=('Verdana', 16), relief="solid", width="30", height="5", bg="ivory")
    prjsum7.grid(row=4,column=1)
    
    prjsum8=Label(prjsum,text="There are a total of 3 Minigames:\n 1)Virtual Cricket \n2)Riddle Game \n 3) Whack a Mole ", font=('Verdana', 16), relief="solid", width="50", height="5", bg="coral")
    prjsum8.grid(row=4,column=2)

def mg1():
    mg1=Toplevel(root)
    mg1.title("Minigame1 (Virtual Cricket!")
    mg1.resizable(0,0)
    mg1=Label(mg1,text="VIRTUAL CRICKET\n In This Minigame a player can play \nvirtual cricket against a computer It \nhas all the aspects of cricket such as \nbatting, bowling, toss.",font=('Verdana',12),relief="solid",width="40",height="10",bg="silver")
    mg1.grid(row=1,column=1)

def mg2():
    mg2=Toplevel(root)
    mg2.title("Minigame2 (Riddle)!")
    mg2.resizable(0,0)
    mg2=Label(mg2,text="RIDDLE GAME\n In this minigame the player has to \nface 3 riddles to proceed to the next level.\n The player can also geta maximum of \n2 hints per question ",font=('Verdana',12),relief="solid",width="40",height="10",bg="lawngreen")
    mg2.grid(row=1,column=1)   

def logop():
    logop=Toplevel(root)
    logop.title("Logical Operators")
    logop.resizable(0,0)
    
    logop1=Label(logop,text="Introduction \n(Logical Operators)", font=('Verdana', 12), relief="solid", width="30", height="10", bg="coral")
    logop1.grid(row=1,column=1)
    
    logop2=Label(logop,text="The logical operator evaluates to either \nTrue or False based on the logical operands on \neither side. Every value is logically \neither True or False", font=('Verdana', 12), relief="solid", width="50", height="10", bg="floral white")
    logop2.grid(row=1,column=2)

def inpf():
    inpf=Toplevel(root)
    inpf.title("input() Function")
    inpf.resizable(0,0)
    
    inpf1=Label(inpf,text="Introduction \n(input() Function)", font=('Verdana', 12), relief="solid", width="40", height="8", bg="coral")
    inpf1.grid(row=1,column=1)
    
    inpf2=Label(inpf,text="This function is used to get data from the user \nwhile working with the script mode. It enables \nus to accept n input in the form of string \nfrom the user.", font=('Verdana', 12), relief="solid", width="40", height="8", bg="floral white")
    inpf2.grid(row=1,column=2)

def strA():
    strA=Toplevel(root)
    strA.title("String")
    strA.resizable(0,0)
    
    strA1=Label(strA,text="Introduction \n(Strings)", font=('Verdana', 12), relief="solid", width="40", height="8", bg="coral")
    strA1.grid(row=1,column=1)
    
    strA2=Label(strA,text="Strings are arrays of bytes representing \nUnicode characters. However, Python does not have \na character data type, a single character is \nsimply a string with a length of 1. Square brackets \ncan be used to access elements of the string.", font=('Verdana', 12), relief="solid", width="50", height="8", bg="floral white")
    strA2.grid(row=1,column=2)
    
def BIF():
    BIF=Toplevel(root)
    BIF.title("Built-in Function")
    BIF.resizable(0,0)
    
    BIF1=Label(BIF,text="Introduction \n(Built-in Function)", font=('Verdana', 12), relief="solid", width="40", height="8", bg="coral")
    BIF1.grid(row=1,column=1)
    
    BIF2=Label(BIF,text="The Python built-in functions are defined \nas the functions whose functionality is pre-defined\n in Python. The python interpreter has several functions \nthat are always present for use. These functions\n are known as Built-in Functions.)", font=('Verdana', 12), relief="solid", width="50", height="8", bg="floral white")
    BIF2.grid(row=1,column=2)

def EstrA():
    EstrA=Toplevel(root)
    EstrA.title("Empty String")
    EstrA.resizable(0,0)
    
    EstrA1=Label(EstrA,text="Introduction \n(Empty String)", font=('Verdana', 12), relief="solid", width="40", height="8", bg="coral")
    EstrA1.grid(row=1,column=1)
    
    EstrA2=Label(EstrA,text="An empty string is a string without \nany characters inside, \nhaving length zero.", font=('Verdana', 12), relief="solid", width="40", height="8", bg="floral white")
    EstrA2.grid(row=1,column=2)
    
def MstrA():
    MstrA=Toplevel(root)
    MstrA.title("Empty String")
    MstrA.resizable(0,0)
    
    MstrA1=Label(MstrA,text="Introduction \n(Multiline String)", font=('Verdana', 12), relief="solid", width="40", height="8", bg="coral")
    MstrA1.grid(row=1,column=1)
    
    MstrA2=Label(MstrA,text="Multiline Strings are represented \nusing triple single(''' ''') \nnor triple double quotes", font=('Verdana', 12), relief="solid", width="40", height="8", bg="floral white")
    MstrA2.grid(row=1,column=2)

def SpecNot():
    SpecNot=Toplevel(root)
    SpecNot.title("Special Note")
    SpecNot.resizable(0,0)
    
    SpecNot1=Label(SpecNot,text="Here in this Window: ", font=('Verdana', 16), relief="solid", width="60", height="4", bg="darkgreen")
    SpecNot1.grid(row=1,column=1)
    
    SpecNot2=Label(SpecNot,text="1) The small buttons on the borders of this window, on clicking \nshows the statements and functions. ", font=('Verdana', 16), relief="solid", width="60", height="6", bg="aquamarine")
    SpecNot2.grid(row=2,column=1)
    
    SpecNot3=Label(SpecNot,text="2) The small buttons below the Thank You bar, \non clicking shows some motivational quotes. )", font=('Verdana', 16), relief="solid", width="60", height="6", bg="aquamarine")
    SpecNot3.grid(row=3,column=1)
    
def impmod():
    impmod=Toplevel(root)
    impmod.title("Import Module")
    impmod.resizable(0,0)
    impmod1=Label(impmod,text="Introduction\n (Import module) ", font=('Verdana', 12), relief="solid", width="30", height="10", bg="aquamarine")
    impmod1.grid(row=1,column=1)
    impmod2=Label(impmod,text="Import in python is similar to #include header_file \nin C/C++. Python modules can get access to code \nfrom another module by importing the file/function using \nimport. The import statement is the most common way \nof involving the import machinery, but it is \nnot the only way. ", font=('Verdana', 12), relief="solid", width="60", height="10", bg="floral white")
    impmod2.grid(row=1,column=2)
    
def qa():
    qa=Toplevel(root)
    qa.title("Quote1")
    qa.resizable(0,0)
    qa1=Label(qa,text="Inspiration does exist, but it must find you working.", font=('Verdana', 12), relief="solid", width="50", height="8", bg="lime")
    qa1.grid(row=1,column=1)
    
def qb():
    qb=Toplevel(root)
    qb.title("Quote2")
    qb.resizable(0,0)
    qb1=Label(qb,text="If there is no struggle, there is no progress.", font=('Verdana', 12), relief="solid", width="50", height="8", bg="lightpink")
    qb1.grid(row=1,column=1)
    
def qc():
    qc=Toplevel(root)
    qc.title("Quote3")
    qc.resizable(0,0)
    qc1=Label(qc,text="Courage is like a muscle. We strengthen it by use.", font=('Verdana', 12), relief="solid", width="50", height="8", bg="lime")
    qc1.grid(row=1,column=1)
    
def qd():
    qd=Toplevel(root)
    qd.title("Quote4")
    qd.resizable(0,0)
    qd1=Label(qd,text="Develop success from failures. \nDiscouragement and failure are two of the surest \nstepping stones to success", font=('Verdana', 12), relief="solid", width="50", height="8", bg="lightpink")
    qd1.grid(row=1,column=1)
    
def qe():
    qe=Toplevel(root)
    qe.title("Quote5")
    qe.resizable(0,0)
    qe1=Label(qe,text="Worry is a misuse of imagination.", font=('Verdana', 12), relief="solid", width="50", height="8", bg="lime")
    qe1.grid(row=1,column=1)

def qf():
    qf=Toplevel(root)
    qf.title("Quote6")
    qf.resizable(0,0)
    qf1=Label(qf,text="You can never leave footprints that \nlast if you are always walking on tiptoe", font=('Verdana', 12), relief="solid", width="50", height="8", bg="lightpink")
    qf1.grid(row=1,column=1)
    
def qg():
    qg=Toplevel(root)
    qg.title("Quote7")
    qg.resizable(0,0)
    qg1=Label(qg,text="If you don’t like the road you’re walking, start paving another one.", font=('Verdana', 12), relief="solid", width="50", height="8", bg="lime")
    qg1.grid(row=1,column=1)
    
def qh():
    qh=Toplevel(root)
    qh.title("Quote8")
    qh.resizable(0,0)
    qh1=Label(qh,text="Optimism is the faith that leads to achievement. \nNothing can be done without hope and confidence.", font=('Verdana', 12), relief="solid", width="50", height="8", bg="lightpink")
    qh1.grid(row=1,column=1)
    
def qi():
    qi=Toplevel(root)
    qi.title("Quote9")
    qi.resizable(0,0)
    qi1=Label(qi,text="Life is like riding a bicycle. \nTo keep your balance you must keep moving.", font=('Verdana', 12), relief="solid", width="50", height="8", bg="lime")
    qi1.grid(row=1,column=1)
    
def qj():
    qj=Toplevel(root)
    qj.title("Quote10")
    qj.resizable(0,0)
    qj1=Label(qj,text="The greater the difficulty, \nthe more the glory in surmounting it.", font=('Verdana', 12), relief="solid", width="50", height="8", bg="lightpink")
    qj1.grid(row=1,column=1)

def qk():
    qk=Toplevel(root)
    qk.title("Quote10")
    qk.resizable(0,0)
    qk1=Label(qk,text="It is a rough road that leads\n to the heights of greatness..", font=('Verdana', 12), relief="solid", width="50", height="8", bg="lime")
    qk1.grid(row=1,column=1)

def ql():
    ql=Toplevel(root)
    ql.title("Quote10")
    ql.resizable(0,0)
    ql1=Label(ql,text="Never give up on a dream just because of the \ntime it will take to accomplish it. \nThe time will pass anyway..", font=('Verdana', 12), relief="solid", width="50", height="8", bg="lightpink")
    ql1.grid(row=1,column=1)

def qm():
    qm=Toplevel(root)
    qm.title("Quote10")
    qm.resizable(0,0)
    qm1=Label(qm,text="Set your goals high, and don’t \nstop till you get there..", font=('Verdana', 12), relief="solid", width="50", height="8", bg="lime")
    qm1.grid(row=1,column=1)

def qn():
    qn=Toplevel(root)
    qn.title("Quote10")
    qn.resizable(0,0)
    qn1=Label(qn,text="Creativity is intelligence having fun.", font=('Verdana', 12), relief="solid", width="50", height="8", bg="lightpink")
    qn1.grid(row=1,column=1)

def qo():
    qo=Toplevel(root)
    qo.title("Quote10")
    qo.resizable(0,0)
    qo1=Label(qo,text="Great spirits have always encountered\n violent opposition from mediocre minds..", font=('Verdana', 12), relief="solid", width="50", height="8", bg="lime")
    qo1.grid(row=1,column=1)

def qp():
    qp=Toplevel(root)
    qp.title("Quote10")
    qp.resizable(0,0)
    qp1=Label(qp,text="Anyone who has never made a mistake \nhas never tried anything new.", font=('Verdana', 12), relief="solid", width="50", height="8", bg="lightpink")
    qp1.grid(row=1,column=1)

def qq():
    qq=Toplevel(root)
    qq.title("Quote10")
    qq.resizable(0,0)
    qq1=Label(qq,text="Logic will get you from A to Z; \nimagination will get you everywhere.", font=('Verdana', 12), relief="solid", width="50", height="8", bg="lime")
    qq1.grid(row=1,column=1)

def qr():
    qr=Toplevel(root)
    qr.title("Quote10")
    qr.resizable(0,0)
    qr1=Label(qr,text="Everything must be made as simple \nas possible. But not simpler.", font=('Verdana', 12), relief="solid", width="50", height="8", bg="lightpink")
    qr1.grid(row=1,column=1)

def qs():
    qs=Toplevel(root)
    qs.title("Quote10")
    qs.resizable(0,0)
    qs1=Label(qs,text="Reality is merely an illusion, \nalbeit a very persistent one.", font=('Verdana', 12), relief="solid", width="50", height="8", bg="lime")
    qs1.grid(row=1,column=1)

def qt():
    qt=Toplevel(root)
    qt.title("Quote10")
    qt.resizable(0,0)
    qt1=Label(qt,text="You never fail until you stop trying..", font=('Verdana', 12), relief="solid", width="50", height="8", bg="lightpink")
    qt1.grid(row=1,column=1)

def qu():
    qu=Toplevel(root)
    qu.title("Quote10")
    qu.resizable(0,0)
    qu1=Label(qu,text="Take your victories, whatever they may be, \ncherish them, use them, \nbut don’t settle for them..", font=('Verdana', 12), relief="solid", width="50", height="8", bg="lime")
    qu1.grid(row=1,column=1)  
    
def qv():
    qv=Toplevel(root)
    qv.title("Quote10")
    qv.resizable(0,0)
    qv1=Label(qv,text="You cannot plow a field by turning \nit over in your mind. \nTo begin, begin.", font=('Verdana', 12), relief="solid", width="50", height="8", bg="lightpink")
    qv1.grid(row=1,column=1)
    
def rand():
    rand=Toplevel(root)
    rand.title("random()")
    rand.resizable(0,0)
    
    rand1=Label(rand,text="Introduction",font=('Verdana',12),relief="solid",width="40",height="5",bg="yellowgreen")
    rand1.grid(row=1,column=1)
    
    rand2=Label(rand,text="Returns a random float \nnumber between 0 and 1",font=('Verdana',12),relief="solid",width="40",height="7",bg="floral white")
    rand2.grid(row=2,column=1)
    
def count():
    count=Toplevel(root)
    count.title("count()")
    count.resizable(0,0)
    
    count1=Label(count,text="Introduction",font=('Verdana',12),relief="solid",width="40",height="5",bg="lime")
    count1.grid(row=1,column=1)
    
    count2=Label(count,text="Returns the number of times a \nspecified value occurs in a tuple",font=('Verdana',12),relief="solid",width="40",height="7",bg="floral white")
    count2.grid(row=2,column=1)
    
def choice():
    choice=Toplevel(root)
    choice.title("choice()")
    choice.resizable(0,0)
    
    choice1=Label(choice,text="Introduction",font=('Verdana',12),relief="solid",width="40",height="5",bg="yellowgreen")
    choice1.grid(row=1,column=1)
    
    choice2=Label(choice,text="Returns a random element \nfrom the given sequence",font=('Verdana',12),relief="solid",width="40",height="7",bg="floral white")
    choice2.grid(row=2,column=1)    

def clear():
    clear=Toplevel(root)
    clear.title("clear()")
    clear.resizable(0,0)
    
    clear1=Label(clear,text="Introduction",font=('Verdana',12),relief="solid",width="40",height="5",bg="lime")
    clear1.grid(row=1,column=1)
    
    clear2=Label(clear,text="Removes all the elements \nfrom the dictionary",font=('Verdana',12),relief="solid",width="40",height="7",bg="floral white")
    clear2.grid(row=2,column=1)
    
def copy():
    copy=Toplevel(root)
    copy.title("copy()")
    copy.resizable(0,0)
    
    copy1=Label(copy,text="Introduction",font=('Verdana',12),relief="solid",width="40",height="5",bg="yellowgreen")
    copy1.grid(row=1,column=1)
    
    copy2=Label(copy,text="Returns a copy of the list",font=('Verdana',12),relief="solid",width="40",height="7",bg="floral white")
    copy2.grid(row=2,column=1)
    
def insert():
    insert=Toplevel(root)
    insert.title("insert()")
    insert.resizable(0,0)
    
    insert1=Label(insert,text="Introduction",font=('Verdana',12),relief="solid",width="40",height="5",bg="lime")
    insert1.grid(row=1,column=1)
    
    insert2=Label(insert,text="Adds an element at the specified position",font=('Verdana',12),relief="solid",width="40",height="7",bg="floral white")
    insert2.grid(row=2,column=1)   

def extend():
    extend=Toplevel(root)
    extend.title("extend()")
    extend.resizable(0,0)
    
    extend1=Label(extend,text="Introduction",font=('Verdana',12),relief="solid",width="40",height="5",bg="yellowgreen")
    extend1.grid(row=1,column=1)
    
    extend2=Label(extend,text="Add the elements of a list (or any iterable), \nto the end of the current list",font=('Verdana',12),relief="solid",width="40",height="7",bg="floral white")
    extend2.grid(row=2,column=1)

def reverse():
    reverse=Toplevel(root)
    reverse.title("reverse()")
    reverse.resizable(0,0)
    
    reverse1=Label(reverse,text="Introduction",font=('Verdana',12),relief="solid",width="40",height="5",bg="lime")
    reverse1.grid(row=1,column=1)
    
    reverse2=Label(reverse,text="Reverses the order of the list",font=('Verdana',12),relief="solid",width="40",height="7",bg="floral white")
    reverse2.grid(row=2,column=1)

def remove():
    remove=Toplevel(root)
    remove.title("remove()")
    remove.resizable(0,0)
    
    remove1=Label(remove,text="Introduction",font=('Verdana',12),relief="solid",width="40",height="5",bg="yellowgreen")
    remove1.grid(row=1,column=1)
    
    remove2=Label(remove,text="Removes the first item \nwith the specified value",font=('Verdana',12),relief="solid",width="40",height="7",bg="floral white")
    remove2.grid(row=2,column=1)

def sort():
    sort=Toplevel(root)
    sort.title("sort()")
    sort.resizable(0,0)
    
    sort1=Label(sort,text="Introduction",font=('Verdana',12),relief="solid",width="40",height="5",bg="lime")
    sort1.grid(row=1,column=1)
    
    sort2=Label(sort,text="Sorts the list",font=('Verdana',12),relief="solid",width="40",height="7",bg="floral white")
    sort2.grid(row=2,column=1) 

def append():
    append=Toplevel(root)
    append.title("append()")
    append.resizable(0,0)
    
    append1=Label(append,text="Introduction",font=('Verdana',12),relief="solid",width="40",height="5",bg="yellowgreen")
    append1.grid(row=1,column=1)
    
    append2=Label(append,text="Adds an element at \nthe end of the list",font=('Verdana',12),relief="solid",width="40",height="7",bg="floral white")
    append2.grid(row=2,column=1)

def clear():
    clear=Toplevel(root)
    clear.title("clear()")
    clear.resizable(0,0)
    
    clear1=Label(clear,text="Introduction",font=('Verdana',12),relief="solid",width="40",height="5",bg="lime")
    clear1.grid(row=1,column=1)
    
    clear2=Label(clear,text="Removes all the elements \nfrom the list",font=('Verdana',12),relief="solid",width="40",height="7",bg="floral white")
    clear2.grid(row=2,column=1)

def pop():
    pop=Toplevel(root)
    pop.title("pop()")
    pop.resizable(0,0)
    
    pop1=Label(pop,text="Introduction",font=('Verdana',12),relief="solid",width="40",height="5",bg="yellowgreen")
    pop1.grid(row=1,column=1)
    
    pop2=Label(pop,text="Removes the element at \nthe specified position",font=('Verdana',12),relief="solid",width="40",height="7",bg="floral white")
    pop2.grid(row=2,column=1)

def seek():
    seek=Toplevel(root)
    seek.title("seek()")
    seek.resizable(0,0)
    
    seek1=Label(seek,text="Introduction",font=('Verdana',12),relief="solid",width="40",height="5",bg="lime")
    seek1.grid(row=1,column=1)
    
    seek2=Label(seek,text="Changes the file position",font=('Verdana',12),relief="solid",width="40",height="7",bg="floral white")
    seek2.grid(row=2,column=1)

def find():
    find=Toplevel(root)
    find.title("find()")
    find.resizable(0,0)
    
    find1=Label(find,text="Introduction",font=('Verdana',12),relief="solid",width="40",height="5",bg="yellowgreen")
    find1.grid(row=1,column=1)
    
    find2=Label(find,text="Searches the string for a specified \nvalue and returns the position of \nwhere it was found",font=('Verdana',12),relief="solid",width="40",height="7",bg="floral white")
    find2.grid(row=2,column=1)

def isdisjoint():
    isdisjoint=Toplevel(root)
    isdisjoint.title("isdisjoint()")
    isdisjoint.resizable(0,0)
    
    isdisjoint1=Label(isdisjoint,text="Introduction",font=('Verdana',12),relief="solid",width="40",height="5",bg="lime")
    isdisjoint1.grid(row=1,column=1)
    
    isdisjoint2=Label(isdisjoint,text="Returns whether two sets \nhave a intersection or not",font=('Verdana',12),relief="solid",width="40",height="7",bg="floral white")
    isdisjoint2.grid(row=2,column=1)

def issubset():
    issubset=Toplevel(root)
    issubset.title("issubset()")
    issubset.resizable(0,0)
    
    issubset1=Label(issubset,text="Introduction",font=('Verdana',12),relief="solid",width="40",height="5",bg="yellowgreen")
    issubset1.grid(row=1,column=1)
    
    issubset2=Label(issubset,text="Returns whether another set contains this set or not",font=('Verdana',12),relief="solid",width="40",height="7",bg="floral white")
    issubset2.grid(row=2,column=1)    

def List():
    List=Toplevel(root)
    List.title("List()")
    List.resizable(0,0)
    
    List1=Label(List,text="Introduction",font=('Verdana',12),relief="solid",width="40",height="5",bg="lime")
    List1.grid(row=1,column=1)
    
    List2=Label(List,text="Lists are just like the arrays, \ndeclared in other languages which \nis a ordered collection of data.",font=('Verdana',12),relief="solid",width="40",height="7",bg="floral white")
    List2.grid(row=2,column=1)

def Dictionary():
    Dictionary=Toplevel(root)
    Dictionary.title("Dictionary()")
    Dictionary.resizable(0,0)
    
    Dictionary1=Label(Dictionary,text="Introduction",font=('Verdana',12),relief="solid",width="40",height="5",bg="yellowgreen")
    Dictionary1.grid(row=1,column=1)
    
    Dictionary2=Label(Dictionary,text="Dictionary in Python is an unordered \ncollection of data values, used to\n store data values like a map",font=('Verdana',12),relief="solid",width="40",height="7",bg="floral white")
    Dictionary2.grid(row=2,column=1)
    
def Set():
    Set=Toplevel(root)
    Set.title("Set()")
    Set.resizable(0,0)
    
    Set1=Label(Set,text="Introduction",font=('Verdana',12),relief="solid",width="40",height="5",bg="lime")
    Set1.grid(row=1,column=1)
    
    Set2=Label(Set,text="Set is an unordered collection \nof data type that is iterable, \nmutable and has no duplicate elements.",font=('Verdana',12),relief="solid",width="40",height="7",bg="floral white")
    Set2.grid(row=2,column=1)

def split():
    split=Toplevel(root)
    split.title("split()")
    split.resizable(0,0)
    
    split1=Label(split,text="Introduction",font=('Verdana',12),relief="solid",width="40",height="5",bg="yellowgreen")
    split1.grid(row=1,column=1)
    
    split2=Label(split,text="This method breaks up a string\n at the specified separator and\n returns a list of substrings.",font=('Verdana',12),relief="solid",width="40",height="7",bg="floral white")
    split2.grid(row=2,column=1)    
 
def replace():
    replace=Toplevel(root)
    replace.title("replace()")
    replace.resizable(0,0)
    
    replace1=Label(replace,text="Introduction",font=('Verdana',12),relief="solid",width="40",height="5",bg="lime")
    replace1.grid(row=1,column=1)
    
    replace2=Label(replace,text="This function replaces all\n the occurrences of the old\n string with the new string.",font=('Verdana',12),relief="solid",width="40",height="7",bg="floral white")
    replace2.grid(row=2,column=1)

def title():
    title=Toplevel(root)
    title.title("title()")
    title.resizable(0,0)
    
    title1=Label(title,text="Introduction",font=('Verdana',12),relief="solid",width="40",height="5",bg="yellowgreen")
    title1.grid(row=1,column=1)
    
    title2=Label(title,text="This function returns the \nstring with first letter of every\n word in the string in uppercase\n and rest in lowercase.",font=('Verdana',12),relief="solid",width="40",height="7",bg="floral white")
    title2.grid(row=2,column=1)

def swapcase():
    swapcase=Toplevel(root)
    swapcase.title("swapcase()")
    swapcase.resizable(0,0)
    
    swapcase1=Label(swapcase,text="Introduction",font=('Verdana',12),relief="solid",width="40",height="5",bg="lime")
    swapcase1.grid(row=1,column=1)
    
    swapcase2=Label(swapcase,text="This function converts and \nreturns all uppercase characters into \nlowercase and vice versa of the given string. \nIt does not take any argument.",font=('Verdana',12),relief="solid",width="40",height="7",bg="floral white")
    swapcase2.grid(row=2,column=1)

def partition():
    partition=Toplevel(root)
    partition.title("partition()")
    partition.resizable(0,0)
    
    partition1=Label(partition,text="Introduction",font=('Verdana',12),relief="solid",width="40",height="5",bg="yellowgreen")
    partition1.grid(row=1,column=1)
    
    partition2=Label(partition,text="This function is used to \nsplit the given string using the specified \nseparator and return a \ntuple with three parts.",font=('Verdana',12),relief="solid",width="40",height="7",bg="floral white")
    partition2.grid(row=2,column=1)

def endswith():
    endswith=Toplevel(root)
    endswith.title("endswith()")
    endswith.resizable(0,0)
    
    endswith1=Label(endswith,text="Introduction",font=('Verdana',12),relief="solid",width="40",height="5",bg="lime")
    endswith1.grid(row=1,column=1)
    
    endswith2=Label(endswith,text="This function returns True \nif the given string ends with the \nspecified substring, else \nreturns False.",font=('Verdana',12),relief="solid",width="40",height="7",bg="floral white")
    endswith2.grid(row=2,column=1)    
    
b1=Button(root, text ='', command=Welc, bg="Black", activebackground="black", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b1.grid(row=1,column=1)

b2=Button(root, text ='', command=IF, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b2.grid(row=1,column=2)

b3=Button(root, text ='', command=ifelse, bg="Black", activebackground="black", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b3.grid(row=1,column=3)

b4=Button(root, text ='', command=nestifelifelse, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b4.grid(row=1,column=4)

b5=Button(root, text ='', command=defkey, bg="Black", activebackground="black", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b5.grid(row=1,column=5)

b6=Button(root, text ='', command=whileloop, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b6.grid(row=1,column=6)

b7=Button(root, text ='', command=Binop, bg="Black", activebackground="black", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b7.grid(row=1,column=7)

b8=Button(root, text ='', command=arithop, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b8.grid(row=1,column=8)

b9=Button(root, text ='', command=Relaop, bg="Black", activebackground="black", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b9.grid(row=1,column=9)

b10=Button(root, text ='', command=logop, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b10.grid(row=1,column=10)

b11=Button(root, text ='', command=inpf, bg="Black", activebackground="black", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b11.grid(row=1,column=11)

b12=Button(root, text ='', command=strA, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b12.grid(row=1,column=12)

b13=Button(root, text ='', command=BIF, bg="Black", activebackground="black", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b13.grid(row=1,column=13)

b14=Button(root, text ='', command=EstrA, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b14.grid(row=1,column=14)

b15=Button(root, text ='', command=MstrA, bg="Black", activebackground="black", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b15.grid(row=1,column=15)

b16=Button(root, text ='', command=impmod, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b16.grid(row=1,column=16)

b17=Button(root, text ='', command=rand, bg="Black", activebackground="black", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b17.grid(row=1,column=17)

b18=Button(root, text ='', command=count, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b18.grid(row=1,column=18)

b19=Button(root, text ='', command=choice, bg="Black", activebackground="black", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b19.grid(row=1,column=19)

b20=Button(root, text ='', command=clear, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b20.grid(row=1,column=20)

b21=Button(root, text ='', command=copy, bg="Black", activebackground="black", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b21.grid(row=1,column=21)

b22=Button(root, text ='', command=insert, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b22.grid(row=1,column=22)

b24=Button(root, text ='', command=extend, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b24.grid(row=2,column=1)

b25=Button(root, text ='', command=reverse, bg="black", activebackground="black", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b25.grid(row=3,column=1)

b26=Button(root, text ='', command=remove, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b26.grid(row=4,column=1)

b27=Button(root, text ='', command=sort, bg="black", activebackground="black", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b27.grid(row=5,column=1)

b28=Button(root, text ='', command=append, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b28.grid(row=6,column=1)

b29=Button(root, text ='', command=clear, bg="black", activebackground="black", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b29.grid(row=7,column=1)

b30=Button(root, text ='', command=pop, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b30.grid(row=8,column=1)

b31=Button(root, text ='', command=seek, bg="black", activebackground="black", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b31.grid(row=9,column=1)

b32=Button(root, text ='', command=find, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b32.grid(row=10,column=1)

b33=Button(root, text ='', command=isdisjoint, bg="black", activebackground="spring green", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b33.grid(row=11,column=1)

b34=Button(root, text ='', command=qa, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b34.grid(row=12,column=1)

b35=Button(root, text ='', command=qb, bg="black", activebackground="black", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b35.grid(row=12,column=2)

b36=Button(root, text ='', command=qc, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b36.grid(row=12,column=3)

b37=Button(root, text ='', command=qd, bg="black", activebackground="black", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b37.grid(row=12,column=4)

b38=Button(root, text ='', command=qe, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b38.grid(row=12,column=5)

b39=Button(root, text ='', command=qf, bg="black", activebackground="black", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b39.grid(row=12,column=6)

b40=Button(root, text ='', command=qg, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b40.grid(row=12,column=7)

b41=Button(root, text ='', command=qh, bg="black", activebackground="black", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b41.grid(row=12,column=8)

b42=Button(root, text ='', command=qi, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b42.grid(row=12,column=9)

b43=Button(root, text ='', command=qj, bg="black", activebackground="black", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b43.grid(row=12,column=10)

b44=Button(root, text ='', command=qk, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b44.grid(row=12,column=11)

b45=Button(root, text ='', command=ql, bg="black", activebackground="black", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b45.grid(row=12,column=12)

b46=Button(root, text ='', command=qm, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b46.grid(row=12,column=13)

b47=Button(root, text ='', command=qn, bg="black", activebackground="black", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b47.grid(row=12,column=14)

b48=Button(root, text ='', command=qo, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b48.grid(row=12,column=15)

b49=Button(root, text ='', command=qp, bg="black", activebackground="black", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b49.grid(row=12,column=16)

b50=Button(root, text ='', command=qq, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b50.grid(row=12,column=17)

b51=Button(root, text ='', command=qr, bg="black", activebackground="black", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b51.grid(row=12,column=18)

b52=Button(root, text ='', command=qs, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b52.grid(row=12,column=19)

b53=Button(root, text ='', command=qt, bg="black", activebackground="black", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b53.grid(row=12,column=20)

b54=Button(root, text ='', command=qu, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b54.grid(row=12,column=21)

b55=Button(root, text ='', command=qv, bg="black", activebackground="black", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b55.grid(row=12,column=22)

b56=Button(root, text ='', command=issubset, bg="black", activebackground="black", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b56.grid(row=2,column=22)

b57=Button(root, text ='', command=List, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b57.grid(row=3,column=22)

b58=Button(root, text ='', command=Dictionary, bg="black", activebackground="black", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b58.grid(row=4,column=22)

b59=Button(root, text ='', command=Set, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b59.grid(row=5,column=22)

b60=Button(root, text ='', command=split, bg="black", activebackground="black", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b60.grid(row=6,column=22)

b61=Button(root, text ='', command=replace, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b61.grid(row=7,column=22)

b62=Button(root, text ='', command=swapcase, bg="black", activebackground="black", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b62.grid(row=8,column=22)

b63=Button(root, text ='', command=partition, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b63.grid(row=9,column=22)

b64=Button(root, text ='', command=endswith, bg="black", activebackground="black", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b64.grid(row=10,column=22)

b65=Button(root, text ='', command=dummy, bg="orange", activebackground="orange", bd="5", font=('Verdana', 15), width="3", height="1", fg="black")
b65.grid(row=11,column=22)

ProjSum=Button(root, text = 'Project Summary', command=prjsum, bg="cyan",bd="7", font=('Verdana', 16), width="83", height="1" ,fg="black",activebackground="blue")
ProjSum.grid(row=3,column=1,columnspan=650) 

Biblo=Button(root, text = 'Biblography', command=Legend, bg="cyan",bd="7", font=('Verdana', 16), width="83", height="1" ,fg="black",activebackground="blue")
Biblo.grid(row=9,column=1,columnspan=650) 

A=Button(root, text = 'Students List', command=lambda:[Stb(),Sta(),Li()], bg="crimson",bd="7", font=('Verdana', 16), width="83", height="1" ,fg="black",activebackground="blue")
A.grid(row=2,column=1,columnspan=650) 
   
SpT=Button(root, text = 'Special Thanks', command=Spt, bg="crimson",bd="7", font=('Verdana', 16), width="83", height="1" ,fg="black",activebackground="blue")
SpT.grid(row=10,column=1,columnspan=650)

BfS=Button(root, text = 'Briefing of Scenes', command=lambda:[Sc1(),Sc2(),Sc3(),Sc4(),Sc5(),Sc6()], bg="crimson",bd="7", font=('Verdana', 16), width="83", height="1" ,fg="black",activebackground="blue")
BfS.grid(row=4,column=1,columnspan=650) 

Bfmg=Button(root, text = 'Briefing of Minigames', command=lambda:[mg1(),mg2()], bg="cyan",bd="7", font=('Verdana', 16), width="83", height="1" ,fg="black",activebackground="blue")
Bfmg.grid(row=5,column=1,columnspan=650)    

Thanks=Button(root, text='THANK YOU',command=Tq,bg="midnightblue",bd="7",font=('Verdana',16),width="92",height="2",fg="floral white",activebackground="black")
Thanks.grid(row=11,column=1,columnspan=650)

SpecN=Button(root, text = 'Special Note', command=SpecNot, bg="crimson",bd="7", font=('Verdana', 16), width="83", height="1" ,fg="black",activebackground="blue")
SpecN.grid(row=8,column=1,columnspan=650)


root.mainloop()


      
      
      





