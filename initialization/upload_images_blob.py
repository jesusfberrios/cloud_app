import os
from azure.storage.blob import BlobServiceClient

def upload_images_to_blob_storage(folder_path):
    # Retrieve credentials from environment variables
    blob_string = os.environ.get('BLOB_STRING')
    blob_container_name = os.environ.get('BLOB_CONTAINER_NAME')

    # Create BlobServiceClient using credentials
    blob_service_client = BlobServiceClient.from_connection_string(blob_string)

    # Create Blob Container client
    container_client = blob_service_client.get_container_client(blob_container_name)

    # List all files in the folder
    files = os.listdir(folder_path)

    # Upload each file to Blob Storage
    for file_name in files:
        # Construct the BlobClient for the file
        blob_client = container_client.get_blob_client(file_name)

        # Upload the file to Blob Storage
        with open(os.path.join(folder_path, file_name), "rb") as data:
            blob_client.upload_blob(data)

    print("Upload completed.")

if __name__ == "__main__":
    # Specify the path to the folder containing the images
    folder_path = "maps"

    # Call the function to upload images to Blob Storage
    upload_images_to_blob_storage(folder_path)
