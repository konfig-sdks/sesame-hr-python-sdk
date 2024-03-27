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

from sesame_hr_python_sdk.pydantic.vacation_day_off_requests_create_request_response_data_vacation_calendar_vacation_configuration_company import VacationDayOffRequestsCreateRequestResponseDataVacationCalendarVacationConfigurationCompany
from sesame_hr_python_sdk.pydantic.vacation_day_off_requests_create_request_response_data_vacation_calendar_vacation_configuration_not_allowed_date_ranges import VacationDayOffRequestsCreateRequestResponseDataVacationCalendarVacationConfigurationNotAllowedDateRanges

class VacationDayOffRequestsCreateRequestResponseDataVacationCalendarVacationConfiguration(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    name: typing.Optional[str] = Field(None, alias='name')

    employee_request_enabled: typing.Optional[bool] = Field(None, alias='employeeRequestEnabled')

    needs_validation: typing.Optional[bool] = Field(None, alias='needsValidation')

    company: typing.Optional[VacationDayOffRequestsCreateRequestResponseDataVacationCalendarVacationConfigurationCompany] = Field(None, alias='company')

    day_type: typing.Optional[Literal["business_day", "calendar_day"]] = Field(None, alias='dayType')

    max_days_off: typing.Optional[int] = Field(None, alias='maxDaysOff')

    is_default: typing.Optional[bool] = Field(None, alias='isDefault')

    not_allowed_date_ranges: typing.Optional[VacationDayOffRequestsCreateRequestResponseDataVacationCalendarVacationConfigurationNotAllowedDateRanges] = Field(None, alias='notAllowedDateRanges')

    creation_date_next_year: typing.Optional[str] = Field(None, alias='creationDateNextYear')

    created_at: typing.Optional[str] = Field(None, alias='createdAt')

    updated_at: typing.Optional[str] = Field(None, alias='updatedAt')

    deleted_at: typing.Optional[typing.Optional[str]] = Field(None, alias='deletedAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
