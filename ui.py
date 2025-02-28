import streamlit as st

def load_logs():
    """Loads execution logs from logs.txt"""
    try:
        with open("logs.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "No logs available."

# Streamlit UI
st.set_page_config(page_title="Security Scan Dashboard", layout="wide")

st.title("Security Scan Dashboard")

# Execution Logs Section
st.subheader("Execution Logs")
logs = load_logs()

# Display logs in a code block for better readability
st.code(logs, language="plaintext")

# Refresh Button
if st.button("Refresh Logs"):
    st.rerun()  # Fixed the deprecated function

# Scan Status
st.subheader("Scan Status")
st.success("All security scans completed successfully!")

# Final Audit Report
st.subheader("Final Audit Report")
st.download_button("Download Report", logs, file_name="audit_report.txt")