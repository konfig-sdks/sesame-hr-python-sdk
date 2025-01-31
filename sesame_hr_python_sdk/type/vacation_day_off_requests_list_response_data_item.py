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

from sesame_hr_python_sdk.type.vacation_day_off_requests_list_response_data_item_days_off import VacationDayOffRequestsListResponseDataItemDaysOff
from sesame_hr_python_sdk.type.vacation_day_off_requests_list_response_data_item_employee import VacationDayOffRequestsListResponseDataItemEmployee
from sesame_hr_python_sdk.type.vacation_day_off_requests_list_response_data_item_vacation_calendar import VacationDayOffRequestsListResponseDataItemVacationCalendar

class RequiredVacationDayOffRequestsListResponseDataItem(TypedDict):
    pass

class OptionalVacationDayOffRequestsListResponseDataItem(TypedDict, total=False):
    id: str

    vacationCalendar: VacationDayOffRequestsListResponseDataItemVacationCalendar

    employee: VacationDayOffRequestsListResponseDataItemEmployee

    daysOff: VacationDayOffRequestsListResponseDataItemDaysOff

    status: str

    type: str

    comment: str

    resolutionComment: str

    resolvedAt: str

    createdAt: str

    updatedAt: str

    deletedAt: str

class VacationDayOffRequestsListResponseDataItem(RequiredVacationDayOffRequestsListResponseDataItem, OptionalVacationDayOffRequestsListResponseDataItem):
    pass
