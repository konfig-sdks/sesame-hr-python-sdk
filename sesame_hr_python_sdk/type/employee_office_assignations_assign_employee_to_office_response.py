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

from sesame_hr_python_sdk.type.employee_office_assignations_assign_employee_to_office_response_data import EmployeeOfficeAssignationsAssignEmployeeToOfficeResponseData
from sesame_hr_python_sdk.type.employee_office_assignations_assign_employee_to_office_response_meta import EmployeeOfficeAssignationsAssignEmployeeToOfficeResponseMeta

class RequiredEmployeeOfficeAssignationsAssignEmployeeToOfficeResponse(TypedDict):
    pass

class OptionalEmployeeOfficeAssignationsAssignEmployeeToOfficeResponse(TypedDict, total=False):
    data: EmployeeOfficeAssignationsAssignEmployeeToOfficeResponseData

    meta: EmployeeOfficeAssignationsAssignEmployeeToOfficeResponseMeta

class EmployeeOfficeAssignationsAssignEmployeeToOfficeResponse(RequiredEmployeeOfficeAssignationsAssignEmployeeToOfficeResponse, OptionalEmployeeOfficeAssignationsAssignEmployeeToOfficeResponse):
    pass
