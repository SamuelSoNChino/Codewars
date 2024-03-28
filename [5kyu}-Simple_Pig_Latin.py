def pig_it(text):
    new_text = ""
    for word in text.split(" "):
        if word not in [".", ",", "?", "!", ":"]:
            new_text += word[1:] + word[0] + "ay "
        else:
            new_text += word + " "
    return new_text[:-1]
