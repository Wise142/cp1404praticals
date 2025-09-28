def main():
    password = get_password()
    print("*"* len(password))


def get_password():
    global get_password

    def get_password():
        password = input("Enter your password:")
        while len(password) <= 3:
            print("Invalid")
            password = input("Enter your password:")
        return password


get_password()
main()