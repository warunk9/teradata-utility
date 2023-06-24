import teradatasql

import teradatasql


class Connection():

    @staticmethod
    def read_from_teradata(hostname, port, user_name, pass_w, database):
        """Reads data from a Teradata database using teradatasql."""
        conn = teradatasql.connect(
            host=hostname,
            dbs_port=port,
            user=user_name,
            password=pass_w,
            database=database,
        )
        return conn.cursor()

