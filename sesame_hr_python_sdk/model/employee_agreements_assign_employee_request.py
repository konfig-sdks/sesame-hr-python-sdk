# coding: utf-8

"""
    Sesame Public API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from sesame_hr_python_sdk import schemas  # noqa: F401


class EmployeeAgreementsAssignEmployeeRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "agreementId",
            "employeeId",
            "startDate",
        }
        
        class properties:
            agreementId = schemas.UUIDSchema
            employeeId = schemas.UUIDSchema
            startDate = schemas.DateSchema
            __annotations__ = {
                "agreementId": agreementId,
                "employeeId": employeeId,
                "startDate": startDate,
            }
    
    agreementId: MetaOapg.properties.agreementId
    employeeId: MetaOapg.properties.employeeId
    startDate: MetaOapg.properties.startDate
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["agreementId"]) -> MetaOapg.properties.agreementId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeId"]) -> MetaOapg.properties.employeeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["agreementId", "employeeId", "startDate", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["agreementId"]) -> MetaOapg.properties.agreementId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeId"]) -> MetaOapg.properties.employeeId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["agreementId", "employeeId", "startDate", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        agreementId: typing.Union[MetaOapg.properties.agreementId, str, uuid.UUID, ],
        employeeId: typing.Union[MetaOapg.properties.employeeId, str, uuid.UUID, ],
        startDate: typing.Union[MetaOapg.properties.startDate, str, date, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeeAgreementsAssignEmployeeRequest':
        return super().__new__(
            cls,
            *args,
            agreementId=agreementId,
            employeeId=employeeId,
            startDate=startDate,
            _configuration=_configuration,
            **kwargs,
        )
