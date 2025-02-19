class UserInterface:
    def __init__(self):
        pass

    def get_movie_and_seats(self):
        """ Get movie information from user """
        while True:
            try:
                movie_title_and_seats = input("Please define movie title and seating map in [Title][Row][SeatsPerRow] format:\n> ").split()
                movie_title = movie_title_and_seats[0]
                rows = int(movie_title_and_seats[1])
                seats_per_row = int(movie_title_and_seats[2])
                return movie_title, rows, seats_per_row
            except(ValueError, IndexError):
                print("Please enter the correct format.")
            except Exception as e:
                print(e)

    def main_menu(self, movie_title, available_seats):
        """ Main menu """
        while True:
            print("Welcome to Rocket Cinemas")
            print(f"[1] Book tickets for {movie_title} ({available_seats} seats available)")
            print("[2] Check bookings")
            print("[3] Exit")
            print("Please enter your selection:")
            selection = input("> ")

            if selection == "1":
                print("1...")
            if selection == "2":
                print("2...")
            if selection == "3":
                print("Thank you for using Rocket Cinemas system. Bye!")
                break
            else:
                print("Please enter a valid selection.")