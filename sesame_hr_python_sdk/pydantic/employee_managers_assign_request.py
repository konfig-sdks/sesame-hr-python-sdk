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


class EmployeeManagersAssignRequest(BaseModel):
    # The identifier of the employee
    employee_id: str = Field(alias='employeeId')

    # The identifier of the employee manager
    manager_id: str = Field(alias='managerId')

    # Type of validation manager
    permission: Literal["check", "vacation"] = Field(alias='permission')

    # The validator order
    order: Literal[0, 1] = Field(alias='order')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
