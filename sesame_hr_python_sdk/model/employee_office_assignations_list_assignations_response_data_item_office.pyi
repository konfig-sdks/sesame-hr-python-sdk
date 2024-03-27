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


class EmployeeOfficeAssignationsListAssignationsResponseDataItemOffice(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            id = schemas.UUIDSchema
            name = schemas.StrSchema
            address = schemas.StrSchema
        
            @staticmethod
            def coordinates() -> typing.Type['EmployeeOfficeAssignationsListAssignationsResponseDataItemOfficeCoordinates']:
                return EmployeeOfficeAssignationsListAssignationsResponseDataItemOfficeCoordinates
            radio = schemas.IntSchema
            __annotations__ = {
                "description": description,
                "id": id,
                "name": name,
                "address": address,
                "coordinates": coordinates,
                "radio": radio,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coordinates"]) -> 'EmployeeOfficeAssignationsListAssignationsResponseDataItemOfficeCoordinates': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["radio"]) -> MetaOapg.properties.radio: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "id", "name", "address", "coordinates", "radio", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> typing.Union[MetaOapg.properties.address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coordinates"]) -> typing.Union['EmployeeOfficeAssignationsListAssignationsResponseDataItemOfficeCoordinates', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["radio"]) -> typing.Union[MetaOapg.properties.radio, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "id", "name", "address", "coordinates", "radio", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        address: typing.Union[MetaOapg.properties.address, str, schemas.Unset] = schemas.unset,
        coordinates: typing.Union['EmployeeOfficeAssignationsListAssignationsResponseDataItemOfficeCoordinates', schemas.Unset] = schemas.unset,
        radio: typing.Union[MetaOapg.properties.radio, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeeOfficeAssignationsListAssignationsResponseDataItemOffice':
        return super().__new__(
            cls,
            *args,
            description=description,
            id=id,
            name=name,
            address=address,
            coordinates=coordinates,
            radio=radio,
            _configuration=_configuration,
            **kwargs,
        )

from sesame_hr_python_sdk.model.employee_office_assignations_list_assignations_response_data_item_office_coordinates import EmployeeOfficeAssignationsListAssignationsResponseDataItemOfficeCoordinates
