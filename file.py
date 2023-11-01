##f1=open("C:\test.txt",encoding="utf8")
##print(f1.read())
##f1.close()
##CODE 2:
##with open("C:test.txt","r",encoding="utf8") as f1:
##    print(f1.read())
fn="C:\test.txt"
f=open(fn,"a")
f.write("Breathe, Its just a bad day, not a bad life\n")
f.close()
