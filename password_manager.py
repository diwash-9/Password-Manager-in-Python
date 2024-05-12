from cryptography.fernet import Fernet


# key + password + text to encrypt = random text
# random text + key + password = text to encrypt

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)

def load_key():
    file = open("key.key","rb")
    key = file.read()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print(user + "|" + fer.decrypt(password.encode()).decode())

def add():
    name = input("Account name: ")
    password = input("Password: ")
    
    with open('passwords.txt', 'a') as f: # with automatically closes the file after use
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")
        


while True:
    mode = input("Would you like to add a new password or view existing ones (view, add)? Press q to quit ")

    if mode.lower() =="q":
        break

    elif mode.lower() == "view":
        view()
        
    elif mode.lower() == "add":
        add()

    else:
        print("Invalid mode")
        continue