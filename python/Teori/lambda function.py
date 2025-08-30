# say_hello = lambda name: print(f"halo nama saya {name}")

# say_hello("mushab")





def login (username, password):
    try:
        if(username == "mushab" and password == "Rahasia2008"):
            print("berhasil login")
        else:
            print("gagal login")
    except Exception :
        print(Exception)
    
username = input("masukan username : ")
password = input("masukan pasword : ")

login(username, password)



