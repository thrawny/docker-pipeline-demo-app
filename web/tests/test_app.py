from unittest import TestCase

from app import create_app


class TestApp(TestCase):
    def setUp(self):
        self.app = create_app('test')
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()

    def tearDown(self):
        self.ctx.pop()

    def test_200_ok(self):
        resp = self.client.get('/')
        assert resp.status_code == 200

    def test_response_content(self):
        resp = self.client.get('/')
        assert b'Hello World' in resp.data

    def test_404(self):
        resp = self.client.get('/does/not/exist')
        assert resp.status_code == 404
