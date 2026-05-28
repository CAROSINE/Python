cache = {}

def set_cache(key, value):
    cache[key] = value

def get_cache(key):
    return cache.get(key, None)

def clear_cache():
    cache.clear()