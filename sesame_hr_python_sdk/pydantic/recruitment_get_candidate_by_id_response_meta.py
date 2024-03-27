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


class RecruitmentGetCandidateByIdResponseMeta(BaseModel):
    current_page: typing.Optional[int] = Field(None, alias='currentPage')

    last_page: typing.Optional[int] = Field(None, alias='lastPage')

    total: typing.Optional[int] = Field(None, alias='total')

    per_page: typing.Optional[int] = Field(None, alias='perPage')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
