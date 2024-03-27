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

from sesame_hr_python_sdk.type.work_entries_update_work_entry_response_data_employee import WorkEntriesUpdateWorkEntryResponseDataEmployee
from sesame_hr_python_sdk.type.work_entries_update_work_entry_response_data_work_entry_in import WorkEntriesUpdateWorkEntryResponseDataWorkEntryIn
from sesame_hr_python_sdk.type.work_entries_update_work_entry_response_data_work_entry_out import WorkEntriesUpdateWorkEntryResponseDataWorkEntryOut

class RequiredWorkEntriesUpdateWorkEntryResponseData(TypedDict):
    pass

class OptionalWorkEntriesUpdateWorkEntryResponseData(TypedDict, total=False):
    id: str

    workCheckTypeId: str

    employee: WorkEntriesUpdateWorkEntryResponseDataEmployee

    workEntryType: str

    workEntryIn: WorkEntriesUpdateWorkEntryResponseDataWorkEntryIn

    workEntryOut: WorkEntriesUpdateWorkEntryResponseDataWorkEntryOut

    workedSeconds: typing.Union[int, float]

    createdAt: str

    updatedAt: str

    deletedAt: str

class WorkEntriesUpdateWorkEntryResponseData(RequiredWorkEntriesUpdateWorkEntryResponseData, OptionalWorkEntriesUpdateWorkEntryResponseData):
    pass
