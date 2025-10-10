from datetime import datetime
import pytest
from util import logs_util

@pytest.mark.usefixtures("setup_teardown")
class BaseTest:
    logger = logs_util.generate_logs()
    def generate_email_with_timestamp(self):
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "myname"+timestamp+"@gmail.com"

