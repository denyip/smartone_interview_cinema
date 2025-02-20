from src.user_interface import UserInterface
from src.movie_and_seats import MovieAndSeats
from src.booking_services import BookingServices

def main():
    ui = UserInterface()
    movie_and_seats = ui.get_movie_and_seats()
    # movie_title, rows, seats_per_row = ui.get_movie_and_seats()
    # movie_and_seats = MovieAndSeats(movie_title, rows, seats_per_row)
    print(f"Movie title: {movie_and_seats.title}, Rows: {movie_and_seats.rows}, Seats per row: {movie_and_seats.seats_per_row}")
    ui.main_menu(movie_and_seats)
    
if __name__ == "__main__":
    main()