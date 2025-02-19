from src.movie_and_seats import MovieAndSeats

class UserInterface:
    def __init__(self):
        pass

    def get_movie_and_seats(self):
        """ Get movie information from user """
        while True:
            try:
                movie_title_and_seats = input(
                    "Please define movie title and seating map in [Title][Row][SeatsPerRow] format:\n> ").split()
                title = movie_title_and_seats[0]
                rows = int(movie_title_and_seats[1])
                seats_per_row = int(movie_title_and_seats[2])
                return MovieAndSeats(title, rows, seats_per_row)
            except (ValueError, IndexError):
                print("Please enter the correct format.")
            except Exception as e:
                print(e)

    def main_menu(self, movie_and_seats: MovieAndSeats):
        """ Main menu """
        while True:
            print("Welcome to Rocket Cinemas")
            print(
                f"[1] Book tickets for {movie_and_seats.title} ({movie_and_seats.available_seats} seats available)")
            print("[2] Check bookings")
            print("[3] Exit")
            print("Please enter your selection:")
            selection = input("> ")

            if selection == "1":
                self.book_tickets()
            if selection == "2":
                print("2...")
            if selection == "3":
                print("Thank you for using Rocket Cinemas system. Bye!")
                break
            else:
                print("Please enter a valid selection.")

    def book_tickets(self):
        """Book tickets menu"""
        while True:
            try:
                num_of_tickets = input(
                    "Enter the number of tickets to book, or enter blank to go back to the main menu:\n> ")
                if not num_of_tickets:  # Go back to main menu per requirement
                    return
                num_of_tickets = int(num_of_tickets)
                if num_of_tickets < 1:
                    print("Please enter a number greater than 0.")
                    continue
                if num_of_tickets > self.available_seats:
                    print("Not enough seats available.")
                    continue
            except ValueError:
                print("Please enter a valid number.")
