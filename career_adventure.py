# I had my friends play the game, he was the one that suggested I use options a, b, c instead of making the user type a long word.
# He also said I should consider turning it into a web project but I don't really know how to do that yet.
# My friend Fatiah said that she loved how the game had chances and consequence and that it is very relatable to the real world.
# ============================================================
# THE ROAD TO YOUR FIRST TECH JOB
# A text-based adventure game about building a tech career
# ============================================================

print("=" * 55)
print("       💻 THE ROAD TO YOUR FIRST TECH JOB 💻")
print("=" * 55)

print("\nYou are trying to become a software developer.")
print("Every decision you make can affect your career journey.")
print("Choose carefully... and try not to get distracted by BTS! 😄")


# ============================================================
# SCENARIO 1
# ============================================================

choice1 = input(
    "\nSCENARIO 1\n"
    "You have free time after your studies.\n"
    "What do you do?\n"
    "A. STUDY\n"
    "B. BUILD A PROJECT\n"
    "C. REST\n"
    "Choose A, B, or C: "
).lower()


# ============================================================
# STUDY PATH
# ============================================================

if choice1 == "a":

    print("\nYou spend the day improving your programming knowledge.")

    choice2 = input(
        "\nSCENARIO 2\n"
        "You have learned enough for today. What next?\n"
        "A. KEEP STUDYING\n"
        "B. BUILD A PROJECT\n"
        "C. WATCH BTS\n"
        "Choose A, B, or C: "
    ).lower()

    if choice2 == "a":

        print("\nYou understand more concepts, but you still have")
        print("nothing new to show potential employers.")
        print("Your portfolio remains weak.")

        choice3 = input(
            "\nSCENARIO 3\n"
            "A job opportunity appears. What do you do?\n"
            "A. APPLY ANYWAY\n"
            "B. BUILD A PROJECT FIRST\n"
            "Choose A or B: "
        ).lower()

        if choice3 == "a":

            print("\nYou apply with very little project evidence.")
            print("The employer chooses another candidate.")
            print("Your job search continues.")

            choice4 = input(
                "\nSCENARIO 4\n"
                "A developer you met online asks about your skills.\n"
                "A. SHOW YOUR EXISTING WORK\n"
                "B. ASK FOR ADVICE\n"
                "Choose A or B: "
            ).lower()

            if choice4 == "a":

                print("\nYou show what you have, but there is little to demonstrate.")
                print("The developer suggests building more projects.")
                print("You realize your portfolio needs work.")

            elif choice4 == "b":

                print("\nYou ask for advice instead of pretending to know everything.")
                print("The developer gives you useful career advice.")
                print("You decide to improve your portfolio.")

            else:
                print("\nInvalid choice. You missed the opportunity.")

        elif choice3 == "b":

            print("\nYou decide to build something useful before applying.")
            print("Your portfolio becomes stronger.")
            print("You now have something to discuss with employers.")

            choice4 = input(
                "\nSCENARIO 4\n"
                "A developer you met online asks about your project.\n"
                "A. SHOW THE PROJECT\n"
                "B. ASK FOR ADVICE\n"
                "Choose A or B: "
            ).lower()

            if choice4 == "a":

                print("\nYou confidently show your project.")
                print("The developer is impressed by your progress.")
                print("You receive useful feedback.")

            elif choice4 == "b":

                print("\nYou ask the developer for feedback.")
                print("They point out areas you can improve.")
                print("Your project becomes stronger.")

            else:
                print("\nInvalid choice. You miss the chance to connect.")

        else:
            print("\nInvalid choice. Please choose A or B.")


    elif choice2 == "b":

        print("\nYou stop studying and start building.")
        print("Your project is difficult, but you keep working.")
        print("You are creating evidence of your skills.")

        choice3 = input(
            "\nSCENARIO 3\n"
            "You find a difficult bug in your project.\n"
            "A. DEBUG IT\n"
            "B. GIVE UP\n"
            "Choose A or B: "
        ).lower()

        if choice3 == "a":

            print("\nYou spend time debugging the problem.")
            print("Eventually, you find and fix the bug.")
            print("You learn something valuable.")

            choice4 = input(
                "\nSCENARIO 4\n"
                "A developer you met online asks about your project.\n"
                "A. SHOW THE PROJECT\n"
                "B. ASK FOR ADVICE\n"
                "Choose A or B: "
            ).lower()

            if choice4 == "a":

                print("\nYou show the project and explain what you built.")
                print("The developer gives you positive feedback.")
                print("Your confidence grows.")

            elif choice4 == "b":

                print("\nYou ask the developer for honest feedback.")
                print("They suggest some improvements.")
                print("You now know what to work on next.")

            else:
                print("\nInvalid choice. The conversation ends.")

        elif choice3 == "b":

            print("\nYou abandon the project when things become difficult.")
            print("You learn that real development involves debugging.")
            print("Your project remains unfinished.")

            choice4 = input(
                "\nSCENARIO 4\n"
                "A developer asks why your project is unfinished.\n"
                "A. BE HONEST\n"
                "B. PRETEND IT IS FINISHED\n"
                "Choose A or B: "
            ).lower()

            if choice4 == "a":

                print("\nYou honestly explain that you struggled with debugging.")
                print("The developer respects your honesty.")
                print("They suggest that you keep practicing.")

            elif choice4 == "b":

                print("\nYou pretend the project is complete.")
                print("The developer asks questions you cannot answer.")
                print("You lose some credibility.")

            else:
                print("\nInvalid choice. You lose the opportunity.")

        else:
            print("\nInvalid choice. Please choose A or B.")


    elif choice2 == "c":

        print("\nYou decide to watch one BTS video.")
        print("One video becomes several hours of watching.")
        print("Your study and project plans are delayed.")

        choice3 = input(
            "\nSCENARIO 3\n"
            "The next morning, you have work to do.\n"
            "A. CATCH UP ON YOUR PROJECT\n"
            "B. KEEP WATCHING BTS\n"
            "Choose A or B: "
        ).lower()

        if choice3 == "a":

            print("\nYou get back to work and recover some lost time.")
            print("Your project starts moving forward again.")
            print("You learn to control distractions.")

            choice4 = input(
                "\nSCENARIO 4\n"
                "A developer asks about your progress.\n"
                "A. SHOW YOUR PROJECT\n"
                "B. ASK FOR ADVICE\n"
                "Choose A or B: "
            ).lower()

            if choice4 == "a":

                print("\nYou show your progress.")
                print("The developer gives you useful feedback.")
                print("Your project improves.")

            elif choice4 == "b":

                print("\nYou ask how to improve your project.")
                print("The developer shares some helpful advice.")
                print("You make a better plan.")

            else:
                print("\nInvalid choice. The opportunity is lost.")

        elif choice3 == "b":

            print("\nYou keep watching BTS instead of working.")
            print("Your deadline gets closer.")
            print("Your project falls behind.")

            choice4 = input(
                "\nSCENARIO 4\n"
                "Your application deadline is tomorrow.\n"
                "A. START WORKING IMMEDIATELY\n"
                "B. IGNORE THE DEADLINE\n"
                "Choose A or B: "
            ).lower()

            if choice4 == "a":

                print("\nYou work hard to finish your project.")
                print("It is not perfect, but you submit it.")
                print("You learn from the experience.")

            elif choice4 == "b":

                print("\nYou ignore the deadline.")
                print("The opportunity passes without you applying.")
                print("Your job search is delayed.")

            else:
                print("\nInvalid choice. The deadline passes.")

        else:
            print("\nInvalid choice. Please choose A or B.")


    else:
        print("\nInvalid choice. Please choose A, B, or C.")


# ============================================================
# BUILD PATH
# ============================================================

elif choice1 == "b":

    print("\nYou decide to build a real project.")
    print("You do not know everything, but you start anyway.")
    print("This is how your portfolio begins.")

    choice2 = input(
        "\nSCENARIO 2\n"
        "You need to decide how to approach the project.\n"
        "A. BUILD IT YOURSELF\n"
        "B. COPY A TUTORIAL COMPLETELY\n"
        "C. GIVE UP BECAUSE IT IS DIFFICULT\n"
        "Choose A, B, or C: "
    ).lower()

    if choice2 == "a":

        print("\nYou build the project yourself and research when needed.")
        print("It takes longer, but you understand what you create.")
        print("Your skills improve.")

        choice3 = input(
            "\nSCENARIO 3\n"
            "Your project has a serious bug.\n"
            "A. DEBUG IT\n"
            "B. ASK FOR HELP\n"
            "C. DELETE THE PROJECT\n"
            "Choose A, B, or C: "
        ).lower()

        if choice3 == "a":

            print("\nYou patiently investigate the bug.")
            print("You eventually find the problem.")
            print("Your debugging skills improve.")

        elif choice3 == "b":

            print("\nYou ask someone for help after trying first.")
            print("They help you understand the problem.")
            print("You fix the bug and learn from it.")

        elif choice3 == "c":

            print("\nYou delete the project because debugging is frustrating.")
            print("You lose your progress.")
            print("You learn that quitting makes difficult problems harder.")

        else:
            print("\nInvalid choice. The project remains unfinished.")


    elif choice2 == "b":

        print("\nYou follow a tutorial and copy most of the project.")
        print("The project works, but you struggle to explain it.")
        print("Your understanding is limited.")

        choice3 = input(
            "\nSCENARIO 3\n"
            "An employer asks about your project.\n"
            "A. EXPLAIN HONESTLY WHAT YOU KNOW\n"
            "B. PRETEND YOU BUILT EVERYTHING YOURSELF\n"
            "Choose A or B: "
        ).lower()

        if choice3 == "a":

            print("\nYou explain which parts you understand.")
            print("The employer appreciates your honesty.")
            print("You know what you need to learn next.")

        elif choice3 == "b":

            print("\nThe employer asks technical questions.")
            print("You cannot explain important parts of the project.")
            print("You lose the opportunity.")

        else:
            print("\nInvalid choice. The interview ends.")


    elif choice2 == "c":

        print("\nYou decide the project is too difficult.")
        print("You stop before learning what you are capable of.")
        print("Your portfolio remains empty.")

        choice3 = input(
            "\nSCENARIO 3\n"
            "A new opportunity appears.\n"
            "A. TRY AGAIN\n"
            "B. IGNORE IT\n"
            "Choose A or B: "
        ).lower()

        if choice3 == "a":

            print("\nYou decide to try again.")
            print("This time, you start with a smaller project.")
            print("You make progress.")

        elif choice3 == "b":

            print("\nYou ignore the opportunity.")
            print("Nothing changes because you took no action.")
            print("Your career progress slows down.")

        else:
            print("\nInvalid choice. You miss the opportunity.")

    else:
        print("\nInvalid choice. Please choose A, B, or C.")


# ============================================================
# REST PATH
# ============================================================

elif choice1 == "c":

    print("\nYou decide to rest after a long week.")
    print("Rest is important when you are working toward a big goal.")
    print("But tomorrow, you need to get back to work.")

    choice2 = input(
        "\nSCENARIO 2\n"
        "The next day, what do you do?\n"
        "A. START WORKING\n"
        "B. REST AGAIN\n"
        "C. WATCH BTS\n"
        "Choose A, B, or C: "
    ).lower()

    if choice2 == "a":

        print("\nYou return to your studies and projects.")
        print("You feel refreshed and productive.")
        print("Your career journey continues.")

        choice3 = input(
            "\nSCENARIO 3\n"
            "You receive a job opportunity.\n"
            "A. APPLY IMMEDIATELY\n"
            "B. IMPROVE YOUR PROJECT FIRST\n"
            "Choose A or B: "
        ).lower()

        if choice3 == "a":

            print("\nYou apply with the skills and projects you currently have.")
            print("Your application gets noticed.")
            print("You receive an interview invitation.")

            choice4 = input(
                "\nSCENARIO 4\n"
                "You are preparing for the interview.\n"
                "A. PRACTICE EXPLAINING YOUR PROJECT\n"
                "B. GO IN WITHOUT PREPARING\n"
                "Choose A or B: "
            ).lower()

            if choice4 == "a":

                print("\nYou practice explaining your project clearly.")
                print("You feel confident during the interview.")
                print("You have a strong chance of success.")

            elif choice4 == "b":

                print("\nYou enter the interview without preparation.")
                print("You struggle to explain some technical decisions.")
                print("The employer chooses another candidate.")

            else:
                print("\nInvalid choice. The interview preparation stops.")

        elif choice3 == "b":

            print("\nYou improve your project before applying.")
            print("Your portfolio becomes stronger.")
            print("You are better prepared for the opportunity.")

            choice4 = input(
                "\nSCENARIO 4\n"
                "A developer asks about your project.\n"
                "A. SHOW THE PROJECT\n"
                "B. ASK FOR FEEDBACK\n"
                "Choose A or B: "
            ).lower()

            if choice4 == "a":

                print("\nYou confidently demonstrate your project.")
                print("The developer likes your initiative.")
                print("You receive useful career advice.")

            elif choice4 == "b":

                print("\nYou ask for honest feedback.")
                print("The developer points out areas to improve.")
                print("Your project becomes stronger.")

            else:
                print("\nInvalid choice. You miss the feedback.")

        else:
            print("\nInvalid choice. Please choose A or B.")


    elif choice2 == "b":

        print("\nYou keep resting instead of returning to your goals.")
        print("Your tasks begin to pile up.")
        print("Your progress slows down.")

        choice3 = input(
            "\nSCENARIO 3\n"
            "You now have several unfinished tasks.\n"
            "A. MAKE A PLAN\n"
            "B. IGNORE EVERYTHING\n"
            "Choose A or B: "
        ).lower()

        if choice3 == "a":

            print("\nYou create a simple plan and tackle one task at a time.")
            print("Your workload becomes manageable.")
            print("You get back on track.")

        elif choice3 == "b":

            print("\nYou continue ignoring your responsibilities.")
            print("Your unfinished work keeps growing.")
            print("Your career progress suffers.")

        else:
            print("\nInvalid choice. Your tasks remain unfinished.")


    elif choice2 == "c":

        print("\nYou start watching BTS instead of returning to work.")
        print("One video turns into several.")
        print("Your schedule falls behind.")

        choice3 = input(
            "\nSCENARIO 3\n"
            "You realize you have wasted most of the day.\n"
            "A. STOP AND WORK\n"
            "B. CONTINUE WATCHING\n"
            "Choose A or B: "
        ).lower()

        if choice3 == "a":

            print("\nYou put your phone away and get back to work.")
            print("You cannot recover the whole day, but you make progress.")
            print("Tomorrow, you plan your time better.")

        elif choice3 == "b":

            print("\nYou continue watching instead of working.")
            print("Another day passes without progress.")
            print("Your career goal gets further away.")

        else:
            print("\nInvalid choice. The day ends without progress.")

    else:
        print("\nInvalid choice. Please choose A, B, or C.")


# ============================================================
# INVALID FIRST CHOICE
# ============================================================

else:

    print("\nInvalid choice.")
    print("You need to choose A, B, or C.")
    print("The adventure ends here.")
