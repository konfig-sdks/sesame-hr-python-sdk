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


class RequiredEmployeeScheduleTemplatesCreateEmployeeScheduleTemplateRequest(TypedDict):
    # Employee UUID
    employeeId: str

    # Schedule template UUID
    scheduleTemplateId: str

    # Start date
    startDate: date

class OptionalEmployeeScheduleTemplatesCreateEmployeeScheduleTemplateRequest(TypedDict, total=False):
    # End date
    endDate: date

class EmployeeScheduleTemplatesCreateEmployeeScheduleTemplateRequest(RequiredEmployeeScheduleTemplatesCreateEmployeeScheduleTemplateRequest, OptionalEmployeeScheduleTemplatesCreateEmployeeScheduleTemplateRequest):
    pass
