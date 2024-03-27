import typing_extensions

from sesame_hr_python_sdk.apis.tags import TagValues
from sesame_hr_python_sdk.apis.tags.recruitment_api import RecruitmentApi
from sesame_hr_python_sdk.apis.tags.work_entries_api import WorkEntriesApi
from sesame_hr_python_sdk.apis.tags.time_entries_api import TimeEntriesApi
from sesame_hr_python_sdk.apis.tags.employees_api import EmployeesApi
from sesame_hr_python_sdk.apis.tags.vacation_day_off_requests_api import VacationDayOffRequestsApi
from sesame_hr_python_sdk.apis.tags.absence_day_off_requests_api import AbsenceDayOffRequestsApi
from sesame_hr_python_sdk.apis.tags.holiday_calendars_api import HolidayCalendarsApi
from sesame_hr_python_sdk.apis.tags.agreements_api import AgreementsApi
from sesame_hr_python_sdk.apis.tags.contracts_api import ContractsApi
from sesame_hr_python_sdk.apis.tags.salaries_api import SalariesApi
from sesame_hr_python_sdk.apis.tags.departments_api import DepartmentsApi
from sesame_hr_python_sdk.apis.tags.offices_api import OfficesApi
from sesame_hr_python_sdk.apis.tags.custom_fields_api import CustomFieldsApi
from sesame_hr_python_sdk.apis.tags.statistics_api import StatisticsApi
from sesame_hr_python_sdk.apis.tags.holidays_api import HolidaysApi
from sesame_hr_python_sdk.apis.tags.customers_api import CustomersApi
from sesame_hr_python_sdk.apis.tags.projects_api import ProjectsApi
from sesame_hr_python_sdk.apis.tags.employee_managers_api import EmployeeManagersApi
from sesame_hr_python_sdk.apis.tags.employee_assignations_roles_api import EmployeeAssignationsRolesApi
from sesame_hr_python_sdk.apis.tags.employee_department_assignations_api import EmployeeDepartmentAssignationsApi
from sesame_hr_python_sdk.apis.tags.employee_office_assignations_api import EmployeeOfficeAssignationsApi
from sesame_hr_python_sdk.apis.tags.vacation_calendars_api import VacationCalendarsApi
from sesame_hr_python_sdk.apis.tags.absence_calendars_api import AbsenceCalendarsApi
from sesame_hr_python_sdk.apis.tags.employee_schedule_templates_api import EmployeeScheduleTemplatesApi
from sesame_hr_python_sdk.apis.tags.employee_agreements_api import EmployeeAgreementsApi
from sesame_hr_python_sdk.apis.tags.documents_api import DocumentsApi
from sesame_hr_python_sdk.apis.tags.security_api import SecurityApi
from sesame_hr_python_sdk.apis.tags.company_api import CompanyApi
from sesame_hr_python_sdk.apis.tags.roles_api import RolesApi
from sesame_hr_python_sdk.apis.tags.check_types_api import CheckTypesApi
from sesame_hr_python_sdk.apis.tags.work_breaks_api import WorkBreaksApi
from sesame_hr_python_sdk.apis.tags.check_validation_api import CheckValidationApi
from sesame_hr_python_sdk.apis.tags.vacation_configurations_api import VacationConfigurationsApi
from sesame_hr_python_sdk.apis.tags.vacation_day_off_api import VacationDayOffApi
from sesame_hr_python_sdk.apis.tags.absence_types_api import AbsenceTypesApi
from sesame_hr_python_sdk.apis.tags.absence_day_off_api import AbsenceDayOffApi
from sesame_hr_python_sdk.apis.tags.schedule_templates_api import ScheduleTemplatesApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.RECRUITMENT: RecruitmentApi,
        TagValues.WORK_ENTRIES: WorkEntriesApi,
        TagValues.TIME_ENTRIES: TimeEntriesApi,
        TagValues.EMPLOYEES: EmployeesApi,
        TagValues.VACATION_DAY_OFF_REQUESTS: VacationDayOffRequestsApi,
        TagValues.ABSENCE_DAY_OFF_REQUESTS: AbsenceDayOffRequestsApi,
        TagValues.HOLIDAY_CALENDARS: HolidayCalendarsApi,
        TagValues.AGREEMENTS: AgreementsApi,
        TagValues.CONTRACTS: ContractsApi,
        TagValues.SALARIES: SalariesApi,
        TagValues.DEPARTMENTS: DepartmentsApi,
        TagValues.OFFICES: OfficesApi,
        TagValues.CUSTOM_FIELDS: CustomFieldsApi,
        TagValues.STATISTICS: StatisticsApi,
        TagValues.HOLIDAYS: HolidaysApi,
        TagValues.CUSTOMERS: CustomersApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.EMPLOYEE_MANAGERS: EmployeeManagersApi,
        TagValues.EMPLOYEE_ASSIGNATIONS_ROLES: EmployeeAssignationsRolesApi,
        TagValues.EMPLOYEE_DEPARTMENT_ASSIGNATIONS: EmployeeDepartmentAssignationsApi,
        TagValues.EMPLOYEE_OFFICE_ASSIGNATIONS: EmployeeOfficeAssignationsApi,
        TagValues.VACATION_CALENDARS: VacationCalendarsApi,
        TagValues.ABSENCE_CALENDARS: AbsenceCalendarsApi,
        TagValues.EMPLOYEE_SCHEDULE_TEMPLATES: EmployeeScheduleTemplatesApi,
        TagValues.EMPLOYEE_AGREEMENTS: EmployeeAgreementsApi,
        TagValues.DOCUMENTS: DocumentsApi,
        TagValues.SECURITY: SecurityApi,
        TagValues.COMPANY: CompanyApi,
        TagValues.ROLES: RolesApi,
        TagValues.CHECK_TYPES: CheckTypesApi,
        TagValues.WORK_BREAKS: WorkBreaksApi,
        TagValues.CHECK_VALIDATION: CheckValidationApi,
        TagValues.VACATION_CONFIGURATIONS: VacationConfigurationsApi,
        TagValues.VACATION_DAY_OFF: VacationDayOffApi,
        TagValues.ABSENCE_TYPES: AbsenceTypesApi,
        TagValues.ABSENCE_DAY_OFF: AbsenceDayOffApi,
        TagValues.SCHEDULE_TEMPLATES: ScheduleTemplatesApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.RECRUITMENT: RecruitmentApi,
        TagValues.WORK_ENTRIES: WorkEntriesApi,
        TagValues.TIME_ENTRIES: TimeEntriesApi,
        TagValues.EMPLOYEES: EmployeesApi,
        TagValues.VACATION_DAY_OFF_REQUESTS: VacationDayOffRequestsApi,
        TagValues.ABSENCE_DAY_OFF_REQUESTS: AbsenceDayOffRequestsApi,
        TagValues.HOLIDAY_CALENDARS: HolidayCalendarsApi,
        TagValues.AGREEMENTS: AgreementsApi,
        TagValues.CONTRACTS: ContractsApi,
        TagValues.SALARIES: SalariesApi,
        TagValues.DEPARTMENTS: DepartmentsApi,
        TagValues.OFFICES: OfficesApi,
        TagValues.CUSTOM_FIELDS: CustomFieldsApi,
        TagValues.STATISTICS: StatisticsApi,
        TagValues.HOLIDAYS: HolidaysApi,
        TagValues.CUSTOMERS: CustomersApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.EMPLOYEE_MANAGERS: EmployeeManagersApi,
        TagValues.EMPLOYEE_ASSIGNATIONS_ROLES: EmployeeAssignationsRolesApi,
        TagValues.EMPLOYEE_DEPARTMENT_ASSIGNATIONS: EmployeeDepartmentAssignationsApi,
        TagValues.EMPLOYEE_OFFICE_ASSIGNATIONS: EmployeeOfficeAssignationsApi,
        TagValues.VACATION_CALENDARS: VacationCalendarsApi,
        TagValues.ABSENCE_CALENDARS: AbsenceCalendarsApi,
        TagValues.EMPLOYEE_SCHEDULE_TEMPLATES: EmployeeScheduleTemplatesApi,
        TagValues.EMPLOYEE_AGREEMENTS: EmployeeAgreementsApi,
        TagValues.DOCUMENTS: DocumentsApi,
        TagValues.SECURITY: SecurityApi,
        TagValues.COMPANY: CompanyApi,
        TagValues.ROLES: RolesApi,
        TagValues.CHECK_TYPES: CheckTypesApi,
        TagValues.WORK_BREAKS: WorkBreaksApi,
        TagValues.CHECK_VALIDATION: CheckValidationApi,
        TagValues.VACATION_CONFIGURATIONS: VacationConfigurationsApi,
        TagValues.VACATION_DAY_OFF: VacationDayOffApi,
        TagValues.ABSENCE_TYPES: AbsenceTypesApi,
        TagValues.ABSENCE_DAY_OFF: AbsenceDayOffApi,
        TagValues.SCHEDULE_TEMPLATES: ScheduleTemplatesApi,
    }
)
