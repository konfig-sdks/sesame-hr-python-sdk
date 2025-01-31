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

from sesame_hr_python_sdk.pydantic.absence_calendars_list_response_data_item_absence_type import AbsenceCalendarsListResponseDataItemAbsenceType
from sesame_hr_python_sdk.pydantic.absence_calendars_list_response_data_item_days_off import AbsenceCalendarsListResponseDataItemDaysOff
from sesame_hr_python_sdk.pydantic.absence_calendars_list_response_data_item_employee import AbsenceCalendarsListResponseDataItemEmployee

class AbsenceCalendarsListResponseDataItem(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    employee: typing.Optional[AbsenceCalendarsListResponseDataItemEmployee] = Field(None, alias='employee')

    days_off: typing.Optional[AbsenceCalendarsListResponseDataItemDaysOff] = Field(None, alias='daysOff')

    max_days_off: typing.Optional[int] = Field(None, alias='maxDaysOff')

    year: typing.Optional[int] = Field(None, alias='year')

    absence_type: typing.Optional[AbsenceCalendarsListResponseDataItemAbsenceType] = Field(None, alias='absenceType')

    created_at: typing.Optional[str] = Field(None, alias='createdAt')

    updated_at: typing.Optional[str] = Field(None, alias='updatedAt')

    deleted_at: typing.Optional[typing.Optional[str]] = Field(None, alias='deletedAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
