import sqlite3

# データベースの初期化
conn = sqlite3.connect('watch_history.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS watch_history
             (user_id INTEGER, video_id INTEGER, watched_at TIMESTAMP)''')
conn.commit()
conn.close()

# 動画を視聴したときの処理
def log_watch_history(user_id, video_id):
    conn = sqlite3.connect('watch_history.db')
    c = conn.cursor()
    c.execute("INSERT INTO watch_history (user_id, video_id, watched_at) VALUES (?, ?, CURRENT_TIMESTAMP)", (user_id, video_id))
    conn.commit()
    conn.close()
