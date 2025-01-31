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


class WorkEntriesStartNewEntryResponseDataWorkEntryIn(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            origin = schemas.StrSchema
            date = schemas.StrSchema
        
            @staticmethod
            def coordinates() -> typing.Type['WorkEntriesStartNewEntryResponseDataWorkEntryInCoordinates']:
                return WorkEntriesStartNewEntryResponseDataWorkEntryInCoordinates
            __annotations__ = {
                "origin": origin,
                "date": date,
                "coordinates": coordinates,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["origin"]) -> MetaOapg.properties.origin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coordinates"]) -> 'WorkEntriesStartNewEntryResponseDataWorkEntryInCoordinates': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["origin", "date", "coordinates", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["origin"]) -> typing.Union[MetaOapg.properties.origin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> typing.Union[MetaOapg.properties.date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coordinates"]) -> typing.Union['WorkEntriesStartNewEntryResponseDataWorkEntryInCoordinates', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["origin", "date", "coordinates", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        origin: typing.Union[MetaOapg.properties.origin, str, schemas.Unset] = schemas.unset,
        date: typing.Union[MetaOapg.properties.date, str, schemas.Unset] = schemas.unset,
        coordinates: typing.Union['WorkEntriesStartNewEntryResponseDataWorkEntryInCoordinates', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WorkEntriesStartNewEntryResponseDataWorkEntryIn':
        return super().__new__(
            cls,
            *args,
            origin=origin,
            date=date,
            coordinates=coordinates,
            _configuration=_configuration,
            **kwargs,
        )

from sesame_hr_python_sdk.model.work_entries_start_new_entry_response_data_work_entry_in_coordinates import WorkEntriesStartNewEntryResponseDataWorkEntryInCoordinates
