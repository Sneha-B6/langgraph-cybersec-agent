from task_manager import TaskManager
from scope_manager import ScopeManager
from logger import generate_report
import streamlit as st
import sys

def main():
    # Define target scope
    allowed_scope = ["example.com"]  # Change as needed
    scope_manager = ScopeManager(allowed_scope)

    # Create Task Manager
    task_manager = TaskManager(scope_manager)

    # Define security task
    security_task = "Scan example.com for open ports and discover directories"

    # Start execution using LangGraph
    task_manager.run(security_task)

    # Generate final report
    print("\n===== Execution Report =====")
    print(generate_report())

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "ui":
        import ui
    else:
        main()