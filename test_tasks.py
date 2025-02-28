import pytest
from scope_manager import ScopeManager
from task_manager import TaskManager
from executor import run_nmap

def test_scope_enforcement():
    scope = ScopeManager(["example.com"])
    assert scope.is_allowed("example.com") == True
    assert scope.is_allowed("hacker.com") == False

def test_task_execution():
    success = run_nmap("example.com")
    assert success is not None  # Nmap should return some output

if __name__ == "__main__":
    pytest.main()
