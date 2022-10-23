#!/bin/sh
# This script is run by the startup script.
pipenv run proxy &
pipenv run dev
