def main():
    if len(sys.argv) != 2:
        print("Usage: python app.py <local_folder_path>")
        sys.exit(1)

    local_folder_path = sys.argv[1]

    # Replace 'your-project-id' and 'your-bucket-name' with your actual Google Cloud project ID and GCS bucket name
    project_id = 'your-project-id'
    bucket_name = 'your-bucket-name'

    # Create an instance of GCP_Helper
    gcp_helper = GCP_Helper(project_id, bucket_name)

    # Upload files from local folder to GCS bucket
    gcp_helper.upload_files_from_folder(local_folder_path)

if __name__ == "__main__":
    main()
