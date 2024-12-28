import chromadb
import json

json_file = "brotherhood_lore.json"
collection_name = "brotherhood_of_steel"

client = chromadb.PersistentClient(path=r"C:\Users\nls08\VirtualEnvironments\ragtag")

# Load JSON file
with open(json_file, "r") as file:
        data = json.load(file)


# Create or retrieve a collection
collection = client.get_or_create_collection(collection_name)


# Add documents to the collection
for entry in data:
        collection.upsert(
            ids=[entry["id"]],
            documents=[entry["content"]],
            metadatas=[entry["metadata"]]
        )