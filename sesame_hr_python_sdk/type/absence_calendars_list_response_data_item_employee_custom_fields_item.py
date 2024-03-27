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


class RequiredAbsenceCalendarsListResponseDataItemEmployeeCustomFieldsItem(TypedDict):
    pass

class OptionalAbsenceCalendarsListResponseDataItemEmployeeCustomFieldsItem(TypedDict, total=False):
    id: str

    companyId: str

    name: str

    slug: str

    type: str

    value: typing.Union[str]

class AbsenceCalendarsListResponseDataItemEmployeeCustomFieldsItem(RequiredAbsenceCalendarsListResponseDataItemEmployeeCustomFieldsItem, OptionalAbsenceCalendarsListResponseDataItemEmployeeCustomFieldsItem):
    pass
