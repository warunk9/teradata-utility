import re
import os
import io
import google.cloud.storage as gcs


class Utility:

    @staticmethod
    def get_view_list(cursor_ob, query):
        cursor_ob.execute(query)
        view_list = [item[0] for item in cursor_ob.fetchall()]
        return view_list

    @staticmethod
    def get_view_ddl(view, cursor_ob):
        get_view_ddl_query = "show view " + view
        cursor_ob.execute(get_view_ddl_query)
        ddl = cursor_ob.fetchone()
        string_ddl = Utility.list_to_string(ddl)
        return string_ddl

    @staticmethod
    def list_to_string(list_input):
        """Converts a list into a single line string."""
        string_output = ""
        for item in list_input:
            string_output += str(item) + " "
        return Utility.replace_cr_by_lf(string_output)

    @staticmethod
    def replace_cr_by_lf(query):
        """Replaces all occurrences of `\r` by `\n` in a query."""
        query_output = re.sub(r"\r", r"\n", query)
        return query_output

    @staticmethod
    def write_string_to_file(filename, string, local_op):
        """Writes a string to a file in the local directory.

        Raises:
            FileExistsError: If the file already exists.
        """
        # Create a file object in memory.
        file_object = io.StringIO(string)
        try:
            if not os.path.exists(local_op):
                os.mkdir(local_op)
            # Write the file object to the local directory.
            with open(os.path.join(local_op, filename), "w") as f:
                f.write(file_object.getvalue())
        except Exception as e:
            print(f"writing {string} in file {filename} failed with exception {e}")

    @staticmethod
    def upload_files_to_gcs(local_directory, bucket_name):
        """Uploads all files from the local directory to the Google Cloud Storage bucket.

        Raises:
            FileNotFoundError: If the local directory does not exist.
        """
        credentials = {
            "project_id": "my-project-id",
            "client_email": "my-client-email",
            "client_secret": "my-client-secret",
            "refresh_token": "my-refresh-token",
        }

        # Create a Google Cloud Storage client.
        client = gcs.Client()

        # Iterate over all files in the local directory.
        for file in os.listdir(local_directory):
            # Get the full path of the file.
            file_path = os.path.join(local_directory, file)

            # Upload the file to the Google Cloud Storage bucket.
            client.bucket(bucket_name).blob(file).upload_from_file(file_path)
