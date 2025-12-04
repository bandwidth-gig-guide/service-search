from fastapi import FastAPI
from fastapi.exceptions import HTTPException

from app.api.all import all

from app.util.test_db_connection import test_db_connection

from app.core.handle.exception import handle_exception
from app.core.handle.http_exception import handle_http_exception

# App
app = FastAPI()

# Routes
app.include_router(all, prefix="/all", tags=["all"])

# Handlers
app.add_exception_handler(Exception, handle_exception)
app.add_exception_handler(HTTPException, handle_http_exception)

# Events
@app.on_event("startup")
def on_startup():
    test_db_connection()