# pip install redis

import redis

# Connect to Redis
cache = redis.StrictRedis(host='localhost', port=6379, db=0)

def fetch_user_postgres(conn, user_id: int):
    # Check if user is cached
    cached_user = cache.get(f"user:{user_id}")
    if cached_user:
        print(f"Cache hit for user {user_id}")
        return cached_user

    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
            user_data = cur.fetchone()
            if user_data:
                cache.set(f"user:{user_id}", str(user_data), ex=60*10)  # Cache for 10 minutes
                print(f"Fetched and cached user {user_id}")
                return user_data
            else:
                print("User not found")
                return None
    except Exception as e:
        print(f"Error fetching user: {e}")
        return None
