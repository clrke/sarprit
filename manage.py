#!/usr/bin/env python
import os
import sys

def check_requirements():
	import django, sklearn

check_requirements()

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sarprit.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
