"""
This will import all modules with name group*.py
and print the result of the corresponding tweet() function
implemented in group*.py.
"""

import os

i=2
for filename in os.listdir("."):
    if filename.startswith("group") and filename.endswith(".py"):
        module_name = filename[:-3]
        try:
            module = __import__(module_name)
            print("group {0} says: {1}".format(i, module.tweet().encode('utf-8')))
        except ImportError:
            pass
