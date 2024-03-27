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

from sesame_hr_python_sdk.pydantic.vacation_day_off_requests_create_request_response_data_days_off import VacationDayOffRequestsCreateRequestResponseDataDaysOff
from sesame_hr_python_sdk.pydantic.vacation_day_off_requests_create_request_response_data_employee import VacationDayOffRequestsCreateRequestResponseDataEmployee
from sesame_hr_python_sdk.pydantic.vacation_day_off_requests_create_request_response_data_vacation_calendar import VacationDayOffRequestsCreateRequestResponseDataVacationCalendar

class VacationDayOffRequestsCreateRequestResponseData(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    vacation_calendar: typing.Optional[VacationDayOffRequestsCreateRequestResponseDataVacationCalendar] = Field(None, alias='vacationCalendar')

    employee: typing.Optional[VacationDayOffRequestsCreateRequestResponseDataEmployee] = Field(None, alias='employee')

    days_off: typing.Optional[VacationDayOffRequestsCreateRequestResponseDataDaysOff] = Field(None, alias='daysOff')

    status: typing.Optional[Literal["accepted", "rejected", "pending"]] = Field(None, alias='status')

    type: typing.Optional[Literal["create", "delete"]] = Field(None, alias='type')

    comment: typing.Optional[str] = Field(None, alias='comment')

    resolution_comment: typing.Optional[str] = Field(None, alias='resolutionComment')

    resolved_at: typing.Optional[str] = Field(None, alias='resolvedAt')

    created_at: typing.Optional[str] = Field(None, alias='createdAt')

    updated_at: typing.Optional[str] = Field(None, alias='updatedAt')

    deleted_at: typing.Optional[str] = Field(None, alias='deletedAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
