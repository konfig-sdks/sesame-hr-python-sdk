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

from sesame_hr_python_sdk.type.time_entries_stop_time_entry_out_response_data_time_entry_in_coordinates import TimeEntriesStopTimeEntryOutResponseDataTimeEntryInCoordinates

class RequiredTimeEntriesStopTimeEntryOutResponseDataTimeEntryIn(TypedDict):
    pass

class OptionalTimeEntriesStopTimeEntryOutResponseDataTimeEntryIn(TypedDict, total=False):
    date: str

    coordinates: TimeEntriesStopTimeEntryOutResponseDataTimeEntryInCoordinates

class TimeEntriesStopTimeEntryOutResponseDataTimeEntryIn(RequiredTimeEntriesStopTimeEntryOutResponseDataTimeEntryIn, OptionalTimeEntriesStopTimeEntryOutResponseDataTimeEntryIn):
    pass
