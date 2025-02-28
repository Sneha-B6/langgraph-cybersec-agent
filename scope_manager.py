from logger import Logger

class ScopeManager:
    def __init__(self, allowed_domains):
        self.allowed_domains = allowed_domains
        self.logger = Logger()

    def is_allowed(self, target):
        """Check if the target is within the allowed scope."""
        for domain in self.allowed_domains:
            if target.endswith(domain):
                return True
        self.logger.log(f"Target {target} is out of scope!")
        return False