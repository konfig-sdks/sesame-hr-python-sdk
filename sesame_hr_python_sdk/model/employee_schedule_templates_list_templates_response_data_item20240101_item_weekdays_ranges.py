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


class EmployeeScheduleTemplatesListTemplatesResponseDataItem20240101ItemWeekdaysRanges(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.UUIDSchema
            weekday = schemas.StrSchema
            startTime = schemas.StrSchema
            endTime = schemas.StrSchema
            weekdayRangeType = schemas.StrSchema
            order = schemas.IntSchema
            __annotations__ = {
                "id": id,
                "weekday": weekday,
                "startTime": startTime,
                "endTime": endTime,
                "weekdayRangeType": weekdayRangeType,
                "order": order,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["weekday"]) -> MetaOapg.properties.weekday: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startTime"]) -> MetaOapg.properties.startTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endTime"]) -> MetaOapg.properties.endTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["weekdayRangeType"]) -> MetaOapg.properties.weekdayRangeType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order"]) -> MetaOapg.properties.order: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "weekday", "startTime", "endTime", "weekdayRangeType", "order", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["weekday"]) -> typing.Union[MetaOapg.properties.weekday, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startTime"]) -> typing.Union[MetaOapg.properties.startTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endTime"]) -> typing.Union[MetaOapg.properties.endTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["weekdayRangeType"]) -> typing.Union[MetaOapg.properties.weekdayRangeType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order"]) -> typing.Union[MetaOapg.properties.order, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "weekday", "startTime", "endTime", "weekdayRangeType", "order", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        weekday: typing.Union[MetaOapg.properties.weekday, str, schemas.Unset] = schemas.unset,
        startTime: typing.Union[MetaOapg.properties.startTime, str, schemas.Unset] = schemas.unset,
        endTime: typing.Union[MetaOapg.properties.endTime, str, schemas.Unset] = schemas.unset,
        weekdayRangeType: typing.Union[MetaOapg.properties.weekdayRangeType, str, schemas.Unset] = schemas.unset,
        order: typing.Union[MetaOapg.properties.order, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeeScheduleTemplatesListTemplatesResponseDataItem20240101ItemWeekdaysRanges':
        return super().__new__(
            cls,
            *args,
            id=id,
            weekday=weekday,
            startTime=startTime,
            endTime=endTime,
            weekdayRangeType=weekdayRangeType,
            order=order,
            _configuration=_configuration,
            **kwargs,
        )
