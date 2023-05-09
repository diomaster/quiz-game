print("welcome to this quiz")

player = input("wanna play?")

if player.lower() != "yes":
    quit()


print("Okay! You asked for it!")
scoring = 0

ans = input("what year did the first zelda game come out?")
if ans.lower() == "1986":
    print('Thats right!')
    scoring += 1
else:
    print('no no no study harder next time!')

ans = input("what were the two launch titles for the n64(please put and inbetween your anwsers)")
if ans.lower() == "super mario 64 and pilotwings 64":
    print('oh yeah')
    scoring += 1
else:
    print('that was a hard one I understand that you did not get it')

ans = input("what year did the orginal final fantasy come to america?")
if ans.lower() == "1987":
    print('yes yes yes!')
    scoring += 1
else:
    print('bruh....')

ans = input("who is the main protagonist in the zelda series (if you say zelda imma injure you.)")
if ans.lower() == "Link":
    print('too easy')
    scoring += 1
else:
    print('I failed you!')


print("You scored " + str(scoring) + " questions right! Nice Job!")
print("You got a  " + str((scoring / 4) * 100) + " questions right! Nice Job!")