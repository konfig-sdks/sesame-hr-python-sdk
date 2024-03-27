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

from sesame_hr_python_sdk.type.employee_schedule_templates_list_templates_response_data_item20240101 import EmployeeScheduleTemplatesListTemplatesResponseDataItem20240101

RequiredEmployeeScheduleTemplatesListTemplatesResponseDataItem = TypedDict("RequiredEmployeeScheduleTemplatesListTemplatesResponseDataItem", {
    })

OptionalEmployeeScheduleTemplatesListTemplatesResponseDataItem = TypedDict("OptionalEmployeeScheduleTemplatesListTemplatesResponseDataItem", {
    "2024-01-01": EmployeeScheduleTemplatesListTemplatesResponseDataItem20240101,
    }, total=False)

class EmployeeScheduleTemplatesListTemplatesResponseDataItem(RequiredEmployeeScheduleTemplatesListTemplatesResponseDataItem, OptionalEmployeeScheduleTemplatesListTemplatesResponseDataItem):
    pass
