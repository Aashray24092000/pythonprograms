import csv
data=[["name","mail","phone"],
      ["ashu","ashray@gmail.com",6248485358],
      ["ashray","gmail.com",879877565]
]
#create csv file 
with open("data.csv","w") as f:
    writer =  csv.writer(f)
    
    for i in data:
        writer.writerow(i)
#how to read csv file
with open("data.csv","r") as f:
    read= csv.reader(f)
    for i in read:
        print(i)
#how to write bin file

with open("test1.bin","wb") as f:
    f.write(b"\x01\x02\x03")
#how to read bin file
with open("test1.bin","rb") as f:
    print(f.read())
