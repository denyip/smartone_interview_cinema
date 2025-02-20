from src.movie_and_seats import MovieAndSeats

class BookingServices:
    def __init__ (self, movie_and_seats: MovieAndSeats, num_of_tickets:int):
        self.movie_and_seats = movie_and_seats
        self.num_of_tickets = num_of_tickets
        self.master_seating_map = movie_and_seats.master_seating_map
        self.target_seating_map = movie_and_seats.target_seating_map
        self.rows = movie_and_seats.rows
        self.seats_per_row = movie_and_seats.seats_per_row

    def find_the_best_seats(self):
        master_seating_map = self.master_seating_map
        target_seating_map = self.target_seating_map
        num_of_tickets = self.num_of_tickets
        rows = self
        seating_per_row = self.seats_per_row

        if(num_of_tickets < seating_per_row):
            mid_seat_pos = seating_per_row // 2
            left_seat_start_pos = mid_seat_pos - num_of_tickets // 2
            right_seat_end_pos = mid_seat_pos + num_of_tickets // 2 + (num_of_tickets % 2)

            for current_searching_row in range(rows-1, -1, -1):
                if all(master_seating_map[current_searching_row][current_sarching_seat] == "•" for current_sarching_seat in range(left_seat_start_pos, right_seat_end_pos))
                    for current_sarching_seat in range(left_seat_start_pos, right_seat_end_pos):
                        target_seating_map[current_searching_row][current_sarching_seat] = "#"
                        