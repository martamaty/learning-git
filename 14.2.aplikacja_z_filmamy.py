def test_get_poster_url_uses_default_size():
   # Przygotowanie danych
   poster_api_path = "some-poster-path"
   expected_default_size = 'w342'
   # Wywołanie kodu, który testujemy
   poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
   # Porównanie wyników
   assert expected_default_size in poster_url

def get_movies_list(list_type):
   endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
   headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(endpoint, headers=headers)
   response.raise_for_status()
   return response.json()

from unittest.mock import Mock

def test_mocking(monkeypatch):
   my_mock = Mock()
   my_mock.return_value = 2
   monkeypatch.setattr("tests.test_tmdb.some_function_to_mock", my_mock)
   result = some_function_to_mock()
   assert result == 2