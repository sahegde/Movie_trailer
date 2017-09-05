"""Stores details of movies and displays them on a website."""
import fresh_tomatoes
import media

def main():
    """Creates six Movie objects, initialising these objects with title, storyline,
    poster image link, video trailer link and release date."""
    aake = media.Movie("Aake",
                          "https://upload.wikimedia.org/wikipedia/commons/3/3f/Aake.jpg",
                          "https://www.youtube.com/watch?v=lhRdOQWCdRU")

    rajvishnu = media.Movie("Rajvishnu",
                          "https://upload.wikimedia.org/wikipedia/commons/a/a5/Rajvishnu.jpg",
                          "https://www.youtube.com/watch?v=4hIZjLI5KZ8")

    kariya = media.Movie("Kariya",
                           "https://upload.wikimedia.org/wikipedia/commons/1/1e/Kariya.jpg",
                           "https://www.youtube.com/watch?v=fsR7OnXOd-M")

    maastigudi = media.Movie("Maastigudi",
                         "https://upload.wikimedia.org/wikipedia/commons/a/a1/Maastigudi.jpg",
                         "https://www.youtube.com/watch?v=gT3LXzzGf2A")

    leader = media.Movie("Leader",
                           "https://upload.wikimedia.org/wikipedia/commons/1/1d/Leader.jpg",
                           "https://www.youtube.com/watch?v=v5vFAw_tTok&t=28s")

    rajakumara = media.Movie("Rajakumara",
                          "https://upload.wikimedia.org/wikipedia/commons/0/0c/Rajakumara.jpg",
                          "https://www.youtube.com/watch?v=q9Yh9HcOmlo")

    # Store the Movie objects in a list.
    movies = [aake, rajvishnu, kariya, maastigudi, leader, rajakumara]

    # Open the movie website in the user's browser, featuring the movies above.
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
