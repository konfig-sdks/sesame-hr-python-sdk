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

from sesame_hr_python_sdk.type.holidays_assign_to_employee_response_data import HolidaysAssignToEmployeeResponseData
from sesame_hr_python_sdk.type.holidays_assign_to_employee_response_meta import HolidaysAssignToEmployeeResponseMeta

class RequiredHolidaysAssignToEmployeeResponse(TypedDict):
    pass

class OptionalHolidaysAssignToEmployeeResponse(TypedDict, total=False):
    data: HolidaysAssignToEmployeeResponseData

    meta: HolidaysAssignToEmployeeResponseMeta

class HolidaysAssignToEmployeeResponse(RequiredHolidaysAssignToEmployeeResponse, OptionalHolidaysAssignToEmployeeResponse):
    pass
