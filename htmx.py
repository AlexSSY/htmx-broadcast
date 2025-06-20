import re
from markupsafe import Markup


def determine_wrapper_tag(html_fragment: str) -> str:
    # Ищем первый открывающий тег с именем (без < и >)
    match = re.search(r'<\s*([a-zA-Z0-9]+)', html_fragment)
    if not match:
        raise ValueError("Empty or invalid html fragment")
    tag = match.group(1).lower()

    if tag == 'tr':
        return 'tbody'
    elif tag == 'td':
        return 'tr'
    elif tag == 'li':
        return 'ul'
    elif tag == 'option':
        return 'select'
    elif tag == 'tbody':
        return 'table'
    else:
        return 'div'


async def prepend(html, target, manager):
    wrapper_tag = determine_wrapper_tag(html)
    html_safe = Markup(html)
    wrapper = f'<{wrapper_tag} id="{target}" hx-swap-oob="afterbegin">{html_safe}</{wrapper_tag}>'
    await manager.broadcast(wrapper)
