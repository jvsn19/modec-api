def test_update_existing_equipment(db, app_helper):
    db.reset_db()
    db.create_vessel('test')
    db.create_equipment('test', 'equip-test', 'my equip', 'brazil')
    response = app_helper.update_equipment('equip-test', 1)

    assert response.status_code == 200

def test_update_nonexisting_equipment(app_helper):
    response = app_helper.update_equipment('equip-test-invalid', 1)

    assert response.status_code == 404

def test_update_invalid_status(app_helper):
    response = app_helper.update_equipment('equip-test', 3)

    assert response.status_code == 406