# 動画の評価の管理
def rate_video(user_id, video_id, rating):
    conn = sqlite3.connect('video_ratings.db')
    c = conn.cursor()
    c.execute("INSERT INTO video_ratings (user_id, video_id, rating) VALUES (?, ?, ?)", (user_id, video_id, rating))
    conn.commit()
    conn.close()

def get_average_rating(video_id):
    conn = sqlite3.connect('video_ratings.db')
    c = conn.cursor()
    c.execute("SELECT AVG(rating) FROM video_ratings WHERE video_id = ?", (video_id,))
    average_rating = c.fetchone()[0]
    conn.close()
    return average_rating
