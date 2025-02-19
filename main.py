from src.user_interface import UserInterface

def main():
    ui = UserInterface()
    movie_title, rows, seats_per_row = ui.get_movie_and_seats()
    print(f"Movie title: {movie_title}, Rows: {rows}, Seats per row: {seats_per_row}")
    ui.main_menu(movie_title, rows * seats_per_row)
    
if __name__ == "__main__":
    main()