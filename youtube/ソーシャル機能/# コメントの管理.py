# コメントの管理
def post_comment(user_id, video_id, comment):
    conn = sqlite3.connect('video_comments.db')
    c = conn.cursor()
    c.execute("INSERT INTO video_comments (user_id, video_id, comment) VALUES (?, ?, ?)", (user_id, video_id, comment))
    conn.commit()
    conn.close()

def get_comments(video_id):
    conn = sqlite3.connect('video_comments.db')
    c = conn.cursor()
    c.execute("SELECT user_id, comment FROM video_comments WHERE video_id = ?", (video_id,))
    comments = c.fetchall()
    conn.close()
    return comments
