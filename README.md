# teradata-utility

git clone https://github.com/warunk9/teradata-utility.git

git clone https://github.com/google/dwh-migration-tools.git

mkdir output

pip3 install dwh-migration-tools/client


warunk@cloudshell:~/warunk/tdutil (data-dev-base-1331)$ cat teradata_config.json
{
"jdbc" : {
"hostname": "141.206.4.13",
"port": "1025",
"db" : "r2d2_dba",
"username" : "WARUN",
"password" : "warun"
},
"output" : {
"local_dir": "/home/warunk/warunk/tdutil/output",
"bucket_name": "view-migration"
}
}

gsutil mb gs://view-migration

pip3 install -r teradata-utility/requirements.txt

python3 teradata-utility/migration/views_migrator.py teradata_config.json


export BQMS_VERBOSE="False"
export BQMS_MULTITHREADED="True"
export BQMS_PROJECT="data-prod-base-0c18"
export BQMS_GCS_BUCKET="view-migration"

rm -rf dwh-migration-tools/client/examples/teradata/sql/input/*

cp -r /home/warunk/warunk/tdutil/output/* dwh-migration-tools/client/examples/teradata/sql/input/

dwh-migration-tools/client/examples/teradata/sql/run.sh

        gcs_source_path: "gs://view-migration/1687683055403148132-21pxaqbaydlt4/preprocessed"
        gcs_target_path: "gs://view-migration/1687683055403148132-21pxaqbaydlt4/translated"

reference : https://github.com/google/dwh-migration-tools/tree/main/client
