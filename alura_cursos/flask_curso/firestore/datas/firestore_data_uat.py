"""Data for firestore."""


def get_documents():
    """Return Documents to be inserted in firestore"""

    return [
        {
            "collection": "system_configuration",
            "id": None,
            "data": {
                "configuration_type": "financial_deadline",
                "year": 2020,
                "description": "Parameters for financial deadline in 2020",
                "parameters": {
                    "q1": {
                        "begin_of_warning": "2020-01-17T23:59:59-0800",
                        "seventy_percent_of_spend": "2020-01-31T23:59:59-0800",
                        "request_business_services": "2020-02-14T23:59:59-0800",
                        "po_deadline": "2020-02-28T23:59:59-0800"
                    },
                    "q2": {
                        "begin_of_warning": "2020-04-16T23:59:59-0800",
                        "seventy_percent_of_spend": "2020-04-30T23:59:59-0800",
                        "request_business_services": "2020-05-15T23:59:59-0800",
                        "po_deadline": "2020-05-29T23:59:59-0800"
                    },
                    "q3": {
                        "begin_of_warning": "2020-07-17T23:59:59-0800",
                        "seventy_percent_of_spend": "2020-07-31T23:59:59-0800",
                        "request_business_services": "2020-08-14T23:59:59-0800",
                        "po_deadline": "2020-08-28T23:59:59-0800"
                    },
                    "q4": {
                        "begin_of_warning": "2020-10-16T23:59:59-0800",
                        "seventy_percent_of_spend": "2020-10-30T23:59:59-0800",
                        "request_business_services": "2020-11-13T23:59:59-0800",
                        "po_deadline": "2020-11-30T23:59:59-0800"
                    }
                }
            },
        },
        {
            "collection": "system_configuration",
            "id": None,
            "data": {
                "configuration_type": "financial_deadline",
                "year": 2021,
                "description": "Parameters for financial deadline in 2021",
                "parameters": {
                    "q1": {
                        "begin_of_warning": "2021-01-15T23:59:59-0800",
                        "seventy_percent_of_spend": "2021-01-29T23:59:59-0800",
                        "request_business_services": "2021-02-12T23:59:59-0800",
                        "po_deadline": "2021-02-26T23:59:59-0800"
                    },
                    "q2": {
                        "begin_of_warning": "2021-04-16T23:59:59-0800",
                        "seventy_percent_of_spend": "2021-04-30T23:59:59-0800",
                        "request_business_services": "2021-05-14T23:59:59-0800",
                        "po_deadline": "2021-05-28T23:59:59-0800"
                    },
                    "q3": {
                        "begin_of_warning": "2021-07-17T23:59:59-0800",
                        "seventy_percent_of_spend": "2021-07-31T23:59:59-0800",
                        "request_business_services": "2021-08-13T23:59:59-0800",
                        "po_deadline": "2021-08-27T23:59:59-0800"
                    },
                    "q4": {
                        "begin_of_warning": "2021-10-16T23:59:59-0800",
                        "seventy_percent_of_spend": "2021-10-29T23:59:59-0800",
                        "request_business_services": "2021-11-12T23:59:59-0800",
                        "po_deadline": "2021-11-26T23:59:59-0800"
                    }
                }
            },
        },
        {
            "collection": "system_configuration",
            "id": None,
            "data": {
                "configuration_type": "woven_questions_mapping",
                "description": "Maps the question",
                "parameters": {
                    "program_instance": {
                        "program_id_question_id": 1011,
                        "program_identifier_question_id": 1012,
                        "sub_region_question_id": 1389,
                        "industry_question_id": 1018,
                        "cloud_solution_question_id": 1367,
                    }
                }
            },
        },
        {
            "collection": "dynamic_options",
            "id": None,
            "data": {
                "field": "non_program",
                "options": [
                    {
                        "id": "infrastructure",
                        "name": "Infrastructure"
                    },
                    {
                        "id": "readiness-enablement",
                        "name": "Readiness/Enablement"
                    },
                    {
                        "id": "tvc",
                        "name": "TVC"
                    }
                ]
            }
        },
    ]


def get_collections():
    """Return all collections from documents"""

    documents = get_documents()
    collections = set(map(lambda item: item["collection"], documents))

    return collections
