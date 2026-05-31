import os
import sys

# Path to your project root (where manage.py is)
BASE_DIR = "/home/hightech/quantumcoresoftware.com/quantum"

# Add project to Python path
sys.path.insert(0, BASE_DIR)

# If your virtualenv is used by Passenger, this is usually optional,
# but you can explicitly activate it like this:
VENV_DIR = "/home/hightech/virtualenv/quantumcoresoftware.com/quantum/3.10"

activate_this = os.path.join(VENV_DIR, "bin", "activate_this.py")
if os.path.exists(activate_this):
    with open(activate_this) as file_:
        exec(file_.read(), dict(__file__=activate_this))

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quantum.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()