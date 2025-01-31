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


class RequiredAbsenceDayOffRequestsCreateDayOffRequestResponseDataAbsenceCalendarDaysOffItem(TypedDict):
    pass

class OptionalAbsenceDayOffRequestsCreateDayOffRequestResponseDataAbsenceCalendarDaysOffItem(TypedDict, total=False):
    date: date

    seconds: int

    startTime: str

    endTime: str

class AbsenceDayOffRequestsCreateDayOffRequestResponseDataAbsenceCalendarDaysOffItem(RequiredAbsenceDayOffRequestsCreateDayOffRequestResponseDataAbsenceCalendarDaysOffItem, OptionalAbsenceDayOffRequestsCreateDayOffRequestResponseDataAbsenceCalendarDaysOffItem):
    pass
