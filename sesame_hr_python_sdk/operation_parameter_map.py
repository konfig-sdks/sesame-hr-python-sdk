operation_parameter_map = {
    '/schedule/v1/absence-calendars-POST': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'absenceTypeId'
            },
            {
                'name': 'year'
            },
            {
                'name': 'daysOff'
            },
        ]
    },
    '/schedule/v1/absence-calendars-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'year[in]'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/schedule/v1/absence-calendars/{id}-PUT': {
        'parameters': [
            {
                'name': 'daysOff'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/schedule/v1/absence-day-off-GET': {
        'parameters': [
            {
                'name': 'employeeIds'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
            {
                'name': 'orderBy'
            },
        ]
    },
    '/schedule/v1/absence-day-off-requests/{id}/accept-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'managerId'
            },
            {
                'name': 'resolutionComment'
            },
        ]
    },
    '/schedule/v1/absence-day-off-requests-POST': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'daysOff'
            },
            {
                'name': 'absenceTypeId'
            },
            {
                'name': 'comment'
            },
        ]
    },
    '/schedule/v1/absence-day-off-requests/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/schedule/v1/absence-day-off-requests-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'absencesValidator'
            },
            {
                'name': 'fromDayOff'
            },
            {
                'name': 'toDayOff'
            },
            {
                'name': 'status'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
            {
                'name': 'orderBy'
            },
        ]
    },
    '/schedule/v1/absence-day-off-requests/{id}/reject-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'resolutionComment'
            },
            {
                'name': 'managerId'
            },
        ]
    },
    '/schedule/v1/absence-types-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/schedule/v1/agreements-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'code'
            },
            {
                'name': 'color'
            },
            {
                'name': 'annualHours'
            },
        ]
    },
    '/schedule/v1/agreements/{agreementId}-DELETE': {
        'parameters': [
            {
                'name': 'agreementId'
            },
        ]
    },
    '/schedule/v1/agreements/{agreementId}-GET': {
        'parameters': [
            {
                'name': 'agreementId'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/schedule/v1/agreements-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/schedule/v1/agreements/{agreementId}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'code'
            },
            {
                'name': 'color'
            },
            {
                'name': 'annualHours'
            },
            {
                'name': 'agreementId'
            },
        ]
    },
    '/schedule/v1/check-types-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/schedule/v1/check-validation-GET': {
        'parameters': [
            {
                'name': 'employeeIds[in]'
            },
            {
                'name': 'status'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/core/v3/companies/{id}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'notificationEmail'
            },
            {
                'name': 'language'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/contract/v1/contracts-POST': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'code'
            },
            {
                'name': 'endAt'
            },
            {
                'name': 'comment'
            },
        ]
    },
    '/contract/v1/contracts/{contractId}-DELETE': {
        'parameters': [
            {
                'name': 'contractId'
            },
        ]
    },
    '/contract/v1/contracts/{employeeId}-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/contract/v1/contracts/{employeeId}/current-contract-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
        ]
    },
    '/contract/v1/contracts/{contractId}-PUT': {
        'parameters': [
            {
                'name': 'startAt'
            },
            {
                'name': 'code'
            },
            {
                'name': 'contractId'
            },
            {
                'name': 'endAt'
            },
            {
                'name': 'comment'
            },
        ]
    },
    '/core/v3/custom-fields-POST': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'type'
            },
            {
                'name': 'slug'
            },
        ]
    },
    '/core/v3/custom-fields/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/core/v3/custom-fields-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
            {
                'name': 'orderBy'
            },
        ]
    },
    '/core/v3/custom-fields/{id}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'id'
            },
            {
                'name': 'slug'
            },
        ]
    },
    '/project/v1/customers-POST': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'customerName'
            },
            {
                'name': 'description'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'email'
            },
            {
                'name': 'phone'
            },
        ]
    },
    '/project/v1/customers-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
            {
                'name': 'orderBy'
            },
        ]
    },
    '/project/v1/customers/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/project/v1/customers/{id}-PUT': {
        'parameters': [
            {
                'name': 'customerName'
            },
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'email'
            },
            {
                'name': 'phone'
            },
        ]
    },
    '/core/v3/departments-POST': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/core/v3/departments-GET': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
            {
                'name': 'orderBy'
            },
        ]
    },
    '/core/v3/departments/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/core/v3/departments/{id}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/document/v1/directories-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'parentDirectoryType'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/document/v1/directories/{directoryId}/documents-POST': {
        'parameters': [
            {
                'name': 'directoryId'
            },
            {
                'name': 'document'
            },
            {
                'name': 'originalDate'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/schedule/v1/agreement-employees-POST': {
        'parameters': [
            {
                'name': 'agreementId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'startDate'
            },
        ]
    },
    '/schedule/v1/agreement-employees/{agreementEmployeeId}-DELETE': {
        'parameters': [
            {
                'name': 'agreementEmployeeId'
            },
        ]
    },
    '/core/v3/roles/assignation-POST': {
        'parameters': [
            {
                'name': 'roleId'
            },
            {
                'name': 'employeeId'
            },
            {
                'name': 'entityAffectedId'
            },
        ]
    },
    '/core/v3/roles/assignation/{employeeId}-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/core/v3/roles/assignation-DELETE': {
        'parameters': [
            {
                'name': 'assignationId'
            },
        ]
    },
    '/core/v3/employee-department-assignations-POST': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'departmentId'
            },
        ]
    },
    '/core/v3/employee-department-assignations-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'departmentId'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/core/v3/employee-department-assignations-DELETE': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'departmentId'
            },
        ]
    },
    '/core/v3/employee-managers-POST': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'managerId'
            },
            {
                'name': 'permission'
            },
            {
                'name': 'order'
            },
        ]
    },
    '/core/v3/employee-managers-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'managerId'
            },
            {
                'name': 'permission'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/core/v3/employee-managers/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/core/v3/employee-office-assignations-POST': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'officeId'
            },
        ]
    },
    '/core/v3/employee-office-assignations-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'officeId'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/core/v3/employee-office-assignations-DELETE': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'officeId'
            },
        ]
    },
    '/schedule/v1/entity-schedule-templates-POST': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'scheduleTemplateId'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
        ]
    },
    '/schedule/v1/employees/{employeeId}/schedule-templates-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/schedule/v1/entity-schedule-templates/{entityScheduleTemplateId}-DELETE': {
        'parameters': [
            {
                'name': 'entityScheduleTemplateId'
            },
        ]
    },
    '/core/v3/employees-POST': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'invitation'
            },
            {
                'name': 'status'
            },
            {
                'name': 'description'
            },
            {
                'name': 'gender'
            },
            {
                'name': 'email'
            },
            {
                'name': 'contractId'
            },
            {
                'name': 'code'
            },
            {
                'name': 'pin'
            },
            {
                'name': 'nid'
            },
            {
                'name': 'identityNumberType'
            },
            {
                'name': 'ssn'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'dateOfBirth'
            },
            {
                'name': 'customFields'
            },
            {
                'name': 'nationality'
            },
            {
                'name': 'maritalStatus'
            },
            {
                'name': 'address'
            },
            {
                'name': 'postalCode'
            },
            {
                'name': 'emergencyPhone'
            },
            {
                'name': 'childrenCount'
            },
            {
                'name': 'disability'
            },
            {
                'name': 'personalEmail'
            },
            {
                'name': 'city'
            },
            {
                'name': 'province'
            },
            {
                'name': 'country'
            },
            {
                'name': 'salaryRange'
            },
            {
                'name': 'studyLevel'
            },
            {
                'name': 'professionalCategoryCode'
            },
            {
                'name': 'professionalCategoryDescription'
            },
            {
                'name': 'bic'
            },
        ]
    },
    '/core/v3/employees/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/core/v3/employees-GET': {
        'parameters': [
            {
                'name': 'code'
            },
            {
                'name': 'dni'
            },
            {
                'name': 'email'
            },
            {
                'name': 'departmentIds'
            },
            {
                'name': 'officeIds'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
            {
                'name': 'orderBy'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/core/v3/employees/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/core/v3/employees/{id}-PUT': {
        'parameters': [
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'status'
            },
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'gender'
            },
            {
                'name': 'email'
            },
            {
                'name': 'contractId'
            },
            {
                'name': 'code'
            },
            {
                'name': 'pin'
            },
            {
                'name': 'nid'
            },
            {
                'name': 'identityNumberType'
            },
            {
                'name': 'ssn'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'dateOfBirth'
            },
            {
                'name': 'customFields'
            },
            {
                'name': 'nationality'
            },
            {
                'name': 'maritalStatus'
            },
            {
                'name': 'address'
            },
            {
                'name': 'postalCode'
            },
            {
                'name': 'emergencyPhone'
            },
            {
                'name': 'childrenCount'
            },
            {
                'name': 'disability'
            },
            {
                'name': 'personalEmail'
            },
            {
                'name': 'city'
            },
            {
                'name': 'province'
            },
            {
                'name': 'country'
            },
            {
                'name': 'salaryRange'
            },
            {
                'name': 'studyLevel'
            },
            {
                'name': 'professionalCategoryCode'
            },
            {
                'name': 'professionalCategoryDescription'
            },
            {
                'name': 'bic'
            },
            {
                'name': 'accountNumber'
            },
        ]
    },
    '/schedule/v1/holiday-calendar-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'daysOff'
            },
        ]
    },
    '/schedule/v1/holiday-calendar/{holidayCalendarId}-GET': {
        'parameters': [
            {
                'name': 'holidayCalendarId'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/schedule/v1/holiday-calendar-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
            {
                'name': 'name[contains]'
            },
        ]
    },
    '/schedule/v1/holiday-calendar/{holidayCalendarId}-DELETE': {
        'parameters': [
            {
                'name': 'holidayCalendarId'
            },
        ]
    },
    '/schedule/v1/holiday-calendar/{holidayCalendarId}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'daysOff'
            },
            {
                'name': 'holidayCalendarId'
            },
        ]
    },
    '/schedule/v1/holidays/{holidayCalendarId}/employees-POST': {
        'parameters': [
            {
                'name': 'holidayCalendarId'
            },
            {
                'name': 'employees'
            },
            {
                'name': 'startDate'
            },
        ]
    },
    '/schedule/v1/holidays/{holidayCalendarId}/employees-GET': {
        'parameters': [
            {
                'name': 'holidayCalendarId'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/schedule/v1/holidays-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'year'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/schedule/v1/holidays/{holidayCalendarId}/employees-DELETE': {
        'parameters': [
            {
                'name': 'holidayCalendarId'
            },
            {
                'name': 'employees'
            },
        ]
    },
    '/core/v3/offices-POST': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'description'
            },
            {
                'name': 'address'
            },
            {
                'name': 'coordinates'
            },
            {
                'name': 'radio'
            },
        ]
    },
    '/core/v3/offices-GET': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
            {
                'name': 'orderBy'
            },
        ]
    },
    '/core/v3/offices/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/core/v3/offices/{id}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'address'
            },
            {
                'name': 'coordinates'
            },
            {
                'name': 'radio'
            },
        ]
    },
    '/project/v1/projects-POST': {
        'parameters': [
            {
                'name': 'companyId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'description'
            },
            {
                'name': 'parentProjectId'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'price'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'managerId'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/project/v1/projects-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'orderBy'
            },
        ]
    },
    '/project/v1/projects/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/project/v1/projects/{id}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'parentProjectId'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'price'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'managerId'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/recruitment/v1/candidates-POST': {
        'parameters': [
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'email'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'vacancyId'
            },
            {
                'name': 'linkedinURL'
            },
            {
                'name': 'desiredSalary'
            },
            {
                'name': 'startWorkDate'
            },
            {
                'name': 'web'
            },
            {
                'name': 'location'
            },
            {
                'name': 'statusId'
            },
        ]
    },
    '/recruitment/v1/candidates/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/recruitment/v1/candidate-status/{vacancyId}-GET': {
        'parameters': [
            {
                'name': 'vacancyId'
            },
        ]
    },
    '/recruitment/v1/vacancies/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/recruitment/v1/vacancies-GET': {
        'parameters': [
        ]
    },
    '/recruitment/v1/candidates/{id}-PUT': {
        'parameters': [
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'email'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'vacancyId'
            },
            {
                'name': 'id'
            },
            {
                'name': 'linkedinURL'
            },
            {
                'name': 'desiredSalary'
            },
            {
                'name': 'startWorkDate'
            },
            {
                'name': 'web'
            },
            {
                'name': 'location'
            },
            {
                'name': 'statusId'
            },
        ]
    },
    '/recruitment/v1/candidates/{id}-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'document'
            },
        ]
    },
    '/core/v3/roles-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/contract/v1/salaries-POST': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'payPeriod'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'grossSalary'
            },
            {
                'name': 'payments'
            },
            {
                'name': 'contributionGroupId'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'comments'
            },
        ]
    },
    '/contract/v1/salaries/{salaryId}-DELETE': {
        'parameters': [
            {
                'name': 'salaryId'
            },
        ]
    },
    '/contract/v1/salaries-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'salaryId'
            },
            {
                'name': 'payPeriod'
            },
            {
                'name': 'grossSalary'
            },
            {
                'name': 'payments'
            },
            {
                'name': 'contributionGroup'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/contract/v1/contribution-groups-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/contract/v1/salaries/{salaryId}-PUT': {
        'parameters': [
            {
                'name': 'salaryId'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'comments'
            },
        ]
    },
    '/schedule/v1/schedule-templates-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/core/v3/info-GET': {
        'parameters': [
        ]
    },
    '/schedule/v1/reports/worked-absence-days-GET': {
        'parameters': [
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'employeeIds[in]'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/schedule/v1/reports/worked-hours-GET': {
        'parameters': [
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'employeeIds[in]'
            },
            {
                'name': 'withChecks'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/schedule/v1/reports/worked-hours-by-week-day-GET': {
        'parameters': [
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'employeeIds[in]'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/schedule/v1/reports/worked-night-hours-GET': {
        'parameters': [
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'employeeIds[in]'
            },
            {
                'name': 'withChecks'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/project/v1/time-entries-POST': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'timeEntryIn'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'tagIds'
            },
            {
                'name': 'comment'
            },
            {
                'name': 'timeEntryOut'
            },
        ]
    },
    '/project/v1/time-entries/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/project/v1/time-entries-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'employeeStatus'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/project/v1/time-entries/start-POST': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'tagIds'
            },
            {
                'name': 'comment'
            },
            {
                'name': 'coordinates'
            },
        ]
    },
    '/project/v1/time-entries/stop-POST': {
        'parameters': [
            {
                'name': 'coordinates'
            },
        ]
    },
    '/project/v1/time-entries/{id}-PUT': {
        'parameters': [
            {
                'name': 'timeEntryIn'
            },
            {
                'name': 'id'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'tagIds'
            },
            {
                'name': 'comment'
            },
            {
                'name': 'timeEntryOut'
            },
        ]
    },
    '/schedule/v1/vacation-calendars-POST': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'vacationConfigurationId'
            },
            {
                'name': 'year'
            },
            {
                'name': 'daysOff'
            },
        ]
    },
    '/schedule/v1/vacation-calendars-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'year[in]'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/schedule/v1/vacation-calendars/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'daysOff'
            },
            {
                'name': 'maxDaysOff'
            },
        ]
    },
    '/schedule/v1/vacation-configurations-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/schedule/v1/vacation-day-off-GET': {
        'parameters': [
            {
                'name': 'employeeIds'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'page'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'orderBy'
            },
        ]
    },
    '/schedule/v1/vacation-day-off-requests/{id}/accept-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'managerId'
            },
        ]
    },
    '/schedule/v1/vacation-day-off-requests-POST': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'calendarId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'daysOff'
            },
            {
                'name': 'comment'
            },
        ]
    },
    '/schedule/v1/vacation-day-off-requests/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/schedule/v1/vacation-day-off-requests-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'absencesValidator'
            },
            {
                'name': 'fromDayOff'
            },
            {
                'name': 'toDayOff'
            },
            {
                'name': 'status'
            },
            {
                'name': 'page'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'orderBy'
            },
        ]
    },
    '/schedule/v1/vacation-day-off-requests/{id}/reject-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'resolutionComment'
            },
            {
                'name': 'managerId'
            },
        ]
    },
    '/schedule/v1/work-breaks-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/schedule/v1/work-entries-POST': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'workEntryType'
            },
            {
                'name': 'workEntryIn'
            },
            {
                'name': 'workBreakId'
            },
            {
                'name': 'workCheckTypeId'
            },
            {
                'name': 'workEntryOut'
            },
        ]
    },
    '/schedule/v1/work-entries/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/schedule/v1/work-entries/clock-out-POST': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'workEntryOut'
            },
        ]
    },
    '/schedule/v1/work-entries-GET': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'updatedAt[gte]'
            },
            {
                'name': 'updatedAt[lte]'
            },
            {
                'name': 'onlyReturn'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
            {
                'name': 'orderBy'
            },
        ]
    },
    '/schedule/v1/work-entries/clock-in-POST': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'workEntryIn'
            },
            {
                'name': 'workCheckTypeId'
            },
            {
                'name': 'workBreakId'
            },
        ]
    },
    '/schedule/v1/work-entries/{id}-PUT': {
        'parameters': [
            {
                'name': 'workEntryType'
            },
            {
                'name': 'workEntryIn'
            },
            {
                'name': 'id'
            },
            {
                'name': 'workEntryOut'
            },
        ]
    },
};