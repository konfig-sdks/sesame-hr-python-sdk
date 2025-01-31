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

from sesame_hr_python_sdk.type.absence_day_off_requests_accept_request_response_data_absence_calendar_absence_type import AbsenceDayOffRequestsAcceptRequestResponseDataAbsenceCalendarAbsenceType
from sesame_hr_python_sdk.type.absence_day_off_requests_accept_request_response_data_absence_calendar_days_off import AbsenceDayOffRequestsAcceptRequestResponseDataAbsenceCalendarDaysOff
from sesame_hr_python_sdk.type.absence_day_off_requests_accept_request_response_data_absence_calendar_employee import AbsenceDayOffRequestsAcceptRequestResponseDataAbsenceCalendarEmployee

class RequiredAbsenceDayOffRequestsAcceptRequestResponseDataAbsenceCalendar(TypedDict):
    pass

class OptionalAbsenceDayOffRequestsAcceptRequestResponseDataAbsenceCalendar(TypedDict, total=False):
    id: str

    employee: AbsenceDayOffRequestsAcceptRequestResponseDataAbsenceCalendarEmployee

    daysOff: AbsenceDayOffRequestsAcceptRequestResponseDataAbsenceCalendarDaysOff

    maxDaysOff: int

    year: int

    absenceType: AbsenceDayOffRequestsAcceptRequestResponseDataAbsenceCalendarAbsenceType

    createdAt: str

    updatedAt: str

    deletedAt: typing.Optional[str]

class AbsenceDayOffRequestsAcceptRequestResponseDataAbsenceCalendar(RequiredAbsenceDayOffRequestsAcceptRequestResponseDataAbsenceCalendar, OptionalAbsenceDayOffRequestsAcceptRequestResponseDataAbsenceCalendar):
    pass
