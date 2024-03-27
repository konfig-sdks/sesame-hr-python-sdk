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


class CustomFieldsCreateFieldResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def data() -> typing.Type['CustomFieldsCreateFieldResponseData']:
                return CustomFieldsCreateFieldResponseData
        
            @staticmethod
            def meta() -> typing.Type['CustomFieldsCreateFieldResponseMeta']:
                return CustomFieldsCreateFieldResponseMeta
            __annotations__ = {
                "data": data,
                "meta": meta,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> 'CustomFieldsCreateFieldResponseData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meta"]) -> 'CustomFieldsCreateFieldResponseMeta': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", "meta", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union['CustomFieldsCreateFieldResponseData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meta"]) -> typing.Union['CustomFieldsCreateFieldResponseMeta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", "meta", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        data: typing.Union['CustomFieldsCreateFieldResponseData', schemas.Unset] = schemas.unset,
        meta: typing.Union['CustomFieldsCreateFieldResponseMeta', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CustomFieldsCreateFieldResponse':
        return super().__new__(
            cls,
            *args,
            data=data,
            meta=meta,
            _configuration=_configuration,
            **kwargs,
        )

from sesame_hr_python_sdk.model.custom_fields_create_field_response_data import CustomFieldsCreateFieldResponseData
from sesame_hr_python_sdk.model.custom_fields_create_field_response_meta import CustomFieldsCreateFieldResponseMeta
