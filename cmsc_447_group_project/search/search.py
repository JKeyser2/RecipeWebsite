import sqlite3
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
# Setup Elasticsearch connection
es = Elasticsearch("http://localhost:9200")

try:
    info = es.info()
    print("Successfully connected to Elasticsearch!")
    print(info)
except Exception as e:
    print("Error connecting to Elasticsearch:", str(e))

def extract_and_transform_data(db_path):
    """ Extracts and transforms data from an SQLite database for Elasticsearch. """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # Adjust the query to select all specified columns
    cursor.execute('SELECT `index`, recipe_name, servings, ingredients, cuisine_path, nutrition, img_src FROM "user recipe view"')
    data = cursor.fetchall()
    conn.close()
    # Transform data into a format suitable for Elasticsearch
    return [
        {
            "_id": str(row[0]),  # Assuming `index` is the primary key
            "recipe_name": row[1],
            "servings": row[2],
            "ingredients": row[3],
            "cuisine_path": row[4],
            "nutrition": row[5],
            "img_src": row[6]
        }
        for row in data
    ]

def load_data_to_es(index_name, data):
    """ Loads data into Elasticsearch. """
    for item in data:
        doc_id = item.pop("_id")  # Extract the _id and remove it from the document
        es.index(index=index_name, id=doc_id, body=item)

# Path to your SQLite database file
db_path = "user.db"

# Extract, transform, and load data from the database
data = extract_and_transform_data(db_path)
load_data_to_es("recipes_index", data)

# Example of how to search data in Elasticsearch
def search_recipes(search_term, field='all'):
    """ Search for recipes by index, name, ingredients, or any other specified field. """
    if field == 'all':
        query = {
            "multi_match": {
                "query": search_term,
                "fields": ["recipe_name", "ingredients", "cuisine_path"]
            }
        }
    elif field == 'index':
        query = {"term": {"_id": search_term}}
    elif field == 'recipe_name':
        query = {"match": {"recipe_name": search_term}}
    elif field == 'ingredients':
        query = {"match": {"ingredients": search_term}}
    elif field == 'cuisine_path':
        query = {"match": {"cuisine_path": search_term}}

    search_results = es.search(index="recipes_index", query=query)
    return [hit["_source"] for hit in search_results['hits']['hits']]

# Usage examples
results = search_recipes("1", "index")

print("Ingredients: ")
results = search_recipes("egg", "ingredients")
for result in results:
    print(result['recipe_name'])
print("\nIndex: ")
results = search_recipes("1", "index")
for result in results:
    print(result['recipe_name'])
print("\nCuisine: ")
results = search_recipes("Dessert", "cuisine_path")
for result in results:
    print(result['recipe_name'])
print("\nName: ")
results = search_recipes("Apple Pie by Grandma Ople", "recipe_name")
for result in results:
    print(result['recipe_name'])
#print(search_recipes("1", "index"))
#print(search_recipes("Italian", "cuisine_path"))