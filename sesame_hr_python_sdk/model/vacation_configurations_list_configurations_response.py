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


class VacationConfigurationsListConfigurationsResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def data() -> typing.Type['VacationConfigurationsListConfigurationsResponseData']:
                return VacationConfigurationsListConfigurationsResponseData
        
            @staticmethod
            def meta() -> typing.Type['VacationConfigurationsListConfigurationsResponseMeta']:
                return VacationConfigurationsListConfigurationsResponseMeta
            __annotations__ = {
                "data": data,
                "meta": meta,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> 'VacationConfigurationsListConfigurationsResponseData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meta"]) -> 'VacationConfigurationsListConfigurationsResponseMeta': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", "meta", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union['VacationConfigurationsListConfigurationsResponseData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meta"]) -> typing.Union['VacationConfigurationsListConfigurationsResponseMeta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", "meta", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        data: typing.Union['VacationConfigurationsListConfigurationsResponseData', schemas.Unset] = schemas.unset,
        meta: typing.Union['VacationConfigurationsListConfigurationsResponseMeta', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VacationConfigurationsListConfigurationsResponse':
        return super().__new__(
            cls,
            *args,
            data=data,
            meta=meta,
            _configuration=_configuration,
            **kwargs,
        )

from sesame_hr_python_sdk.model.vacation_configurations_list_configurations_response_data import VacationConfigurationsListConfigurationsResponseData
from sesame_hr_python_sdk.model.vacation_configurations_list_configurations_response_meta import VacationConfigurationsListConfigurationsResponseMeta
