import requests
import json
import random

api_key = "593ee0e026916046ec2bd64276f49d06"


genre = """ Aksiyon - 28
            Macera - 12
            Animasyon - 16
            Komedi - 35
            Suç - 80",
            Belgesel - 99
            Dram - 18
            Aile - 10751
            Fantastik - 14
            Tarihi - 36
            Korku - 27
            Müzikal - 10402
            Gizem - 9648
            Romantik - 10749
            Bilim Kurgu - 878
            Gerilim - 53
            Savaş - 10752"""
print(genre)

genre_id = input("Hangi türde bir film önerisi istersiniz? (Tür ID'si girin): ")




url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_genres={genre_id}"
response = requests.get(url)
data = json.loads(response.text)


if not data['results']:
    print("Belirtilen türde film bulunamadı.")
else:

    movie = random.choice(data['results'])
    title = movie['title']
    release_date = movie['release_date']
    overview = movie['overview']
    poster_path = movie['poster_path']
    print(f"Size önerimiz: {title} ({release_date})")
    print(overview)
    print(f"Poster URL: https://image.tmdb.org/t/p/original{poster_path}")
