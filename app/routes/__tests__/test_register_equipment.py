def test_register_new_equipment(app_helper, db):
    db.reset_db()
    db.create_vessel('test')
    response = app_helper.create_equipment(
        'test',
        'test-equip',
        'my brand new equip',
        'brazil'
    )

    assert response.status_code == 201

def test_register_repeated_equipment(app_helper):
    response = app_helper.create_equipment(
        'test',
        'test-equip',
        'my brand new equip',
        'brazil'
    )

    assert response.status_code == 409

def test_register_equipment_invalid_vessel(app_helper, db):
    db.reset_db()

    response = app_helper.create_equipment(
        'test',
        'test-equip',
        'my brand new equip',
        'brazil'
    )

    assert response.status_code == 404