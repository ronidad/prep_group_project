def sentence_maker(phrase):
    interogatives = ("how", "why", "what")
    capitalized = phrase.capitalize()
    
    if phrase.startswith(interogatives):
        return (capitalized + str("?"))
    else:
        return (capitalized + str("."))



results = []

while True:
    user_input = input("say something: ")
    if user_input =="\end":
        break
    else:
        results.append(sentence_maker(user_input))
#print(results)
print(" ".join(results))
