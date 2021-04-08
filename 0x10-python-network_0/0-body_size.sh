#!/bin/bash
# Command to display content lenght
curl -sI $1 | grep Content-Length | cut -d" " -f2
