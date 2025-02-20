from typing import List
from src.constants import *
from src.movie_and_seats import MovieAndSeats

class BookingServices:
    def __init__ (self, movie_and_seats: MovieAndSeats, num_of_tickets:int, target_seating_map: List[List[str]]):
        self.num_of_tickets = num_of_tickets
        self.seating_map = movie_and_seats.seating_map
        self.target_seating_map = target_seating_map
        self.movie_and_seats = movie_and_seats
        self.current_booking_id = ""
        self.best_seats = []

    def find_the_best_seats(self):
        """
            - Start from the furthest row from the screen
            - Start from the middle-most possible col.
            - When a row is not enough to accommodate the number of tickets, it should overflow to the next row closer to the screen
        Returns:
            List[Tuple[int, int]]: list of coordinates of the best seats
        """
        self.best_seats = []
        seating_map = self.seating_map
        num_of_tickets = self.num_of_tickets
        rows = len(seating_map)
        seating_per_row = len(seating_map[0])

        if num_of_tickets < seating_per_row:
            mid_seat_pos = seating_per_row // 2
            left_seat_start_pos = mid_seat_pos - num_of_tickets // 2
            right_seat_end_pos = mid_seat_pos + num_of_tickets // 2 + (num_of_tickets % 2)

            for current_searching_row in range(rows):
                if all(seating_map[current_searching_row][current_searching_seat] == AVAILABLE_SEAT_MARK for current_searching_seat in range(left_seat_start_pos, right_seat_end_pos)):
                    best_seats = []
                    for current_searching_seat in range(left_seat_start_pos, right_seat_end_pos):
                        best_seats.append((current_searching_row, current_searching_seat))
                    self.best_seats = best_seats
                    return best_seats

    def create_booking_id(self):
        self.movie_and_seats.booking_counter += 1
        self.current_booking_id = f"HKG{self.movie_and_seats.booking_counter:04d}"
        return self.current_booking_id

    def confirm_booking(self):
        self.seating_map = self.target_seating_map
        self.movie_and_seats.available_seats -= self.num_of_tickets
        self.movie_and_seats.booking_records[self.current_booking_id] = self.best_seats
