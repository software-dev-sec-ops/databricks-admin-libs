"""
Create Databricks Cluster using databricks-sdk
"""

import os
import time
import logging
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.compute import (
    WorkspaceStorageInfo,
    InitScriptInfo,
    DbfsStorageInfo,
)


def initialize_logging():
    """sets up logging to both console and file

    Returns:
        _type_: logging.Logger
    """
    logger = logging.getLogger("db_cluster_logger")

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    ch.setFormatter(formatter)

    fh = logging.FileHandler(filename="db_cluster_logger.log")
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger


logger = initialize_logging()


def create_cluster():
    """Creates Databricks Cluster"""
    try:
        w = WorkspaceClient()
        latest = w.clusters.select_spark_version(latest=True)
        cluster_name = f"db-sdk-{time.time_ns()}"
        clstr = w.clusters.create(
            cluster_name=cluster_name,
            spark_version=latest,
            autotermination_minutes=15,
            num_workers=1,
            init_scripts=[
                InitScriptInfo(
                    WorkspaceStorageInfo("dbfs:/databricks/cluster/scripts/init.sh")
                )
            ],
            cluster_log_conf=[DbfsStorageInfo("dbfs:/databricks/cluster/logs")],
        ).result()
        logger.info(
            "Successfully created cluster {}".format(", ".join(key for key in clstr))
        )
    except Exception as e:
        logger.error("Error creating cluster str(e)")


def main():
    """Entry point"""
    # set Databricks authentication
    os.environ["DATABRICKS_CONFIG_PROFILE"] = "REPLACE_ME_WITH_DATABRICKS_PROFILE"
    create_cluster()
    return None


if __name__ == "__main__":
    main()
