import redis

# Connect to Redis
cache = redis.StrictRedis(host='localhost', port=6379, db=0)


def fetch_user_mongodb(db, user_id: str):
    # Check if user is cached
    cached_user = cache.get(f"user:{user_id}")
    if cached_user:
        print(f"Cache hit for user {user_id}")
        return cached_user

    try:
        collection = db["users"]
        user = collection.find_one({"_id": user_id})
        if user:
            cache.set(f"user:{user_id}", str(user), ex=60*10)  # Cache for 10 minutes
            print(f"Fetched and cached user {user_id}")
            return user
        else:
            print("User not found")
            return None
    except Exception as e:
        print(f"Error fetching user: {e}")
        return None
