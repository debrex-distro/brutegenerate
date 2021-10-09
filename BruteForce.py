import hashlib

flag=0

pass_hash=input("md5 hash: ")

wordlist = input ("file name: ")
try:
    pass_file=open(wordlist,"r")
except:
    print("No such file found! Program ended.")
    quit()
for word in pass_file:
    enc_wrd=word.encode("utf-8")
    digest=hashlib.md5(enc_wrd.strip()).hexdigest()
    if digest.strip()==pass_hash.strip():
        print("Possible Password found!!!")
        print("Password is: " + word)
        flag=1
        break
if flag==0:
    print("All guesses were tried/tried to try. No passwords in list matches with your list/the server marked us as sus and banned us. Bruteforce has ended. Tool made by Orkun Hatipoğlu.")
