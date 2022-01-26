import inputOrganizer
import commonWords

sentence = input()
listed_sentence = inputOrganizer.make_list(sentence)
for item in listed_sentence:
    if item in commonWords.get_hello():
        print("There is a greeting!")
    if item in commonWords.get_curse():
        print("Don't curse.")
