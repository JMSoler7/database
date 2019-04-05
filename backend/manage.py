#!/usr/bin/env python
import os
import sys
from dotenv import load_dotenv, find_dotenv

if __name__ == "__main__":
    load_dotenv(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env'),
        find_dotenv()
    )
    settings_module = os.getenv(
        'DJANGO_SETTINGS_MODULE',
        default='database.settings.production'
    )
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            import django  # NOQA F401
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
