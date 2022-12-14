import os
import tempfile
from typing_extensions import assert_never

import pytest

from flaskr import flaskr


@pytest.fixture
def client():
    db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
    flaskr.app.config['TESTING'] = True

    with flaskr.app.test_client() as client:
        with flaskr.app.app_context():
            flaskr.init_db()
        yield client

    os.close(db_fd)
    os.unlink(flaskr.app.config['DATABASE'])

def setUp(self):
        self.app = create_app()
        self.appctx = self.app.app_context()
        self.appctx.push()

def tearDown(self):
        self.appctx.pop()
        self.app = None
        self.appctx = None

def test_app(self):
        assert self.app is not None
        assert current_app == self.app




