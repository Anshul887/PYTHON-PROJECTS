from database import execute_query, fetch_query

def register(username, password):
    user = fetch_query(
        "SELECT * FROM users WHERE username=?",
        (username,)
    )

    if user:
        return False

    execute_query(
        "INSERT INTO users(username,password) VALUES(?,?)",
        (username, password)
    )

    return True

def login(username, password):
    user = fetch_query(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    return bool(user)
