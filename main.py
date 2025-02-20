from src.user_interface import UserInterface

def main():
    ui = UserInterface()
    ui.get_movie_and_seats()
    ui.main_menu()

if __name__ == "__main__":
    main()