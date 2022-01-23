"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730458544"

created_word: str = input("Enter a 5-character word:")
if len(created_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

single_letter: str = input("Enter a single character:")
if len(single_letter) > 1:
    print("Error: Character must be a single character.")
    exit()
else:
    if len(single_letter) < 1:
        print("Error: Character must be a single character.")
        exit()

matching_count: int = 0
print("Searching for " + single_letter + " in " + created_word)

if created_word[0] == single_letter:
    print(single_letter + " found at index 0")
    matching_count = matching_count + 1
if created_word[1] == single_letter:
    print(single_letter + " found at index 1")
    matching_count = matching_count + 1
if created_word[2] == single_letter:
    print(single_letter + " found at index 2")
    matching_count = matching_count + 1
if created_word[3] == single_letter:
    print(single_letter + " found at index 3")
    matching_count = matching_count + 1
if created_word[4] == single_letter: 
    print(single_letter + " found at index 4")
    matching_count = matching_count + 1

if matching_count == 0:
    print("No instances of " + single_letter + " found in " + created_word)
else:
    if matching_count == 1:
        print("1 instance of " + single_letter + " found in " + created_word)
    else:
        if matching_count == 2:
            print("2 instances of " + single_letter + " found in " + created_word)
        else:
            if matching_count == 3:
                print("3 instances of " + single_letter + " found in " + created_word)
            else:
                if matching_count == 4:
                    print("4 instances of " + single_letter + " found in " + created_word)
                else:
                    if matching_count == 5:
                        print("5 instances of " + single_letter + " found in " + created_word)