f=open("file.txt","r")

text=f.read()

words=text.split()
f.close()

longest=''
for word in words:
    if(len(word)>len(longest)):
        longest=word

print(f'The longest word in the file is: {longest}')