# 匯率轉換 API

此專案實作了一個匯率轉換 API，使用 Python 和 FastAPI 框架，並使用 Docker 進行容器化。

## 環境需求

- Docker
- Docker Compose

## 安裝與啟動

### 1. 克隆專案

```sh
git clone https://github.com/ToooAir/currency-exchange-api.git
cd currency-exchange-api
```

### 2. 使用 Docker Compose 建構並啟動服務
```sh
docker-compose up --build
```
建構 Docker 映像
啟動 FastAPI 服務，並在 http://localhost:8000 提供 API

## API 使用說明

### 端點：/convert
方法：GET

請求範例
```json
GET /convert?source=USD&target=JPY&amount=1,525
```
回應範例
```json
{
    "msg": "success",
    "amount": "170,496.53"
}
```

## 測試
此專案使用 pytest 進行單元測試。

### 執行測試
```sh
docker run --rm -v $(pwd):/app -w /app python:slim sh -c "pip install -r requirements.txt && pytest"
```

### 測試案例
測試案例位於 app/tests/test_currency_exchange_service.py，包含以下測試：

1. 轉換匯率的有效性測試
2. 不支援的貨幣測試
3. 無效金額測試
4. 金額輸入輸出四捨五入測試