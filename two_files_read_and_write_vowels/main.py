f=open('file1.txt','r')

words=f.read().split()
f.close()

f=open('file2.txt','w')

for word in words:
    if(word[0]=='a' or word[0]=='o' or word[0]=='u'or word[0]=='i' or word[0]=='e'):
        f.write(f'{word} \n')

f=open('file2.txt','r')
print(f.read())

f.close()
