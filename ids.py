_auto_inc_id = 1

def get_id():
    global _auto_inc_id
    _auto_inc_id += 1
    return _auto_inc_id
