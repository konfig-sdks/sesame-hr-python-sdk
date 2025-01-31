# coding: utf-8

"""
    Sesame Public API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from sesame_hr_python_sdk.type.time_entries_stop_time_entry_out_response_data_time_entry_out_coordinates import TimeEntriesStopTimeEntryOutResponseDataTimeEntryOutCoordinates

class RequiredTimeEntriesStopTimeEntryOutResponseDataTimeEntryOut(TypedDict):
    pass

class OptionalTimeEntriesStopTimeEntryOutResponseDataTimeEntryOut(TypedDict, total=False):
    date: str

    coordinates: TimeEntriesStopTimeEntryOutResponseDataTimeEntryOutCoordinates

class TimeEntriesStopTimeEntryOutResponseDataTimeEntryOut(RequiredTimeEntriesStopTimeEntryOutResponseDataTimeEntryOut, OptionalTimeEntriesStopTimeEntryOutResponseDataTimeEntryOut):
    pass
