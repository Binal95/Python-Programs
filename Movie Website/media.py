import webbrowser

class Movie():
    """This class provides a way to store movie related information"""
    
    VALID_RATINGS = ["G","PG","PG-13", "R"]
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline= movie_storyline  #if write only storyline= movie_storyline then storyline becomes local varaible not an instance varialbe
        #(instance variable are those those have different values for different object such as here title, storyline, umage, trailer all instace variable a
        #as they have different values for toystory and avatar objects)
        self.poster_image_url= poster_image
        self.trailer_youtube_url=trailer_youtube
        
    def  show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
    
#https://google.github.io/styleguide/pyguide.html how to give name to class, function etc in python
