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

from sesame_hr_python_sdk.pydantic.vacation_day_off_list_response_data_item_calendar_vacation_configuration_not_allowed_date_ranges import VacationDayOffListResponseDataItemCalendarVacationConfigurationNotAllowedDateRanges

class VacationDayOffListResponseDataItemCalendarVacationConfiguration(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    name: typing.Optional[str] = Field(None, alias='name')

    employee_request_enabled: typing.Optional[bool] = Field(None, alias='employeeRequestEnabled')

    needs_validation: typing.Optional[bool] = Field(None, alias='needsValidation')

    day_type: typing.Optional[Literal["business_day", "calendar_day"]] = Field(None, alias='dayType')

    max_days_off: typing.Optional[int] = Field(None, alias='maxDaysOff')

    is_default: typing.Optional[bool] = Field(None, alias='isDefault')

    not_allowed_date_ranges: typing.Optional[VacationDayOffListResponseDataItemCalendarVacationConfigurationNotAllowedDateRanges] = Field(None, alias='notAllowedDateRanges')

    created_at: typing.Optional[str] = Field(None, alias='createdAt')

    updated_at: typing.Optional[str] = Field(None, alias='updatedAt')

    created_by: typing.Optional[str] = Field(None, alias='createdBy')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
