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


class AbsenceDayOffRequestsAcceptRequestResponseDataAbsenceCalendarAbsenceType(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.UUIDSchema
            name = schemas.StrSchema
            needsValidation = schemas.BoolSchema
        
            @staticmethod
            def company() -> typing.Type['AbsenceDayOffRequestsAcceptRequestResponseDataAbsenceCalendarAbsenceTypeCompany']:
                return AbsenceDayOffRequestsAcceptRequestResponseDataAbsenceCalendarAbsenceTypeCompany
            createdAt = schemas.StrSchema
            updatedAt = schemas.StrSchema
            
            
            class deletedAt(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'deletedAt':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def NORMAL(cls):
                    return cls("normal")
                
                @schemas.classproperty
                def PRIVATE(cls):
                    return cls("private")
            
            
            class pickMode(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def DAYS(cls):
                    return cls("by_days")
                
                @schemas.classproperty
                def TIME_RANGE(cls):
                    return cls("by_time_range")
            __annotations__ = {
                "id": id,
                "name": name,
                "needsValidation": needsValidation,
                "company": company,
                "createdAt": createdAt,
                "updatedAt": updatedAt,
                "deletedAt": deletedAt,
                "type": type,
                "pickMode": pickMode,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["needsValidation"]) -> MetaOapg.properties.needsValidation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company"]) -> 'AbsenceDayOffRequestsAcceptRequestResponseDataAbsenceCalendarAbsenceTypeCompany': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updatedAt"]) -> MetaOapg.properties.updatedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deletedAt"]) -> MetaOapg.properties.deletedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pickMode"]) -> MetaOapg.properties.pickMode: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "needsValidation", "company", "createdAt", "updatedAt", "deletedAt", "type", "pickMode", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["needsValidation"]) -> typing.Union[MetaOapg.properties.needsValidation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company"]) -> typing.Union['AbsenceDayOffRequestsAcceptRequestResponseDataAbsenceCalendarAbsenceTypeCompany', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdAt"]) -> typing.Union[MetaOapg.properties.createdAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updatedAt"]) -> typing.Union[MetaOapg.properties.updatedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deletedAt"]) -> typing.Union[MetaOapg.properties.deletedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pickMode"]) -> typing.Union[MetaOapg.properties.pickMode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "needsValidation", "company", "createdAt", "updatedAt", "deletedAt", "type", "pickMode", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        needsValidation: typing.Union[MetaOapg.properties.needsValidation, bool, schemas.Unset] = schemas.unset,
        company: typing.Union['AbsenceDayOffRequestsAcceptRequestResponseDataAbsenceCalendarAbsenceTypeCompany', schemas.Unset] = schemas.unset,
        createdAt: typing.Union[MetaOapg.properties.createdAt, str, schemas.Unset] = schemas.unset,
        updatedAt: typing.Union[MetaOapg.properties.updatedAt, str, schemas.Unset] = schemas.unset,
        deletedAt: typing.Union[MetaOapg.properties.deletedAt, None, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        pickMode: typing.Union[MetaOapg.properties.pickMode, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AbsenceDayOffRequestsAcceptRequestResponseDataAbsenceCalendarAbsenceType':
        return super().__new__(
            cls,
            *args,
            id=id,
            name=name,
            needsValidation=needsValidation,
            company=company,
            createdAt=createdAt,
            updatedAt=updatedAt,
            deletedAt=deletedAt,
            type=type,
            pickMode=pickMode,
            _configuration=_configuration,
            **kwargs,
        )

from sesame_hr_python_sdk.model.absence_day_off_requests_accept_request_response_data_absence_calendar_absence_type_company import AbsenceDayOffRequestsAcceptRequestResponseDataAbsenceCalendarAbsenceTypeCompany
