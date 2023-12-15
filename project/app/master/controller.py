from project import collection


def insert_post_in_db(id, title, body, user_id, reactions, tags):
    try:
        result = collection.insert_many(
            [{"id": id, "title": title, "post": body, "userid": user_id, "reactions": reactions, "tags": tags}])
        return True if result else False
    except Exception as e:
        return str(e)


def insert_many_posts(post):
    result = collection.insert_many(post)
    return True if result else False


def get_all_posts():
    try:
        result = collection.find({}, {"_id": 0})
        return list(result)
    except Exception as e:
        return str(e)
