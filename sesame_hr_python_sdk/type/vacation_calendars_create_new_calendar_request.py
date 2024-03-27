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

from sesame_hr_python_sdk.type.vacation_calendars_create_new_calendar_request_days_off import VacationCalendarsCreateNewCalendarRequestDaysOff

class RequiredVacationCalendarsCreateNewCalendarRequest(TypedDict):
    employeeId: str

    vacationConfigurationId: str

    year: int

    daysOff: VacationCalendarsCreateNewCalendarRequestDaysOff

class OptionalVacationCalendarsCreateNewCalendarRequest(TypedDict, total=False):
    pass

class VacationCalendarsCreateNewCalendarRequest(RequiredVacationCalendarsCreateNewCalendarRequest, OptionalVacationCalendarsCreateNewCalendarRequest):
    pass
