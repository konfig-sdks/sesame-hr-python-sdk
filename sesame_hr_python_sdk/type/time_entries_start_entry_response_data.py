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

from sesame_hr_python_sdk.type.time_entries_start_entry_response_data_employee import TimeEntriesStartEntryResponseDataEmployee
from sesame_hr_python_sdk.type.time_entries_start_entry_response_data_tag_ids import TimeEntriesStartEntryResponseDataTagIds
from sesame_hr_python_sdk.type.time_entries_start_entry_response_data_time_entry_in import TimeEntriesStartEntryResponseDataTimeEntryIn

class RequiredTimeEntriesStartEntryResponseData(TypedDict):
    pass

class OptionalTimeEntriesStartEntryResponseData(TypedDict, total=False):
    id: str

    employee: TimeEntriesStartEntryResponseDataEmployee

    projectId: str

    tagIds: TimeEntriesStartEntryResponseDataTagIds

    timeEntryIn: TimeEntriesStartEntryResponseDataTimeEntryIn

    timeEntryOut: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    comment: str

    createdAt: str

    updatedAt: str

    deletedAt: typing.Optional[str]

class TimeEntriesStartEntryResponseData(RequiredTimeEntriesStartEntryResponseData, OptionalTimeEntriesStartEntryResponseData):
    pass
