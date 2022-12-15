f=open("test.txt","wb")
text="Joji's adventures"
text_new=text.encode('ascii')
f.write(text_new)
f.close()

f=open("test.txt","rb")
text=f.read()
text_new=text.decode("ascii")
print(text_new)
f.close()