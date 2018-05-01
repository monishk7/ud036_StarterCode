import media
import fresh_tomatoes

a_quiet_place = media.Movie("A Quiet Place",
                            "A family is forced to live in silence.",
                            "https://upload.wikimedia.org/wikipedia/en"
                            "/a/a0/A_Quiet_Place_film_poster.png",
                            "https://www.youtube.com/watch?v=WR7cc5t7tv8")

avengers = media.Movie("Avengers: Infinity War",
                       "The Avengers fights Thanos.",
                       "https://upload.wikimedia.org/wikipedia"
                       "/fi/9/90/Avengers_Infinity_War.jpg",
                       "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

rampage = media.Movie("Rampage",
                      "Hero fights to save the city",
                      "https://upload.wikimedia.org/wikipedia/"
                      "en/6/6b/Rampage_teaser_film_poster.jpg",
                      "https://www.youtube.com/watch?v=coOKvrsmQiI")

doctor_strange = media.Movie("Doctor Strange",
                             "On a journey of spiritual healing,"
                             " Dr. Strange learns magic.",
                             "https://upload.wikimedia.org/wikipedia/"
                             "en/c/c7/Doctor_Strange_poster.jpg",
                             "https://www.youtube.com/watch?v=HSzx-zryEgM")

black_panther = media.Movie("Black Panther",
                            "T'Challa fights his brother to become king",
                            "https://upload.wikimedia.org/wikipedia/en/0"
                            "/0c/Black_Panther_film_poster.jpg",
                            "https://www.youtube.com/watch?v=xjDjIWPwcPU")

thor_ragnarok = media.Movie("Thor: Ragnarok",
                            "Thor fights with powerful villain Hela.",
                            "https://upload.wikimedia.org/wikipedia/en/7/7d/"
                            "Thor_Ragnarok_poster.jpg",
                            "https://www.youtube.com/watch?v=ue80QwXMRHg")


movies = [a_quiet_place, avengers, rampage,
          doctor_strange, black_panther, thor_ragnarok]
fresh_tomatoes.open_movies_page(movies)
