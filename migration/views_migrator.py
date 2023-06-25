import sys
import logging
from utils import Utility

from connect_t import Connection
from config import Configuration


def log(message):
    """
    Log a message with timestamp.

    Args:
    message: The message to log.
    """
    logging.basicConfig(
        format='%(levelname)s:%(asctime)s:%(message)s', level=logging.DEBUG
    )
    try:
        logging.info("{}".format(message))
    except Exception as er:
        logging.error("Error logging message: {}".format(er))


if __name__ == "__main__":
    config_file = sys.argv[1]
    config = Configuration()
    hostname, port, db, username, password, local_dir, bucket_name = config.get_params_from_json(config_file)

    log(f"hostname: {hostname}")
    log(f"port: {port}")
    log(f"db: {db}")
    log(f"username: {username}")
    log(f"local output dir : {local_dir}")
    log(f"bucket_name output  : {bucket_name}")
    query = "SELECT tablename FROM DBC.TablesV where databasename = 'R2D2_DBA' and tablekind = 'V' and tablename in ('MECHANICAL_CALC_RATE_WRK','SUBSCRIBER_SERVICE_ACTIVITY');"
    cursor_ob = Connection.read_from_teradata(hostname, port, username, password, db)

    view_list = Utility.get_view_list(cursor_ob, query)

    log(view_list)
    for view in view_list:
        log(view)
        full_ddl = Utility.get_view_ddl(view, cursor_ob)
        filename = view+".sql"
        Utility.write_string_to_file(filename, full_ddl, local_dir)

    #Utility.upload_files_to_gcs(local_dir, bucket_name)

