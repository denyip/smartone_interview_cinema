from src.user_interface import UserInterface
from src.movie_and_seats import MovieAndSeats
from src.booking_services import BookingServices

def main():
    ui = UserInterface()
    ui.get_movie_and_seats()
    ui.main_menu()

if __name__ == "__main__":
    main()