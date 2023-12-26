def main():
    if len(sys.argv) != 3:
        #print("Usage: python app.py <local_folder_path> <bucket_name>")
        sys.exit(1)

    local_folder_path, bucket_name = sys.argv[1:]

    # Replace 'your-project-id' with your actual Google Cloud project ID
    project_id = 'manipalpr-1677473940279'

    # Create an instance of GCP_Helper
    gcp_helper = GCP_Helper(project_id)

    # Upload files from local folder to GCS bucket
    gcp_helper.upload_files_from_folder(bucket_name, local_folder_path)

if __name__ == "__main__":
    main()
