import io
with open("test2.txt","wb") as f:
    file=io.BufferedWriter(f)
    
    file.write(b"hello sir")
    file.write(b"hyyy sir")
    file.flush()
