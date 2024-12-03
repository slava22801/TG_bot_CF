import sqlite3


def initDb():
    conn = sqlite3.connect("users.db")


    conn.execute("""
    CREATE TABLE IF NOT EXISTS events (
        userid INTEGER UNIQUE,
        event TEXT,
        countEvents INTEGER
    );
    """)


def initUser(userId):
    conn = sqlite3.connect("users.db")


    conn.execute("""
    INSERT INTO events (userid, event, countEvents) VALUES (?, ?, ?)
    ON CONFLICT(userid) DO NOTHING;
    """, (userId, "null", 0)
    )
    conn.commit()
    conn.close()