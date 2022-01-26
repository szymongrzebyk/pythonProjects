punctuations = [",", ".", "-", "!", "?"]


def make_list(sentence):
    list_of_words = sentence.split()
    list_of_words = separate_punctuations(list_of_words)
    list_of_words = lower_case(list_of_words)
    return list_of_words


def separate_punctuations(changed_list):
    for i in range(len(changed_list)):
        if changed_list[i][-1] in punctuations and len(changed_list[i]) > 1:
            changed_list.insert(i + 1, changed_list[i][-1])
            word_with_punctuation = changed_list[i]
            word_with_punctuation = word_with_punctuation[:-1]
            changed_list[i] = word_with_punctuation
            i += 2
    return changed_list


def lower_case(list_of_words):
    mapped_list = map(str.lower, list_of_words)
    lowercase_list = list(mapped_list)
    return lowercase_list
