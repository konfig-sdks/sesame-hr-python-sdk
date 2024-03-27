# coding: utf-8

"""
    Sesame Public API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0.0
    Generated by: https://konfigthis.com
"""

from sesame_hr_python_sdk.paths.contract_v1_contracts.post import CreateNewContract
from sesame_hr_python_sdk.paths.contract_v1_contracts_contract_id.delete import DeleteContract
from sesame_hr_python_sdk.paths.contract_v1_contracts_employee_id.get import GetByEmployeeId
from sesame_hr_python_sdk.paths.contract_v1_contracts_employee_id_current_contract.get import GetCurrentContractByEmployeeId
from sesame_hr_python_sdk.paths.contract_v1_contracts_contract_id.put import UpdateContract
from sesame_hr_python_sdk.apis.tags.contracts_api_raw import ContractsApiRaw


class ContractsApi(
    CreateNewContract,
    DeleteContract,
    GetByEmployeeId,
    GetCurrentContractByEmployeeId,
    UpdateContract,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ContractsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ContractsApiRaw(api_client)
