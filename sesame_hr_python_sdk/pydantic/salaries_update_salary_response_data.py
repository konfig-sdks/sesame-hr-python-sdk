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


class SalariesUpdateSalaryResponseData(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    pay_period: typing.Optional[Literal["daily", "weekly", "biweekly", "monthly", "yearly"]] = Field(None, alias='payPeriod')

    currency: typing.Optional[str] = Field(None, alias='currency')

    gross_salary: typing.Optional[int] = Field(None, alias='grossSalary')

    payments: typing.Optional[int] = Field(None, alias='payments')

    contribution_group: typing.Optional[str] = Field(None, alias='contributionGroup')

    start_date: typing.Optional[date] = Field(None, alias='startDate')

    end_date: typing.Optional[date] = Field(None, alias='endDate')

    comments: typing.Optional[str] = Field(None, alias='comments')

    monthly_gross_salary: typing.Optional[int] = Field(None, alias='monthlyGrossSalary')

    created_at: typing.Optional[str] = Field(None, alias='createdAt')

    updated_at: typing.Optional[str] = Field(None, alias='updatedAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
