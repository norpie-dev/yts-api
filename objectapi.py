import webapi

def main():
    print("Main - Start")
    print(list_movies(query_term="tt0119567").genres)
    print("Main - Stop")

class Torrent:
    def __init__(self, url, hash, quality, type, size, size_bytes):
        self.url = url 
        self.hash = hash 
        self.quality = quality 
        self.type = type 
        self.size_colloquial = size 
        self.size_bytes = size_bytes

class Movie:
    def __init__(self, movie_json):
        # Codes
        self.id = movie_json["id"]
        self.url = movie_json["url"]
        self.imdb_code = movie_json["imdb_code"]
        # Data
        self.mpa_rating = movie_json["mpa_rating"]
        self.rating = movie_json["rating"]
        self.year = movie_json["year"]
        self.runtime = movie_json["runtime"]
        # Genres parsing
        self.genres = movie_json["genres"]
        # Text
        self.title = movie_json["title"]
        self.title_long = movie_json["title_long"]
        self.slug = movie_json["slug"]
        self.summary = movie_json["summary"]
        self.description = movie_json["description_full"]
        self.synopsis = movie_json["synopsis"]
        # Images
        self.yt_trailer_url = "https://www.youtube.com/watch?v=" + movie_json["yt_trailer_code"]
        self.background_image = movie_json["background_image"]
        self.background_image_original = movie_json["background_image_original"]
        self.small_cover_image = movie_json["small_cover_image"]
        self.medium_cover_image = movie_json["medium_cover_image"]
        self.large_cover_image = movie_json["large_cover_image"]
        # Torrents parsing
        self.torrents = []
        for torrent_json in movie_json["torrents"]:
            self.torrents.append(Torrent(torrent_json["url"], torrent_json["hash"], torrent_json["quality"], \
                    torrent_json["type"], torrent_json["size"], torrent_json["size_bytes"]))
            


# List Movies - https://yts.mx/api#list_movies
def list_movies(limit="20", page="1", quality="1080p", minimum_rating="0", query_term="0", \
        genre="all", sort_by="date_added", order_by="desc", with_rt_ratings="false"):
    json = webapi.list_movies(limit=limit, page=page, quality=quality, minimum_rating=minimum_rating, \
        query_term=query_term, genre=genre, sort_by=sort_by, order_by=order_by, with_rt_ratings=with_rt_ratings)
    movie_json = json["data"]["movies"][0]
    return Movie(movie_json)

# Movie Details - https://yts.mx/api#movie_details
def movie_details(movie_id, with_images="false", with_cast="false"):
    json = webapi.movie_details(movie_id=movie_id, with_images=with_images, with_cast=with_cast)

if __name__ == "__main__":
    main() 
