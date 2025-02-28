import subprocess
from logger import Logger

logger = Logger()

def run_nmap(target):
    """Runs an Nmap scan on the target."""
    logger.log(f"Running Nmap on {target}")
    try:
        result = subprocess.run(["nmap", "-sV", target], capture_output=True, text=True)
        logger.log(result.stdout)
        return result.stdout
    except Exception as e:
        logger.log(f"Nmap failed: {e}")
        return None

def run_gobuster(target):
    """Runs a Gobuster scan on the target."""
    logger.log(f"Running Gobuster on {target}")
    try:
        result = subprocess.run(["gobuster", "dns", "-d", target, "-w", "/usr/share/wordlists/dirb/common.txt"], capture_output=True, text=True)
        logger.log(result.stdout)
        return result.stdout
    except Exception as e:
        logger.log(f"Gobuster failed: {e}")
        return None

def run_ffuf(target):
    """Runs FFUF fuzzing on the target."""
    logger.log(f"Running FFUF on {target}")
    try:
        result = subprocess.run(["ffuf", "-u", f"http://{target}/FUZZ", "-w", "/usr/share/wordlists/dirb/common.txt"], capture_output=True, text=True)
        logger.log(result.stdout)
        return result.stdout
    except Exception as e:
        logger.log(f"FFUF failed: {e}")
        return None 
