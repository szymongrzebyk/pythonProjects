greetings = ["hi", "hello", "welcome", "sup"]
confirmations = ["yes", "sure", "right", "yup", "yeah"]
negations = ["no", "nope", "wrong"]
personal_pronouns = ["i", "you", "he", "she", "it", "we", "they", "me", "him", "her", "us", "them",
                     "my", "your", "his", "hers", "its", "our", "their", "mine", "yours", "ours", "theirs",
                     "myself", "yourself", "himself", "herself", "itself", "ourselves", "yourselves", "themselves"]
curses = ["fuck", "shit", "motherfucker", "whore", "slut", "nigger"]


def get_hello():
    return greetings


def get_yes():
    return confirmations


def get_no():
    return negations


def get_curse():
    return curses
