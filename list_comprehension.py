#to save spaces we dont save lists with . we save whole number then divide
temps = [234, 321, 123,-9999,34]
new_temps = [temp/10 for temp in temps if temp!=-9999]

print(new_temps)

lists = [34,56,"1",4]
def make_list(lists):
    
    new_list = [lst for lst in lists if type(lst)==int]
    return new_list
print(make_list(lists))