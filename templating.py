import os
from fastapi.templating import Jinja2Templates


CURRENT_PATH = os.path.dirname(__file__)
template_dirs = [os.path.join(CURRENT_PATH, 'templates')]
templating = Jinja2Templates(template_dirs)
