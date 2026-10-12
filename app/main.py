from datetime import datetime, timezone
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from fastapi import FastAPI, HTTPException


app = FastAPI(title="VPe04 Time Server", version="1.0.0")


@app.get("/")
def root() -> dict[str, str]:
    return {
        "message": "VPe04 Time Server is running",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "healthy"}


@app.get("/time")
def current_time() -> dict[str, str]:
    return {"timezone": "UTC", "datetime": datetime.now(timezone.utc).isoformat()}


@app.get("/time/{timezone_name}")
def time_in_timezone(timezone_name: str) -> dict[str, str]:
    try:
        zone = ZoneInfo(timezone_name)
    except ZoneInfoNotFoundError as exc:
        raise HTTPException(status_code=404, detail="Unknown timezone") from exc

    return {
        "timezone": timezone_name,
        "datetime": datetime.now(zone).isoformat(),
    }
