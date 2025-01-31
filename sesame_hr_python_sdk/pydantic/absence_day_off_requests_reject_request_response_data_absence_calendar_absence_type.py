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

from sesame_hr_python_sdk.pydantic.absence_day_off_requests_reject_request_response_data_absence_calendar_absence_type_company import AbsenceDayOffRequestsRejectRequestResponseDataAbsenceCalendarAbsenceTypeCompany

class AbsenceDayOffRequestsRejectRequestResponseDataAbsenceCalendarAbsenceType(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    name: typing.Optional[str] = Field(None, alias='name')

    needs_validation: typing.Optional[bool] = Field(None, alias='needsValidation')

    company: typing.Optional[AbsenceDayOffRequestsRejectRequestResponseDataAbsenceCalendarAbsenceTypeCompany] = Field(None, alias='company')

    created_at: typing.Optional[str] = Field(None, alias='createdAt')

    updated_at: typing.Optional[str] = Field(None, alias='updatedAt')

    deleted_at: typing.Optional[typing.Optional[str]] = Field(None, alias='deletedAt')

    type: typing.Optional[Literal["normal", "private"]] = Field(None, alias='type')

    pick_mode: typing.Optional[Literal["by_days", "by_time_range"]] = Field(None, alias='pickMode')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
