def test_valid_operation_insert_(mocker, db_load):
    # team_patcher = mocker.patch(
    #     "backend.adapters.gateway.cloudsql.repository.program_instance_repository.ProgramInstanceRepository"
    #     ".team_information_repo"
    # )
    # team_patcher.get_by_property.return_value = [
    #     TeamInformationEntity().load(
    #         {
    #             "id": 1,
    #             "description": "Description Test",
    #             "team_id": 1,
    #             "prefix": "TST",
    #             "instance_id_prefix": "PGI",
    #             "instance_id_counter": 1,
    #         }
    #     )
    # ]
    # team_id = 1
    # print(team_patcher.get_by_property.return_value)
    # db, fixtures_dirs = db_load
    # load_fixtures_from_file(db, "program_instance.json", fixtures_dirs)
    # pi_entity = ProgramInstanceRepository().get_by_id(1)
    result = ProgramInstanceRepository()._insert_or_update(operation="insert", entity=new_program_instance)