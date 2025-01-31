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

from sesame_hr_python_sdk.type.absence_calendars_list_response_data_item_absence_type import AbsenceCalendarsListResponseDataItemAbsenceType
from sesame_hr_python_sdk.type.absence_calendars_list_response_data_item_days_off import AbsenceCalendarsListResponseDataItemDaysOff
from sesame_hr_python_sdk.type.absence_calendars_list_response_data_item_employee import AbsenceCalendarsListResponseDataItemEmployee

class RequiredAbsenceCalendarsListResponseDataItem(TypedDict):
    pass

class OptionalAbsenceCalendarsListResponseDataItem(TypedDict, total=False):
    id: str

    employee: AbsenceCalendarsListResponseDataItemEmployee

    daysOff: AbsenceCalendarsListResponseDataItemDaysOff

    maxDaysOff: int

    year: int

    absenceType: AbsenceCalendarsListResponseDataItemAbsenceType

    createdAt: str

    updatedAt: str

    deletedAt: typing.Optional[str]

class AbsenceCalendarsListResponseDataItem(RequiredAbsenceCalendarsListResponseDataItem, OptionalAbsenceCalendarsListResponseDataItem):
    pass
