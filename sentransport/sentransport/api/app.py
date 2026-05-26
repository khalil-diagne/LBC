from flask import request
import json
from pathlib import Path
from flask import Flask, jsonify
from flask_cors import CORS

app=Flask(__name__)
CORS(app)
# Charger les données des lignes de bus DDD à partir du fichier JSON
data_path = Path(__file__).with_name("lignes_DDD.json")
with open(data_path, 'r') as f:
    lignes=json.load(f)

@app.route("/")
def accueil():
    return jsonify({"message": "Bienvenue sur l'API de Sentransport!", "endpoint": ["/lignes", "/lignes/<int:ligne_id>"]})

@app.route("/lignes")
def get_lignes():
    return jsonify(lignes)

@app.route("/lignes/<int:ligne_id>")
def get_ligne(ligne_id):
    ligne = next((l for l in lignes if l["id"] == ligne_id), None)
    if ligne is None:
        return jsonify({"error": "Ligne non trouvée"}), 404
    return jsonify(ligne)

@app.route("/arrets")
def get_arrets():
    tous = set()
    for ligne in lignes:
        for arret in ligne["listeArrets"]:
            tous.add(arret)
    return jsonify(list(tous))


@app.route("/stats")
def get_stats():
    total_lignes = len(lignes)
    total_arrets = sum(l["arrets"] for l in lignes)
    max_ligne = max(lignes, key=lambda l: l["arrets"])
    return jsonify({
        "total_lignes": total_lignes,
        "total_arrets": total_arrets,
        "ligne_max_arrets": max_ligne["numero"]
    })


@app.route("/lignes/recherche")
def recherche_lignes():
    q = request.args.get("q","").lower()
    resultats = [
        l for l in lignes
        if q in l["depart"].lower() or q in l["arrive"].lower()
    ]
    return jsonify(resultats)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
