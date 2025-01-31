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

from sesame_hr_python_sdk.type.time_entries_update_entry_response_data_employee import TimeEntriesUpdateEntryResponseDataEmployee
from sesame_hr_python_sdk.type.time_entries_update_entry_response_data_tag_ids import TimeEntriesUpdateEntryResponseDataTagIds
from sesame_hr_python_sdk.type.time_entries_update_entry_response_data_time_entry_in import TimeEntriesUpdateEntryResponseDataTimeEntryIn
from sesame_hr_python_sdk.type.time_entries_update_entry_response_data_time_entry_out import TimeEntriesUpdateEntryResponseDataTimeEntryOut

class RequiredTimeEntriesUpdateEntryResponseData(TypedDict):
    pass

class OptionalTimeEntriesUpdateEntryResponseData(TypedDict, total=False):
    id: str

    employee: TimeEntriesUpdateEntryResponseDataEmployee

    projectId: str

    tagIds: TimeEntriesUpdateEntryResponseDataTagIds

    timeEntryIn: TimeEntriesUpdateEntryResponseDataTimeEntryIn

    timeEntryOut: TimeEntriesUpdateEntryResponseDataTimeEntryOut

    comment: str

    createdAt: str

    updatedAt: str

    deletedAt: typing.Optional[str]

class TimeEntriesUpdateEntryResponseData(RequiredTimeEntriesUpdateEntryResponseData, OptionalTimeEntriesUpdateEntryResponseData):
    pass
