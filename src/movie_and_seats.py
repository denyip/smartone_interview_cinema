class MovieAndSeats:
    def __init__(self, title, rows, seats_per_row):
        self.title = title
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.validate_input()
        self.available_seats = rows * seats_per_row
        self.seating_map = [
            ["•" for _ in range(seats_per_row)] for _ in range(rows)]

    def validate_input(self):
        if self.rows > 26 or self.seats_per_row > 50:
            raise ValueError(
                "Rows must be less than 26 and seats per row must be less than 50.")

    def display_seating_map(self):
        """ Display seating map """
        LETTER_A_ASCII = 65
        rows = self.rows
        seats_per_row = self.seats_per_row
        seating_map = self.seating_map
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
