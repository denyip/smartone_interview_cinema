from src.movie_and_seats import MovieAndSeats
from src.booking_services import BookingServices
from typing import List

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

            except IndexError:
                print("Please enter the correct format.")
            except Exception as e:
                print(e)

    def main_menu(self, movie_and_seats: MovieAndSeats):
        """ Main menu """
        while True:
            self.display_seating_map(movie_and_seats.seating_map)
            print("Welcome to Rocket Cinemas")
            print(
                f"[1] Book tickets for {movie_and_seats.title} ({movie_and_seats.total_seats} seats available)")
            print("[2] Check bookings")
            print("[3] Exit")
            print("Please enter your selection:")
            selection = input("> ")

            if selection == "1":
                self.book_tickets(movie_and_seats)
            if selection == "2":
                print("2...")
            if selection == "3":
                print("Thank you for using Rocket Cinemas system. Bye!")
                break
            else:
                print("Please enter a valid selection.")

    def book_tickets(self, movie_and_seats: MovieAndSeats):
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
                if num_of_tickets > movie_and_seats.available_seats:
                    print("Not enough seats available.")
                    continue
                booking_services = BookingServices(movie_and_seats, num_of_tickets)
                target_seating_map = booking_services.find_the_best_seats()
                unconfirmed_seating_map = [row[:] for row in target_seating_map]
                movie_and_seats.seating_map = target_seating_map
                movie_and_seats.booking_id += 1
                print(f"Successfully reserved {num_of_tickets} {movie_and_seats.title} tickets.")
                print(f"Booking ID: HKG{movie_and_seats.booking_id:04d}")
                self.display_seating_map(unconfirmed_seating_map)
            except ValueError:
                print("Please enter a valid number.")

    def display_seating_map(self, seating_map: List[List[str]]):
        """ Display seating map """
        LETTER_A_ASCII = 65
        rows = len(seating_map)
        seats_per_row = len(seating_map[0])
        total_width = (seats_per_row*2)+1
        screen_text = "S C R E E N"
        screen_text_padding = " "*((total_width - len(screen_text)) // 2)
        print(f"{screen_text_padding}{screen_text}{screen_text_padding}")
        print("-" * total_width)
        for i in range(rows-1, -1, -1):
            row_letter = chr(LETTER_A_ASCII + i)
            print(f"{row_letter} {' '.join(seating_map[i])}")
        number_str = " ".join(str(i+1) for i in range(seats_per_row))
        print(f"  {number_str}")