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

from sesame_hr_python_sdk.type.absence_calendars_update_by_id_response_data_absence_type_company import AbsenceCalendarsUpdateByIdResponseDataAbsenceTypeCompany

class RequiredAbsenceCalendarsUpdateByIdResponseDataAbsenceType(TypedDict):
    pass

class OptionalAbsenceCalendarsUpdateByIdResponseDataAbsenceType(TypedDict, total=False):
    id: str

    name: str

    needsValidation: bool

    company: AbsenceCalendarsUpdateByIdResponseDataAbsenceTypeCompany

    createdAt: str

    updatedAt: str

    deletedAt: typing.Optional[str]

    type: str

    pickMode: str

class AbsenceCalendarsUpdateByIdResponseDataAbsenceType(RequiredAbsenceCalendarsUpdateByIdResponseDataAbsenceType, OptionalAbsenceCalendarsUpdateByIdResponseDataAbsenceType):
    pass
