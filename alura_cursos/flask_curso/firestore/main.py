"""."""
import traceback
from google.cloud import firestore
import sys

DATA = {
    'dev': 'firestore_data_dev',
    'qa': 'firestore_data_qa,',
    'e2e': 'firestore_data_e2e',
    'uat': 'firestore_data_uat',
    'prd': 'firestore_data_prd'
}

gcp_project = sys.argv[1]
env = gcp_project[-3:]

print(f"gcp_project: {gcp_project}")
client = firestore.Client(gcp_project)


def execute():
    """."""
    try:
        _drop_collections()
        _insert_data()
        print("Firestore migration executed with success")

    except Exception as ex:
        print(f"Error when doing the Firestore migration. Exception: {ex}")
        traceback.print_exc()


def _drop_collections():
    """."""
    firestore_data = _get_environments_data(DATA.get(env))
    print(firestore_data)
    print("Dropping collections")
    collections_names = firestore_data.get_collections()

    for collection_name in collections_names:
        collection = client.collection(collection_name)
        documents = collection.stream()

        for document in documents:
            document.reference.delete()


def _insert_data():
    """."""
    firestore_data = _get_environments_data(DATA.get(env))
    print("Inserting documents")
    documents = firestore_data.get_documents()
    print(documents)

    for document in documents:
        collection = document["collection"]
        document_id = document["id"]
        data = document["data"]

        client.collection(collection).document(document_id).set(data)


def _get_environments_data(env):
    """."""
    from importlib import import_module
    try:
        return import_module(f'datas.{env.lower()}')
    except ImportError:
        return import_module(f'.datas.{env.lower()}')

if __name__ == "__main__":
    execute()
