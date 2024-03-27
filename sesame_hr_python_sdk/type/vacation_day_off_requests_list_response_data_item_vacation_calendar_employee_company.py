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


class RequiredVacationDayOffRequestsListResponseDataItemVacationCalendarEmployeeCompany(TypedDict):
    pass

class OptionalVacationDayOffRequestsListResponseDataItemVacationCalendarEmployeeCompany(TypedDict, total=False):
    id: str

    name: str

    notificationEmail: str

    language: str

    createdAt: str

    updatedAt: str

class VacationDayOffRequestsListResponseDataItemVacationCalendarEmployeeCompany(RequiredVacationDayOffRequestsListResponseDataItemVacationCalendarEmployeeCompany, OptionalVacationDayOffRequestsListResponseDataItemVacationCalendarEmployeeCompany):
    pass
