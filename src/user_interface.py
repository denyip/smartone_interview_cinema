from src.constants import *
from src.movie_and_seats import MovieAndSeats
from src.booking_services import BookingServices
from typing import List
import re

class UserInterface:
    def __init__(self):
        self.movie_and_seats = None

    def get_movie_and_seats(self):
        """ Get movie information from user """
        while True:
            try:
                movie_title_and_seats = input(
                    "Please define movie title and seating map in [Title][Row][SeatsPerRow] format:\n> ").split()
                title = movie_title_and_seats[0]
                rows = int(movie_title_and_seats[1])
                seats_per_row = int(movie_title_and_seats[2])
                self.movie_and_seats = MovieAndSeats(title, rows, seats_per_row)
                break
            except IndexError:
                print("Please enter the correct format.")
            except Exception as e:
                print(e)

    def main_menu(self):
        """ Main menu """
        movie_and_seats = self.movie_and_seats
        print(f"Movie title: {movie_and_seats.title}, Rows: {movie_and_seats.rows}, Seats per row: {movie_and_seats.seats_per_row}")
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
                continue
            if selection == "2":
                self.check_bookings()
                continue
            if selection == "3":
                print("Thank you for using Rocket Cinemas system. Bye!")
                break
            else:
                print("Please enter a valid selection.")

    def book_tickets(self):
        """Book tickets menu"""
        movie_and_seats = self.movie_and_seats
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
                target_seating_map = [row[:] for row in movie_and_seats.seating_map]
                booking_services = BookingServices(movie_and_seats, num_of_tickets, target_seating_map)
                best_seats = booking_services.find_the_best_seats()
                for seat in best_seats:
                    row, col = seat
                    target_seating_map[row][col] = SELECTED_SEAT_MARK
                booking_id = booking_services.create_booking_id()
                print(f"Successfully reserved {num_of_tickets} {movie_and_seats.title} tickets.")
                print(f"Booking ID: {booking_id}")
                self.display_seating_map(target_seating_map)
                new_postion = input("Enter blank to accept seat selection, or enter a new seating position\n>")
                if not new_postion:
                    booking_services.confirm_booking()
                    break
                else:
                    if not self.is_seat_input_string_valid(new_postion):
                        break
                    print("New position accepted.")
            except ValueError:
                print("Please enter a valid number.")

    def display_seating_map(self, seating_map: List[List[str]]):
        """ Display seating map """
        rows = len(seating_map)
        seats_per_row = len(seating_map[0])
        total_width = (seats_per_row*2)+1
        screen_text_padding = SPACE_CHAR*((total_width - len(SCREEN_TEXT)) // 2)
        print(f"{screen_text_padding}{SCREEN_TEXT}{screen_text_padding}")
        print("-" * total_width)
        for i in range(rows-1, -1, -1):
            row_letter = chr(LETTER_A_ASCII + i)
            print(f"{row_letter} {SPACE_CHAR.join(seating_map[i])}")
        number_str = SPACE_CHAR.join(str(i+1) for i in range(seats_per_row))
        print(f"  {number_str}")
    
    def check_bookings(self):
        """ Check bookings """
        movie_and_seats = self.movie_and_seats
        while True:
            booking_id = input("Enter booking ID to check booking details, or enter blank to go back to the main menu:\n> ")
            if not booking_id:
                return
            if not re.match(r'^HKG[0-9]{4}$', booking_id):
                print("Invalid booking ID format. Please try again.")
                return
            if booking_id not in movie_and_seats.booking_records:
                print("Booking ID not found.")
                return
            print(f"Booking ID: {booking_id}")
            seating_map = [row[:] for row in movie_and_seats.seating_map]
            for seat in movie_and_seats.booking_records[booking_id]:
                row, col = seat
                seating_map[row][col] = SELECTED_SEAT_MARK
            self.display_seating_map(seating_map)
    
    def is_seat_input_string_valid(self, seat_input: str):
        """ Validate seat input string """
        movie_and_seats = self.movie_and_seats
        if not re.match(r'^[A-Z][1-9]$|^[A-Z][1-4][0-9]$|^[A-Z]50$', seat_input):
            print("Invalid seating position format. Please try again.")
            return False
        try:
            row_letter = seat_input[0].upper()
            seat_number = int(seat_input[1:]) - 1
            row_index = ord(row_letter) - LETTER_A_ASCII
            if row_index < 0 or row_index >= len(movie_and_seats.seating_map) or seat_number < 0 or seat_number >= len(movie_and_seats.seating_map[0]):
                print("Invalid seating position. Please try again.")
                return False
            if movie_and_seats.seating_map[row_index][seat_number] == SELECTED_SEAT_MARK:
                print("Seat already taken. Please choose another seat.")
                return False
            return True
        except (ValueError, IndexError):
            print("Invalid seating position. Please try again.")