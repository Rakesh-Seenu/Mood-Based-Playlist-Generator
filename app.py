from flask import Flask, render_template, request

app = Flask(__name__)

# Predefined playlists for different moods
mood_playlists = {
    "happy": [
        {"title": "Akasha Iste | Galipata ", "link": "https://www.youtube.com/watch?v=HfNtBJSkprk"},
        {"title": "Dwapara Lyrical | Krishnam Pranaya Sakhi", "link": "https://www.youtube.com/watch?v=wiur_AGatGU"},
        {"title": "Googly | Yeno Yeno Aagide", "link": "https://www.youtube.com/watch?v=sWk9lpkGAfs&list=RDwiur_AGatGU&index=5"},
        {"title": "ALL OK | Happy Video", "link": "https://www.youtube.com/watch?v=hRkc-OPHApY&list=RDwiur_AGatGU&index=6"},
        {"title": "Belageddu | Kirik Party", "link": "https://www.youtube.com/watch?v=ebz20FHrT44&list=RDwiur_AGatGU&index=15"}    
    ],
    "sad": [
        {"title": "Googly - Bisilu Kudreyondu", "link": "https://www.youtube.com/watch?v=N4GFIkcp5Wo"},
        {"title": "Sanchariyagu Nee | Love Mocktail 2", "link": "https://www.youtube.com/watch?v=c8xBKXXJeBA"},
        {"title": "Ninadene Januma  | Love Mocktail 2", "link": "https://www.youtube.com/watch?v=mONihsDGNxQ"},
        {"title": "Mugulu nage | Mugulu nage", "link": "https://www.youtube.com/watch?v=D1yAeW2OmDA"},
        {"title": "Noorondu Nenapu  | Bandana", "link": "https://www.youtube.com/watch?v=INngsSMSAlg"}
    ],
    "energetic": [
        {"title": "Vishnuvardhana | One Two Three", "link": "https://www.youtube.com/watch?v=MhVMMcUBsw0&list=RDwiur_AGatGU&index=16"},
        {"title": "Jackie | Jackie Jackie", "link": "https://www.youtube.com/watch?v=9eShOnkYfUg&list=RDwiur_AGatGU&index=18"},
        {"title": "Masterpiece | Annange Love Aagidhe", "link": "https://www.youtube.com/watch?v=rf6-5k9bzmM&list=PLjity7Lwv-zp0qs6_iOGdhNfMnF1A_CJ9"},
        {"title": "Bahadur | Subbalakshmi", "link": "https://www.youtube.com/watch?v=rH8hV4lvonw&list=PLjity7Lwv-zp0qs6_iOGdhNfMnF1A_CJ9&index=17"},
        {"title": "Bahaddur | Starade", "link": "https://www.youtube.com/watch?v=lqMktF1zzwo&list=PLjity7Lwv-zp0qs6_iOGdhNfMnF1A_CJ9&index=18"},
    ],
    "relaxed": [
        {"title": "Betiyada Jaga | Kannadakkagi Ondannu Otti", "link": "https://www.youtube.com/watch?v=EtKXVZOK_3A"},
        {"title": "Mungaru Male 2 | Sariyaagi Nenapide ", "link": "https://www.youtube.com/watch?v=YZhUwHFsCO0&list=RDEtKXVZOK_3A&index=2"},
        {"title": "Usire Usire Song | Huccha", "link": "https://www.youtube.com/watch?v=uMnGO1CAa2E&list=RDEtKXVZOK_3A&index=8"},
        {"title": "Arjuna | Sakhiye Sakhiye", "link": "https://www.youtube.com/watch?v=wcWvllcAhcc&list=RDEtKXVZOK_3A&index=12"},
        {"title": "Smile Ore Smilu | Navagraha", "link": "https://www.youtube.com/watch?v=NIO2hSX6Iuk&list=RDwiur_AGatGU&index=19"},
      ]
}

@app.route("/", methods=["GET", "POST"])
def index():
    playlist = []
    mood = ""
    if request.method == "POST":
        mood = request.form.get("mood").lower()
        if mood in mood_playlists:
            playlist = mood_playlists[mood]
    
    return render_template("index.html", playlist=playlist, mood=mood)

if __name__ == "__main__":
    app.run(debug=True)
