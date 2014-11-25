#!/usr/bin/env python
import os
import sys

def check_requirements():
	import django, sklearn

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sarprit.settings")

    from django.core.management import execute_from_command_line

    if "--nrc" not in sys.argv:
    	print("Checking for requirements. Use 'manage.py --nrc <command>' to skip requirements check.")
    	check_requirements()
    else:
    	sys.argv.remove("--nrc")

    execute_from_command_line(sys.argv)
