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


class RecruitmentListVacanciesResponseDataItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            id = schemas.UUIDSchema
            companyId = schemas.UUIDSchema
            name = schemas.StrSchema
            department = schemas.StrSchema
            contactType = schemas.StrSchema
            experience = schemas.StrSchema
            createdById = schemas.UUIDSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "open": "OPEN",
                        "closed": "CLOSED",
                        "draft": "DRAFT",
                    }
                
                @schemas.classproperty
                def OPEN(cls):
                    return cls("open")
                
                @schemas.classproperty
                def CLOSED(cls):
                    return cls("closed")
                
                @schemas.classproperty
                def DRAFT(cls):
                    return cls("draft")
            openedAt = schemas.StrSchema
            createdAt = schemas.StrSchema
            updatedAt = schemas.StrSchema
            public = schemas.BoolSchema
        
            @staticmethod
            def locationVacancy() -> typing.Type['RecruitmentListVacanciesResponseDataItemLocationVacancy']:
                return RecruitmentListVacanciesResponseDataItemLocationVacancy
        
            @staticmethod
            def scheduleType() -> typing.Type['RecruitmentListVacanciesResponseDataItemScheduleType']:
                return RecruitmentListVacanciesResponseDataItemScheduleType
        
            @staticmethod
            def category() -> typing.Type['RecruitmentListVacanciesResponseDataItemCategory']:
                return RecruitmentListVacanciesResponseDataItemCategory
            __annotations__ = {
                "description": description,
                "id": id,
                "companyId": companyId,
                "name": name,
                "department": department,
                "contactType": contactType,
                "experience": experience,
                "createdById": createdById,
                "status": status,
                "openedAt": openedAt,
                "createdAt": createdAt,
                "updatedAt": updatedAt,
                "public": public,
                "locationVacancy": locationVacancy,
                "scheduleType": scheduleType,
                "category": category,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["companyId"]) -> MetaOapg.properties.companyId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["department"]) -> MetaOapg.properties.department: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contactType"]) -> MetaOapg.properties.contactType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["experience"]) -> MetaOapg.properties.experience: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdById"]) -> MetaOapg.properties.createdById: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["openedAt"]) -> MetaOapg.properties.openedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updatedAt"]) -> MetaOapg.properties.updatedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["public"]) -> MetaOapg.properties.public: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["locationVacancy"]) -> 'RecruitmentListVacanciesResponseDataItemLocationVacancy': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scheduleType"]) -> 'RecruitmentListVacanciesResponseDataItemScheduleType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category"]) -> 'RecruitmentListVacanciesResponseDataItemCategory': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "id", "companyId", "name", "department", "contactType", "experience", "createdById", "status", "openedAt", "createdAt", "updatedAt", "public", "locationVacancy", "scheduleType", "category", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["companyId"]) -> typing.Union[MetaOapg.properties.companyId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["department"]) -> typing.Union[MetaOapg.properties.department, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contactType"]) -> typing.Union[MetaOapg.properties.contactType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["experience"]) -> typing.Union[MetaOapg.properties.experience, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdById"]) -> typing.Union[MetaOapg.properties.createdById, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["openedAt"]) -> typing.Union[MetaOapg.properties.openedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdAt"]) -> typing.Union[MetaOapg.properties.createdAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updatedAt"]) -> typing.Union[MetaOapg.properties.updatedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["public"]) -> typing.Union[MetaOapg.properties.public, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["locationVacancy"]) -> typing.Union['RecruitmentListVacanciesResponseDataItemLocationVacancy', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scheduleType"]) -> typing.Union['RecruitmentListVacanciesResponseDataItemScheduleType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category"]) -> typing.Union['RecruitmentListVacanciesResponseDataItemCategory', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "id", "companyId", "name", "department", "contactType", "experience", "createdById", "status", "openedAt", "createdAt", "updatedAt", "public", "locationVacancy", "scheduleType", "category", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        companyId: typing.Union[MetaOapg.properties.companyId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        department: typing.Union[MetaOapg.properties.department, str, schemas.Unset] = schemas.unset,
        contactType: typing.Union[MetaOapg.properties.contactType, str, schemas.Unset] = schemas.unset,
        experience: typing.Union[MetaOapg.properties.experience, str, schemas.Unset] = schemas.unset,
        createdById: typing.Union[MetaOapg.properties.createdById, str, uuid.UUID, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        openedAt: typing.Union[MetaOapg.properties.openedAt, str, schemas.Unset] = schemas.unset,
        createdAt: typing.Union[MetaOapg.properties.createdAt, str, schemas.Unset] = schemas.unset,
        updatedAt: typing.Union[MetaOapg.properties.updatedAt, str, schemas.Unset] = schemas.unset,
        public: typing.Union[MetaOapg.properties.public, bool, schemas.Unset] = schemas.unset,
        locationVacancy: typing.Union['RecruitmentListVacanciesResponseDataItemLocationVacancy', schemas.Unset] = schemas.unset,
        scheduleType: typing.Union['RecruitmentListVacanciesResponseDataItemScheduleType', schemas.Unset] = schemas.unset,
        category: typing.Union['RecruitmentListVacanciesResponseDataItemCategory', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RecruitmentListVacanciesResponseDataItem':
        return super().__new__(
            cls,
            *args,
            description=description,
            id=id,
            companyId=companyId,
            name=name,
            department=department,
            contactType=contactType,
            experience=experience,
            createdById=createdById,
            status=status,
            openedAt=openedAt,
            createdAt=createdAt,
            updatedAt=updatedAt,
            public=public,
            locationVacancy=locationVacancy,
            scheduleType=scheduleType,
            category=category,
            _configuration=_configuration,
            **kwargs,
        )

from sesame_hr_python_sdk.model.recruitment_list_vacancies_response_data_item_category import RecruitmentListVacanciesResponseDataItemCategory
from sesame_hr_python_sdk.model.recruitment_list_vacancies_response_data_item_location_vacancy import RecruitmentListVacanciesResponseDataItemLocationVacancy
from sesame_hr_python_sdk.model.recruitment_list_vacancies_response_data_item_schedule_type import RecruitmentListVacanciesResponseDataItemScheduleType
