# my_file = open("my_file.txt")
# content = my_file.read()
# print(content)
#this helps work with the file and close it immedietly 
with open('my_file.txt') as f:
    content = f.read()
print(content)

# we can also  write a new file. if you use with on existing file, it will overwrite
with open('tomato.txt', 'w') as f:
    content = f.write("this is my file \n onions \n veges")

#adding to the list without overwriting 
with open('my_file.txt') as f:
    content = f.read()
print(content[:90])
    
with open('my_file.txt') as f:
    content = f.read()
    with open('first.txt','w') as f2:
        f2.write(content[:90])

#adding to the list without overwriting. use a.. append
with open('first.txt', 'a') as f:
    f.write('\n more')
