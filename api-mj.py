from flask import Flask, request, jsonify

app = Flask(__name__)

musicas = [
  { "titulo": "Don't Stop 'Til You Get Enough", "album": "Off the Wall", "epoca": "Anos 70", "estilo": "funk", "tema": "diversão", "impacto": "hit mundial" },
  { "titulo": "Rock With You", "album": "Off the Wall", "epoca": "Anos 70", "estilo": "disco", "tema": "romance", "impacto": "clipe icônico" },
  { "titulo": "Working Day and Night", "album": "Off the Wall", "epoca": "Anos 70", "estilo": "funk", "tema": "diversão", "impacto": "faixa cult" },
  { "titulo": "Get on the Floor", "album": "Off the Wall", "epoca": "Anos 70", "estilo": "funk", "tema": "diversão", "impacto": "faixa cult" },
  { "titulo": "Off the Wall", "album": "Off the Wall", "epoca": "Anos 70", "estilo": "disco", "tema": "autoafirmação", "impacto": "faixa cult" },
  { "titulo": "Girlfriend", "album": "Off the Wall", "epoca": "Anos 70", "estilo": "pop", "tema": "romance", "impacto": "faixa cult" },
  { "titulo": "She's Out of My Life", "album": "Off the Wall", "epoca": "Anos 70", "estilo": "balada", "tema": "romance", "impacto": "faixa cult" },
  { "titulo": "I Can't Help It", "album": "Off the Wall", "epoca": "Anos 70", "estilo": "soul", "tema": "romance", "impacto": "faixa cult" },
  { "titulo": "It's the Falling in Love", "album": "Off the Wall", "epoca": "Anos 70", "estilo": "pop", "tema": "romance", "impacto": "faixa cult" },
  { "titulo": "Burn This Disco Out", "album": "Off the Wall", "epoca": "Anos 70", "estilo": "disco", "tema": "diversão", "impacto": "faixa cult" },

  { "titulo": "Wanna Be Startin' Somethin'", "album": "Thriller", "epoca": "Anos 80", "estilo": "funk", "tema": "diversão", "impacto": "hit mundial" },
  { "titulo": "Baby Be Mine", "album": "Thriller", "epoca": "Anos 80", "estilo": "R&B", "tema": "romance", "impacto": "faixa cult" },
  { "titulo": "The Girl Is Mine", "album": "Thriller", "epoca": "Anos 80", "estilo": "pop", "tema": "romance", "impacto": "colaboração" },
  { "titulo": "Thriller", "album": "Thriller", "epoca": "Anos 80", "estilo": "pop", "tema": "diversão", "impacto": "clipe icônico" },
  { "titulo": "Beat It", "album": "Thriller", "epoca": "Anos 80", "estilo": "rock", "tema": "rebeldia", "impacto": "clipe icônico" },
  { "titulo": "Billie Jean", "album": "Thriller", "epoca": "Anos 80", "estilo": "pop", "tema": "autoafirmação", "impacto": "hit mundial" },
  { "titulo": "Human Nature", "album": "Thriller", "epoca": "Anos 80", "estilo": "balada", "tema": "romance", "impacto": "faixa cult" },
  { "titulo": "P.Y.T. (Pretty Young Thing)", "album": "Thriller", "epoca": "Anos 80", "estilo": "funk", "tema": "romance", "impacto": "faixa cult" },
  { "titulo": "The Lady in My Life", "album": "Thriller", "epoca": "Anos 80", "estilo": "balada", "tema": "romance", "impacto": "faixa cult" },

  { "titulo": "Bad", "album": "Bad", "epoca": "Anos 80", "estilo": "pop", "tema": "autoafirmação", "impacto": "hit mundial" },
  { "titulo": "The Way You Make Me Feel", "album": "Bad", "epoca": "Anos 80", "estilo": "pop", "tema": "romance", "impacto": "clipe icônico" },
  { "titulo": "Speed Demon", "album": "Bad", "epoca": "Anos 80", "estilo": "funk", "tema": "diversão", "impacto": "faixa cult" },
  { "titulo": "Liberian Girl", "album": "Bad", "epoca": "Anos 80", "estilo": "balada", "tema": "romance", "impacto": "faixa cult" },
  { "titulo": "Just Good Friends", "album": "Bad", "epoca": "Anos 80", "estilo": "pop", "tema": "romance", "impacto": "colaboração" },
  { "titulo": "Another Part of Me", "album": "Bad", "epoca": "Anos 80", "estilo": "funk", "tema": "diversão", "impacto": "faixa cult" },
  { "titulo": "Man in the Mirror", "album": "Bad", "epoca": "Anos 80", "estilo": "balada", "tema": "protesto social", "impacto": "faixa cult" },
  { "titulo": "I Just Can't Stop Loving You", "album": "Bad", "epoca": "Anos 80", "estilo": "balada", "tema": "romance", "impacto": "hit mundial" },
  { "titulo": "Dirty Diana", "album": "Bad", "epoca": "Anos 80", "estilo": "rock", "tema": "romance", "impacto": "hit mundial" },
  { "titulo": "Smooth Criminal", "album": "Bad", "epoca": "Anos 80", "estilo": "pop", "tema": "rebeldia", "impacto": "clipe icônico" },
  { "titulo": "Leave Me Alone", "album": "Bad", "epoca": "Anos 80", "estilo": "pop", "tema": "autoafirmação", "impacto": "faixa cult" },

  { "titulo": "Jam", "album": "Dangerous", "epoca": "Anos 90", "estilo": "hip hop", "tema": "diversão", "impacto": "faixa cult" },
  { "titulo": "Why You Wanna Trip on Me", "album": "Dangerous", "epoca": "Anos 90", "estilo": "pop", "tema": "rebeldia", "impacto": "faixa cult" },
  { "titulo": "In the Closet", "album": "Dangerous", "epoca": "Anos 90", "estilo": "R&B", "tema": "romance", "impacto": "clipe icônico" },
  { "titulo": "She Drives Me Wild", "album": "Dangerous", "epoca": "Anos 90", "estilo": "hip hop", "tema": "romance", "impacto": "faixa cult" },
  { "titulo": "Remember the Time", "album": "Dangerous", "epoca": "Anos 90", "estilo": "R&B", "tema": "romance", "impacto": "clipe icônico" },
  { "titulo": "Can't Let Her Get Away", "album": "Dangerous", "epoca": "Anos 90", "estilo": "funk", "tema": "romance", "impacto": "faixa cult" },
  { "titulo": "Heal the World", "album": "Dangerous", "epoca": "Anos 90", "estilo": "balada", "tema": "protesto social", "impacto": "faixa cult" },
  { "titulo": "Black or White", "album": "Dangerous", "epoca": "Anos 90", "estilo": "pop rock", "tema": "protesto social", "impacto": "clipe icônico" },
  { "titulo": "Who Is It", "album": "Dangerous", "epoca": "Anos 90", "estilo": "R&B", "tema": "romance", "impacto": "faixa cult" },
  { "titulo": "Give In to Me", "album": "Dangerous", "epoca": "Anos 90", "estilo": "rock", "tema": "romance", "impacto": "faixa cult" },
  { "titulo": "Will You Be There", "album": "Dangerous", "epoca": "Anos 90", "estilo": "balada", "tema": "protesto social", "impacto": "hit mundial" },
  { "titulo": "Keep the Faith", "album": "Dangerous", "epoca": "Anos 90", "estilo": "balada", "tema": "autoafirmação", "impacto": "faixa cult" },
  { "titulo": "Gone Too Soon", "album": "Dangerous", "epoca": "Anos 90", "estilo": "balada", "tema": "protesto social", "impacto": "faixa cult" },
  { "titulo": "Dangerous", "album": "Dangerous", "epoca": "Anos 90", "estilo": "pop", "tema": "autoafirmação", "impacto": "faixa cult" },

{ "titulo": "Scream", "album": "HIStory", "epoca": "Anos 90", "estilo": "pop", "tema": "rebeldia", "impacto": "colaboração" },
  { "titulo": "They Don't Care About Us", "album": "HIStory", "epoca": "Anos 90", "estilo": "pop", "tema": "protesto social", "impacto": "clipe icônico" },
  { "titulo": "Stranger in Moscow", "album": "HIStory", "epoca": "Anos 90", "estilo": "balada", "tema": "introspecção", "impacto": "faixa cult" },
  { "titulo": "This Time Around", "album": "HIStory", "epoca": "Anos 90", "estilo": "hip hop", "tema": "rebeldia", "impacto": "faixa cult" },
  { "titulo": "Earth Song", "album": "HIStory", "epoca": "Anos 90", "estilo": "balada", "tema": "protesto social", "impacto": "faixa cult" },
  { "titulo": "D.S.", "album": "HIStory", "epoca": "Anos 90", "estilo": "rock", "tema": "rebeldia", "impacto": "faixa cult" },
  { "titulo": "Money", "album": "HIStory", "epoca": "Anos 90", "estilo": "funk", "tema": "crítica social", "impacto": "faixa cult" },
  { "titulo": "Come Together", "album": "HIStory", "epoca": "Anos 90", "estilo": "rock", "tema": "diversão", "impacto": "cover" },
  { "titulo": "You Are Not Alone", "album": "HIStory", "epoca": "Anos 90", "estilo": "balada", "tema": "romance", "impacto": "hit mundial" },
  { "titulo": "Childhood", "album": "HIStory", "epoca": "Anos 90", "estilo": "balada", "tema": "introspecção", "impacto": "faixa cult" },
  { "titulo": "Tabloid Junkie", "album": "HIStory", "epoca": "Anos 90", "estilo": "pop", "tema": "crítica social", "impacto": "faixa cult" },
  { "titulo": "2 Bad", "album": "HIStory", "epoca": "Anos 90", "estilo": "hip hop", "tema": "rebeldia", "impacto": "faixa cult" },
  { "titulo": "HIStory", "album": "HIStory", "epoca": "Anos 90", "estilo": "pop", "tema": "autoafirmação", "impacto": "faixa cult" },
  { "titulo": "Little Susie", "album": "HIStory", "epoca": "Anos 90", "estilo": "balada", "tema": "drama", "impacto": "faixa cult" },
  { "titulo": "Smile", "album": "HIStory", "epoca": "Anos 90", "estilo": "balada", "tema": "esperança", "impacto": "cover" },

  { "titulo": "Unbreakable", "album": "Invincible", "epoca": "Anos 2000", "estilo": "R&B", "tema": "autoafirmação", "impacto": "faixa cult" },
  { "titulo": "Heartbreaker", "album": "Invincible", "epoca": "Anos 2000", "estilo": "hip hop", "tema": "romance", "impacto": "faixa cult" },
  { "titulo": "Invincible", "album": "Invincible", "epoca": "Anos 2000", "estilo": "pop", "tema": "autoafirmação", "impacto": "faixa cult" },
  { "titulo": "Break of Dawn", "album": "Invincible", "epoca": "Anos 2000", "estilo": "R&B", "tema": "romance", "impacto": "faixa cult" },
  { "titulo": "Heaven Can Wait", "album": "Invincible", "epoca": "Anos 2000", "estilo": "R&B", "tema": "romance", "impacto": "faixa cult" },
  { "titulo": "You Rock My World", "album": "Invincible", "epoca": "Anos 2000", "estilo": "R&B", "tema": "romance", "impacto": "clipe icônico" },
  { "titulo": "Butterflies", "album": "Invincible", "epoca": "Anos 2000", "estilo": "R&B", "tema": "romance", "impacto": "faixa cult" },
  { "titulo": "Speechless", "album": "Invincible", "epoca": "Anos 2000", "estilo": "balada", "tema": "romance", "impacto": "faixa cult" },
  { "titulo": "2000 Watts", "album": "Invincible", "epoca": "Anos 2000", "estilo": "hip hop", "tema": "diversão", "impacto": "faixa cult" },
  { "titulo": "You Are My Life", "album": "Invincible", "epoca": "Anos 2000", "estilo": "balada", "tema": "romance", "impacto": "faixa cult" },
  { "titulo": "Privacy", "album": "Invincible", "epoca": "Anos 2000", "estilo": "pop", "tema": "crítica social", "impacto": "faixa cult" },
  { "titulo": "Don't Walk Away", "album": "Invincible", "epoca": "Anos 2000", "estilo": "balada", "tema": "romance", "impacto": "faixa cult" },
  { "titulo": "Cry", "album": "Invincible", "epoca": "Anos 2000", "estilo": "balada", "tema": "protesto social", "impacto": "faixa cult" },
  { "titulo": "The Lost Children", "album": "Invincible", "epoca": "Anos 2000", "estilo": "balada", "tema": "esperança", "impacto": "faixa cult" },
  { "titulo": "Whatever Happens", "album": "Invincible", "epoca": "Anos 2000", "estilo": "pop rock", "tema": "romance", "impacto": "colaboração" },
  { "titulo": "Threatened", "album": "Invincible", "epoca": "Anos 2000", "estilo": "hip hop", "tema": "diversão", "impacto": "faixa cult" }
]

@app.route("/musicas", methods=["GET"])
def buscar_musicas():
    album = request.args.get("album")
    epoca = request.args.get("epoca")
    estilo = request.args.get("estilo")
    tema = request.args.get("tema")
    impacto = request.args.get("impacto")

    if not album and not epoca and not estilo and not tema and not impacto:
        return jsonify(musicas)
    
    if album:
        nova_lista = [musica for musica in musicas if album.lower() in musica["album"].lower()]
        return jsonify(nova_lista)

    if epoca:
        nova_lista = [musica for musica in musicas if epoca.lower() in musica["epoca"].lower()]
        return jsonify(nova_lista)

    if estilo:
        nova_lista = [musica for musica in musicas if estilo.lower() in musica["estilo"].lower()]
        return jsonify(nova_lista)

    if tema:
        nova_lista = [musica for musica in musicas if tema.lower() in musica["tema"].lower()]
        return jsonify(nova_lista)

    if impacto:
        nova_lista = [musica for musica in musicas if impacto.lower() in musica["impacto"].lower()]
        return jsonify(nova_lista)

if __name__ == "__main__":
    app.run(debug=True)