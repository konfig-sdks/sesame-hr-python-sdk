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

from sesame_hr_python_sdk.pydantic.absence_calendars_update_by_id_request_days_off_item import AbsenceCalendarsUpdateByIdRequestDaysOffItem

AbsenceCalendarsUpdateByIdRequestDaysOff = typing.List[AbsenceCalendarsUpdateByIdRequestDaysOffItem]
