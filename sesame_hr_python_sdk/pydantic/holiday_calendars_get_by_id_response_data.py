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

from sesame_hr_python_sdk.pydantic.holiday_calendars_get_by_id_response_data_day_off import HolidayCalendarsGetByIdResponseDataDayOff

class HolidayCalendarsGetByIdResponseData(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    # The name of the holidays
    name: typing.Optional[str] = Field(None, alias='name')

    company_id: typing.Optional[str] = Field(None, alias='companyId')

    day_off: typing.Optional[HolidayCalendarsGetByIdResponseDataDayOff] = Field(None, alias='dayOff')

    type_id: typing.Optional[str] = Field(None, alias='typeId')

    default: typing.Optional[bool] = Field(None, alias='default')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
