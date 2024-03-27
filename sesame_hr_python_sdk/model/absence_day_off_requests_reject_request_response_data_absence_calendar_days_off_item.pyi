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


class AbsenceDayOffRequestsRejectRequestResponseDataAbsenceCalendarDaysOffItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            date = schemas.DateSchema
            seconds = schemas.IntSchema
            startTime = schemas.StrSchema
            endTime = schemas.StrSchema
            __annotations__ = {
                "date": date,
                "seconds": seconds,
                "startTime": startTime,
                "endTime": endTime,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["seconds"]) -> MetaOapg.properties.seconds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startTime"]) -> MetaOapg.properties.startTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endTime"]) -> MetaOapg.properties.endTime: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["date", "seconds", "startTime", "endTime", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> typing.Union[MetaOapg.properties.date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["seconds"]) -> typing.Union[MetaOapg.properties.seconds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startTime"]) -> typing.Union[MetaOapg.properties.startTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endTime"]) -> typing.Union[MetaOapg.properties.endTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["date", "seconds", "startTime", "endTime", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        date: typing.Union[MetaOapg.properties.date, str, date, schemas.Unset] = schemas.unset,
        seconds: typing.Union[MetaOapg.properties.seconds, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        startTime: typing.Union[MetaOapg.properties.startTime, str, schemas.Unset] = schemas.unset,
        endTime: typing.Union[MetaOapg.properties.endTime, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AbsenceDayOffRequestsRejectRequestResponseDataAbsenceCalendarDaysOffItem':
        return super().__new__(
            cls,
            *args,
            date=date,
            seconds=seconds,
            startTime=startTime,
            endTime=endTime,
            _configuration=_configuration,
            **kwargs,
        )
