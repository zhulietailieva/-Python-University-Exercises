n=int(input("n="))
res=""
for x in range(1,n+1):
    line=""
    for y in range (x):
        line+="*"
    res+=line+"\n"

print(res.strip())