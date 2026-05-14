import sys
import os

# Add your project directory to the sys.path
project_home = '/home/hightech/project24.quantumcoresoftware.com/quantum'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Activate virtualenv
venv = '/home/hightech/virtualenv/project24.quantumcoresoftware.com/quantum/3.10'
activate_this = os.path.join(venv, 'bin', 'activate_this.py')

with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Set Django settings module
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'quantum.settings'
)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()