import sqlite3

def create_db():
    conn = sqlite3.connect('nba_games.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS games (
            team_name TEXT,
            game_id TEXT,
            status TEXT,
            home_team TEXT,
            home_team_score INTEGER,
            away_team TEXT,
            away_team_score INTEGER
        )
    ''')
    games = [
        ("warriors", "401585601", "Final", "Los Angeles Lakers", 121, "Golden State Warriors", 128),
        ("lakers", "401585601", "Final", "Los Angeles Lakers", 121, "Golden State Warriors", 128),
        ("nuggets", "401585577", "Final", "Miami Heat", 88, "Denver Nuggets", 100),
        ("heat", "401585577", "Final", "Miami Heat", 88, "Denver Nuggets", 100)
    ]
    c.executemany('INSERT INTO games (team_name, game_id, status, home_team, home_team_score, away_team, away_team_score) VALUES (?, ?, ?, ?, ?, ?, ?)', games)
    conn.commit()
    conn.close()

create_db()