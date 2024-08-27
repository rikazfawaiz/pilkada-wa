from fastapi import FastAPI, HTTPException
import model as ml
import whatsapp as wa

app = FastAPI()

@app.post('/send-msg-wa')
async def get_wa_data(callback_data: ml.ReceviceDataWhatsappModel):
    try:
        result = wa.get_wa_data(callback_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

