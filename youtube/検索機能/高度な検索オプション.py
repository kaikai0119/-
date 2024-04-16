def advanced_search_videos(posted_after=None, views_greater_than=None, min_rating=None):
    query = "SELECT * FROM videos WHERE 1=1"
    params = []

    if posted_after:
        query += " AND posted_at > ?"
        params.append(posted_after)

    if views_greater_than:
        query += " AND views > ?"
        params.append(views_greater_than)

    if min_rating:
        query += " AND rating >= ?"
        params.append(min_rating)

    conn = sqlite3.connect('videos.db')
    c = conn.cursor()
    c.execute(query, params)
    videos = c.fetchall()
    conn.close()
    return videos
