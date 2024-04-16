# フォロー/フォロワー関係の管理
def follow_user(user_id, followed_user_id):
    conn = sqlite3.connect('user_relationships.db')
    c = conn.cursor()
    c.execute("INSERT INTO user_relationships (user_id, followed_user_id) VALUES (?, ?)", (user_id, followed_user_id))
    conn.commit()
    conn.close()

def unfollow_user(user_id, followed_user_id):
    conn = sqlite3.connect('user_relationships.db')
    c = conn.cursor()
    c.execute("DELETE FROM user_relationships WHERE user_id = ? AND followed_user_id = ?", (user_id, followed_user_id))
    conn.commit()
    conn.close()

def get_followers(user_id):
    conn = sqlite3.connect('user_relationships.db')
    c = conn.cursor()
    c.execute("SELECT user_id FROM user_relationships WHERE followed_user_id = ?", (user_id,))
    followers = c.fetchall()
    conn.close()
    return followers

def get_following(user_id):
    conn = sqlite3.connect('user_relationships.db')
    c = conn.cursor()
    c.execute("SELECT followed_user_id FROM user_relationships WHERE user_id = ?", (user_id,))
    following = c.fetchall()
    conn.close()
    return following
