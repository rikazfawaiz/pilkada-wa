from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ReceviceDataWhatsappModel(BaseModel):
    id: Optional[str]
    gateway_no: Optional[str]
    sender: Optional[str]
    receive_date: Optional[datetime]
    message: Optional[str]