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


class SalariesCreateSalaryRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "payPeriod",
            "payments",
            "currency",
            "employeeId",
            "grossSalary",
            "contributionGroupId",
            "startDate",
        }
        
        class properties:
            employeeId = schemas.UUIDSchema
            
            
            class payPeriod(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def DAILY(cls):
                    return cls("daily")
                
                @schemas.classproperty
                def WEEKLY(cls):
                    return cls("weekly")
                
                @schemas.classproperty
                def BIWEEKLY(cls):
                    return cls("biweekly")
                
                @schemas.classproperty
                def MONTHLY(cls):
                    return cls("monthly")
                
                @schemas.classproperty
                def YEARLY(cls):
                    return cls("yearly")
            currency = schemas.StrSchema
            grossSalary = schemas.Float32Schema
            payments = schemas.IntSchema
            contributionGroupId = schemas.UUIDSchema
            startDate = schemas.DateSchema
            endDate = schemas.DateSchema
            comments = schemas.StrSchema
            __annotations__ = {
                "employeeId": employeeId,
                "payPeriod": payPeriod,
                "currency": currency,
                "grossSalary": grossSalary,
                "payments": payments,
                "contributionGroupId": contributionGroupId,
                "startDate": startDate,
                "endDate": endDate,
                "comments": comments,
            }
    
    payPeriod: MetaOapg.properties.payPeriod
    payments: MetaOapg.properties.payments
    currency: MetaOapg.properties.currency
    employeeId: MetaOapg.properties.employeeId
    grossSalary: MetaOapg.properties.grossSalary
    contributionGroupId: MetaOapg.properties.contributionGroupId
    startDate: MetaOapg.properties.startDate
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeId"]) -> MetaOapg.properties.employeeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payPeriod"]) -> MetaOapg.properties.payPeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["grossSalary"]) -> MetaOapg.properties.grossSalary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payments"]) -> MetaOapg.properties.payments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contributionGroupId"]) -> MetaOapg.properties.contributionGroupId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endDate"]) -> MetaOapg.properties.endDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comments"]) -> MetaOapg.properties.comments: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["employeeId", "payPeriod", "currency", "grossSalary", "payments", "contributionGroupId", "startDate", "endDate", "comments", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeId"]) -> MetaOapg.properties.employeeId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payPeriod"]) -> MetaOapg.properties.payPeriod: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["grossSalary"]) -> MetaOapg.properties.grossSalary: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payments"]) -> MetaOapg.properties.payments: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contributionGroupId"]) -> MetaOapg.properties.contributionGroupId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endDate"]) -> typing.Union[MetaOapg.properties.endDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comments"]) -> typing.Union[MetaOapg.properties.comments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["employeeId", "payPeriod", "currency", "grossSalary", "payments", "contributionGroupId", "startDate", "endDate", "comments", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        payPeriod: typing.Union[MetaOapg.properties.payPeriod, str, ],
        payments: typing.Union[MetaOapg.properties.payments, decimal.Decimal, int, ],
        currency: typing.Union[MetaOapg.properties.currency, str, ],
        employeeId: typing.Union[MetaOapg.properties.employeeId, str, uuid.UUID, ],
        grossSalary: typing.Union[MetaOapg.properties.grossSalary, decimal.Decimal, int, float, ],
        contributionGroupId: typing.Union[MetaOapg.properties.contributionGroupId, str, uuid.UUID, ],
        startDate: typing.Union[MetaOapg.properties.startDate, str, date, ],
        endDate: typing.Union[MetaOapg.properties.endDate, str, date, schemas.Unset] = schemas.unset,
        comments: typing.Union[MetaOapg.properties.comments, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SalariesCreateSalaryRequest':
        return super().__new__(
            cls,
            *args,
            payPeriod=payPeriod,
            payments=payments,
            currency=currency,
            employeeId=employeeId,
            grossSalary=grossSalary,
            contributionGroupId=contributionGroupId,
            startDate=startDate,
            endDate=endDate,
            comments=comments,
            _configuration=_configuration,
            **kwargs,
        )
