from texttospeech import texttospeechf 
import imdb 
  
def movie_review(name):

    ia = imdb.IMDb() 
  
    search = ia.search_movie(name) 
  
    if(search):
        id=search[0].getID()

        movie=ia.get_movie(id)

        texttospeechf("Movie Review")
        texttospeechf(f"{movie['title']} - {movie['year']}")
        texttospeechf(f"ratings : {movie['rating']}")

        directors=movie['directors']
        casting=movie['cast']

        directors=' and '.join(map(str,directors))
        casting=" , ".join(map(str,casting[0:7]))
        
        texttospeechf(f"Directors:{directors}")
        texttospeechf(f"actors : {casting} and some more")


def actors(name):
    ia = imdb.IMDb() 
  
    search = ia.search_movie(name) 
  
    if(search):
        id=search[0].getID()

        movie=ia.get_movie(id)

        casting=movie['cast']
        casting=" , ".join(map(str,casting[0:]))
        
        texttospeechf(f"actors : {casting} ")



