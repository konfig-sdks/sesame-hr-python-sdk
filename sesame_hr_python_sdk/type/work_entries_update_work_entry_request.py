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


class RequiredWorkEntriesUpdateWorkEntryRequest(TypedDict):
    # value should be \"work\"
    workEntryType: str

    workEntryIn: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class OptionalWorkEntriesUpdateWorkEntryRequest(TypedDict, total=False):
    workEntryOut: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class WorkEntriesUpdateWorkEntryRequest(RequiredWorkEntriesUpdateWorkEntryRequest, OptionalWorkEntriesUpdateWorkEntryRequest):
    pass
