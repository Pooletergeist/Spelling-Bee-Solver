import json


def onlyComposedOf(candidate, substrate):
    """True iff candidate is composed out of only letters in substrate"""
    for letter in candidate:
        if letter not in substrate:
            return False
    return True

def isPangram(word, puzzle):
    """returns whether given valid-puzzle word is a pangram"""
    for letter in puzzle:
        if letter not in word:
            return False
    return True


def pointsOf(word):
    """returns non-pangram Spelling-Bee Points of a given word"""
    if len(word) == 4:
       return 1
    else:
        return len(word)
 

def solvePuzzle():
    """requests a puzzle from a user, returns a dictionary of solution words 
        with their point values """

    # requests a puzzle in the command line, with the center letter first

    isValidPuzzle = False

    while not isValidPuzzle:
        puzzle = input(("Please enter your puzzle, starting with "
            "the letter in the center hex: \n"))
        if len(puzzle) == 7 and puzzle.isalpha():
            isValidPuzzle = True

    # loads Merriam Webster 2009 english dictionary as python dictionary
    with open('dictionary_MW_2009.json') as json_file:
        dictionary = json.load(json_file)

    solution = {} 
    pangrams = {}
    total_points = 0
    total_words = 0

    # checks each word for candidacy as a solution word:
    # a word must be at least 4 letters in length, must contain
    # the center letter, and must contain no letters not in the puzzle
    for word in dictionary:
        if len(word) >= 4:
            if puzzle[0] in word:
                if onlyComposedOf(word, puzzle):
                    score = pointsOf(word)

                    if isPangram(word, puzzle):
                        score += 7
                        pangrams[word] = score

                    solution[word] = score
                    total_points += score
                    total_words += 1

    print("=======")
    print(solution)
    print("=======")

    print("The total number of words is " + str(total_words))
    print("The total number of points is " + str(total_points))
    print("Pangram(s): ")
    print(pangrams)

    return solution


if __name__ == "__main__":
    solvePuzzle()
