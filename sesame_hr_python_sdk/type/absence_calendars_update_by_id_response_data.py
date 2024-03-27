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

from sesame_hr_python_sdk.type.absence_calendars_update_by_id_response_data_absence_type import AbsenceCalendarsUpdateByIdResponseDataAbsenceType
from sesame_hr_python_sdk.type.absence_calendars_update_by_id_response_data_days_off import AbsenceCalendarsUpdateByIdResponseDataDaysOff
from sesame_hr_python_sdk.type.absence_calendars_update_by_id_response_data_employee import AbsenceCalendarsUpdateByIdResponseDataEmployee

class RequiredAbsenceCalendarsUpdateByIdResponseData(TypedDict):
    pass

class OptionalAbsenceCalendarsUpdateByIdResponseData(TypedDict, total=False):
    id: str

    employee: AbsenceCalendarsUpdateByIdResponseDataEmployee

    daysOff: AbsenceCalendarsUpdateByIdResponseDataDaysOff

    maxDaysOff: int

    year: int

    absenceType: AbsenceCalendarsUpdateByIdResponseDataAbsenceType

    createdAt: str

    updatedAt: str

    deletedAt: typing.Optional[str]

class AbsenceCalendarsUpdateByIdResponseData(RequiredAbsenceCalendarsUpdateByIdResponseData, OptionalAbsenceCalendarsUpdateByIdResponseData):
    pass
