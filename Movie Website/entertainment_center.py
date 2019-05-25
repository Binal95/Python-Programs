import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/4/4c/Toy_Story_4_poster.jpg",
                        "https://www.youtube.com/watch?v=Pl9JS8-gnWQ")
#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/sco/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=6ziBFh3V1aM")
#print(avatar.storyline)
#avatar.show_trailer()

fast_Furious= media.Movie("Fast and Furious",
                     "Film focused on racing, and culminated in the standalone film ",
                     "https://upload.wikimedia.org/wikipedia/en/2/2d/The_Fate_of_The_Furious_Theatrical_Poster.jpg",
                     "https://www.youtube.com/watch?v=HZ7PAyCDwEg")

movies = [toy_story,avatar,fast_Furious]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS )
#print(media.Movie.__doc__)
