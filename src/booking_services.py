from src.movie_and_seats import MovieAndSeats

class BookingServices:
    def __init__ (self, movie_and_seats: MovieAndSeats, num_of_tickets:int):
        self.num_of_tickets = num_of_tickets
        self.master_seating_map = movie_and_seats.seating_map
        self.target_seating_map = [row[:] for row in self.master_seating_map]

    def find_the_best_seats(self):
        """
            - Start from the furthest row from the screen
            - Start from the middle-most possible col.
            - When a row is not enough to accommodate the number of tickets, it should overflow to the next row closer to the screen
        Returns:
            List[List[str]]: target seating map
        """
        master_seating_map = self.master_seating_map
        target_seating_map = self.target_seating_map
        num_of_tickets = self.num_of_tickets
        rows = len(target_seating_map)
        seating_per_row = len(target_seating_map[0])

        if(num_of_tickets < seating_per_row):
            mid_seat_pos = seating_per_row // 2
            left_seat_start_pos = mid_seat_pos - num_of_tickets // 2
            right_seat_end_pos = mid_seat_pos + num_of_tickets // 2 + (num_of_tickets % 2)

            for current_searching_row in range(rows):
                if all(master_seating_map[current_searching_row][current_sarching_seat] == "•" for current_sarching_seat in range(left_seat_start_pos, right_seat_end_pos)):
                    for current_sarching_seat in range(left_seat_start_pos, right_seat_end_pos):
                        target_seating_map[current_searching_row][current_sarching_seat] = "#"
                    return target_seating_map
