"""
Full Name:  Evan O'Hara
Class-Section: 1
Assignment Title: average from pseudocode to python
Submission Date: 11/17/25
"""


#creates function to calculate exam scores
def calculate_average():
    try:
        #has user input the first test score
        score1 = float(input('Enter your first score: '))
        #has user input the second test score
        score2 = float(input('Enter your second score: '))
        #has user input the third test score
        score3 = float(input('Enter your thrid score: '))
        #add's up the 3 test scores
        added_score = score1 + score2 + score3
        #prints the first exam score
        print(f'your first exam score was: {score1}')
        #prints the second exam score
        print(f'your second exam score was: {score2}')
        #prints the third exam score
        print(f'your third exam score was: {score3}')
        #gets the average of the 3 exam scores
        print(added_score / 3)
    except ValueError:
        print("Please restart the program and try again with only numbers :)")


#calls function back to main and runs it
calculate_average()