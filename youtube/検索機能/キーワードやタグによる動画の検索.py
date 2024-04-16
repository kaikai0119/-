def search_videos_by_keyword(keyword):
    conn = sqlite3.connect('videos.db')
    c = conn.cursor()
    c.execute("SELECT * FROM videos WHERE title LIKE ? OR description LIKE ?", ('%' + keyword + '%', '%' + keyword + '%'))
    videos = c.fetchall()
    conn.close()
    return videos

def search_videos_by_tag(tag):
    conn = sqlite3.connect('videos.db')
    c = conn.cursor()
    c.execute("SELECT * FROM videos WHERE tags LIKE ?", ('%' + tag + '%',))
    videos = c.fetchall()
    conn.close()
    return videos
