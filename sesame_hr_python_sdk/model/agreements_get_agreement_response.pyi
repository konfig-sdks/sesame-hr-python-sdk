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


class AgreementsGetAgreementResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.UUIDSchema
            companyId = schemas.UUIDSchema
            name = schemas.StrSchema
            code = schemas.StrSchema
            color = schemas.StrSchema
            annualHours = schemas.NumberSchema
            additionalHoursPercent = schemas.NumberSchema
            totalAdditionalHours = schemas.NumberSchema
            maxDaysToWork = schemas.NumberSchema
            createdAt = schemas.StrSchema
            updatedAt = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "companyId": companyId,
                "name": name,
                "code": code,
                "color": color,
                "annualHours": annualHours,
                "additionalHoursPercent": additionalHoursPercent,
                "totalAdditionalHours": totalAdditionalHours,
                "maxDaysToWork": maxDaysToWork,
                "createdAt": createdAt,
                "updatedAt": updatedAt,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["companyId"]) -> MetaOapg.properties.companyId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["annualHours"]) -> MetaOapg.properties.annualHours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["additionalHoursPercent"]) -> MetaOapg.properties.additionalHoursPercent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalAdditionalHours"]) -> MetaOapg.properties.totalAdditionalHours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxDaysToWork"]) -> MetaOapg.properties.maxDaysToWork: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updatedAt"]) -> MetaOapg.properties.updatedAt: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "companyId", "name", "code", "color", "annualHours", "additionalHoursPercent", "totalAdditionalHours", "maxDaysToWork", "createdAt", "updatedAt", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["companyId"]) -> typing.Union[MetaOapg.properties.companyId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> typing.Union[MetaOapg.properties.code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color"]) -> typing.Union[MetaOapg.properties.color, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["annualHours"]) -> typing.Union[MetaOapg.properties.annualHours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["additionalHoursPercent"]) -> typing.Union[MetaOapg.properties.additionalHoursPercent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalAdditionalHours"]) -> typing.Union[MetaOapg.properties.totalAdditionalHours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxDaysToWork"]) -> typing.Union[MetaOapg.properties.maxDaysToWork, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdAt"]) -> typing.Union[MetaOapg.properties.createdAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updatedAt"]) -> typing.Union[MetaOapg.properties.updatedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "companyId", "name", "code", "color", "annualHours", "additionalHoursPercent", "totalAdditionalHours", "maxDaysToWork", "createdAt", "updatedAt", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        companyId: typing.Union[MetaOapg.properties.companyId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        code: typing.Union[MetaOapg.properties.code, str, schemas.Unset] = schemas.unset,
        color: typing.Union[MetaOapg.properties.color, str, schemas.Unset] = schemas.unset,
        annualHours: typing.Union[MetaOapg.properties.annualHours, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        additionalHoursPercent: typing.Union[MetaOapg.properties.additionalHoursPercent, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        totalAdditionalHours: typing.Union[MetaOapg.properties.totalAdditionalHours, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        maxDaysToWork: typing.Union[MetaOapg.properties.maxDaysToWork, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        createdAt: typing.Union[MetaOapg.properties.createdAt, str, schemas.Unset] = schemas.unset,
        updatedAt: typing.Union[MetaOapg.properties.updatedAt, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AgreementsGetAgreementResponse':
        return super().__new__(
            cls,
            *args,
            id=id,
            companyId=companyId,
            name=name,
            code=code,
            color=color,
            annualHours=annualHours,
            additionalHoursPercent=additionalHoursPercent,
            totalAdditionalHours=totalAdditionalHours,
            maxDaysToWork=maxDaysToWork,
            createdAt=createdAt,
            updatedAt=updatedAt,
            _configuration=_configuration,
            **kwargs,
        )
