import json
import time
import sys
from os import listdir, environ
from os.path import isfile, join

from elasticsearch import Elasticsearch


def insert_data(es_writer, data_dir="data/"):
    # Loads the local log files from the specified data dir
    print("Starting parse log process")
    print("Opening log file and reading")
    print("Loading logs into ES")
    elastic_files = [f for f in listdir(data_dir) if isfile(join(data_dir, f))]
    for elastic_file in elastic_files:
        full_path = f"{data_dir}/{elastic_file}"
        print(f"Processing: {full_path}")
        with open(full_path, "r") as input_file:
            for line in input_file:
                log = json.loads(line)
                # These are items from Kibana we don't care about importing
                if (
                    not log["_id"].startswith("application_usage_transactional")
                    and not log["_id"].startswith("ui-metric")
                    and not log["_id"].startswith("telemetry")
                ):
                    # print(log["_id"], log["_index"])
                    es_writer.index(
                        index=log["_index"], id=log["_id"], body=log["_source"]
                    )
    print("Done")


if __name__ == "__main__":
    es_connected = False
    es_writer = None
    host = environ["ELASTICSEARCH_HOSTS"]
    es_writer = Elasticsearch(host)
    # Dirty hack to deal with this container not starting first
    # And if the ES connection doesn't work
    while not es_writer.ping():
        print("Failed to connect sleeping for 5")
        time.sleep(5)
    insert_data(es_writer)
