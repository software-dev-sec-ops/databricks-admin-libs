#!/bin/bash

#############################################
## Install packages on the databricks cluster
#############################################
fn install_packages() {
    /databricks/python/bin/pip install -r /dbfs/requirements.txt
    RESULT=$?
    if [ $RESULT == 0]; then
        echo "Successfully installed python libraries"
        exit 0
    else
        exit 1
    fi
}

install_packages
