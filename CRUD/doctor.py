from fastapi import APIRouter, HTTPException, Path
from fastapi.responses import JSONResponse
from database import *
from models import *

router = APIRouter(
    prefix="/doctors",
    tags=["Doctor"]
)