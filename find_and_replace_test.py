#This is to make it so I can turn an excel cluster into a dictionary content

original = """hello, world
where, are, we"""

new_word = original.replace(",","")

print (new_word)

target = open("lazy.txt", "r")
buffer1 = target.read()
buffer2 = buffer1.replace("	","\',\'")
buffer2 = buffer2.replace("\',\':\',","\' : [")
buffer2 = buffer2.replace("\n","'],\n\t\'")

target2 = open("lazy2.txt","a")
target2.write(buffer2)
