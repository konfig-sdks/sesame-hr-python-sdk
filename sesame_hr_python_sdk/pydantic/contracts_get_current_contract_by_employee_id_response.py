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

from sesame_hr_python_sdk.pydantic.contracts_get_current_contract_by_employee_id_response_data import ContractsGetCurrentContractByEmployeeIdResponseData
from sesame_hr_python_sdk.pydantic.contracts_get_current_contract_by_employee_id_response_meta import ContractsGetCurrentContractByEmployeeIdResponseMeta

class ContractsGetCurrentContractByEmployeeIdResponse(BaseModel):
    data: typing.Optional[ContractsGetCurrentContractByEmployeeIdResponseData] = Field(None, alias='data')

    meta: typing.Optional[ContractsGetCurrentContractByEmployeeIdResponseMeta] = Field(None, alias='meta')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
