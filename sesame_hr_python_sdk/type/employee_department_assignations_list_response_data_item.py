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

from sesame_hr_python_sdk.type.employee_department_assignations_list_response_data_item_department import EmployeeDepartmentAssignationsListResponseDataItemDepartment
from sesame_hr_python_sdk.type.employee_department_assignations_list_response_data_item_employee import EmployeeDepartmentAssignationsListResponseDataItemEmployee

class RequiredEmployeeDepartmentAssignationsListResponseDataItem(TypedDict):
    pass

class OptionalEmployeeDepartmentAssignationsListResponseDataItem(TypedDict, total=False):
    id: str

    employee: EmployeeDepartmentAssignationsListResponseDataItemEmployee

    department: EmployeeDepartmentAssignationsListResponseDataItemDepartment

    createdAt: str

    updatedAt: str

class EmployeeDepartmentAssignationsListResponseDataItem(RequiredEmployeeDepartmentAssignationsListResponseDataItem, OptionalEmployeeDepartmentAssignationsListResponseDataItem):
    pass
