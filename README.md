<h1 > 
  Kaun Banega Crorepati Game 👑
</h1>

<h2> Structure ䷦  </h2>

- Admin() function: This function takes user input to get the player's name, the total prize amount, and the total number of questions (tQ). It returns these values to the caller.

- Question_Answers() function: This function defines a list of questions and their corresponding answers. It returns these lists to the caller.
- Mcqs() function: This function defines multiple-choice options for each question and returns a list of lists (q) containing the options.
- code() function: This is the main function that implements the game logic. It uses a while loop to iterate through the questions. It presents each question to the player, takes their input as the answer, and checks if it's correct. Based on the correctness of the answer and the time taken to respond, it calculates the number of correct answers (num_correct) and the prize amount won (amount_won).
- Main Execution:
The user is asked to input the required details through Admin() function (name, prize amount, and total number of questions).
Some introductory messages and instructions are printed, and their corresponding speech messages are played using os.system('say ...').
The user is prompted to press 'S' to start the game. If 'S' is pressed, the game starts, and the questions are presented to the player.

- The code() function is called to handle the game logic.
- Player is given 10 seconds to answer each question otherwise he will win prize amount according to previously correct answered questions.
- If the player answers all questions correctly, a victory message is displayed along with the amount won.
- This game is made using terminal window
