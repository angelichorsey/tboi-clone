"""
This doesn't really do anything special now, but if we want to add options
to runt he game with different parameters, configuration, etc then we would
put it in here.
"""

# Adding src to python's path so it can find the imports without needing
# to modify the import lines. Somewhat of a hack and may not be a long
# term solution.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Import main function from main.py and then run it.
from main import main
main()
