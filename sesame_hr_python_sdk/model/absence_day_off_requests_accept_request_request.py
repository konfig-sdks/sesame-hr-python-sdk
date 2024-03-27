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


class AbsenceDayOffRequestsAcceptRequestRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            managerId = schemas.UUIDSchema
            resolutionComment = schemas.StrSchema
            __annotations__ = {
                "managerId": managerId,
                "resolutionComment": resolutionComment,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["managerId"]) -> MetaOapg.properties.managerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resolutionComment"]) -> MetaOapg.properties.resolutionComment: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["managerId", "resolutionComment", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["managerId"]) -> typing.Union[MetaOapg.properties.managerId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resolutionComment"]) -> typing.Union[MetaOapg.properties.resolutionComment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["managerId", "resolutionComment", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        managerId: typing.Union[MetaOapg.properties.managerId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        resolutionComment: typing.Union[MetaOapg.properties.resolutionComment, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AbsenceDayOffRequestsAcceptRequestRequest':
        return super().__new__(
            cls,
            *args,
            managerId=managerId,
            resolutionComment=resolutionComment,
            _configuration=_configuration,
            **kwargs,
        )
