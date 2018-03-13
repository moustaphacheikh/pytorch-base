#!/bin/sh

#==================================================
# Defines useful environment variables used 
# throughout the code
#==================================================

if [[ "${BASH_SOURCE[0]}" == "${0}" ]];
then
  echo "Please source this script from the root src directory"
  exit 1
fi

set -x

export PROJECT_NAME="DEFAULT"

export ${PROJECT_NAME}_DATA_DIR=`pwd`/data

export ${PROJECT_NAME}_ACTIVE=1

set +x
