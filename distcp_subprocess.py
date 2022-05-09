import subprocess
from subprocess import check_call

def distcp(from_path: str, to_path: str) -> None:
    check_call(['hadoop', 'distcp', from_path, to_path], stderr=subprocess.STDOUT)
