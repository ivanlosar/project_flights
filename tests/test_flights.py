import pytest
from httpx import AsyncClient
from app.main import app

API_KEY = {"X-API-Key": "demo-key"}

@pytest.mark.asyncio
async def test_list_flights_ok():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        r = await ac.get("/flights/", headers=API_KEY)
        assert r.status_code == 200
        assert isinstance(r.json(), list)

@pytest.mark.asyncio
async def test_get_flight_404():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        r = await ac.get("/flights/NOPE", headers=API_KEY)
        assert r.status_code == 404
