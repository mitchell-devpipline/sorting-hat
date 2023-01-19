gryfindor = 0
slytherin = 0
hufflepuff = 0
ravenclaw = 0


def tie_breaker(tie):
    gryf = gryfindor
    slyt = slytherin
    huff = hufflepuff
    rave = ravenclaw

    if tie.title() == "Gryfindor":
        gryf += 6
        print("You are a Gryfindor")

    elif tie.title() == "Slytherin":
        slyt += 6
        print("You are a Slytherin")
    elif tie.title() == "Hufflepuff":
        huff += 6
        print("You are in Hufflepuff")
    elif tie.title() == "Ravenclaw":
        rave += 6
        print("You are a Ravenclaw")
    return gryf, slyt, huff, rave


def answer(question):
    gryf = gryfindor
    slyt = slytherin
    huff = hufflepuff
    rave = ravenclaw
    if question.lower() == "a":
        gryf += 1

    elif question.lower() == "b":
        slyt += 1

    elif question.lower() == "c":
        huff += 1

    elif question.lower() == "d":
        rave += 1

    return gryf, slyt, huff, rave


print(gryfindor, slytherin, hufflepuff, ravenclaw)
# question 1
while True:
    question1 = input(
        """\nYou see a hungry and dirty puppy on the road what is your reaction?
    a. I'll avenge this injustice!
    b. Disgusting whelp!
    c. You're safe now, I'll take care of you!
    d. I should take this puppy to the shelter.
    answer: """
    )
    if question1.lower() not in ["a", "b", "c", "d"]:
        print("invalid option")
        continue
    else:
        break


gryfindor, slytherin, hufflepuff, ravenclaw = answer(question1)

# question 2
while True:
    question2 = input(
        """\nwhat sport do you prefer?
    a. rugby
    b. fox hunting
    c. baseball
    d. chess
    answer: """
    )

    if question2.lower() not in ["a", "b", "c", "d"]:
        print("invalid option")
        continue
    else:
        break


gryfindor, slytherin, hufflepuff, ravenclaw = answer(question2)

# question 3
while True:
    question3 = input(
        """\nWhich word describes you best?
    a. Friendly
    b. Hard-working
    c. Obliging
    d. Loyal
    answer: """
    )

    if question3.lower() not in ["a", "b", "c", "d"]:
        print("invalid option")
        continue
    else:
        break


gryfindor, slytherin, hufflepuff, ravenclaw = answer(question3)

# question 4
while True:
    question4 = input(
        """\nWhich one of these would be the best pet ever?
    a. Dog
    b. Cat
    c. Hamster
    d. Bird
    answer: """
    )

    if question4.lower() not in ["a", "b", "c", "d"]:
        print("invalid option")
        continue
    else:
        break

gryfindor, slytherin, hufflepuff, ravenclaw = answer(question4)

# question 5
while True:
    question5 = input(
        """\nWhat would be your favorite hobby?
    a. Slaying dragons
    b. Mortician
    c. Art
    d. researching
    answer: """
    )

    if question5.lower() not in ["a", "b", "c", "d"]:
        print("invalid option")
        continue
    else:
        break
gryfindor, slytherin, hufflepuff, ravenclaw = answer(question5)

if gryfindor > slytherin and gryfindor > ravenclaw and gryfindor > hufflepuff:
    print("you are a gryfindor")
elif slytherin > hufflepuff and slytherin > ravenclaw and slytherin > gryfindor:
    print("you are a slytherin")
elif hufflepuff > ravenclaw and hufflepuff > gryfindor and hufflepuff > slytherin:
    print("you are a hufflepuff")
elif ravenclaw > gryfindor and ravenclaw > slytherin and ravenclaw > hufflepuff:
    print("you are a ravenclaw")
else:
    tie = input("What house do you think you belong in?: ")
    tie_breaker(tie)
