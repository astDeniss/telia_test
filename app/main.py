import os

from fastapi import FastAPI, APIRouter

from .api.endpoints.ticket import router as ticket_router
from .db.mongodb_utils import close_mongo_connection, connect_to_mongo


router = APIRouter()
router.include_router(ticket_router)

app = FastAPI(port=os.environ.get('PORT'), title='FAST API - TICKET API')
app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)
app.include_router(router)
