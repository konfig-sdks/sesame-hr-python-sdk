import typing_extensions

from sesame_hr_python_sdk.paths import PathValues
from sesame_hr_python_sdk.apis.paths.core_v3_info import CoreV3Info
from sesame_hr_python_sdk.apis.paths.core_v3_companies_id import CoreV3CompaniesId
from sesame_hr_python_sdk.apis.paths.core_v3_employees import CoreV3Employees
from sesame_hr_python_sdk.apis.paths.core_v3_employees_id import CoreV3EmployeesId
from sesame_hr_python_sdk.apis.paths.core_v3_employee_managers import CoreV3EmployeeManagers
from sesame_hr_python_sdk.apis.paths.core_v3_employee_managers_id import CoreV3EmployeeManagersId
from sesame_hr_python_sdk.apis.paths.core_v3_roles import CoreV3Roles
from sesame_hr_python_sdk.apis.paths.core_v3_roles_assignation_employee_id import CoreV3RolesAssignationEmployeeId
from sesame_hr_python_sdk.apis.paths.core_v3_roles_assignation import CoreV3RolesAssignation
from sesame_hr_python_sdk.apis.paths.core_v3_departments import CoreV3Departments
from sesame_hr_python_sdk.apis.paths.core_v3_departments_id import CoreV3DepartmentsId
from sesame_hr_python_sdk.apis.paths.core_v3_employee_department_assignations import CoreV3EmployeeDepartmentAssignations
from sesame_hr_python_sdk.apis.paths.core_v3_offices import CoreV3Offices
from sesame_hr_python_sdk.apis.paths.core_v3_offices_id import CoreV3OfficesId
from sesame_hr_python_sdk.apis.paths.core_v3_employee_office_assignations import CoreV3EmployeeOfficeAssignations
from sesame_hr_python_sdk.apis.paths.core_v3_custom_fields import CoreV3CustomFields
from sesame_hr_python_sdk.apis.paths.core_v3_custom_fields_id import CoreV3CustomFieldsId
from sesame_hr_python_sdk.apis.paths.schedule_v1_work_entries_clock_in import ScheduleV1WorkEntriesClockIn
from sesame_hr_python_sdk.apis.paths.schedule_v1_work_entries_clock_out import ScheduleV1WorkEntriesClockOut
from sesame_hr_python_sdk.apis.paths.schedule_v1_work_entries import ScheduleV1WorkEntries
from sesame_hr_python_sdk.apis.paths.schedule_v1_work_entries_id import ScheduleV1WorkEntriesId
from sesame_hr_python_sdk.apis.paths.schedule_v1_check_types import ScheduleV1CheckTypes
from sesame_hr_python_sdk.apis.paths.schedule_v1_work_breaks import ScheduleV1WorkBreaks
from sesame_hr_python_sdk.apis.paths.schedule_v1_check_validation import ScheduleV1CheckValidation
from sesame_hr_python_sdk.apis.paths.schedule_v1_reports_worked_hours import ScheduleV1ReportsWorkedHours
from sesame_hr_python_sdk.apis.paths.schedule_v1_reports_worked_hours_by_week_day import ScheduleV1ReportsWorkedHoursByWeekDay
from sesame_hr_python_sdk.apis.paths.schedule_v1_reports_worked_night_hours import ScheduleV1ReportsWorkedNightHours
from sesame_hr_python_sdk.apis.paths.schedule_v1_reports_worked_absence_days import ScheduleV1ReportsWorkedAbsenceDays
from sesame_hr_python_sdk.apis.paths.schedule_v1_vacation_configurations import ScheduleV1VacationConfigurations
from sesame_hr_python_sdk.apis.paths.schedule_v1_vacation_calendars import ScheduleV1VacationCalendars
from sesame_hr_python_sdk.apis.paths.schedule_v1_vacation_calendars_id import ScheduleV1VacationCalendarsId
from sesame_hr_python_sdk.apis.paths.schedule_v1_vacation_day_off import ScheduleV1VacationDayOff
from sesame_hr_python_sdk.apis.paths.schedule_v1_vacation_day_off_requests import ScheduleV1VacationDayOffRequests
from sesame_hr_python_sdk.apis.paths.schedule_v1_vacation_day_off_requests_id_accept import ScheduleV1VacationDayOffRequestsIdAccept
from sesame_hr_python_sdk.apis.paths.schedule_v1_vacation_day_off_requests_id_reject import ScheduleV1VacationDayOffRequestsIdReject
from sesame_hr_python_sdk.apis.paths.schedule_v1_vacation_day_off_requests_id import ScheduleV1VacationDayOffRequestsId
from sesame_hr_python_sdk.apis.paths.schedule_v1_absence_types import ScheduleV1AbsenceTypes
from sesame_hr_python_sdk.apis.paths.schedule_v1_absence_calendars import ScheduleV1AbsenceCalendars
from sesame_hr_python_sdk.apis.paths.schedule_v1_absence_calendars_id import ScheduleV1AbsenceCalendarsId
from sesame_hr_python_sdk.apis.paths.schedule_v1_absence_day_off import ScheduleV1AbsenceDayOff
from sesame_hr_python_sdk.apis.paths.schedule_v1_absence_day_off_requests import ScheduleV1AbsenceDayOffRequests
from sesame_hr_python_sdk.apis.paths.schedule_v1_absence_day_off_requests_id_accept import ScheduleV1AbsenceDayOffRequestsIdAccept
from sesame_hr_python_sdk.apis.paths.schedule_v1_absence_day_off_requests_id_reject import ScheduleV1AbsenceDayOffRequestsIdReject
from sesame_hr_python_sdk.apis.paths.schedule_v1_absence_day_off_requests_id import ScheduleV1AbsenceDayOffRequestsId
from sesame_hr_python_sdk.apis.paths.schedule_v1_holiday_calendar import ScheduleV1HolidayCalendar
from sesame_hr_python_sdk.apis.paths.schedule_v1_holiday_calendar_holiday_calendar_id import ScheduleV1HolidayCalendarHolidayCalendarId
from sesame_hr_python_sdk.apis.paths.schedule_v1_holidays import ScheduleV1Holidays
from sesame_hr_python_sdk.apis.paths.schedule_v1_holidays_holiday_calendar_id_employees import ScheduleV1HolidaysHolidayCalendarIdEmployees
from sesame_hr_python_sdk.apis.paths.schedule_v1_schedule_templates import ScheduleV1ScheduleTemplates
from sesame_hr_python_sdk.apis.paths.schedule_v1_employees_employee_id_schedule_templates import ScheduleV1EmployeesEmployeeIdScheduleTemplates
from sesame_hr_python_sdk.apis.paths.schedule_v1_entity_schedule_templates import ScheduleV1EntityScheduleTemplates
from sesame_hr_python_sdk.apis.paths.schedule_v1_entity_schedule_templates_entity_schedule_template_id import ScheduleV1EntityScheduleTemplatesEntityScheduleTemplateId
from sesame_hr_python_sdk.apis.paths.schedule_v1_agreements import ScheduleV1Agreements
from sesame_hr_python_sdk.apis.paths.schedule_v1_agreements_agreement_id import ScheduleV1AgreementsAgreementId
from sesame_hr_python_sdk.apis.paths.schedule_v1_agreement_employees import ScheduleV1AgreementEmployees
from sesame_hr_python_sdk.apis.paths.schedule_v1_agreement_employees_agreement_employee_id import ScheduleV1AgreementEmployeesAgreementEmployeeId
from sesame_hr_python_sdk.apis.paths.contract_v1_contracts_employee_id import ContractV1ContractsEmployeeId
from sesame_hr_python_sdk.apis.paths.contract_v1_contracts import ContractV1Contracts
from sesame_hr_python_sdk.apis.paths.contract_v1_contracts_contract_id import ContractV1ContractsContractId
from sesame_hr_python_sdk.apis.paths.contract_v1_contracts_employee_id_current_contract import ContractV1ContractsEmployeeIdCurrentContract
from sesame_hr_python_sdk.apis.paths.contract_v1_contribution_groups import ContractV1ContributionGroups
from sesame_hr_python_sdk.apis.paths.contract_v1_salaries import ContractV1Salaries
from sesame_hr_python_sdk.apis.paths.contract_v1_salaries_salary_id import ContractV1SalariesSalaryId
from sesame_hr_python_sdk.apis.paths.project_v1_time_entries_start import ProjectV1TimeEntriesStart
from sesame_hr_python_sdk.apis.paths.project_v1_time_entries_stop import ProjectV1TimeEntriesStop
from sesame_hr_python_sdk.apis.paths.project_v1_time_entries import ProjectV1TimeEntries
from sesame_hr_python_sdk.apis.paths.project_v1_time_entries_id import ProjectV1TimeEntriesId
from sesame_hr_python_sdk.apis.paths.project_v1_customers import ProjectV1Customers
from sesame_hr_python_sdk.apis.paths.project_v1_customers_id import ProjectV1CustomersId
from sesame_hr_python_sdk.apis.paths.project_v1_projects import ProjectV1Projects
from sesame_hr_python_sdk.apis.paths.project_v1_projects_id import ProjectV1ProjectsId
from sesame_hr_python_sdk.apis.paths.document_v1_directories import DocumentV1Directories
from sesame_hr_python_sdk.apis.paths.document_v1_directories_directory_id_documents import DocumentV1DirectoriesDirectoryIdDocuments
from sesame_hr_python_sdk.apis.paths.recruitment_v1_vacancies import RecruitmentV1Vacancies
from sesame_hr_python_sdk.apis.paths.recruitment_v1_vacancies_id import RecruitmentV1VacanciesId
from sesame_hr_python_sdk.apis.paths.recruitment_v1_candidates import RecruitmentV1Candidates
from sesame_hr_python_sdk.apis.paths.recruitment_v1_candidates_id import RecruitmentV1CandidatesId
from sesame_hr_python_sdk.apis.paths.recruitment_v1_candidate_status_vacancy_id import RecruitmentV1CandidateStatusVacancyId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.CORE_V3_INFO: CoreV3Info,
        PathValues.CORE_V3_COMPANIES_ID: CoreV3CompaniesId,
        PathValues.CORE_V3_EMPLOYEES: CoreV3Employees,
        PathValues.CORE_V3_EMPLOYEES_ID: CoreV3EmployeesId,
        PathValues.CORE_V3_EMPLOYEEMANAGERS: CoreV3EmployeeManagers,
        PathValues.CORE_V3_EMPLOYEEMANAGERS_ID: CoreV3EmployeeManagersId,
        PathValues.CORE_V3_ROLES: CoreV3Roles,
        PathValues.CORE_V3_ROLES_ASSIGNATION_EMPLOYEE_ID: CoreV3RolesAssignationEmployeeId,
        PathValues.CORE_V3_ROLES_ASSIGNATION: CoreV3RolesAssignation,
        PathValues.CORE_V3_DEPARTMENTS: CoreV3Departments,
        PathValues.CORE_V3_DEPARTMENTS_ID: CoreV3DepartmentsId,
        PathValues.CORE_V3_EMPLOYEEDEPARTMENTASSIGNATIONS: CoreV3EmployeeDepartmentAssignations,
        PathValues.CORE_V3_OFFICES: CoreV3Offices,
        PathValues.CORE_V3_OFFICES_ID: CoreV3OfficesId,
        PathValues.CORE_V3_EMPLOYEEOFFICEASSIGNATIONS: CoreV3EmployeeOfficeAssignations,
        PathValues.CORE_V3_CUSTOMFIELDS: CoreV3CustomFields,
        PathValues.CORE_V3_CUSTOMFIELDS_ID: CoreV3CustomFieldsId,
        PathValues.SCHEDULE_V1_WORKENTRIES_CLOCKIN: ScheduleV1WorkEntriesClockIn,
        PathValues.SCHEDULE_V1_WORKENTRIES_CLOCKOUT: ScheduleV1WorkEntriesClockOut,
        PathValues.SCHEDULE_V1_WORKENTRIES: ScheduleV1WorkEntries,
        PathValues.SCHEDULE_V1_WORKENTRIES_ID: ScheduleV1WorkEntriesId,
        PathValues.SCHEDULE_V1_CHECKTYPES: ScheduleV1CheckTypes,
        PathValues.SCHEDULE_V1_WORKBREAKS: ScheduleV1WorkBreaks,
        PathValues.SCHEDULE_V1_CHECKVALIDATION: ScheduleV1CheckValidation,
        PathValues.SCHEDULE_V1_REPORTS_WORKEDHOURS: ScheduleV1ReportsWorkedHours,
        PathValues.SCHEDULE_V1_REPORTS_WORKEDHOURSBYWEEKDAY: ScheduleV1ReportsWorkedHoursByWeekDay,
        PathValues.SCHEDULE_V1_REPORTS_WORKEDNIGHTHOURS: ScheduleV1ReportsWorkedNightHours,
        PathValues.SCHEDULE_V1_REPORTS_WORKEDABSENCEDAYS: ScheduleV1ReportsWorkedAbsenceDays,
        PathValues.SCHEDULE_V1_VACATIONCONFIGURATIONS: ScheduleV1VacationConfigurations,
        PathValues.SCHEDULE_V1_VACATIONCALENDARS: ScheduleV1VacationCalendars,
        PathValues.SCHEDULE_V1_VACATIONCALENDARS_ID: ScheduleV1VacationCalendarsId,
        PathValues.SCHEDULE_V1_VACATIONDAYOFF: ScheduleV1VacationDayOff,
        PathValues.SCHEDULE_V1_VACATIONDAYOFFREQUESTS: ScheduleV1VacationDayOffRequests,
        PathValues.SCHEDULE_V1_VACATIONDAYOFFREQUESTS_ID_ACCEPT: ScheduleV1VacationDayOffRequestsIdAccept,
        PathValues.SCHEDULE_V1_VACATIONDAYOFFREQUESTS_ID_REJECT: ScheduleV1VacationDayOffRequestsIdReject,
        PathValues.SCHEDULE_V1_VACATIONDAYOFFREQUESTS_ID: ScheduleV1VacationDayOffRequestsId,
        PathValues.SCHEDULE_V1_ABSENCETYPES: ScheduleV1AbsenceTypes,
        PathValues.SCHEDULE_V1_ABSENCECALENDARS: ScheduleV1AbsenceCalendars,
        PathValues.SCHEDULE_V1_ABSENCECALENDARS_ID: ScheduleV1AbsenceCalendarsId,
        PathValues.SCHEDULE_V1_ABSENCEDAYOFF: ScheduleV1AbsenceDayOff,
        PathValues.SCHEDULE_V1_ABSENCEDAYOFFREQUESTS: ScheduleV1AbsenceDayOffRequests,
        PathValues.SCHEDULE_V1_ABSENCEDAYOFFREQUESTS_ID_ACCEPT: ScheduleV1AbsenceDayOffRequestsIdAccept,
        PathValues.SCHEDULE_V1_ABSENCEDAYOFFREQUESTS_ID_REJECT: ScheduleV1AbsenceDayOffRequestsIdReject,
        PathValues.SCHEDULE_V1_ABSENCEDAYOFFREQUESTS_ID: ScheduleV1AbsenceDayOffRequestsId,
        PathValues.SCHEDULE_V1_HOLIDAYCALENDAR: ScheduleV1HolidayCalendar,
        PathValues.SCHEDULE_V1_HOLIDAYCALENDAR_HOLIDAY_CALENDAR_ID: ScheduleV1HolidayCalendarHolidayCalendarId,
        PathValues.SCHEDULE_V1_HOLIDAYS: ScheduleV1Holidays,
        PathValues.SCHEDULE_V1_HOLIDAYS_HOLIDAY_CALENDAR_ID_EMPLOYEES: ScheduleV1HolidaysHolidayCalendarIdEmployees,
        PathValues.SCHEDULE_V1_SCHEDULETEMPLATES: ScheduleV1ScheduleTemplates,
        PathValues.SCHEDULE_V1_EMPLOYEES_EMPLOYEE_ID_SCHEDULETEMPLATES: ScheduleV1EmployeesEmployeeIdScheduleTemplates,
        PathValues.SCHEDULE_V1_ENTITYSCHEDULETEMPLATES: ScheduleV1EntityScheduleTemplates,
        PathValues.SCHEDULE_V1_ENTITYSCHEDULETEMPLATES_ENTITY_SCHEDULE_TEMPLATE_ID: ScheduleV1EntityScheduleTemplatesEntityScheduleTemplateId,
        PathValues.SCHEDULE_V1_AGREEMENTS: ScheduleV1Agreements,
        PathValues.SCHEDULE_V1_AGREEMENTS_AGREEMENT_ID: ScheduleV1AgreementsAgreementId,
        PathValues.SCHEDULE_V1_AGREEMENTEMPLOYEES: ScheduleV1AgreementEmployees,
        PathValues.SCHEDULE_V1_AGREEMENTEMPLOYEES_AGREEMENT_EMPLOYEE_ID: ScheduleV1AgreementEmployeesAgreementEmployeeId,
        PathValues.CONTRACT_V1_CONTRACTS_EMPLOYEE_ID: ContractV1ContractsEmployeeId,
        PathValues.CONTRACT_V1_CONTRACTS: ContractV1Contracts,
        PathValues.CONTRACT_V1_CONTRACTS_CONTRACT_ID: ContractV1ContractsContractId,
        PathValues.CONTRACT_V1_CONTRACTS_EMPLOYEE_ID_CURRENTCONTRACT: ContractV1ContractsEmployeeIdCurrentContract,
        PathValues.CONTRACT_V1_CONTRIBUTIONGROUPS: ContractV1ContributionGroups,
        PathValues.CONTRACT_V1_SALARIES: ContractV1Salaries,
        PathValues.CONTRACT_V1_SALARIES_SALARY_ID: ContractV1SalariesSalaryId,
        PathValues.PROJECT_V1_TIMEENTRIES_START: ProjectV1TimeEntriesStart,
        PathValues.PROJECT_V1_TIMEENTRIES_STOP: ProjectV1TimeEntriesStop,
        PathValues.PROJECT_V1_TIMEENTRIES: ProjectV1TimeEntries,
        PathValues.PROJECT_V1_TIMEENTRIES_ID: ProjectV1TimeEntriesId,
        PathValues.PROJECT_V1_CUSTOMERS: ProjectV1Customers,
        PathValues.PROJECT_V1_CUSTOMERS_ID: ProjectV1CustomersId,
        PathValues.PROJECT_V1_PROJECTS: ProjectV1Projects,
        PathValues.PROJECT_V1_PROJECTS_ID: ProjectV1ProjectsId,
        PathValues.DOCUMENT_V1_DIRECTORIES: DocumentV1Directories,
        PathValues.DOCUMENT_V1_DIRECTORIES_DIRECTORY_ID_DOCUMENTS: DocumentV1DirectoriesDirectoryIdDocuments,
        PathValues.RECRUITMENT_V1_VACANCIES: RecruitmentV1Vacancies,
        PathValues.RECRUITMENT_V1_VACANCIES_ID: RecruitmentV1VacanciesId,
        PathValues.RECRUITMENT_V1_CANDIDATES: RecruitmentV1Candidates,
        PathValues.RECRUITMENT_V1_CANDIDATES_ID: RecruitmentV1CandidatesId,
        PathValues.RECRUITMENT_V1_CANDIDATESTATUS_VACANCY_ID: RecruitmentV1CandidateStatusVacancyId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.CORE_V3_INFO: CoreV3Info,
        PathValues.CORE_V3_COMPANIES_ID: CoreV3CompaniesId,
        PathValues.CORE_V3_EMPLOYEES: CoreV3Employees,
        PathValues.CORE_V3_EMPLOYEES_ID: CoreV3EmployeesId,
        PathValues.CORE_V3_EMPLOYEEMANAGERS: CoreV3EmployeeManagers,
        PathValues.CORE_V3_EMPLOYEEMANAGERS_ID: CoreV3EmployeeManagersId,
        PathValues.CORE_V3_ROLES: CoreV3Roles,
        PathValues.CORE_V3_ROLES_ASSIGNATION_EMPLOYEE_ID: CoreV3RolesAssignationEmployeeId,
        PathValues.CORE_V3_ROLES_ASSIGNATION: CoreV3RolesAssignation,
        PathValues.CORE_V3_DEPARTMENTS: CoreV3Departments,
        PathValues.CORE_V3_DEPARTMENTS_ID: CoreV3DepartmentsId,
        PathValues.CORE_V3_EMPLOYEEDEPARTMENTASSIGNATIONS: CoreV3EmployeeDepartmentAssignations,
        PathValues.CORE_V3_OFFICES: CoreV3Offices,
        PathValues.CORE_V3_OFFICES_ID: CoreV3OfficesId,
        PathValues.CORE_V3_EMPLOYEEOFFICEASSIGNATIONS: CoreV3EmployeeOfficeAssignations,
        PathValues.CORE_V3_CUSTOMFIELDS: CoreV3CustomFields,
        PathValues.CORE_V3_CUSTOMFIELDS_ID: CoreV3CustomFieldsId,
        PathValues.SCHEDULE_V1_WORKENTRIES_CLOCKIN: ScheduleV1WorkEntriesClockIn,
        PathValues.SCHEDULE_V1_WORKENTRIES_CLOCKOUT: ScheduleV1WorkEntriesClockOut,
        PathValues.SCHEDULE_V1_WORKENTRIES: ScheduleV1WorkEntries,
        PathValues.SCHEDULE_V1_WORKENTRIES_ID: ScheduleV1WorkEntriesId,
        PathValues.SCHEDULE_V1_CHECKTYPES: ScheduleV1CheckTypes,
        PathValues.SCHEDULE_V1_WORKBREAKS: ScheduleV1WorkBreaks,
        PathValues.SCHEDULE_V1_CHECKVALIDATION: ScheduleV1CheckValidation,
        PathValues.SCHEDULE_V1_REPORTS_WORKEDHOURS: ScheduleV1ReportsWorkedHours,
        PathValues.SCHEDULE_V1_REPORTS_WORKEDHOURSBYWEEKDAY: ScheduleV1ReportsWorkedHoursByWeekDay,
        PathValues.SCHEDULE_V1_REPORTS_WORKEDNIGHTHOURS: ScheduleV1ReportsWorkedNightHours,
        PathValues.SCHEDULE_V1_REPORTS_WORKEDABSENCEDAYS: ScheduleV1ReportsWorkedAbsenceDays,
        PathValues.SCHEDULE_V1_VACATIONCONFIGURATIONS: ScheduleV1VacationConfigurations,
        PathValues.SCHEDULE_V1_VACATIONCALENDARS: ScheduleV1VacationCalendars,
        PathValues.SCHEDULE_V1_VACATIONCALENDARS_ID: ScheduleV1VacationCalendarsId,
        PathValues.SCHEDULE_V1_VACATIONDAYOFF: ScheduleV1VacationDayOff,
        PathValues.SCHEDULE_V1_VACATIONDAYOFFREQUESTS: ScheduleV1VacationDayOffRequests,
        PathValues.SCHEDULE_V1_VACATIONDAYOFFREQUESTS_ID_ACCEPT: ScheduleV1VacationDayOffRequestsIdAccept,
        PathValues.SCHEDULE_V1_VACATIONDAYOFFREQUESTS_ID_REJECT: ScheduleV1VacationDayOffRequestsIdReject,
        PathValues.SCHEDULE_V1_VACATIONDAYOFFREQUESTS_ID: ScheduleV1VacationDayOffRequestsId,
        PathValues.SCHEDULE_V1_ABSENCETYPES: ScheduleV1AbsenceTypes,
        PathValues.SCHEDULE_V1_ABSENCECALENDARS: ScheduleV1AbsenceCalendars,
        PathValues.SCHEDULE_V1_ABSENCECALENDARS_ID: ScheduleV1AbsenceCalendarsId,
        PathValues.SCHEDULE_V1_ABSENCEDAYOFF: ScheduleV1AbsenceDayOff,
        PathValues.SCHEDULE_V1_ABSENCEDAYOFFREQUESTS: ScheduleV1AbsenceDayOffRequests,
        PathValues.SCHEDULE_V1_ABSENCEDAYOFFREQUESTS_ID_ACCEPT: ScheduleV1AbsenceDayOffRequestsIdAccept,
        PathValues.SCHEDULE_V1_ABSENCEDAYOFFREQUESTS_ID_REJECT: ScheduleV1AbsenceDayOffRequestsIdReject,
        PathValues.SCHEDULE_V1_ABSENCEDAYOFFREQUESTS_ID: ScheduleV1AbsenceDayOffRequestsId,
        PathValues.SCHEDULE_V1_HOLIDAYCALENDAR: ScheduleV1HolidayCalendar,
        PathValues.SCHEDULE_V1_HOLIDAYCALENDAR_HOLIDAY_CALENDAR_ID: ScheduleV1HolidayCalendarHolidayCalendarId,
        PathValues.SCHEDULE_V1_HOLIDAYS: ScheduleV1Holidays,
        PathValues.SCHEDULE_V1_HOLIDAYS_HOLIDAY_CALENDAR_ID_EMPLOYEES: ScheduleV1HolidaysHolidayCalendarIdEmployees,
        PathValues.SCHEDULE_V1_SCHEDULETEMPLATES: ScheduleV1ScheduleTemplates,
        PathValues.SCHEDULE_V1_EMPLOYEES_EMPLOYEE_ID_SCHEDULETEMPLATES: ScheduleV1EmployeesEmployeeIdScheduleTemplates,
        PathValues.SCHEDULE_V1_ENTITYSCHEDULETEMPLATES: ScheduleV1EntityScheduleTemplates,
        PathValues.SCHEDULE_V1_ENTITYSCHEDULETEMPLATES_ENTITY_SCHEDULE_TEMPLATE_ID: ScheduleV1EntityScheduleTemplatesEntityScheduleTemplateId,
        PathValues.SCHEDULE_V1_AGREEMENTS: ScheduleV1Agreements,
        PathValues.SCHEDULE_V1_AGREEMENTS_AGREEMENT_ID: ScheduleV1AgreementsAgreementId,
        PathValues.SCHEDULE_V1_AGREEMENTEMPLOYEES: ScheduleV1AgreementEmployees,
        PathValues.SCHEDULE_V1_AGREEMENTEMPLOYEES_AGREEMENT_EMPLOYEE_ID: ScheduleV1AgreementEmployeesAgreementEmployeeId,
        PathValues.CONTRACT_V1_CONTRACTS_EMPLOYEE_ID: ContractV1ContractsEmployeeId,
        PathValues.CONTRACT_V1_CONTRACTS: ContractV1Contracts,
        PathValues.CONTRACT_V1_CONTRACTS_CONTRACT_ID: ContractV1ContractsContractId,
        PathValues.CONTRACT_V1_CONTRACTS_EMPLOYEE_ID_CURRENTCONTRACT: ContractV1ContractsEmployeeIdCurrentContract,
        PathValues.CONTRACT_V1_CONTRIBUTIONGROUPS: ContractV1ContributionGroups,
        PathValues.CONTRACT_V1_SALARIES: ContractV1Salaries,
        PathValues.CONTRACT_V1_SALARIES_SALARY_ID: ContractV1SalariesSalaryId,
        PathValues.PROJECT_V1_TIMEENTRIES_START: ProjectV1TimeEntriesStart,
        PathValues.PROJECT_V1_TIMEENTRIES_STOP: ProjectV1TimeEntriesStop,
        PathValues.PROJECT_V1_TIMEENTRIES: ProjectV1TimeEntries,
        PathValues.PROJECT_V1_TIMEENTRIES_ID: ProjectV1TimeEntriesId,
        PathValues.PROJECT_V1_CUSTOMERS: ProjectV1Customers,
        PathValues.PROJECT_V1_CUSTOMERS_ID: ProjectV1CustomersId,
        PathValues.PROJECT_V1_PROJECTS: ProjectV1Projects,
        PathValues.PROJECT_V1_PROJECTS_ID: ProjectV1ProjectsId,
        PathValues.DOCUMENT_V1_DIRECTORIES: DocumentV1Directories,
        PathValues.DOCUMENT_V1_DIRECTORIES_DIRECTORY_ID_DOCUMENTS: DocumentV1DirectoriesDirectoryIdDocuments,
        PathValues.RECRUITMENT_V1_VACANCIES: RecruitmentV1Vacancies,
        PathValues.RECRUITMENT_V1_VACANCIES_ID: RecruitmentV1VacanciesId,
        PathValues.RECRUITMENT_V1_CANDIDATES: RecruitmentV1Candidates,
        PathValues.RECRUITMENT_V1_CANDIDATES_ID: RecruitmentV1CandidatesId,
        PathValues.RECRUITMENT_V1_CANDIDATESTATUS_VACANCY_ID: RecruitmentV1CandidateStatusVacancyId,
    }
)
