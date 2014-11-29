#!/bin/bash

gunicorn app:app --bind unix:/tmp/intro_server.sock -w 2 &

