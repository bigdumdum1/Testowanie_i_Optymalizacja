import unittest
from unittest.mock import MagicMock
from app import get_comments, create_html_table


class TestApp(unittest.TestCase):

    def test_get_comments_success(self):
        # Symulacja udanej odpowiedzi
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{'name': 'user1', 'email': 'user1@example.com', 'body': 'comment1'}]
        with unittest.mock.patch('app.request.get', return_value=mock_response):
            comments = get_comments()
            self.assertEqual(len(comments), 1)
            self.assertEqual(comments[0]['name'], 'user1')
            self.assertEqual(comments[0]['email'], 'user1@example.com')
            self.assertEqual(comments[0]['body'], 'comment1')

    def test_get_comments_failure(self):
        # Symulacja nieudanej odpowiedzi
        mock_response = MagicMock()
        mock_response.status_code = 404
        with unittest.mock.patch('app.request.get', return_value=mock_response):
            comments = get_comments()
            self.assertEqual(len(comments), 0)

    def test_create_html_table(self):
        comments = [{'name': 'user1', 'email': 'user1@example.com', 'body': 'comment1'}]
        html_table = create_html_table(comments)
        expected_table = """
        <table>
        <thead>
            <tr>
                <th>Nazwa użytkownika</th>
                <th>Email</th>
                <th>Treść</th>
            </tr>
        </thead>
        <tbody id="comments-table-body">
        </tbody>
    </table>
        """
        self.assertEqual(html_table.strip(), expected_table.strip())


if __name__ == '__main__':
    unittest.main()