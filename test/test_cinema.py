from src.constants import *
from src.movie_and_seats import MovieAndSeats
from src.booking_services import BookingServices

def test_movie_and_seats_creation():
    movie_and_seats = MovieAndSeats("The Matrix", 10, 10)
    assert movie_and_seats.title == "The Matrix"
    assert movie_and_seats.rows == 10
    assert movie_and_seats.seats_per_row == 10
    assert movie_and_seats.total_seats == 100
    assert movie_and_seats.available_seats == 100
    assert movie_and_seats.seating_map == [
        [AVAILABLE_SEAT_MARK for _ in range(10)] for _ in range(10)]

def test_invalid_rows_and_seats_per_row():
    try:
        MovieAndSeats("The Matrix", MAX_ROWS+1, MAX_SEATS_PER_ROW+1)
    except ValueError as e:
        assert str(e) == f"Rows must be less than {MAX_ROWS} and seats per row must be less than {MAX_SEATS_PER_ROW}."

def test_find_the_best_seats_case_one():
    movie_and_seats = MovieAndSeats("The Matrix", 10, 10)
    booking_services = BookingServices(movie_and_seats, 5, movie_and_seats.seating_map)
    best_seats = booking_services.find_the_best_seats()
    print(best_seats)
    assert best_seats == [(0, 4), (0, 5), (0, 6), (0, 3), (0, 7)]