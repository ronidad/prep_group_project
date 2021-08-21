def greet(who_to_greet):
    greetings = "Hello " + str(who_to_greet)
    return greetings


print(greet("Ronnie"))


def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean

