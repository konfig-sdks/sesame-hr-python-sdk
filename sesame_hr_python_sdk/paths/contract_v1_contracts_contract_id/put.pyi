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

from sesame_hr_python_sdk.model.contracts_update_contract_response import ContractsUpdateContractResponse as ContractsUpdateContractResponseSchema
from sesame_hr_python_sdk.model.contracts_update_contract_request import ContractsUpdateContractRequest as ContractsUpdateContractRequestSchema

from sesame_hr_python_sdk.type.contracts_update_contract_request import ContractsUpdateContractRequest
from sesame_hr_python_sdk.type.contracts_update_contract_response import ContractsUpdateContractResponse

from ...api_client import Dictionary
from sesame_hr_python_sdk.pydantic.contracts_update_contract_response import ContractsUpdateContractResponse as ContractsUpdateContractResponsePydantic
from sesame_hr_python_sdk.pydantic.contracts_update_contract_request import ContractsUpdateContractRequest as ContractsUpdateContractRequestPydantic

# Path params
ContractIdSchema = schemas.UUIDSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'contractId': typing.Union[ContractIdSchema, str, uuid.UUID, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_contract_id = api_client.PathParameter(
    name="contractId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ContractIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = ContractsUpdateContractRequestSchema


request_body_contracts_update_contract_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = ContractsUpdateContractResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ContractsUpdateContractResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ContractsUpdateContractResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _update_contract_mapped_args(
        self,
        start_at: date,
        code: str,
        contract_id: str,
        end_at: typing.Optional[date] = None,
        comment: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if start_at is not None:
            _body["startAt"] = start_at
        if end_at is not None:
            _body["endAt"] = end_at
        if code is not None:
            _body["code"] = code
        if comment is not None:
            _body["comment"] = comment
        args.body = _body
        if contract_id is not None:
            _path_params["contractId"] = contract_id
        args.path = _path_params
        return args

    async def _aupdate_contract_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
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
        Update a contract
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_contract_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
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
            path_template='/contract/v1/contracts/{contractId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_contracts_update_contract_request.serialize(body, content_type)
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


    def _update_contract_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
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
        Update a contract
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_contract_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
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
            path_template='/contract/v1/contracts/{contractId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_contracts_update_contract_request.serialize(body, content_type)
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


class UpdateContractRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_contract(
        self,
        start_at: date,
        code: str,
        contract_id: str,
        end_at: typing.Optional[date] = None,
        comment: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_contract_mapped_args(
            start_at=start_at,
            code=code,
            contract_id=contract_id,
            end_at=end_at,
            comment=comment,
        )
        return await self._aupdate_contract_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_contract(
        self,
        start_at: date,
        code: str,
        contract_id: str,
        end_at: typing.Optional[date] = None,
        comment: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_contract_mapped_args(
            start_at=start_at,
            code=code,
            contract_id=contract_id,
            end_at=end_at,
            comment=comment,
        )
        return self._update_contract_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateContract(BaseApi):

    async def aupdate_contract(
        self,
        start_at: date,
        code: str,
        contract_id: str,
        end_at: typing.Optional[date] = None,
        comment: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ContractsUpdateContractResponsePydantic:
        raw_response = await self.raw.aupdate_contract(
            start_at=start_at,
            code=code,
            contract_id=contract_id,
            end_at=end_at,
            comment=comment,
            **kwargs,
        )
        if validate:
            return ContractsUpdateContractResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ContractsUpdateContractResponsePydantic, raw_response.body)
    
    
    def update_contract(
        self,
        start_at: date,
        code: str,
        contract_id: str,
        end_at: typing.Optional[date] = None,
        comment: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ContractsUpdateContractResponsePydantic:
        raw_response = self.raw.update_contract(
            start_at=start_at,
            code=code,
            contract_id=contract_id,
            end_at=end_at,
            comment=comment,
        )
        if validate:
            return ContractsUpdateContractResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ContractsUpdateContractResponsePydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        start_at: date,
        code: str,
        contract_id: str,
        end_at: typing.Optional[date] = None,
        comment: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_contract_mapped_args(
            start_at=start_at,
            code=code,
            contract_id=contract_id,
            end_at=end_at,
            comment=comment,
        )
        return await self._aupdate_contract_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        start_at: date,
        code: str,
        contract_id: str,
        end_at: typing.Optional[date] = None,
        comment: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_contract_mapped_args(
            start_at=start_at,
            code=code,
            contract_id=contract_id,
            end_at=end_at,
            comment=comment,
        )
        return self._update_contract_oapg(
            body=args.body,
            path_params=args.path,
        )

