#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinestar.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
        #intercambié "sys.argv" por "['manage.py', 'runserver']" para ejecutar el programa dandole click al botón Execute
        #Abrir por terminal: "python manage.py runserver"
    execute_from_command_line(['manage.py', 'runserver'])


if __name__ == '__main__':
    main()
