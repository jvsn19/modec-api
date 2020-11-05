def test_create_new_vessel(app_helper, db):
    db.reset_db()
    response = app_helper.create_vessel('test')
    assert response.status_code == 201

def test_repeated_vessel_error(app_helper):
    response = app_helper.create_vessel('test')
    assert response.status_code == 409