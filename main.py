from fastapi import Request, WebSocket, WebSocketDisconnect
from app import app
from templating import templating
import crud
from connection_manager import manager
import htmx
import helpers


@app.get("/")
def home(request: Request):
    foo_records = crud.foo_list(sort=("id", "desc"))
    context = {"records": foo_records, "model_name": "Foo"}
    return templating.TemplateResponse(request, "home.html", context)


@app.post("/")
async def add_random(request: Request):
    instance = crud.foo_add_random()
    context = {"record": instance, "model_name": "Foo", "request": request}
    await htmx.broadcast_prepend_to(
        target_id="Foo_table",
        template_name="_foo.html",
        context=context,
        target_tag="tbody",
    )


@app.post("/delete/{id}/", name="delete")
async def delete(id: int):
    instance = crud.foo_delete(id)
    if instance:
        await htmx.broadcast_delete_to(helpers.dom_id(instance))


@app.post("/update/{id}/", name="update")
async def update(request: Request, id: int):
    instance = crud.foo_update(id, name='Rosa', description='Mose')
    if instance:
        context = {"record": instance, "model_name": "Foo", "request": request}
        await htmx.broadcast_update_to(
            target_id=helpers.dom_id(instance),
            template_name="_foo.html",
            context=context,
            target_tag="tbody",
        )


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()  # или pass, если клиент не отправляет
    except WebSocketDisconnect:
        manager.disconnect(websocket)
