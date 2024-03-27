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


class HolidayCalendarsListCalendarResponseDataItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.UUIDSchema
            name = schemas.StrSchema
            companyId = schemas.UUIDSchema
        
            @staticmethod
            def dayOff() -> typing.Type['HolidayCalendarsListCalendarResponseDataItemDayOff']:
                return HolidayCalendarsListCalendarResponseDataItemDayOff
            typeId = schemas.UUIDSchema
            default = schemas.BoolSchema
            __annotations__ = {
                "id": id,
                "name": name,
                "companyId": companyId,
                "dayOff": dayOff,
                "typeId": typeId,
                "default": default,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["companyId"]) -> MetaOapg.properties.companyId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dayOff"]) -> 'HolidayCalendarsListCalendarResponseDataItemDayOff': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["typeId"]) -> MetaOapg.properties.typeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["default"]) -> MetaOapg.properties.default: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "companyId", "dayOff", "typeId", "default", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["companyId"]) -> typing.Union[MetaOapg.properties.companyId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dayOff"]) -> typing.Union['HolidayCalendarsListCalendarResponseDataItemDayOff', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["typeId"]) -> typing.Union[MetaOapg.properties.typeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["default"]) -> typing.Union[MetaOapg.properties.default, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "companyId", "dayOff", "typeId", "default", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        companyId: typing.Union[MetaOapg.properties.companyId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        dayOff: typing.Union['HolidayCalendarsListCalendarResponseDataItemDayOff', schemas.Unset] = schemas.unset,
        typeId: typing.Union[MetaOapg.properties.typeId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        default: typing.Union[MetaOapg.properties.default, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'HolidayCalendarsListCalendarResponseDataItem':
        return super().__new__(
            cls,
            *args,
            id=id,
            name=name,
            companyId=companyId,
            dayOff=dayOff,
            typeId=typeId,
            default=default,
            _configuration=_configuration,
            **kwargs,
        )

from sesame_hr_python_sdk.model.holiday_calendars_list_calendar_response_data_item_day_off import HolidayCalendarsListCalendarResponseDataItemDayOff
