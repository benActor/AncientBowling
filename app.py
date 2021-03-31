from ancientBowling import AncientBowling

if __name__ == '__main__':
    bowling = AncientBowling()

    def valid_input(user_input):
        try:
            int(user_input)
            return True
        except ValueError:
            return False

    user_input = input("enter the pins Shot: ")

    while True:
        if not valid_input(user_input):
            user_input = input("Shot must be integer: ")
        else:
            print(f"Your Score is: {bowling.shot(int(user_input))}")
            user_input = input("enter the pins Shot: ")