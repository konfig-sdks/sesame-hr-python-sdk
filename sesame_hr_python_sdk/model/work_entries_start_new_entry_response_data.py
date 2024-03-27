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


class WorkEntriesStartNewEntryResponseData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.UUIDSchema
            workCheckTypeId = schemas.UUIDSchema
        
            @staticmethod
            def employee() -> typing.Type['WorkEntriesStartNewEntryResponseDataEmployee']:
                return WorkEntriesStartNewEntryResponseDataEmployee
            workEntryType = schemas.StrSchema
        
            @staticmethod
            def workEntryIn() -> typing.Type['WorkEntriesStartNewEntryResponseDataWorkEntryIn']:
                return WorkEntriesStartNewEntryResponseDataWorkEntryIn
            workEntryOut = schemas.DictSchema
            createdAt = schemas.StrSchema
            updatedAt = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "workCheckTypeId": workCheckTypeId,
                "employee": employee,
                "workEntryType": workEntryType,
                "workEntryIn": workEntryIn,
                "workEntryOut": workEntryOut,
                "createdAt": createdAt,
                "updatedAt": updatedAt,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workCheckTypeId"]) -> MetaOapg.properties.workCheckTypeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee"]) -> 'WorkEntriesStartNewEntryResponseDataEmployee': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workEntryType"]) -> MetaOapg.properties.workEntryType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workEntryIn"]) -> 'WorkEntriesStartNewEntryResponseDataWorkEntryIn': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workEntryOut"]) -> MetaOapg.properties.workEntryOut: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updatedAt"]) -> MetaOapg.properties.updatedAt: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "workCheckTypeId", "employee", "workEntryType", "workEntryIn", "workEntryOut", "createdAt", "updatedAt", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workCheckTypeId"]) -> typing.Union[MetaOapg.properties.workCheckTypeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee"]) -> typing.Union['WorkEntriesStartNewEntryResponseDataEmployee', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workEntryType"]) -> typing.Union[MetaOapg.properties.workEntryType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workEntryIn"]) -> typing.Union['WorkEntriesStartNewEntryResponseDataWorkEntryIn', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workEntryOut"]) -> typing.Union[MetaOapg.properties.workEntryOut, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdAt"]) -> typing.Union[MetaOapg.properties.createdAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updatedAt"]) -> typing.Union[MetaOapg.properties.updatedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "workCheckTypeId", "employee", "workEntryType", "workEntryIn", "workEntryOut", "createdAt", "updatedAt", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        workCheckTypeId: typing.Union[MetaOapg.properties.workCheckTypeId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        employee: typing.Union['WorkEntriesStartNewEntryResponseDataEmployee', schemas.Unset] = schemas.unset,
        workEntryType: typing.Union[MetaOapg.properties.workEntryType, str, schemas.Unset] = schemas.unset,
        workEntryIn: typing.Union['WorkEntriesStartNewEntryResponseDataWorkEntryIn', schemas.Unset] = schemas.unset,
        workEntryOut: typing.Union[MetaOapg.properties.workEntryOut, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        createdAt: typing.Union[MetaOapg.properties.createdAt, str, schemas.Unset] = schemas.unset,
        updatedAt: typing.Union[MetaOapg.properties.updatedAt, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WorkEntriesStartNewEntryResponseData':
        return super().__new__(
            cls,
            *args,
            id=id,
            workCheckTypeId=workCheckTypeId,
            employee=employee,
            workEntryType=workEntryType,
            workEntryIn=workEntryIn,
            workEntryOut=workEntryOut,
            createdAt=createdAt,
            updatedAt=updatedAt,
            _configuration=_configuration,
            **kwargs,
        )

from sesame_hr_python_sdk.model.work_entries_start_new_entry_response_data_employee import WorkEntriesStartNewEntryResponseDataEmployee
from sesame_hr_python_sdk.model.work_entries_start_new_entry_response_data_work_entry_in import WorkEntriesStartNewEntryResponseDataWorkEntryIn
