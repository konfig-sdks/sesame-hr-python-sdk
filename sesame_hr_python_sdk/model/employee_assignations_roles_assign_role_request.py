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


class EmployeeAssignationsRolesAssignRoleRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "entityAffectedId",
            "roleId",
            "employeeId",
        }
        
        class properties:
            roleId = schemas.UUIDSchema
            employeeId = schemas.UUIDSchema
            entityAffectedId = schemas.UUIDSchema
            __annotations__ = {
                "roleId": roleId,
                "employeeId": employeeId,
                "entityAffectedId": entityAffectedId,
            }
    
    entityAffectedId: MetaOapg.properties.entityAffectedId
    roleId: MetaOapg.properties.roleId
    employeeId: MetaOapg.properties.employeeId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["roleId"]) -> MetaOapg.properties.roleId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeId"]) -> MetaOapg.properties.employeeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entityAffectedId"]) -> MetaOapg.properties.entityAffectedId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["roleId", "employeeId", "entityAffectedId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["roleId"]) -> MetaOapg.properties.roleId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeId"]) -> MetaOapg.properties.employeeId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entityAffectedId"]) -> MetaOapg.properties.entityAffectedId: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["roleId", "employeeId", "entityAffectedId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        entityAffectedId: typing.Union[MetaOapg.properties.entityAffectedId, str, uuid.UUID, ],
        roleId: typing.Union[MetaOapg.properties.roleId, str, uuid.UUID, ],
        employeeId: typing.Union[MetaOapg.properties.employeeId, str, uuid.UUID, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeeAssignationsRolesAssignRoleRequest':
        return super().__new__(
            cls,
            *args,
            entityAffectedId=entityAffectedId,
            roleId=roleId,
            employeeId=employeeId,
            _configuration=_configuration,
            **kwargs,
        )
