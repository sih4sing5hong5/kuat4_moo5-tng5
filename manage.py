#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kuat4_moo5_tng5.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
