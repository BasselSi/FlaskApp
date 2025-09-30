import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import app as flask_app_module

@pytest.fixture
def client():
	flask_app_module.app.config['TESTING'] = True
	with flask_app_module.app.test_client() as client:
		yield client

def test_sum_page(client):
	# Send dummy inputs
	response = client.post('/', data={'x': '2', 'y': '3'})
	assert response.status_code == 200
	# Check that the result is shown on the page
	assert b'Result: 5' in response.data
