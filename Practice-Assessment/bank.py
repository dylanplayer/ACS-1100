
def getPeopleFrom(filePath):
    data = []
    with open(filePath) as file:
        lines = file.readlines()
        for line in lines:
            data.append(line.strip().split(','))
    return data

def userExists(users, username, password):
    for user in users:
        if user[0] == username and user[1] == password:
            return True
        else:
            return False

def getUser(users, username, password):
    for user in users:
        if user[0] == username and user[1] == password:
            return user

def printUserData(user):
    print('Name:', user[2])
    print("Balance:", user[3])

def run():
    users = getPeopleFrom('data.txt')
    username = input('Enter Username: ')
    password = input('Enter Password: ')
    while not userExists(users, username, password):
        print('Username and password not found')
        username = input('Enter Username: ')
        password = input('Enter Password: ')
    printUserData(getUser(users, username, password))

run()