import os
from fastapi.templating import Jinja2Templates
from helpers import dom_id


CURRENT_PATH = os.path.dirname(__file__)
template_dirs = [os.path.join(CURRENT_PATH, 'templates')]
templating = Jinja2Templates(template_dirs)
templating.env.globals['dom_id'] = dom_id


def render_to_string(template_name, context):
    template = templating.get_template(template_name)
    return template.render(context)
