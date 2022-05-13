# This program runs a wordle game using a imported word list file

import os.path
import random

# 1. Create the wordlist

def createWordlist(filename):       # From HW 11, creates wordlist w/o repeating letters
    wordFile = open(filename, "r")
    wordlist = []
    words = wordFile.readlines()

    for word in words:
        if len(word) == 6 and word[4] != "s":     # Filters the words that end with s and have more than 5 letters
            same = 0
            temp = 0
            # go through every letter in the word and compare to each other
            for a in range(len(word)):       # Only compare to greater indexed letters, 4 and 4 don't need to be compared
                # Does not compare to letters that have already been compared
                for b in range(a, len(word)):
                    # compare to all letters except for the letter at hand
                    if word[a] == word[b] and a != b:
                        same += 1
                    temp += 1

            if same == 0:        # Do not have letters in common
                newword = ""
                for i in range(len(word) - 1):
                    newword += word[i]
                wordlist.append(newword)
    return wordlist, len(wordlist)

# 2. Check if a word is on the wordlist

def BinarySearch ( lst , key ):     # From slideset 10
    low = 0
    high = len(lst) - 1
    while (high >= low):
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return mid
        else :
            low = mid + 1
    return (-low - 1)

def playWordle(word = None):
    # 3. welcome message
    print("\nWelcome to WORDLE, the popular word game. The goal is to guess a \
        \nfive letter word chosen at random from our wordlist.  None of the \
        \nwords on the wordlist have any duplicate letters. \
        \n\nYou will be allowed 6 guesses.  Guesses must be from the allowed \
        \nwordlist.  We'll tell you if they're not.")

    print("\nEach letter in your guess will be marked as follows: \
        \n\n   x means that the letter does not appear in the answer \
        \n   ^ means that the letter is correct and in the correct location \
        \n   + means that the letter is correct, but in the wrong location")

    print("\nGood luck!\n")

    # 4. Get filename

    file = input("Enter the name of the file from which to extract the wordlist: ")
    # Checks if the file exists and prompts the user if the file DNE
    while os.path.isfile(file) is False:
        print("File does not exist. Try again!")
        file = input("Enter the name of the file from which to extract the wordlist: ")

    # 6. Compare words

    def compareWords(answer, wlist):
        turn = 1    # Number of turns, starts at 1
        gprompt = "Enter your guess (" + str(turn) + "): "  # the prompt for user entered word
        print() 
        guess = input(gprompt)
        while (turn <= 6):
            guess = guess.lower()    # make guess entirely lowercase to compare to the words in the list
            answerlist = list(answer)   # make a list of all the letters in the answer word
            results = ""    # empty string to print the +, ^, and x results for each letter in wordle format
            printguess = ""     # empty string to print the guess word in the wordle format
            if BinarySearch(wlist, guess) >= 0:   # find word in wordlist
                if guess == answer:     # if everything is same place same letter, print congrats and exit
                        for i in range(len(guess)):
                            printguess += guess[i].upper()  # add to string in uppercase
                            printguess += "  "
                        results = "^  ^  ^  ^  ^  "
                        print(printguess)
                        print(results)
                        print("CONGRATULATIONS! You win!\n")
                        break
                for i in range(len(guess)):
                    if (guess[i] in answerlist) and (guess[i] != answerlist[i]):    # letter in the word but wrong pos
                        results += "+  "
                        printguess += guess[i].upper()
                        printguess += "  "
                    elif (guess[i] in answerlist) and (guess[i] == answerlist[i]):  # letter in the right spot
                        results += "^  "
                        printguess += guess[i].upper()
                        printguess += "  "
                    else:       # letter not in the word
                        results += "x  "
                        printguess += guess[i].upper()
                        printguess += "  "
                print(printguess)
                print(results)
                turn += 1
                gprompt = "Enter your guess (" + str(turn) + "): "  # reestablish the turn number
                if turn > 6:
                    break
                guess = input(gprompt)
            else:
                while BinarySearch(wlist, guess) < 0:   # if the word is not in wordlist
                    print("Guess must be a 5-letter word in the wordlist.  Try again!")
                    guess = input(gprompt)
        if (turn > 6) and (guess != answer):    # 6 tries have been reached
            print("Sorry!  The word was ", answer, ". Better luck next time!\n", sep="")

    # 5. Pick answer

    wordlist, listlength = createWordlist(file)     # assigns list to a variable and length to a variable
    if word == None:    # generate random word
        wordleW = wordlist[random.randint(0, listlength)]
        compareWords(wordleW, wordlist)
    elif BinarySearch(wordlist, word) >= 0:     # inputted word
        wordleW = word.lower()
        compareWords(wordleW, wordlist)
    else:       # not in wordlist
        print("\nAnswer supplied is not legal.\n")
    

playWordle()