from dataclasses import dataclass
from datetime import date
from enum import Enum

from model.forecast_request import CurrentEnum


@dataclass
class HistoricalWeatherParam:
    lattitude: float
    longitude: float
    start_date: date
    end_date: date
    hourly: list[CurrentEnum]
