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

from sesame_hr_python_sdk.type.employee_department_assignations_assign_department_to_employee_response_data import EmployeeDepartmentAssignationsAssignDepartmentToEmployeeResponseData
from sesame_hr_python_sdk.type.employee_department_assignations_assign_department_to_employee_response_meta import EmployeeDepartmentAssignationsAssignDepartmentToEmployeeResponseMeta

class RequiredEmployeeDepartmentAssignationsAssignDepartmentToEmployeeResponse(TypedDict):
    pass

class OptionalEmployeeDepartmentAssignationsAssignDepartmentToEmployeeResponse(TypedDict, total=False):
    data: EmployeeDepartmentAssignationsAssignDepartmentToEmployeeResponseData

    meta: EmployeeDepartmentAssignationsAssignDepartmentToEmployeeResponseMeta

class EmployeeDepartmentAssignationsAssignDepartmentToEmployeeResponse(RequiredEmployeeDepartmentAssignationsAssignDepartmentToEmployeeResponse, OptionalEmployeeDepartmentAssignationsAssignDepartmentToEmployeeResponse):
    pass
