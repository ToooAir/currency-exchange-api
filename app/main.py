from fastapi import FastAPI, HTTPException, Query
from app.services import CurrencyExchangeService

app = FastAPI()

rates = {
    "TWD": {"TWD": 1, "JPY": 3.669, "USD": 0.03281},
    "JPY": {"TWD": 0.26956, "JPY": 1, "USD": 0.00885},
    "USD": {"TWD": 30.444, "JPY": 111.801, "USD": 1},
}

exchange_service = CurrencyExchangeService(rates)

@app.get("/convert")
def convert_currency(source: str = Query(...), target: str = Query(...), amount: str = Query(...)):
    try:
        result = exchange_service.convert(source, target, amount)
        return {"msg": "success", "amount": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
