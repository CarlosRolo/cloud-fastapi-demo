from httpx import AsyncClient, ASGITransport
from app.main import app
import pytest


@pytest.mark.asyncio
async def test_create_item():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.post(
            "/api/v1/items",
            json={"name": "Raspberry Pi 4", "description": "SBC", "price": 55.0},
        )
    assert response.status_code == 201
    assert response.json()["name"] == "Raspberry Pi 4"


@pytest.mark.asyncio
async def test_get_item_not_found():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get("/api/v1/items/9999")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_list_items():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        await client.post(
            "/api/v1/items",
            json={"name": "MQTT Broker", "price": 1.0},
        )
        response = await client.get("/api/v1/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
