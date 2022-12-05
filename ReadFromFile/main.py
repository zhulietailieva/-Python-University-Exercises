def read(name_of_file):
    reader= open(name_of_file,'r')
    content = reader.read()
    print(content)
    reader.close()


def find_text(name_of_file,text_to_read):
    reader = open(name_of_file, 'r')
    content = reader.read()
    if text_to_read in content:
       print(f'{text_to_read} is in {name_of_file}')
       reader.close()
    else:
        print(f'created a new file with {text_to_read}')
        writer=open('text1.txt','w')
        writer.write(text_to_read)
        writer.write('\n')
        writer.close()


try:
#read("text.txt")
    find_text('text.txt','some1 text')

except FileNotFoundError:
    print("File not found!")


