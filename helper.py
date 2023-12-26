from google.cloud import storage

class GCP_Helper:
    def __init__(self, project_id):
        self.project_id = project_id
        self.storage_client = storage.Client(project=project_id)

    def download_file_cloud_storage(self, bucket_name, source_blob_name, destination_file_name):
        bucket = self.storage_client.bucket(bucket_name)
        blob = bucket.blob(source_blob_name)

        blob.download_to_filename(destination_file_name)
        print(f"Downloaded file {source_blob_name} to {destination_file_name}")

    def upload_file_cloud_storage(self, bucket_name, source_file_name, destination_blob_name):
        bucket = self.storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)
        print(f"File {source_file_name} uploaded to {destination_blob_name} in {bucket_name}")

# Example usage in app.py
if __name__ == "__main__":
    # Replace 'your-project-id' with your actual Google Cloud project ID
    project_id = 'manipalpr-1677473940279'
    
    # Replace 'your-bucket-name' with the name of your GCS bucket
    bucket_name = 'bkt-dec26-skr-v2'

    # Replace 'local-file.txt' with the path to the file you want to upload
    local_file_path = 'D:\SKR.docx'

    # Replace 'uploaded-file.txt' with the desired name in GCS
    gcs_blob_name = 'temp.docx'

    # Create an instance of GCP_Helper
    gcp_helper = GCP_Helper(project_id)

    # Upload file to GCS
    gcp_helper.upload_file_cloud_storage(bucket_name, local_file_path, gcs_blob_name)

    # Download file from GCS
    gcp_helper.download_file_cloud_storage(bucket_name, gcs_blob_name, 'downloaded-file.txt')

