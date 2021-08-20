def sentence_maker(phrase):
    capitalized = phrase.capitalize()
    interogatives = ("how".capitalize(), "why".capitalize(), "what".capitalize())
    if capitalized.startswith(interogatives):
        print(capitalized + str("?"))
    else:
        print(capitalized)

print(sentence_maker ("HOW ARE YOU"))
