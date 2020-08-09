#!/usr/bin/env bash

# set
# -e            exit on error
# -u            treat unset variables as an error
# -f            disable filename expansion (globbing)
# -o pipefail   the return value of a pipeline is the value of the last (rightmost)
#                   command to exit with a non-zero status

set -euf -o pipefail

output_dir="output"
if [ ! -d "$output_dir" ]; then
    mkdir $output_dir
    # make it writable for gunicorn
    chmod o+rwx $output_dir
fi

cd docker
docker-compose up -d
cd ..