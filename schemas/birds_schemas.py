from typing import Optional, List
from pydantic import BaseModel, Field, TypeAdapter, field_validator


class Bird(BaseModel):
    id: int = Field(ge=0)
    device_id: str = Field(min_length=1, max_length=100)
    detection_type: str
    species: str = Field(min_length=1, max_length=100)
    confidence: Optional[float] = Field(ge=0.0, le=1.0)
    photo_url: Optional[str] = None
    audio_url: Optional[str] = None
    location_lat: Optional[float] = Field(ge=-90, le=90)
    location_lon: Optional[float] = Field(ge=-180, le=180)

    @field_validator("detection_type")
    @classmethod
    def validate_detection_type(cls, v: str) -> str:
        allowed = ["audio", "video"]
        if v not in allowed:
            raise ValueError(f"detection_type must be one of {allowed}, got {v}")
        return v

    @field_validator("confidence")
    @classmethod
    def validate_confidence(cls, v: Optional[float]) -> Optional[float]:
        if v is not None and (v < 0 or v > 1):
            raise ValueError(f"confidence must be between 0 and 1, got {v}")
        return v


BirdListAdapter = TypeAdapter(List[Bird])


class CreateBirdRequest(BaseModel):
    device_id: str = Field(min_length=1, max_length=100)
    detection_type: str
    species: str = Field(min_length=1, max_length=100)
    confidence: Optional[float] = Field(None, ge=0.0, le=1.0)
    photo_url: Optional[str] = None
    audio_url: Optional[str] = None
    location_lat: Optional[float] = Field(None, ge=-90, le=90)
    location_lon: Optional[float] = Field(None, ge=-180, le=180)

    @field_validator("detection_type")
    @classmethod
    def validate_detection_type(cls, v: str) -> str:
        allowed = ["audio", "video"]
        if v not in allowed:
            raise ValueError(f"detection_type must be one of {allowed}, got {v}")
        return v


class UpdateBirdRequest(BaseModel):
    device_id: Optional[str] = Field(None, min_length=1, max_length=100)
    detection_type: Optional[str] = None
    species: Optional[str] = Field(None, min_length=1, max_length=100)
    confidence: Optional[float] = Field(None, ge=0.0, le=1.0)
    photo_url: Optional[str] = None
    audio_url: Optional[str] = None
    location_lat: Optional[float] = Field(None, ge=-90, le=90)
    location_lon: Optional[float] = Field(None, ge=-180, le=180)

    @field_validator("detection_type")
    @classmethod
    def validate_detection_type(cls, v: Optional[str]) -> Optional[str]:
        if v is not None:
            allowed = ["audio", "video"]
            if v not in allowed:
                raise ValueError(f"detection_type must be one of {allowed}, got {v}")
        return v