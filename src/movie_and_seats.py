class MovieAndSeats:
    def __init__(self, title, rows, seats_per_row):
        self.title = title
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.validate_input()
        self.available_seats = rows * seats_per_row
        self.seating_map = [["•" for _ in range(seats_per_row)] for _ in range(rows)]

    def validate_input(self):
        if self.rows > 26 or self.seats_per_row > 50:
            raise ValueError("Rows must be less than 26 and seats per row must be less than 50.")