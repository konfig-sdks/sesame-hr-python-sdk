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


class RecruitmentUpdateCandidateResponseData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.UUIDSchema
            companyId = schemas.UUIDSchema
        
            @staticmethod
            def vacancy() -> typing.Type['RecruitmentUpdateCandidateResponseDataVacancy']:
                return RecruitmentUpdateCandidateResponseDataVacancy
            vacancyId = schemas.UUIDSchema
            firstName = schemas.StrSchema
            lastName = schemas.StrSchema
            email = schemas.StrSchema
            phone = schemas.StrSchema
            type = schemas.StrSchema
            statusId = schemas.UUIDSchema
        
            @staticmethod
            def status() -> typing.Type['RecruitmentUpdateCandidateResponseDataStatus']:
                return RecruitmentUpdateCandidateResponseDataStatus
            linkedInURL = schemas.StrSchema
            desiredSalary = schemas.StrSchema
            startWorkDate = schemas.StrSchema
            evaluation = schemas.IntSchema
            web = schemas.StrSchema
            location = schemas.StrSchema
            hasDocument = schemas.BoolSchema
            comment = schemas.StrSchema
            appliedAt = schemas.StrSchema
            threadId = schemas.UUIDSchema
            lastComment = schemas.DictSchema
            numComments = schemas.IntSchema
            imageProfileURL = schemas.StrSchema
            checklist = schemas.DictSchema
            createdAt = schemas.StrSchema
            updatedAt = schemas.StrSchema
            employeeId = schemas.UUIDSchema
            __annotations__ = {
                "id": id,
                "companyId": companyId,
                "vacancy": vacancy,
                "vacancyId": vacancyId,
                "firstName": firstName,
                "lastName": lastName,
                "email": email,
                "phone": phone,
                "type": type,
                "statusId": statusId,
                "status": status,
                "linkedInURL": linkedInURL,
                "desiredSalary": desiredSalary,
                "startWorkDate": startWorkDate,
                "evaluation": evaluation,
                "web": web,
                "location": location,
                "hasDocument": hasDocument,
                "comment": comment,
                "appliedAt": appliedAt,
                "threadId": threadId,
                "lastComment": lastComment,
                "numComments": numComments,
                "imageProfileURL": imageProfileURL,
                "checklist": checklist,
                "createdAt": createdAt,
                "updatedAt": updatedAt,
                "employeeId": employeeId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["companyId"]) -> MetaOapg.properties.companyId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vacancy"]) -> 'RecruitmentUpdateCandidateResponseDataVacancy': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vacancyId"]) -> MetaOapg.properties.vacancyId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone"]) -> MetaOapg.properties.phone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statusId"]) -> MetaOapg.properties.statusId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'RecruitmentUpdateCandidateResponseDataStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["linkedInURL"]) -> MetaOapg.properties.linkedInURL: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["desiredSalary"]) -> MetaOapg.properties.desiredSalary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startWorkDate"]) -> MetaOapg.properties.startWorkDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["evaluation"]) -> MetaOapg.properties.evaluation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["web"]) -> MetaOapg.properties.web: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location"]) -> MetaOapg.properties.location: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hasDocument"]) -> MetaOapg.properties.hasDocument: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["appliedAt"]) -> MetaOapg.properties.appliedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["threadId"]) -> MetaOapg.properties.threadId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastComment"]) -> MetaOapg.properties.lastComment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numComments"]) -> MetaOapg.properties.numComments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["imageProfileURL"]) -> MetaOapg.properties.imageProfileURL: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["checklist"]) -> MetaOapg.properties.checklist: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updatedAt"]) -> MetaOapg.properties.updatedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeId"]) -> MetaOapg.properties.employeeId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "companyId", "vacancy", "vacancyId", "firstName", "lastName", "email", "phone", "type", "statusId", "status", "linkedInURL", "desiredSalary", "startWorkDate", "evaluation", "web", "location", "hasDocument", "comment", "appliedAt", "threadId", "lastComment", "numComments", "imageProfileURL", "checklist", "createdAt", "updatedAt", "employeeId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["companyId"]) -> typing.Union[MetaOapg.properties.companyId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vacancy"]) -> typing.Union['RecruitmentUpdateCandidateResponseDataVacancy', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vacancyId"]) -> typing.Union[MetaOapg.properties.vacancyId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstName"]) -> typing.Union[MetaOapg.properties.firstName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastName"]) -> typing.Union[MetaOapg.properties.lastName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone"]) -> typing.Union[MetaOapg.properties.phone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statusId"]) -> typing.Union[MetaOapg.properties.statusId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union['RecruitmentUpdateCandidateResponseDataStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["linkedInURL"]) -> typing.Union[MetaOapg.properties.linkedInURL, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["desiredSalary"]) -> typing.Union[MetaOapg.properties.desiredSalary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startWorkDate"]) -> typing.Union[MetaOapg.properties.startWorkDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["evaluation"]) -> typing.Union[MetaOapg.properties.evaluation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["web"]) -> typing.Union[MetaOapg.properties.web, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location"]) -> typing.Union[MetaOapg.properties.location, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hasDocument"]) -> typing.Union[MetaOapg.properties.hasDocument, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> typing.Union[MetaOapg.properties.comment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["appliedAt"]) -> typing.Union[MetaOapg.properties.appliedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["threadId"]) -> typing.Union[MetaOapg.properties.threadId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastComment"]) -> typing.Union[MetaOapg.properties.lastComment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numComments"]) -> typing.Union[MetaOapg.properties.numComments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["imageProfileURL"]) -> typing.Union[MetaOapg.properties.imageProfileURL, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["checklist"]) -> typing.Union[MetaOapg.properties.checklist, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdAt"]) -> typing.Union[MetaOapg.properties.createdAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updatedAt"]) -> typing.Union[MetaOapg.properties.updatedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeId"]) -> typing.Union[MetaOapg.properties.employeeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "companyId", "vacancy", "vacancyId", "firstName", "lastName", "email", "phone", "type", "statusId", "status", "linkedInURL", "desiredSalary", "startWorkDate", "evaluation", "web", "location", "hasDocument", "comment", "appliedAt", "threadId", "lastComment", "numComments", "imageProfileURL", "checklist", "createdAt", "updatedAt", "employeeId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        companyId: typing.Union[MetaOapg.properties.companyId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        vacancy: typing.Union['RecruitmentUpdateCandidateResponseDataVacancy', schemas.Unset] = schemas.unset,
        vacancyId: typing.Union[MetaOapg.properties.vacancyId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        firstName: typing.Union[MetaOapg.properties.firstName, str, schemas.Unset] = schemas.unset,
        lastName: typing.Union[MetaOapg.properties.lastName, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        phone: typing.Union[MetaOapg.properties.phone, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        statusId: typing.Union[MetaOapg.properties.statusId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        status: typing.Union['RecruitmentUpdateCandidateResponseDataStatus', schemas.Unset] = schemas.unset,
        linkedInURL: typing.Union[MetaOapg.properties.linkedInURL, str, schemas.Unset] = schemas.unset,
        desiredSalary: typing.Union[MetaOapg.properties.desiredSalary, str, schemas.Unset] = schemas.unset,
        startWorkDate: typing.Union[MetaOapg.properties.startWorkDate, str, schemas.Unset] = schemas.unset,
        evaluation: typing.Union[MetaOapg.properties.evaluation, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        web: typing.Union[MetaOapg.properties.web, str, schemas.Unset] = schemas.unset,
        location: typing.Union[MetaOapg.properties.location, str, schemas.Unset] = schemas.unset,
        hasDocument: typing.Union[MetaOapg.properties.hasDocument, bool, schemas.Unset] = schemas.unset,
        comment: typing.Union[MetaOapg.properties.comment, str, schemas.Unset] = schemas.unset,
        appliedAt: typing.Union[MetaOapg.properties.appliedAt, str, schemas.Unset] = schemas.unset,
        threadId: typing.Union[MetaOapg.properties.threadId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        lastComment: typing.Union[MetaOapg.properties.lastComment, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        numComments: typing.Union[MetaOapg.properties.numComments, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        imageProfileURL: typing.Union[MetaOapg.properties.imageProfileURL, str, schemas.Unset] = schemas.unset,
        checklist: typing.Union[MetaOapg.properties.checklist, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        createdAt: typing.Union[MetaOapg.properties.createdAt, str, schemas.Unset] = schemas.unset,
        updatedAt: typing.Union[MetaOapg.properties.updatedAt, str, schemas.Unset] = schemas.unset,
        employeeId: typing.Union[MetaOapg.properties.employeeId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RecruitmentUpdateCandidateResponseData':
        return super().__new__(
            cls,
            *args,
            id=id,
            companyId=companyId,
            vacancy=vacancy,
            vacancyId=vacancyId,
            firstName=firstName,
            lastName=lastName,
            email=email,
            phone=phone,
            type=type,
            statusId=statusId,
            status=status,
            linkedInURL=linkedInURL,
            desiredSalary=desiredSalary,
            startWorkDate=startWorkDate,
            evaluation=evaluation,
            web=web,
            location=location,
            hasDocument=hasDocument,
            comment=comment,
            appliedAt=appliedAt,
            threadId=threadId,
            lastComment=lastComment,
            numComments=numComments,
            imageProfileURL=imageProfileURL,
            checklist=checklist,
            createdAt=createdAt,
            updatedAt=updatedAt,
            employeeId=employeeId,
            _configuration=_configuration,
            **kwargs,
        )

from sesame_hr_python_sdk.model.recruitment_update_candidate_response_data_status import RecruitmentUpdateCandidateResponseDataStatus
from sesame_hr_python_sdk.model.recruitment_update_candidate_response_data_vacancy import RecruitmentUpdateCandidateResponseDataVacancy
