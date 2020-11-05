def test_get_equipments(app_helper, db):
    db.reset_db()
    db.create_vessel('test-vessel')
    db.create_equipment('test-vessel', 'equip-a', 'my equip a', 'usa')
    db.create_equipment('test-vessel', 'equip-b', 'my equip b', 'brazil')
    db.create_equipment('test-vessel', 'equip-c', 'my equip c', 'japan')
    response = app_helper.get_equipments('test-vessel')
    
    to_compare = {
        'equip-a': {
            'name': 'my equip a',
            'location': 'usa',
            'code': 'equip-a',
            'status': '0'
        },
        'equip-b': {
            'name': 'my equip b',
            'location': 'brazil',
            'code': 'equip-b',
            'status': '0'
        },
        'equip-c': {
            'name': 'my equip c',
            'location': 'japan',
            'code': 'equip-c',
            'status': '0'
        },
    }

    assert response.status_code == 200
    assert response.get_json() == to_compare

def test_get_equipments_nonexisting_vessel(app_helper):
    response = app_helper.get_equipments('test-vessel-invalid')
    
    assert response.status_code == 404