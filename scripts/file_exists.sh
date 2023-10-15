#!/bin/bash

#############################################
## Check if requirements.txt exists
#############################################
FILE=requirements.txt
fn requirements_file_exists() {
    if [ -f "$FILE" ]; then
        echo "$FILE exists."
        exit 0
    else 
        echo "$FILE does not exist."
        exit 1
    fi
}

requirements_file_exists