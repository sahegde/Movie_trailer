"""Stores details of movies and displays them on a website."""
import fresh_tomatoes
import media


def main():
    """Creates six Movie objects, initialising these objects with title, storyline,
    poster image link, video trailer link and release date."""
    aake = media.Movie(
                        "Aake",
                        "https://i.ytimg.com/vi/lhRdOQWCdRU/maxresdefault.jpg",
                        "https://www.youtube.com/watch?v=lhRdOQWCdRU"
                      )

    rajvishnu = media.Movie(
                            "Rajvishnu",
                            "https://goo.gl/ZyDgeR",
                            "https://www.youtube.com/watch?v=4hIZjLI5KZ8"
                            )

    kariya = media.Movie(
                          "Kariya",
                          "https://goo.gl/kCbMj3",
                          "https://www.youtube.com/watch?v=fsR7OnXOd-M"
                        )

    maastigudi = media.Movie(
                              "Maastigudi",
                              "https://goo.gl/z1ypAz",
                              "https://www.youtube.com/watch?v=gT3LXzzGf2A"
                            )

    leader = media.Movie(
                          "Leader",
                          "https://goo.gl/JRspr6",
                          "https://www.youtube.com/watch?v=v5vFAw_tTok&t=28s"
                        )

    rajakumara = media.Movie(
                              "Rajakumara",
                              "https://goo.gl/NAe6f3",
                              "https://www.youtube.com/watch?v=q9Yh9HcOmlo"
                             )

    # Store the Movie objects in a list.
    movies = [aake, rajvishnu, kariya, maastigudi, leader, rajakumara]

    # Open the movie website in the user's browser, featuring the movies above.
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
