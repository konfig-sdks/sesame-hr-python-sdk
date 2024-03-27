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

from sesame_hr_python_sdk.pydantic.work_entries_create_new_entry_response_data_work_entry_in_coordinates import WorkEntriesCreateNewEntryResponseDataWorkEntryInCoordinates

class WorkEntriesCreateNewEntryResponseDataWorkEntryIn(BaseModel):
    origin: typing.Optional[str] = Field(None, alias='origin')

    date: typing.Optional[str] = Field(None, alias='date')

    coordinates: typing.Optional[WorkEntriesCreateNewEntryResponseDataWorkEntryInCoordinates] = Field(None, alias='coordinates')

    office_id: typing.Optional[str] = Field(None, alias='officeId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
