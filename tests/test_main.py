import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_root_endpoint(client: AsyncClient):
    response = await client.get("/")
    assert response.status_code == 200
    assert "Finance Tracker API" in response.json()["message"]

@pytest.mark.asyncio
async def test_health_endpoint(client: AsyncClient):
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

@pytest.mark.asyncio
async def test_api_root(client: AsyncClient):
    response = await client.get("/api/")
    assert response.status_code == 200
    assert "Finance Tracker API v1" in response.json()["message"]
