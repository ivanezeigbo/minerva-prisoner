#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from otree.management.cli import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django or Otree. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv, script_file=__file__)
