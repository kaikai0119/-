# ユーザーの動画ライブラリの管理
def add_to_library(user_id, video_id):
    conn = sqlite3.connect('user_library.db')
    c = conn.cursor()
    c.execute("INSERT INTO user_library (user_id, video_id) VALUES (?, ?)", (user_id, video_id))
    conn.commit()
    conn.close()

def get_user_library(user_id):
    conn = sqlite3.connect('user_library.db')
    c = conn.cursor()
    c.execute("SELECT video_id FROM user_library WHERE user_id = ?", (user_id,))
    library = c.fetchall()
    conn.close()
    return library
