#!/bin/bash
# !!! attention “important”
# As this is a non-root container, the mounted files and directories must have the proper permissions for the UID 1001.
# sudo chown -R 1001.1001 annotations-data/

sudo docker run -it -p 8080:8080 -v `pwd`/annotations-data:/label-studio/data heartexlabs/label-studio:latest
