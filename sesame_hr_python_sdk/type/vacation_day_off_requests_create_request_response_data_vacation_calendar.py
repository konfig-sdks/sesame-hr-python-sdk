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

from sesame_hr_python_sdk.type.vacation_day_off_requests_create_request_response_data_vacation_calendar_days_off import VacationDayOffRequestsCreateRequestResponseDataVacationCalendarDaysOff
from sesame_hr_python_sdk.type.vacation_day_off_requests_create_request_response_data_vacation_calendar_employee import VacationDayOffRequestsCreateRequestResponseDataVacationCalendarEmployee
from sesame_hr_python_sdk.type.vacation_day_off_requests_create_request_response_data_vacation_calendar_vacation_configuration import VacationDayOffRequestsCreateRequestResponseDataVacationCalendarVacationConfiguration

class RequiredVacationDayOffRequestsCreateRequestResponseDataVacationCalendar(TypedDict):
    pass

class OptionalVacationDayOffRequestsCreateRequestResponseDataVacationCalendar(TypedDict, total=False):
    id: str

    employee: VacationDayOffRequestsCreateRequestResponseDataVacationCalendarEmployee

    daysOff: VacationDayOffRequestsCreateRequestResponseDataVacationCalendarDaysOff

    maxDaysOff: int

    year: int

    vacationConfiguration: VacationDayOffRequestsCreateRequestResponseDataVacationCalendarVacationConfiguration

    createdAt: str

    updatedAt: str

    deletedAt: str

class VacationDayOffRequestsCreateRequestResponseDataVacationCalendar(RequiredVacationDayOffRequestsCreateRequestResponseDataVacationCalendar, OptionalVacationDayOffRequestsCreateRequestResponseDataVacationCalendar):
    pass
