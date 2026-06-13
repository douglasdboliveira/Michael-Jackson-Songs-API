from flask import Flask, request, jsonify

app = Flask(__name__)

songs = [
  { "title": "Don't Stop 'Til You Get Enough", "album": "Off the Wall", "era": "70s", "genre": "funk", "theme": "fun", "impact": "global hit" },
  { "title": "Rock With You", "album": "Off the Wall", "era": "70s", "genre": "disco", "theme": "romance", "impact": "iconic music video" },
  { "title": "Working Day and Night", "album": "Off the Wall", "era": "70s", "genre": "funk", "theme": "fun", "impact": "cult track" },
  { "title": "Get on the Floor", "album": "Off the Wall", "era": "70s", "genre": "funk", "theme": "fun", "impact": "cult track" },
  { "title": "Off the Wall", "album": "Off the Wall", "era": "70s", "genre": "disco", "theme": "self-affirmation", "impact": "cult track" },
  { "title": "Girlfriend", "album": "Off the Wall", "era": "70s", "genre": "pop", "theme": "romance", "impact": "cult track" },
  { "title": "She's Out of My Life", "album": "Off the Wall", "era": "70s", "genre": "ballad", "theme": "romance", "impact": "cult track" },
  { "title": "I Can't Help It", "album": "Off the Wall", "era": "70s", "genre": "soul", "theme": "romance", "impact": "cult track" },
  { "title": "It's the Falling in Love", "album": "Off the Wall", "era": "70s", "genre": "pop", "theme": "romance", "impact": "cult track" },
  { "title": "Burn This Disco Out", "album": "Off the Wall", "era": "70s", "genre": "disco", "theme": "fun", "impact": "cult track" },

  { "title": "Wanna Be Startin' Somethin'", "album": "Thriller", "era": "80s", "genre": "funk", "theme": "fun", "impact": "global hit" },
  { "title": "Baby Be Mine", "album": "Thriller", "era": "80s", "genre": "R&B", "theme": "romance", "impact": "cult track" },
  { "title": "The Girl Is Mine", "album": "Thriller", "era": "80s", "genre": "pop", "theme": "romance", "impact": "collaboration" },
  { "title": "Thriller", "album": "Thriller", "era": "80s", "genre": "pop", "theme": "fun", "impact": "iconic music video" },
  { "title": "Beat It", "album": "Thriller", "era": "80s", "genre": "rock", "theme": "rebellion", "impact": "iconic music video" },
  { "title": "Billie Jean", "album": "Thriller", "era": "80s", "genre": "pop", "theme": "self-affirmation", "impact": "global hit" },
  { "title": "Human Nature", "album": "Thriller", "era": "80s", "genre": "ballad", "theme": "romance", "impact": "cult track" },
  { "title": "P.Y.T. (Pretty Young Thing)", "album": "Thriller", "era": "80s", "genre": "funk", "theme": "romance", "impact": "cult track" },
  { "title": "The Lady in My Life", "album": "Thriller", "era": "80s", "genre": "ballad", "theme": "romance", "impact": "cult track" },

  { "title": "Bad", "album": "Bad", "era": "80s", "genre": "pop", "theme": "self-affirmation", "impact": "global hit" },
  { "title": "The Way You Make Me Feel", "album": "Bad", "era": "80s", "genre": "pop", "theme": "romance", "impact": "iconic music video" },
  { "title": "Speed Demon", "album": "Bad", "era": "80s", "genre": "funk", "theme": "fun", "impact": "cult track" },
  { "title": "Liberian Girl", "album": "Bad", "era": "80s", "genre": "ballad", "theme": "romance", "impact": "cult track" },
  { "title": "Just Good Friends", "album": "Bad", "era": "80s", "genre": "pop", "theme": "romance", "impact": "collaboration" },
  { "title": "Another Part of Me", "album": "Bad", "era": "80s", "genre": "funk", "theme": "fun", "impact": "cult track" },
  { "title": "Man in the Mirror", "album": "Bad", "era": "80s", "genre": "ballad", "theme": "social protest", "impact": "cult track" },
  { "title": "I Just Can't Stop Loving You", "album": "Bad", "era": "80s", "genre": "ballad", "theme": "romance", "impact": "global hit" },
  { "title": "Dirty Diana", "album": "Bad", "era": "80s", "genre": "rock", "theme": "romance", "impact": "global hit" },
  { "title": "Smooth Criminal", "album": "Bad", "era": "80s", "genre": "pop", "theme": "rebellion", "impact": "iconic music video" },
  { "title": "Leave Me Alone", "album": "Bad", "era": "80s", "genre": "pop", "theme": "self-affirmation", "impact": "cult track" },

  { "title": "Jam", "album": "Dangerous", "era": "90s", "genre": "hip hop", "theme": "fun", "impact": "cult track" },
  { "title": "Why You Wanna Trip on Me", "album": "Dangerous", "era": "90s", "genre": "pop", "theme": "rebellion", "impact": "cult track" },
  { "title": "In the Closet", "album": "Dangerous", "era": "90s", "genre": "R&B", "theme": "romance", "impact": "iconic music video" },
  { "title": "She Drives Me Wild", "album": "Dangerous", "era": "90s", "genre": "hip hop", "theme": "romance", "impact": "cult track" },
  { "title": "Remember the Time", "album": "Dangerous", "era": "90s", "genre": "R&B", "theme": "romance", "impact": "iconic music video" },
  { "title": "Can't Let Her Get Away", "album": "Dangerous", "era": "90s", "genre": "funk", "theme": "romance", "impact": "cult track" },
  { "title": "Heal the World", "album": "Dangerous", "era": "90s", "genre": "ballad", "theme": "social protest", "impact": "cult track" },
  { "title": "Black or White", "album": "Dangerous", "era": "90s", "genre": "pop rock", "theme": "social protest", "impact": "iconic music video" },
  { "title": "Who Is It", "album": "Dangerous", "era": "90s", "genre": "R&B", "theme": "romance", "impact": "cult track" },
  { "title": "Give In to Me", "album": "Dangerous", "era": "90s", "genre": "rock", "theme": "romance", "impact": "cult track" },
  { "title": "Will You Be There", "album": "Dangerous", "era": "90s", "genre": "ballad", "theme": "social protest", "impact": "global hit" },
  { "title": "Keep the Faith", "album": "Dangerous", "era": "90s", "genre": "ballad", "theme": "self-affirmation", "impact": "cult track" },
  { "title": "Gone Too Soon", "album": "Dangerous", "era": "90s", "genre": "ballad", "theme": "social protest", "impact": "cult track" },
  { "title": "Dangerous", "album": "Dangerous", "era": "90s", "genre": "pop", "theme": "self-affirmation", "impact": "cult track" },

  { "title": "Scream", "album": "HIStory", "era": "90s", "genre": "pop", "theme": "rebellion", "impact": "collaboration" },
  { "title": "They Don't Care About Us", "album": "HIStory", "era": "90s", "genre": "pop", "theme": "social protest", "impact": "iconic music video" },
  { "title": "Stranger in Moscow", "album": "HIStory", "era": "90s", "genre": "ballad", "theme": "introspection", "impact": "cult track" },
  { "title": "This Time Around", "album": "HIStory", "era": "90s", "genre": "hip hop", "theme": "rebellion", "impact": "cult track" },
  { "title": "Earth Song", "album": "HIStory", "era": "90s", "genre": "ballad", "theme": "social protest", "impact": "cult track" },
  { "title": "D.S.", "album": "HIStory", "era": "90s", "genre": "rock", "theme": "rebellion", "impact": "cult track" },
  { "title": "Money", "album": "HIStory", "era": "90s", "genre": "funk", "theme": "social criticism", "impact": "cult track" },
  { "title": "Come Together", "album": "HIStory", "era": "90s", "genre": "rock", "theme": "fun", "impact": "cover" },
  { "title": "You Are Not Alone", "album": "HIStory", "era": "90s", "genre": "ballad", "theme": "romance", "impact": "global hit" },
  { "title": "Childhood", "album": "HIStory", "era": "90s", "genre": "ballad", "theme": "introspection", "impact": "cult track" },
  { "title": "Tabloid Junkie", "album": "HIStory", "era": "90s", "genre": "pop", "theme": "social criticism", "impact": "cult track" },
  { "title": "2 Bad", "album": "HIStory", "era": "90s", "genre": "hip hop", "theme": "rebellion", "impact": "cult track" },
  { "title": "HIStory", "album": "HIStory", "era": "90s", "genre": "pop", "theme": "self-affirmation", "impact": "cult track" },
  { "title": "Little Susie", "album": "HIStory", "era": "90s", "genre": "ballad", "theme": "drama", "impact": "cult track" },
  { "title": "Smile", "album": "HIStory", "era": "90s", "genre": "ballad", "theme": "hope", "impact": "cover" },

  { "title": "Unbreakable", "album": "Invincible", "era": "2000s", "genre": "R&B", "theme": "self-affirmation", "impact": "cult track" },
  { "title": "Heartbreaker", "album": "Invincible", "era": "2000s", "genre": "hip hop", "theme": "romance", "impact": "cult track" },
  { "title": "Invincible", "album": "Invincible", "era": "2000s", "genre": "pop", "theme": "self-affirmation", "impact": "cult track" },
  { "title": "Break of Dawn", "album": "Invincible", "era": "2000s", "genre": "R&B", "theme": "romance", "impact": "cult track" },
  { "title": "Heaven Can Wait", "album": "Invincible", "era": "2000s", "genre": "R&B", "theme": "romance", "impact": "cult track" },
  { "title": "You Rock My World", "album": "Invincible", "era": "2000s", "genre": "R&B", "theme": "romance", "impact": "iconic music video" },
  { "title": "Butterflies", "album": "Invincible", "era": "2000s", "genre": "R&B", "theme": "romance", "impact": "cult track" },
  { "title": "Speechless", "album": "Invincible", "era": "2000s", "genre": "ballad", "theme": "romance", "impact": "cult track" },
  { "title": "2000 Watts", "album": "Invincible", "era": "2000s", "genre": "hip hop", "theme": "fun", "impact": "cult track" },
  { "title": "You Are My Life", "album": "Invincible", "era": "2000s", "genre": "ballad", "theme": "romance", "impact": "cult track" },
  { "title": "Privacy", "album": "Invincible", "era": "2000s", "genre": "pop", "theme": "social criticism", "impact": "cult track" },
  { "title": "Don't Walk Away", "album": "Invincible", "era": "2000s", "genre": "ballad", "theme": "romance", "impact": "cult track" },
  { "title": "Cry", "album": "Invincible", "era": "2000s", "genre": "ballad", "theme": "social protest", "impact": "cult track" },
  { "title": "The Lost Children", "album": "Invincible", "era": "2000s", "genre": "ballad", "theme": "hope", "impact": "cult track" },
  { "title": "Whatever Happens", "album": "Invincible", "era": "2000s", "genre": "pop rock", "theme": "romance", "impact": "collaboration" },
  { "title": "Threatened", "album": "Invincible", "era": "2000s", "genre": "hip hop", "theme": "fun", "impact": "cult track" }
]

@app.route("/songs", methods=["GET"])
def fetch_songs():
    album = request.args.get("album")
    era = request.args.get("era")
    genre = request.args.get("genre")
    theme = request.args.get("theme")
    impact = request.args.get("impact")

    if not album and not era and not genre and not theme and not impact:
        return jsonify(songs)
    
    if album:
        new_list = [song for song in songs if album.lower() in song["album"].lower()]
        return jsonify(new_list)

    if era:
        new_list = [song for song in songs if era.lower() in song["era"].lower()]
        return jsonify(new_list)

    if genre:
        new_list = [song for song in songs if genre.lower() in song["genre"].lower()]
        return jsonify(new_list)

    if theme:
        new_list = [song for song in songs if theme.lower() in song["theme"].lower()]
        return jsonify(new_list)

    if impact:
        new_list = [song for song in songs if impact.lower() in song["impact"].lower()]
        return jsonify(new_list)

if __name__ == "__main__":
    app.run(debug=True)