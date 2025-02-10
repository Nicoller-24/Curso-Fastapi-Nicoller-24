import requests
from fastapi import APIRouter, HTTPException, Depends, status
from sqlmodel import select
from db import SessionDep
from models import Weather, WeatherCreate

router = APIRouter()

API_KEY = "ee8d20f96a2af7c6c1cea357e9b6112b"

@router.get("/weather", response_model=list[Weather], tags=["weather"])
async def list_hottest_day(session: SessionDep):
    return session.exec(select(Weather)).all()

@router.get("/weather/{lat}/{lon}/{cnt}", tags=["weather"])
async def get_weather(lat: float, lon: float, cnt: int):
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&cnt={cnt}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="No se pudo obtener el clima")
    
    return response.json()


@router.post("/save_weather/{lat}/{lon}/{cnt}", tags=["weather"], status_code=status.HTTP_201_CREATED)
async def save_weather(lat: float, lon: float, cnt: int, session: SessionDep):
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&cnt={cnt}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="No se pudo obtener el clima")

    data = response.json()
    city_name = data["city"]["name"]

    hottest_entry = max(data["list"], key=lambda x: x["main"]["temp_max"])

    hottest_day = Weather(
        city_name=city_name,
        date=hottest_entry["dt_txt"],
        temp_max=hottest_entry["main"]["temp_max"],
        temp_min=hottest_entry["main"]["temp_min"],
        lat=lat,
        lon=lon,
        is_hottest_day=True  
    )

    session.add(hottest_day)
    session.commit()
    session.refresh(hottest_day)

    return {
        "message": "Día más caluroso guardado correctamente",
        "hottest_day": hottest_day
    }

@router.delete("/weather/{weather_id}", tags=["weather"])
async def delete_hottest_day(weather_id: int, session: SessionDep):
    weather_db = session.get(Weather, weather_id)
    if not weather_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="The day doesn't exist"
        )
    session.delete(weather_db)
    session.commit()
    return {"detail": "ok"}