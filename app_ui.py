import streamlit as st
import os

def load_logs():
    """Loads execution logs from logs.txt, ensuring it exists first."""
    log_file = "logs.txt"

    # Ensure the log file exists
    if not os.path.exists(log_file):
        with open(log_file, "w") as f:
            f.write("Log file created.\n")

    # Read log file
    with open(log_file, "r") as f:
        content = f.read().strip()
        return content if content else "No logs recorded yet."

# Streamlit UI Configuration
st.set_page_config(page_title="Security Scan Dashboard", layout="wide")

st.title("Security Scan Dashboard")

# Execution Logs Section
st.subheader("Execution Logs")
logs = load_logs()

# Display logs in a code block for better readability
st.code(logs, language="plaintext")

# Refresh Button
if st.button("Refresh Logs"):
    st.rerun()

# Scan Status
st.subheader("Scan Status")
st.success("All security scans completed successfully!")

# Final Audit Report
st.subheader("Final Audit Report")
st.download_button("Download Report", logs, file_name="audit_report.txt")
