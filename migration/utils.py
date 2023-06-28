import re
import os
import io
import teradatasql


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
        # string_ddl = Utility.list_to_string(ddl)
        return ddl

    @staticmethod
    def list_to_string(list_input):
        """Converts a list into a single line string."""
        # Check if the input is a list.
        if not isinstance(list_input, list):
            raise TypeError("The input must be a list.")
        string_output = ""
        for item in list_input:
            string_output += str(item) + " "
        return Utility.replace_cr_by_lf(string_output).strip()

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
            print(f"[ERROR]: writing {string} in file {filename} failed with exception {e}")

    @staticmethod
    def get_teradata_conn_cursor(hostname, port, user_name, pass_w, database):
        """Reads data from a Teradata database using teradatasql."""
        try:
            conn = teradatasql.connect(
                host=hostname,
                dbs_port=port,
                user=user_name,
                password=pass_w,
                database=database,
            )
            return conn.cursor()
        except Exception as e:
            print(f"[ERROR]: connection failure with exception {e}")
