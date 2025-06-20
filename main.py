from fastapi import Request, WebSocket, WebSocketDisconnect
from app import app
from templating import templating
import crud
from connection_manager import manager
from markupsafe import Markup


@app.get('/')
def home(request: Request):
    foo_records = crud.foo_list()
    context = {
        'records': foo_records,
        'model_name': 'Foo'
    }
    return templating.TemplateResponse(request, 'home.html', context)


@app.post('/')
async def add_random(request: Request):
    instance = crud.foo_add_random()
    context = {
        'record': instance,
        'model_name': 'Foo'
    }
    foo_partial_html = templating.get_template('_foo.html').render(context)
    html = f'<div id="insert_Foo_{instance.id}" hx-swap-oob="afterbegin:#Foo_table">{foo_partial_html}</div>'
    await manager.broadcast(Markup(html))


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()  # или pass, если клиент не отправляет
    except WebSocketDisconnect:
        manager.disconnect(websocket)
