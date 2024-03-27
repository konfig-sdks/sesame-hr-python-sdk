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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from sesame_hr_python_sdk.pydantic.work_entries_list_response_data_item_employee import WorkEntriesListResponseDataItemEmployee
from sesame_hr_python_sdk.pydantic.work_entries_list_response_data_item_work_entry_in import WorkEntriesListResponseDataItemWorkEntryIn
from sesame_hr_python_sdk.pydantic.work_entries_list_response_data_item_work_entry_out import WorkEntriesListResponseDataItemWorkEntryOut

class WorkEntriesListResponseDataItem(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    work_check_type_id: typing.Optional[str] = Field(None, alias='workCheckTypeId')

    employee: typing.Optional[WorkEntriesListResponseDataItemEmployee] = Field(None, alias='employee')

    work_entry_type: typing.Optional[str] = Field(None, alias='workEntryType')

    work_entry_in: typing.Optional[WorkEntriesListResponseDataItemWorkEntryIn] = Field(None, alias='workEntryIn')

    work_entry_out: typing.Optional[WorkEntriesListResponseDataItemWorkEntryOut] = Field(None, alias='workEntryOut')

    worked_seconds: typing.Optional[typing.Union[int, float]] = Field(None, alias='workedSeconds')

    created_at: typing.Optional[str] = Field(None, alias='createdAt')

    updated_at: typing.Optional[str] = Field(None, alias='updatedAt')

    deleted_at: typing.Optional[str] = Field(None, alias='deletedAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
