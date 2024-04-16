def get_popular_videos(limit=10):
    conn = sqlite3.connect('videos.db')
    c = conn.cursor()
    c.execute("SELECT * FROM videos ORDER BY views DESC LIMIT ?", (limit,))
    popular_videos = c.fetchall()
    conn.close()
    return popular_videos
