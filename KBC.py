import os
import time


def Admin():
    print("Admin menu")
    player_name = input("Enter the name of the participant: ")
    prize_amount = int(input("Enter the total prize amount: "))
    tQ = int(input("Enter the total Questions: "))
    return player_name, prize_amount, tQ


def Question_Answers():
    questions = ["When did Pakistan come into being?",
                 "What is the capital of France?",
                 "How many planets are there in our solar system?",
                 "Who painted the Mona Lisa?",
                 "What is the largest organ in the human body?",
                 "What is the chemical symbol for gold?",
                 "Which country is known as the Land of the Rising Sun?",
                 "What is the main language spoken in Brazil?",
                 "Who is the author of the Harry Potter book series?",
                 "What is the tallest mountain in the world?"]

    answers = ["1947",
               "Paris",
               "8",
               "Leonardo da Vinci",
               "Skin",
               "Au",
               "Japan",
               "Portuguese",
               "J.K. Rowling",
               "Mount Everest"]
    return questions, answers


def Mcqs():
    q = [
        ["1823", "1974", "1947", "1950"],
        ["Berlin", "Paris", "Lisbon", "Lahore"]
    ]
    return q


def code():
    i = 0
    flag = 0
    num_correct = 0
    while i < tQ:
        print(questions[i])
        os.system(f"say '{questions[i]}'")
        for j in range(len(q[i])):
            print(f"{j + 1}. {q[i][j]}")
            os.system(f"say '{q[i][j]}'")
        os.system("say 'Enter your choice'")
        start = time.time()
        ch1 = input("Enter your choice: ")
        ch1 = ch1.capitalize()
        end = time.time()
        ttime = end - start
        if ch1 == answers[i]:
            if ttime < 10:
                print("Correct!")
                num_correct += 1
                os.system(f"say 'Correct'")
            else:
                print("Time's up")
                os.system("say Times up")
                print(f"You have answered {num_correct} out of {tQ}")
                os.system(f"say You have answered {num_correct} out of {tQ}")
                amount_won = (num_correct / 10) * prize_amount
                print(f"You have won {amount_won} out of {prize_amount}.\nBetter Luck next time")
                os.system(f"say You have won {amount_won} out of {prize_amount}. Better Luck next time")
                os.system("say 'Game ended'")
                flag = 1
                break
        else:
            print("Wrong!")
            os.system(f"say 'Wrong'")
            print(f"You have answered {i} out of {tQ}")
            os.system(f"say 'You have answered {i} out of {tQ}'")
            amount_won = i / 10 * prize_amount
            print(f"You have won {amount_won} out of {prize_amount}.\nBetter Luck next time")
            os.system(f"say 'You have won {amount_won} out of {prize_amount}. Better Luck next time'")
            os.system("say 'Game ended'")
            flag = 1
            break
        i += 1
        os.system('clear')

    return flag


if __name__ == '__main__':
    player_name, prize_amount, tQ = Admin()
    opening = "Welcome to Kaun Banega Crorepati"
    opening1 = "This is your Host Amitaab Bachhan."
    print(opening)
    os.system(f"say '{opening}'")
    print(opening1)
    os.system(f"say '{opening1}'")
    os.system(f"say 'Prize amount is {prize_amount}'$")
    os.system('clear')
    opening1 = f"Today we have 1 guest {player_name} who will be playing this game."
    print(opening1)
    os.system(f"say {opening1}")
    os.system('clear')
    Explanation = f"There are a total of {tQ} Questions."
    Explanation1 = "Each question carries 10 percent of the total prize amount."
    Explanation2 = "You have 10 seconds to answer each question otherwise game will end."
    print(Explanation)
    os.system(f"say '{Explanation}'")
    print(Explanation1)
    os.system(f"say '{Explanation1}'")
    print(Explanation2)
    os.system(f"say '{Explanation2}'")
    os.system('clear')

    start = "Press S to start the game"
    print(start)
    os.system(f"say '{start}'")
    ch = input()
    os.system("clear")
    flag = None
    if ch.upper() == 'S':
        os.system(f"say 'Game started'")
        questions, answers = Question_Answers()
        q = Mcqs()
        flag = code()

        if flag == 0:
            victory = "Congratulations! You have won the game!"
            print(victory)
            os.system(f"say '{victory}'")
            print(f"You have won {prize_amount} $.")
            os.system(f"say You have won prize amount of {prize_amount} $ .")

    else:
        print("Invalid Input\n Terminated")
        os.system("say Invalid Input. Terminated")
