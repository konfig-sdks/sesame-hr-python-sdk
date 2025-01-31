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

from sesame_hr_python_sdk.pydantic.vacation_day_off_requests_list_response_data_item_days_off import VacationDayOffRequestsListResponseDataItemDaysOff
from sesame_hr_python_sdk.pydantic.vacation_day_off_requests_list_response_data_item_employee import VacationDayOffRequestsListResponseDataItemEmployee
from sesame_hr_python_sdk.pydantic.vacation_day_off_requests_list_response_data_item_vacation_calendar import VacationDayOffRequestsListResponseDataItemVacationCalendar

class VacationDayOffRequestsListResponseDataItem(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    vacation_calendar: typing.Optional[VacationDayOffRequestsListResponseDataItemVacationCalendar] = Field(None, alias='vacationCalendar')

    employee: typing.Optional[VacationDayOffRequestsListResponseDataItemEmployee] = Field(None, alias='employee')

    days_off: typing.Optional[VacationDayOffRequestsListResponseDataItemDaysOff] = Field(None, alias='daysOff')

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
