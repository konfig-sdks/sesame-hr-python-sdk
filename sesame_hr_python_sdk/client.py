# coding: utf-8
"""
    Sesame Public API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0.0
    Generated by: https://konfigthis.com
"""

import typing
import inspect
from datetime import date, datetime
from sesame_hr_python_sdk.client_custom import ClientCustom
from sesame_hr_python_sdk.configuration import Configuration
from sesame_hr_python_sdk.api_client import ApiClient
from sesame_hr_python_sdk.type_util import copy_signature
from sesame_hr_python_sdk.apis.tags.absence_calendars_api import AbsenceCalendarsApi
from sesame_hr_python_sdk.apis.tags.absence_day_off_api import AbsenceDayOffApi
from sesame_hr_python_sdk.apis.tags.absence_day_off_requests_api import AbsenceDayOffRequestsApi
from sesame_hr_python_sdk.apis.tags.absence_types_api import AbsenceTypesApi
from sesame_hr_python_sdk.apis.tags.agreements_api import AgreementsApi
from sesame_hr_python_sdk.apis.tags.check_types_api import CheckTypesApi
from sesame_hr_python_sdk.apis.tags.check_validation_api import CheckValidationApi
from sesame_hr_python_sdk.apis.tags.company_api import CompanyApi
from sesame_hr_python_sdk.apis.tags.contracts_api import ContractsApi
from sesame_hr_python_sdk.apis.tags.custom_fields_api import CustomFieldsApi
from sesame_hr_python_sdk.apis.tags.customers_api import CustomersApi
from sesame_hr_python_sdk.apis.tags.departments_api import DepartmentsApi
from sesame_hr_python_sdk.apis.tags.documents_api import DocumentsApi
from sesame_hr_python_sdk.apis.tags.employee_agreements_api import EmployeeAgreementsApi
from sesame_hr_python_sdk.apis.tags.employee_assignations_roles_api import EmployeeAssignationsRolesApi
from sesame_hr_python_sdk.apis.tags.employee_department_assignations_api import EmployeeDepartmentAssignationsApi
from sesame_hr_python_sdk.apis.tags.employee_managers_api import EmployeeManagersApi
from sesame_hr_python_sdk.apis.tags.employee_office_assignations_api import EmployeeOfficeAssignationsApi
from sesame_hr_python_sdk.apis.tags.employee_schedule_templates_api import EmployeeScheduleTemplatesApi
from sesame_hr_python_sdk.apis.tags.employees_api import EmployeesApi
from sesame_hr_python_sdk.apis.tags.holiday_calendars_api import HolidayCalendarsApi
from sesame_hr_python_sdk.apis.tags.holidays_api import HolidaysApi
from sesame_hr_python_sdk.apis.tags.offices_api import OfficesApi
from sesame_hr_python_sdk.apis.tags.projects_api import ProjectsApi
from sesame_hr_python_sdk.apis.tags.recruitment_api import RecruitmentApi
from sesame_hr_python_sdk.apis.tags.roles_api import RolesApi
from sesame_hr_python_sdk.apis.tags.salaries_api import SalariesApi
from sesame_hr_python_sdk.apis.tags.schedule_templates_api import ScheduleTemplatesApi
from sesame_hr_python_sdk.apis.tags.security_api import SecurityApi
from sesame_hr_python_sdk.apis.tags.statistics_api import StatisticsApi
from sesame_hr_python_sdk.apis.tags.time_entries_api import TimeEntriesApi
from sesame_hr_python_sdk.apis.tags.vacation_calendars_api import VacationCalendarsApi
from sesame_hr_python_sdk.apis.tags.vacation_configurations_api import VacationConfigurationsApi
from sesame_hr_python_sdk.apis.tags.vacation_day_off_api import VacationDayOffApi
from sesame_hr_python_sdk.apis.tags.vacation_day_off_requests_api import VacationDayOffRequestsApi
from sesame_hr_python_sdk.apis.tags.work_breaks_api import WorkBreaksApi
from sesame_hr_python_sdk.apis.tags.work_entries_api import WorkEntriesApi



class SesameHr(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.absence_calendars: AbsenceCalendarsApi = AbsenceCalendarsApi(api_client)
        self.absence_day_off: AbsenceDayOffApi = AbsenceDayOffApi(api_client)
        self.absence_day_off_requests: AbsenceDayOffRequestsApi = AbsenceDayOffRequestsApi(api_client)
        self.absence_types: AbsenceTypesApi = AbsenceTypesApi(api_client)
        self.agreements: AgreementsApi = AgreementsApi(api_client)
        self.check_types: CheckTypesApi = CheckTypesApi(api_client)
        self.check_validation: CheckValidationApi = CheckValidationApi(api_client)
        self.company: CompanyApi = CompanyApi(api_client)
        self.contracts: ContractsApi = ContractsApi(api_client)
        self.custom_fields: CustomFieldsApi = CustomFieldsApi(api_client)
        self.customers: CustomersApi = CustomersApi(api_client)
        self.departments: DepartmentsApi = DepartmentsApi(api_client)
        self.documents: DocumentsApi = DocumentsApi(api_client)
        self.employee_agreements: EmployeeAgreementsApi = EmployeeAgreementsApi(api_client)
        self.employee_assignations_roles: EmployeeAssignationsRolesApi = EmployeeAssignationsRolesApi(api_client)
        self.employee_department_assignations: EmployeeDepartmentAssignationsApi = EmployeeDepartmentAssignationsApi(api_client)
        self.employee_managers: EmployeeManagersApi = EmployeeManagersApi(api_client)
        self.employee_office_assignations: EmployeeOfficeAssignationsApi = EmployeeOfficeAssignationsApi(api_client)
        self.employee_schedule_templates: EmployeeScheduleTemplatesApi = EmployeeScheduleTemplatesApi(api_client)
        self.employees: EmployeesApi = EmployeesApi(api_client)
        self.holiday_calendars: HolidayCalendarsApi = HolidayCalendarsApi(api_client)
        self.holidays: HolidaysApi = HolidaysApi(api_client)
        self.offices: OfficesApi = OfficesApi(api_client)
        self.projects: ProjectsApi = ProjectsApi(api_client)
        self.recruitment: RecruitmentApi = RecruitmentApi(api_client)
        self.roles: RolesApi = RolesApi(api_client)
        self.salaries: SalariesApi = SalariesApi(api_client)
        self.schedule_templates: ScheduleTemplatesApi = ScheduleTemplatesApi(api_client)
        self.security: SecurityApi = SecurityApi(api_client)
        self.statistics: StatisticsApi = StatisticsApi(api_client)
        self.time_entries: TimeEntriesApi = TimeEntriesApi(api_client)
        self.vacation_calendars: VacationCalendarsApi = VacationCalendarsApi(api_client)
        self.vacation_configurations: VacationConfigurationsApi = VacationConfigurationsApi(api_client)
        self.vacation_day_off: VacationDayOffApi = VacationDayOffApi(api_client)
        self.vacation_day_off_requests: VacationDayOffRequestsApi = VacationDayOffRequestsApi(api_client)
        self.work_breaks: WorkBreaksApi = WorkBreaksApi(api_client)
        self.work_entries: WorkEntriesApi = WorkEntriesApi(api_client)
