import util

BASE_API="https://yts.mx/api/v2/"

def main():
    print("Testing start")
    print(list_movies(query_term="The Lost World: Jurassic Park").items())
    print("Testing end")

# List Movies - https://yts.mx/api#list_movies
def list_movies(limit="20", page="1", quality="1080p", minimum_rating="0", query_term="0", genre="all", sort_by="date_added", order_by="desc", with_rt_ratings="false"):
    return util.request(BASE_API+"list_movies.json", "limit=" + str(limit), "page=" + str(page), "quality" + str(quality), "minimum_rating" + str(minimum_rating), "query_term=" + str(query_term), "genre=" + str(genre), "sort_by" + str(sort_by), "order_by=" + str(order_by), "with_rt_ratings=" + str(with_rt_ratings))

# Movie Details - https://yts.mx/api#movie_details
def movie_details(movie_id, with_images="false", with_cast="false"):
    return util.request(BASE_API+"movie_details.json", "movie_id=" + str(movie_id), "with_images=" + str(with_images), "with_cast=" + str(with_cast))

if __name__ == "__main__":
    main()
