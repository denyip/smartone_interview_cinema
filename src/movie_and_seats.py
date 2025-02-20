from src.constants import *

class MovieAndSeats:
    def __init__(self, title, rows, seats_per_row):
        self.title = title
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.validate_input()
        self.total_seats = rows * seats_per_row
        self.available_seats = self.total_seats
        self.seating_map = [
            [AVAILABLE_SEAT_MARK for _ in range(seats_per_row)] for _ in range(rows)]
        self.booking_id = 0

    def validate_input(self):
        if self.rows > MAX_ROWS or self.seats_per_row > MAX_SEATS_PER_ROW:
            raise ValueError(f"Rows must be less than {MAX_ROWS} and seats per row must be less than {MAX_SEATS_PER_ROW}.")