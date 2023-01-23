username = [
    {"user": "testuser00", "passwd": "admin"},
    {"user": "testuser01", "passwd": "admin"},
    {"user": "testuser02", "passwd": "admin"},
]

def _find_user(user):
    data = [x for x in username if x['user']==user]
    return data

def _add_user(user):
    global username
    username.append(user)
    return username