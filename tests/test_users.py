import pytest
from httpx import AsyncClient
from app.main import app

API_KEY = {"X-API-Key": "demo-key"}

@pytest.mark.asyncio
async def test_create_and_get_user():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        payload = {"id": "u3", "email": "eva@example.com", "name": "Eva"}
        r = await ac.post("/users/", headers=API_KEY, json=payload)
        assert r.status_code == 200
        r2 = await ac.get("/users/u3", headers=API_KEY)
        assert r2.status_code == 200
        assert r2.json()["email"] == "eva@example.com"
