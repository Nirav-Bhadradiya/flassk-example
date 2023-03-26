import unittest
from unittest.mock import Mock, patch
from app import app

class FlaskTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('app.jsonify')
    def test_hello(self, mock_jsonify):
        mock_jsonify.return_value = {'message': 'Hello, World!'}
        response = self.app.get('/hello')
        mock_jsonify.assert_called_once_with({'message': 'Hello, World!'})
        self.assertEqual(response.status_code, 200)

    @patch('app.request')
    @patch('app.jsonify')
    def test_add(self, mock_jsonify, mock_request):
        mock_request.args.get.side_effect = lambda key, default: {
            'a': 2,
            'b': 3
        }.get(key, default)
        mock_jsonify.return_value = {'result': 5}
        response = self.app.get('/add')
        mock_request.args.get.assert_any_call('a', type=int)
        mock_request.args.get.assert_any_call('b', type=int)
        mock_jsonify.assert_called_once_with({'result': 5})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
