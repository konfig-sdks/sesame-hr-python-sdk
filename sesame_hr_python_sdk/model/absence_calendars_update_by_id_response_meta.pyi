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


class AbsenceCalendarsUpdateByIdResponseMeta(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            currentPage = schemas.IntSchema
            lastPage = schemas.IntSchema
            total = schemas.IntSchema
            perPage = schemas.IntSchema
            __annotations__ = {
                "currentPage": currentPage,
                "lastPage": lastPage,
                "total": total,
                "perPage": perPage,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currentPage"]) -> MetaOapg.properties.currentPage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastPage"]) -> MetaOapg.properties.lastPage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["perPage"]) -> MetaOapg.properties.perPage: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["currentPage", "lastPage", "total", "perPage", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currentPage"]) -> typing.Union[MetaOapg.properties.currentPage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastPage"]) -> typing.Union[MetaOapg.properties.lastPage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> typing.Union[MetaOapg.properties.total, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["perPage"]) -> typing.Union[MetaOapg.properties.perPage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["currentPage", "lastPage", "total", "perPage", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        currentPage: typing.Union[MetaOapg.properties.currentPage, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        lastPage: typing.Union[MetaOapg.properties.lastPage, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        total: typing.Union[MetaOapg.properties.total, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        perPage: typing.Union[MetaOapg.properties.perPage, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AbsenceCalendarsUpdateByIdResponseMeta':
        return super().__new__(
            cls,
            *args,
            currentPage=currentPage,
            lastPage=lastPage,
            total=total,
            perPage=perPage,
            _configuration=_configuration,
            **kwargs,
        )
