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

from sesame_hr_python_sdk.type.employees_remove_by_id_response_meta import EmployeesRemoveByIdResponseMeta

class RequiredEmployeesRemoveByIdResponse(TypedDict):
    pass

class OptionalEmployeesRemoveByIdResponse(TypedDict, total=False):
    data: str

    meta: EmployeesRemoveByIdResponseMeta

class EmployeesRemoveByIdResponse(RequiredEmployeesRemoveByIdResponse, OptionalEmployeesRemoveByIdResponse):
    pass
