from project import collection


def insert_post_in_db(title, body, user_id, reactions, tags):
    try:
        result = collection.insert_one(
            {"title": title, "body": body, "userId": user_id, "reactions": reactions, "tags": tags})
        return result
    except Exception as e:
        return str(e)


def insert_many_posts(post):
    result = collection.insert_many(post)
    return True if result else False


def get_all_posts():
    try:
        result = list(collection.aggregate([{"$project": {"_id": {"$toString": "$_id"}, "title": 1, "body": 1, "userId": 1, "reactions": 1, "tags": 1}}]))

        return result
    except Exception as e:
        return str(e)
