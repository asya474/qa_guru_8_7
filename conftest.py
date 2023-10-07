import os
import shutil
import pytest
from utils import TMP_PATH


@pytest.fixture
def tmp_directory(scope="function"):
    if not os.path.exists(TMP_PATH):
        os.mkdir('tmp')

    yield

    shutil.rmtree(TMP_PATH)
