import sys
from google.cloud import storage

class GCP_Helper:
    def __init__(self, project_id):
        self.project_id = project_id
        self.storage_client = storage.Client(project=project_id)

    def upload_file_cloud_storage(self, bucket_name, source_file_name, destination_blob_name):
        bucket = self.storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)
        print(f"File {source_file_name} uploaded to {destination_blob_name} in {bucket_name}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python app.py <file_path> <bucket_name> <destination_blob_name>")
        sys.exit(1)

    file_path, bucket_name, destination_blob_name = sys.argv[1:]

    # Replace 'your-project-id' with your actual Google Cloud project ID
    project_id = 'manipalpr-1677473940279'

    # Create an instance of GCP_Helper
    gcp_helper = GCP_Helper(project_id)

    # Upload file to GCS
    gcp_helper.upload_file_cloud_storage(bucket_name, file_path, destination_blob_name)

if __name__ == "__main__":
    main()
