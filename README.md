# langgraph-cybersec-agent

## Overview
This project implements a **LangGraph-based security pipeline** that:
- Dynamically executes **nmap, gobuster, and ffuf** for penetration testing.
- Enforces **scope restrictions** to prevent unauthorized scans.
- Handles **failures & retries** automatically.
- Logs execution steps and generates **audit reports**.
- Provides a **Streamlit UI** for monitoring execution.

## System Architecture
The system consists of **modular components** for structured execution:

- `main.py` → **Entry point** that initializes the workflow.
- `task_manager.py` → **Breaks down security tasks** and dynamically adjusts execution.
- `executor.py` → **Runs security tools** (`nmap`, `gobuster`, `ffuf`).
- `scope_manager.py` → **Restricts scans** to allowed targets.
- `logger.py` → **Logs execution, handles failures, and generates reports**.
- `ui.py` → **Streamlit-based dashboard** for monitoring execution.

---

## Agent Roles & Responsibilities
### **Task Manager (task_manager.py)**
- Accepts a security instruction (e.g., "Scan for open ports").
- Uses **LangGraph** to break it into steps:
  - **Step 1:** Run `nmap`.
  - **Step 2:** Analyze results → If subdomains are found, run `gobuster`.
  - **Step 3:** Use `ffuf` for fuzzing if needed.
- Handles **failure detection & retries**.

### **Execution Agent (executor.py)**
- Directly runs **security tools** (`nmap`, `gobuster`, `ffuf`).
- Captures real-time **output logs**.
- Implements **error handling** (e.g., retries on failure).

### **Scope Manager (scope_manager.py)**
- **Prevents out-of-scope scans** by enforcing domain/IP restrictions.
- Logs unauthorized scan attempts.

---

## Scope Enforcement Strategy
1. **Predefined Allowed Domains/IPs**  
   - Defined in `.env` (Example: `TARGET_SCOPE=example.com`).
   - Any scan **outside this scope is blocked**.

2. **Dynamic Scope Validation**  
   - Before running any scan, `scope_manager.py` checks:
     ```python
     if target.endswith(allowed_domain):
         return True
     ```
   - If out of scope, it logs:
     ```
     [ERROR] Target xyz.com is out of scope!
     ```

---

##Installation

### **Prerequisites**
Ensure you have the following installed:
- **Python 3.11** (Check version: `python --version`)
- **System tools** (Run this in the terminal):
  ```sh
  brew install nmap gobuster ffuf
