from typing import List
from src.constants import *
from src.movie_and_seats import MovieAndSeats


class BookingServices:
    def __init__(self, movie_and_seats: MovieAndSeats, num_of_tickets: int, target_seating_map: List[List[str]]):
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

        if num_of_tickets > self.movie_and_seats.available_seats:
            print("Not enough seats available.")
            return self.best_seats

        seats_need_to_book = num_of_tickets
        for current_searching_row in range(rows):
            if seating_per_row % 2 == 0:
                mid_seat_pos = []
                mid_seat_pos.append(seating_per_row // 2 - 1)
                mid_seat_pos.append(seating_per_row // 2)
                mid_left_seat_pos = mid_seat_pos[0]
                mid_right_seat_pos = mid_seat_pos[1]
                if seating_map[current_searching_row][mid_left_seat_pos] == AVAILABLE_SEAT_MARK and seats_need_to_book > 0:
                    self.best_seats.append(
                        (current_searching_row, mid_left_seat_pos))
                    seats_need_to_book -= 1
                if seating_map[current_searching_row][mid_right_seat_pos] == AVAILABLE_SEAT_MARK and seats_need_to_book > 0:
                    self.best_seats.append(
                        (current_searching_row, mid_right_seat_pos))
                    seats_need_to_book -= 1
                seat_idx = 1
                while seats_need_to_book > 0 and mid_seat_pos[1] + seat_idx < seating_per_row and mid_seat_pos[0] - seat_idx >= 0:
                    left_seat_pos = mid_left_seat_pos - seat_idx
                    right_seat_pos = mid_right_seat_pos + seat_idx
                    if seating_map[current_searching_row][right_seat_pos] == AVAILABLE_SEAT_MARK:
                        self.best_seats.append(
                            (current_searching_row, right_seat_pos))
                        seats_need_to_book -= 1
                    if seating_map[current_searching_row][left_seat_pos] == AVAILABLE_SEAT_MARK and seats_need_to_book > 0:
                        self.best_seats.append(
                            (current_searching_row, left_seat_pos))
                        seats_need_to_book -= 1
                    seat_idx += 1
            else:
                mid_seat_pos = seating_per_row // 2
                # Try to fill the middle-most seats first
                if seating_map[current_searching_row][mid_seat_pos] == AVAILABLE_SEAT_MARK and seats_need_to_book > 0:
                    self.best_seats.append(
                        (current_searching_row, mid_seat_pos))
                    seats_need_to_book -= 1
                seat_idx = 1
                while seats_need_to_book > 0 and mid_seat_pos + seat_idx <= seating_per_row and mid_seat_pos - seat_idx >= 0:
                    if mid_seat_pos + seat_idx < seating_per_row and seating_map[current_searching_row][mid_seat_pos + seat_idx] == AVAILABLE_SEAT_MARK:
                        self.best_seats.append(
                            (current_searching_row, mid_seat_pos + seat_idx))
                        seats_need_to_book -= 1
                    if seating_map[current_searching_row][mid_seat_pos - seat_idx] == AVAILABLE_SEAT_MARK and seats_need_to_book > 0:
                        self.best_seats.append(
                            (current_searching_row, mid_seat_pos - seat_idx))
                        seats_need_to_book -= 1
                    seat_idx += 1
        return self.best_seats

    def create_booking_id(self):
        self.movie_and_seats.booking_counter += 1
        self.current_booking_id = f"HKG{self.movie_and_seats.booking_counter:04d}"
        return self.current_booking_id

    def confirm_booking(self):
        self.movie_and_seats.seating_map = self.target_seating_map
        self.movie_and_seats.available_seats -= self.num_of_tickets
        self.movie_and_seats.booking_records[self.current_booking_id] = self.best_seats
