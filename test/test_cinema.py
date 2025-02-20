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
        ["•" for _ in range(10)] for _ in range(10)]

def test_invalid_rows_and_seats_per_row():
    try:
        MovieAndSeats("The Matrix", 26, 50)
    except ValueError as e:
        assert str(e) == "Rows must be less than 26 and seats per row must be less than 50."

def test_find_the_best_seats_case_one():
    movie_and_seats = MovieAndSeats("The Matrix", 10, 10)
    booking_services = BookingServices(movie_and_seats, 5)
    best_seats = booking_services.find_the_best_seats()
    target_seating_map = [
        ["•" for _ in range(10)] for _ in range(10)]
    for i in range(5):
        target_seating_map[0][i+3] = "#"
    assert best_seats == target_seating_map