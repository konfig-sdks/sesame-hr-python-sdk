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

from sesame_hr_python_sdk.type.absence_types_list_response_data import AbsenceTypesListResponseData
from sesame_hr_python_sdk.type.absence_types_list_response_meta import AbsenceTypesListResponseMeta

class RequiredAbsenceTypesListResponse(TypedDict):
    pass

class OptionalAbsenceTypesListResponse(TypedDict, total=False):
    data: AbsenceTypesListResponseData

    meta: AbsenceTypesListResponseMeta

class AbsenceTypesListResponse(RequiredAbsenceTypesListResponse, OptionalAbsenceTypesListResponse):
    pass
