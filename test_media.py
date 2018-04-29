import media
import fresh_tomatoes

a_quiet_place = media.Movie("A Quiet Place",
                        "A family is forced to live in silence while hiding from creatures that hunt by sound.",
                        "https://upload.wikimedia.org/wikipedia/en/a/a0/A_Quiet_Place_film_poster.png",
                        "https://www.youtube.com/watch?v=WR7cc5t7tv8")

avengers_infinity_war = media.Movie("Avengers: Infinity War",
                       "The Avengers and their allies must be willing to sacrifice all in an attempt to defeat the powerful Thanos before his blitz of devastation and ruin puts an end to the universe.",
                       "https://upload.wikimedia.org/wikipedia/fi/9/90/Avengers_Infinity_War.jpg",
                       "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

rampage = media.Movie("Rampage",
                      "When three different animals become infected with a dangerous pathogen, a primatologist and a geneticist team up to stop them from destroying Chicago.",
                      "https://upload.wikimedia.org/wikipedia/en/6/6b/Rampage_teaser_film_poster.jpg",
                      "https://www.youtube.com/watch?v=coOKvrsmQiI")

doctor_strange = media.Movie("Doctor Strange",
                             "While on a journey of physical and spiritual healing, a brilliant neurosurgeon is drawn into the world of the mystic arts.",
                             "https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg",
                            "https://www.youtube.com/watch?v=HSzx-zryEgM")

black_panther = media.Movie("Black Panther",
                       "T'Challa, the King of Wakanda, rises to the throne in the isolated, technologically advanced African nation, but his claim is challenged by a vengeful outsider who was a childhood victim of T'Challa's father's mistake.",
                       "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg",
                       "https://www.youtube.com/watch?v=xjDjIWPwcPU")

thor_ragnarok = media.Movie("Thor: Ragnarok",
                       "Thor is imprisoned on the planet Sakaar, and must race against time to return to Asgard and stop Ragnarök, the destruction of his world, which is at the hands of the powerful and ruthless villain Hela.",
                       "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg",
                       "https://www.youtube.com/watch?v=ue80QwXMRHg")


movies = [a_quiet_place, avengers_infinity_war, rampage, doctor_strange, black_panther, thor_ragnarok]
fresh_tomatoes.open_movies_page(movies)
