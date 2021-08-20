def sentence_maker(phrase):
    capitalized = phrase.capitalize()
    interogatives = ("how".capitalize(), "why".capitalize(), "what".capitalize())
    if capitalized.startswith(interogatives):
        print(capitalized + str("?"))
    else:
        print(capitalized)

print(sentence_maker ("HOW ARE YOU"))

results = []

while True:
    user_input = input("say something: ")
    if user_input =="\end":
        break
    else:
        results.append(user_input)
print(results)

