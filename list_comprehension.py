#to save spaces we dont save lists with . we save whole number then divide
temps = [234, 321, 123,-9999,34]
new_temps = [temp/10 for temp in temps if temp!=-9999]

print(new_temps)

lists = [34,56,"1",4]
def make_list(lists):
    
    new_list = [lst for lst in lists if type(lst)==int]
    return new_list
print(make_list(lists))

listss = [30, 1, 4, 45, 12]
def list_maker(lists):
    new_list =[lst for lst in listss if lst>5]
    return new_list
print(list_maker(lists))

#function for args. *args are the urguiments to take in for a function
def mean(*args):
    the_mean = sum(args)/len(args)
    return the_mean

print(mean(2,4,6))

#kwarg. here the arguments have to be assigned

def find_sum(**kwargs):
    total = sum(kwargs.values())
    return total
print(find_sum(a=5,b=11))