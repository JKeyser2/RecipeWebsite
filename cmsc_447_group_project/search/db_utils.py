import mysql.connector
from elasticsearch import Elasticsearch
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB, ELASTICSEARCH_URL

def connect_mysql():
    """ Connect to the MySQL database. """
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )

def sync_to_elasticsearch():
    """ Synchronize MySQL data with Elasticsearch. """
    db = connect_mysql()
    cursor = db.cursor()

    es = Elasticsearch(ELASTICSEARCH_URL)

    # Recreate the index to update the mapping if needed
    es.indices.delete(index='recipes', ignore=[400, 404])
    es.indices.create(index='recipes', ignore=400, body={
        "mappings": {
            "properties": {
                "title": {"type": "text"},
                "description": {"type": "text"},
                "ingredients": {"type": "text"},
                "rating": {"type": "integer"}
            }
        }
    })

    query = """
        SELECT r.id, u.username, r.title, r.description, r.ingredients, r.method, r.rating
        FROM recipes r JOIN users u ON r.user_id = u.id
    """
    cursor.execute(query)
    for recipe_id, username, title, description, ingredients, method, rating in cursor.fetchall():
        doc = {
            'username': username,
            'title': title,
            'description': description,
            'ingredients': ingredients,
            'method': method,
            'rating': rating
        }
        es.index(index="recipes", id=recipe_id, document=doc)

    cursor.close()
    db.close()