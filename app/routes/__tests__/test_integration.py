def test_integration(app_helper):
    # Create Vessel
    response_create_vessel = app_helper.create_vessel('my-vessel')
    
    assert response_create_vessel.status_code == 201

    response_create_equip = app_helper.create_equipment(
        'my-vessel',
        'test-equip',
        'my brand new equip',
        'brazil'
    )

    assert response_create_equip.status_code == 201

    response_update_equip = app_helper.update_equipment('test-equip', 1)

    assert response_update_equip.status_code == 200

    response_get_equips = app_helper.get_equipments('my-vessel')

    assert response_get_equips.status_code == 200
    equip = response_get_equips.get_json()['test-equip']
    assert equip['status'] == '1'

