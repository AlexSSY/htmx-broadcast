from functools import partial
from templating import render_to_string
from connection_manager import manager


async def broadcast_to(*, target_id, template_name, context, swap_oob, manager, target_tag='div'):
    html_safe = render_to_string(template_name, context)
    if swap_oob == 'true':
        wrapper = html_safe
    else:
        wrapper = f'<{target_tag} id="{target_id}" hx-swap-oob="{swap_oob}">{html_safe}</{target_tag}>'
    await manager.broadcast(wrapper)


broadcast_prepend_to = partial(broadcast_to, swap_oob='afterbegin', manager=manager)
broadcast_update_to = partial(broadcast_to, swap_oob='true', manager=manager)


async def broadcast_delete_to(target_id, manager=manager):
    await manager.broadcast(f'<div id="{target_id}" hx-swap-oob="delete"></div>')
