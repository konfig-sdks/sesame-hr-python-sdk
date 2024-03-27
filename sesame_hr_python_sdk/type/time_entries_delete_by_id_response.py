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

from sesame_hr_python_sdk.type.time_entries_delete_by_id_response_meta import TimeEntriesDeleteByIdResponseMeta

class RequiredTimeEntriesDeleteByIdResponse(TypedDict):
    pass

class OptionalTimeEntriesDeleteByIdResponse(TypedDict, total=False):
    data: str

    meta: TimeEntriesDeleteByIdResponseMeta

class TimeEntriesDeleteByIdResponse(RequiredTimeEntriesDeleteByIdResponse, OptionalTimeEntriesDeleteByIdResponse):
    pass
