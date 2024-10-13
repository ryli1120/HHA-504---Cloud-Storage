from azure.storage.blob import BlobServiceClient

# Azure storage account details
connection_string = 'gcp_ryan_secret.json'
container_name = '504storage'
blob_name = 'hello.txt'
file_path = "D:\Data\AHI\AHI Python\504 Cloud\HHA-504---Cloud-Storage\hello.txt"

# Create BlobServiceClient object
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Get the container client
container_client = blob_service_client.get_container_client(container_name)

# Upload the file to Blob storage
with open(file_path, 'rb') as file_data:
    container_client.upload_blob(blob_name, file_data)

print(f"File {blob_name} uploaded to Azure Blob Storage successfully.")
