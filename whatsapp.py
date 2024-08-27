def get_wa_data(callback_data):
    processed_data = {
        "id": callback_data.id, 
        "gateway_no": callback_data.gateway_no,
        "sender": callback_data.sender,
        "receive_date": callback_data.receive_date,
        "message": callback_data.message
    }
    return {"status": "success", "data": processed_data}