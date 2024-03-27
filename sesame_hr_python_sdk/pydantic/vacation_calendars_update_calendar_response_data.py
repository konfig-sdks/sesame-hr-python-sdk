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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from sesame_hr_python_sdk.pydantic.vacation_calendars_update_calendar_response_data_days_off import VacationCalendarsUpdateCalendarResponseDataDaysOff
from sesame_hr_python_sdk.pydantic.vacation_calendars_update_calendar_response_data_employee import VacationCalendarsUpdateCalendarResponseDataEmployee
from sesame_hr_python_sdk.pydantic.vacation_calendars_update_calendar_response_data_vacation_configuration import VacationCalendarsUpdateCalendarResponseDataVacationConfiguration

class VacationCalendarsUpdateCalendarResponseData(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    employee: typing.Optional[VacationCalendarsUpdateCalendarResponseDataEmployee] = Field(None, alias='employee')

    days_off: typing.Optional[VacationCalendarsUpdateCalendarResponseDataDaysOff] = Field(None, alias='daysOff')

    max_days_off: typing.Optional[int] = Field(None, alias='maxDaysOff')

    year: typing.Optional[int] = Field(None, alias='year')

    vacation_configuration: typing.Optional[VacationCalendarsUpdateCalendarResponseDataVacationConfiguration] = Field(None, alias='vacationConfiguration')

    created_at: typing.Optional[str] = Field(None, alias='createdAt')

    updated_at: typing.Optional[str] = Field(None, alias='updatedAt')

    deleted_at: typing.Optional[str] = Field(None, alias='deletedAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
