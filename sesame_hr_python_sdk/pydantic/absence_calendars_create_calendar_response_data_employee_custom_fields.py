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

from sesame_hr_python_sdk.pydantic.absence_calendars_create_calendar_response_data_employee_custom_fields_item import AbsenceCalendarsCreateCalendarResponseDataEmployeeCustomFieldsItem

AbsenceCalendarsCreateCalendarResponseDataEmployeeCustomFields = typing.List[AbsenceCalendarsCreateCalendarResponseDataEmployeeCustomFieldsItem]
