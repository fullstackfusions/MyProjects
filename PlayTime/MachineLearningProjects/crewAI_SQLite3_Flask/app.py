from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_game_score(team_name):
    conn = sqlite3.connect('nba_games.db')
    c = conn.cursor()
    team_name = team_name.lower()
    c.execute('SELECT * FROM games WHERE team_name = ?', (team_name,))
    result = c.fetchone()
    conn.close()
    if result:
        keys = ["game_id", "status", "home_team", "home_team_score", "away_team", "away_team_score"]
        return dict(zip(keys, result[1:]))
    else:
        return {"team_name": team_name, "score": "unknown"}

@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to the NBA Scores API. Use /score?team=<team_name> to fetch game scores.'
    })

@app.route('/score', methods=['GET'])
def score():
    team_name = request.args.get('team', '')
    print(f"\n\n\n\n\nteam_name: {team_name}\n\n\n\n\n\n")
    if not team_name:
        return jsonify({'error': 'Missing team name'}), 400
    score = get_game_score(team_name)
    return jsonify(score)

if __name__ == '__main__':
    app.run(debug=True)