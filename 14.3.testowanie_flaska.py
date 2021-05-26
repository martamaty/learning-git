import pytest

@pytest.mark.parametrize('n, result', (
   (0, 0),
   (1, 1),
   (2, 1),
   (3, 2),
   (10, 55),
   (15, 610)
))
def test_fibonacci(n, result):
   assert get_fibonacci_number(n) == result

@pytest.mark.parametrize('nazwa_parametru1, nazwa_parametru2, ...', (
  ('wartosc1', 'wartosc2'),
  ('inna wartosc', 'jeszcze inna wartość')
))
def test_something(nazwa_parametru1, nazwa_parametru2):

from main import app
from unittest.mock import Mock

def test_homepage(monkeypatch):
   api_mock = Mock(return_value={'results': []})
   monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

   with app.test_client() as client:
       response = client.get('/')
       assert response.status_code == 200
       api_mock.assert_called_once_with('movie/popular')