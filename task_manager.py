from executor import run_nmap, run_gobuster, run_ffuf
from logger import Logger
from scope_manager import ScopeManager
from langgraph.graph import StateGraph

class TaskManager:
    def __init__(self, scope_manager):
        self.scope_manager = scope_manager
        self.logger = Logger()
        self.graph = StateGraph(self.initial_state())

    def initial_state(self):
        """Initial state setup for LangGraph"""
        return {"nmap_results": None, "gobuster_results": None, "ffuf_results": None}

    def run(self, instruction):
        self.logger.log(f"Received instruction: {instruction}")

        # Build graph with nodes and edges
        self.graph.add_node("nmap_scan", self.run_nmap)
        self.graph.add_node("gobuster_scan", self.run_gobuster)
        self.graph.add_node("ffuf_fuzz", self.run_ffuf)

        # Define dynamic execution flow
        self.graph.add_edge("nmap_scan", "gobuster_scan", condition=self.should_run_gobuster)
        self.graph.add_edge("gobuster_scan", "ffuf_fuzz", condition=self.should_run_ffuf)

        # Start execution from first node
        self.graph.set_entry_point("nmap_scan")
        self.graph.compile()

        self.logger.log("Executing security scans using LangGraph...")
        result = self.graph.invoke(self.initial_state())

        self.logger.log("All tasks completed.")
        return result

    def run_nmap(self, state):
        """Runs Nmap scan and updates state"""
        if self.scope_manager.is_allowed("example.com"):
            result = run_nmap("example.com")
            state["nmap_results"] = result
        return state

    def run_gobuster(self, state):
        """Runs Gobuster scan based on Nmap results"""
        if state["nmap_results"] and self.scope_manager.is_allowed("example.com"):
            result = run_gobuster("example.com")
            state["gobuster_results"] = result
        return state

    def run_ffuf(self, state):
        """Runs FFUF fuzzing based on Gobuster results"""
        if state["gobuster_results"] and self.scope_manager.is_allowed("example.com"):
            result = run_ffuf("example.com")
            state["ffuf_results"] = result
        return state

    def should_run_gobuster(self, state):
        """Check if Gobuster should run based on Nmap results"""
        return state["nmap_results"] is not None

    def should_run_ffuf(self, state):
        """Check if FFUF should run based on Gobuster results"""
        return state["gobuster_results"] is not None
