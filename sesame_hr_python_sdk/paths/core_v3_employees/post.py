# coding: utf-8

"""
    Sesame Public API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from sesame_hr_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from sesame_hr_python_sdk.api_response import AsyncGeneratorResponse
from sesame_hr_python_sdk import api_client, exceptions
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

from sesame_hr_python_sdk.model.employees_create_new_employee_response import EmployeesCreateNewEmployeeResponse as EmployeesCreateNewEmployeeResponseSchema
from sesame_hr_python_sdk.model.employees_create_new_employee_request import EmployeesCreateNewEmployeeRequest as EmployeesCreateNewEmployeeRequestSchema
from sesame_hr_python_sdk.model.employees_create_new_employee_request_custom_fields import EmployeesCreateNewEmployeeRequestCustomFields as EmployeesCreateNewEmployeeRequestCustomFieldsSchema

from sesame_hr_python_sdk.type.employees_create_new_employee_request_custom_fields import EmployeesCreateNewEmployeeRequestCustomFields
from sesame_hr_python_sdk.type.employees_create_new_employee_request import EmployeesCreateNewEmployeeRequest
from sesame_hr_python_sdk.type.employees_create_new_employee_response import EmployeesCreateNewEmployeeResponse

from ...api_client import Dictionary
from sesame_hr_python_sdk.pydantic.employees_create_new_employee_response import EmployeesCreateNewEmployeeResponse as EmployeesCreateNewEmployeeResponsePydantic
from sesame_hr_python_sdk.pydantic.employees_create_new_employee_request import EmployeesCreateNewEmployeeRequest as EmployeesCreateNewEmployeeRequestPydantic
from sesame_hr_python_sdk.pydantic.employees_create_new_employee_request_custom_fields import EmployeesCreateNewEmployeeRequestCustomFields as EmployeesCreateNewEmployeeRequestCustomFieldsPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = EmployeesCreateNewEmployeeRequestSchema


request_body_employees_create_new_employee_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'Bearer',
]
SchemaFor200ResponseBodyApplicationJson = EmployeesCreateNewEmployeeResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: EmployeesCreateNewEmployeeResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: EmployeesCreateNewEmployeeResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_new_employee_mapped_args(
        self,
        company_id: str,
        first_name: str,
        last_name: str,
        invitation: bool,
        status: str,
        description: typing.Optional[str] = None,
        gender: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        contract_id: typing.Optional[str] = None,
        code: typing.Optional[int] = None,
        pin: typing.Optional[int] = None,
        nid: typing.Optional[str] = None,
        identity_number_type: typing.Optional[str] = None,
        ssn: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        date_of_birth: typing.Optional[date] = None,
        custom_fields: typing.Optional[EmployeesCreateNewEmployeeRequestCustomFields] = None,
        nationality: typing.Optional[str] = None,
        marital_status: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        emergency_phone: typing.Optional[str] = None,
        children_count: typing.Optional[int] = None,
        disability: typing.Optional[int] = None,
        personal_email: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        province: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        salary_range: typing.Optional[str] = None,
        study_level: typing.Optional[str] = None,
        professional_category_code: typing.Optional[str] = None,
        professional_category_description: typing.Optional[str] = None,
        bic: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if description is not None:
            _body["description"] = description
        if company_id is not None:
            _body["companyId"] = company_id
        if first_name is not None:
            _body["firstName"] = first_name
        if last_name is not None:
            _body["lastName"] = last_name
        if invitation is not None:
            _body["invitation"] = invitation
        if status is not None:
            _body["status"] = status
        if gender is not None:
            _body["gender"] = gender
        if email is not None:
            _body["email"] = email
        if contract_id is not None:
            _body["contractId"] = contract_id
        if code is not None:
            _body["code"] = code
        if pin is not None:
            _body["pin"] = pin
        if nid is not None:
            _body["nid"] = nid
        if identity_number_type is not None:
            _body["identityNumberType"] = identity_number_type
        if ssn is not None:
            _body["ssn"] = ssn
        if phone is not None:
            _body["phone"] = phone
        if date_of_birth is not None:
            _body["dateOfBirth"] = date_of_birth
        if custom_fields is not None:
            _body["customFields"] = custom_fields
        if nationality is not None:
            _body["nationality"] = nationality
        if marital_status is not None:
            _body["maritalStatus"] = marital_status
        if address is not None:
            _body["address"] = address
        if postal_code is not None:
            _body["postalCode"] = postal_code
        if emergency_phone is not None:
            _body["emergencyPhone"] = emergency_phone
        if children_count is not None:
            _body["childrenCount"] = children_count
        if disability is not None:
            _body["disability"] = disability
        if personal_email is not None:
            _body["personalEmail"] = personal_email
        if city is not None:
            _body["city"] = city
        if province is not None:
            _body["province"] = province
        if country is not None:
            _body["country"] = country
        if salary_range is not None:
            _body["salaryRange"] = salary_range
        if study_level is not None:
            _body["studyLevel"] = study_level
        if professional_category_code is not None:
            _body["professionalCategoryCode"] = professional_category_code
        if professional_category_description is not None:
            _body["professionalCategoryDescription"] = professional_category_description
        if bic is not None:
            _body["bic"] = bic
        args.body = _body
        return args

    async def _acreate_new_employee_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create an employee
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/core/v3/employees',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_employees_create_new_employee_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_new_employee_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create an employee
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/core/v3/employees',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_employees_create_new_employee_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateNewEmployeeRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new_employee(
        self,
        company_id: str,
        first_name: str,
        last_name: str,
        invitation: bool,
        status: str,
        description: typing.Optional[str] = None,
        gender: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        contract_id: typing.Optional[str] = None,
        code: typing.Optional[int] = None,
        pin: typing.Optional[int] = None,
        nid: typing.Optional[str] = None,
        identity_number_type: typing.Optional[str] = None,
        ssn: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        date_of_birth: typing.Optional[date] = None,
        custom_fields: typing.Optional[EmployeesCreateNewEmployeeRequestCustomFields] = None,
        nationality: typing.Optional[str] = None,
        marital_status: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        emergency_phone: typing.Optional[str] = None,
        children_count: typing.Optional[int] = None,
        disability: typing.Optional[int] = None,
        personal_email: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        province: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        salary_range: typing.Optional[str] = None,
        study_level: typing.Optional[str] = None,
        professional_category_code: typing.Optional[str] = None,
        professional_category_description: typing.Optional[str] = None,
        bic: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_employee_mapped_args(
            company_id=company_id,
            first_name=first_name,
            last_name=last_name,
            invitation=invitation,
            status=status,
            description=description,
            gender=gender,
            email=email,
            contract_id=contract_id,
            code=code,
            pin=pin,
            nid=nid,
            identity_number_type=identity_number_type,
            ssn=ssn,
            phone=phone,
            date_of_birth=date_of_birth,
            custom_fields=custom_fields,
            nationality=nationality,
            marital_status=marital_status,
            address=address,
            postal_code=postal_code,
            emergency_phone=emergency_phone,
            children_count=children_count,
            disability=disability,
            personal_email=personal_email,
            city=city,
            province=province,
            country=country,
            salary_range=salary_range,
            study_level=study_level,
            professional_category_code=professional_category_code,
            professional_category_description=professional_category_description,
            bic=bic,
        )
        return await self._acreate_new_employee_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_new_employee(
        self,
        company_id: str,
        first_name: str,
        last_name: str,
        invitation: bool,
        status: str,
        description: typing.Optional[str] = None,
        gender: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        contract_id: typing.Optional[str] = None,
        code: typing.Optional[int] = None,
        pin: typing.Optional[int] = None,
        nid: typing.Optional[str] = None,
        identity_number_type: typing.Optional[str] = None,
        ssn: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        date_of_birth: typing.Optional[date] = None,
        custom_fields: typing.Optional[EmployeesCreateNewEmployeeRequestCustomFields] = None,
        nationality: typing.Optional[str] = None,
        marital_status: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        emergency_phone: typing.Optional[str] = None,
        children_count: typing.Optional[int] = None,
        disability: typing.Optional[int] = None,
        personal_email: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        province: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        salary_range: typing.Optional[str] = None,
        study_level: typing.Optional[str] = None,
        professional_category_code: typing.Optional[str] = None,
        professional_category_description: typing.Optional[str] = None,
        bic: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_employee_mapped_args(
            company_id=company_id,
            first_name=first_name,
            last_name=last_name,
            invitation=invitation,
            status=status,
            description=description,
            gender=gender,
            email=email,
            contract_id=contract_id,
            code=code,
            pin=pin,
            nid=nid,
            identity_number_type=identity_number_type,
            ssn=ssn,
            phone=phone,
            date_of_birth=date_of_birth,
            custom_fields=custom_fields,
            nationality=nationality,
            marital_status=marital_status,
            address=address,
            postal_code=postal_code,
            emergency_phone=emergency_phone,
            children_count=children_count,
            disability=disability,
            personal_email=personal_email,
            city=city,
            province=province,
            country=country,
            salary_range=salary_range,
            study_level=study_level,
            professional_category_code=professional_category_code,
            professional_category_description=professional_category_description,
            bic=bic,
        )
        return self._create_new_employee_oapg(
            body=args.body,
        )

class CreateNewEmployee(BaseApi):

    async def acreate_new_employee(
        self,
        company_id: str,
        first_name: str,
        last_name: str,
        invitation: bool,
        status: str,
        description: typing.Optional[str] = None,
        gender: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        contract_id: typing.Optional[str] = None,
        code: typing.Optional[int] = None,
        pin: typing.Optional[int] = None,
        nid: typing.Optional[str] = None,
        identity_number_type: typing.Optional[str] = None,
        ssn: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        date_of_birth: typing.Optional[date] = None,
        custom_fields: typing.Optional[EmployeesCreateNewEmployeeRequestCustomFields] = None,
        nationality: typing.Optional[str] = None,
        marital_status: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        emergency_phone: typing.Optional[str] = None,
        children_count: typing.Optional[int] = None,
        disability: typing.Optional[int] = None,
        personal_email: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        province: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        salary_range: typing.Optional[str] = None,
        study_level: typing.Optional[str] = None,
        professional_category_code: typing.Optional[str] = None,
        professional_category_description: typing.Optional[str] = None,
        bic: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> EmployeesCreateNewEmployeeResponsePydantic:
        raw_response = await self.raw.acreate_new_employee(
            company_id=company_id,
            first_name=first_name,
            last_name=last_name,
            invitation=invitation,
            status=status,
            description=description,
            gender=gender,
            email=email,
            contract_id=contract_id,
            code=code,
            pin=pin,
            nid=nid,
            identity_number_type=identity_number_type,
            ssn=ssn,
            phone=phone,
            date_of_birth=date_of_birth,
            custom_fields=custom_fields,
            nationality=nationality,
            marital_status=marital_status,
            address=address,
            postal_code=postal_code,
            emergency_phone=emergency_phone,
            children_count=children_count,
            disability=disability,
            personal_email=personal_email,
            city=city,
            province=province,
            country=country,
            salary_range=salary_range,
            study_level=study_level,
            professional_category_code=professional_category_code,
            professional_category_description=professional_category_description,
            bic=bic,
            **kwargs,
        )
        if validate:
            return EmployeesCreateNewEmployeeResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(EmployeesCreateNewEmployeeResponsePydantic, raw_response.body)
    
    
    def create_new_employee(
        self,
        company_id: str,
        first_name: str,
        last_name: str,
        invitation: bool,
        status: str,
        description: typing.Optional[str] = None,
        gender: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        contract_id: typing.Optional[str] = None,
        code: typing.Optional[int] = None,
        pin: typing.Optional[int] = None,
        nid: typing.Optional[str] = None,
        identity_number_type: typing.Optional[str] = None,
        ssn: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        date_of_birth: typing.Optional[date] = None,
        custom_fields: typing.Optional[EmployeesCreateNewEmployeeRequestCustomFields] = None,
        nationality: typing.Optional[str] = None,
        marital_status: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        emergency_phone: typing.Optional[str] = None,
        children_count: typing.Optional[int] = None,
        disability: typing.Optional[int] = None,
        personal_email: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        province: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        salary_range: typing.Optional[str] = None,
        study_level: typing.Optional[str] = None,
        professional_category_code: typing.Optional[str] = None,
        professional_category_description: typing.Optional[str] = None,
        bic: typing.Optional[str] = None,
        validate: bool = False,
    ) -> EmployeesCreateNewEmployeeResponsePydantic:
        raw_response = self.raw.create_new_employee(
            company_id=company_id,
            first_name=first_name,
            last_name=last_name,
            invitation=invitation,
            status=status,
            description=description,
            gender=gender,
            email=email,
            contract_id=contract_id,
            code=code,
            pin=pin,
            nid=nid,
            identity_number_type=identity_number_type,
            ssn=ssn,
            phone=phone,
            date_of_birth=date_of_birth,
            custom_fields=custom_fields,
            nationality=nationality,
            marital_status=marital_status,
            address=address,
            postal_code=postal_code,
            emergency_phone=emergency_phone,
            children_count=children_count,
            disability=disability,
            personal_email=personal_email,
            city=city,
            province=province,
            country=country,
            salary_range=salary_range,
            study_level=study_level,
            professional_category_code=professional_category_code,
            professional_category_description=professional_category_description,
            bic=bic,
        )
        if validate:
            return EmployeesCreateNewEmployeeResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(EmployeesCreateNewEmployeeResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        company_id: str,
        first_name: str,
        last_name: str,
        invitation: bool,
        status: str,
        description: typing.Optional[str] = None,
        gender: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        contract_id: typing.Optional[str] = None,
        code: typing.Optional[int] = None,
        pin: typing.Optional[int] = None,
        nid: typing.Optional[str] = None,
        identity_number_type: typing.Optional[str] = None,
        ssn: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        date_of_birth: typing.Optional[date] = None,
        custom_fields: typing.Optional[EmployeesCreateNewEmployeeRequestCustomFields] = None,
        nationality: typing.Optional[str] = None,
        marital_status: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        emergency_phone: typing.Optional[str] = None,
        children_count: typing.Optional[int] = None,
        disability: typing.Optional[int] = None,
        personal_email: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        province: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        salary_range: typing.Optional[str] = None,
        study_level: typing.Optional[str] = None,
        professional_category_code: typing.Optional[str] = None,
        professional_category_description: typing.Optional[str] = None,
        bic: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_employee_mapped_args(
            company_id=company_id,
            first_name=first_name,
            last_name=last_name,
            invitation=invitation,
            status=status,
            description=description,
            gender=gender,
            email=email,
            contract_id=contract_id,
            code=code,
            pin=pin,
            nid=nid,
            identity_number_type=identity_number_type,
            ssn=ssn,
            phone=phone,
            date_of_birth=date_of_birth,
            custom_fields=custom_fields,
            nationality=nationality,
            marital_status=marital_status,
            address=address,
            postal_code=postal_code,
            emergency_phone=emergency_phone,
            children_count=children_count,
            disability=disability,
            personal_email=personal_email,
            city=city,
            province=province,
            country=country,
            salary_range=salary_range,
            study_level=study_level,
            professional_category_code=professional_category_code,
            professional_category_description=professional_category_description,
            bic=bic,
        )
        return await self._acreate_new_employee_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        company_id: str,
        first_name: str,
        last_name: str,
        invitation: bool,
        status: str,
        description: typing.Optional[str] = None,
        gender: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        contract_id: typing.Optional[str] = None,
        code: typing.Optional[int] = None,
        pin: typing.Optional[int] = None,
        nid: typing.Optional[str] = None,
        identity_number_type: typing.Optional[str] = None,
        ssn: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        date_of_birth: typing.Optional[date] = None,
        custom_fields: typing.Optional[EmployeesCreateNewEmployeeRequestCustomFields] = None,
        nationality: typing.Optional[str] = None,
        marital_status: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        emergency_phone: typing.Optional[str] = None,
        children_count: typing.Optional[int] = None,
        disability: typing.Optional[int] = None,
        personal_email: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        province: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        salary_range: typing.Optional[str] = None,
        study_level: typing.Optional[str] = None,
        professional_category_code: typing.Optional[str] = None,
        professional_category_description: typing.Optional[str] = None,
        bic: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_employee_mapped_args(
            company_id=company_id,
            first_name=first_name,
            last_name=last_name,
            invitation=invitation,
            status=status,
            description=description,
            gender=gender,
            email=email,
            contract_id=contract_id,
            code=code,
            pin=pin,
            nid=nid,
            identity_number_type=identity_number_type,
            ssn=ssn,
            phone=phone,
            date_of_birth=date_of_birth,
            custom_fields=custom_fields,
            nationality=nationality,
            marital_status=marital_status,
            address=address,
            postal_code=postal_code,
            emergency_phone=emergency_phone,
            children_count=children_count,
            disability=disability,
            personal_email=personal_email,
            city=city,
            province=province,
            country=country,
            salary_range=salary_range,
            study_level=study_level,
            professional_category_code=professional_category_code,
            professional_category_description=professional_category_description,
            bic=bic,
        )
        return self._create_new_employee_oapg(
            body=args.body,
        )

