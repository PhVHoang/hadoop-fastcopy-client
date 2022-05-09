import subprocess
from subprocess import check_call

from typing import Optional

def distcp(from_path: str, to_path: str, log_path: Optional[str] = None) -> None:
    """
    Run hadoop distcp by using python subprocess.
    """
    if not log_path:
        log_path = "/user/namespace1/distcp_log_test"

    check_call(['hadoop', 'distcp', '-log', log_path, '-skipcrccheck', from_path, to_path], stderr=subprocess.STDOUT)
