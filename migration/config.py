import json
from types import SimpleNamespace


class Configuration(object):

    def get_config_json(self, config_fl):
        try:
            with open(config_fl, "r") as fp:
                return json.load(fp, object_hook=lambda d: SimpleNamespace(**d))
        except FileNotFoundError as e:
            raise FileNotFoundError(f"[ERROR]Config file not found, check config file path '{self.config_file}'") from e

    def get_params_from_json(self, config_fl):
        config_json_ob = self.get_config_json(config_fl)
        hostname = config_json_ob.jdbc.hostname
        port = config_json_ob.jdbc.port
        db = config_json_ob.jdbc.db
        username = config_json_ob.jdbc.username
        password = config_json_ob.jdbc.password
        local_dir = config_json_ob.output.local_dir
        bucket_name = config_json_ob.output.bucket_name

        return hostname, port, db, username, password, local_dir, bucket_name
