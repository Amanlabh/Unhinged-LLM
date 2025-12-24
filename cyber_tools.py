"""Cybersecurity tools and utilities"""
from rich.console import Console
from rich.table import Table
from cyber_knowledge import CYBER_TOOLS, ATTACK_TECHNIQUES

class CyberTools:
    """Helper class for cybersecurity tools"""
    
    def __init__(self):
        self.console = Console()
    
    def list_tools(self):
        """Display available cybersecurity tools"""
        table = Table(title="Cybersecurity Tools", show_header=True, header_style="bold magenta")
        table.add_column("Category", style="cyan", no_wrap=True)
        table.add_column("Tools", style="green")
        
        for category, tools in CYBER_TOOLS.items():
            category_name = category.replace("_", " ").title()
            tools_list = ", ".join(tools)
            table.add_row(category_name, tools_list)
        
        self.console.print(table)
    
    def get_tool_info(self, tool_name: str) -> dict:
        """Get information about a specific tool"""
        tool_name_lower = tool_name.lower()
        
        for category, tools in CYBER_TOOLS.items():
            for tool in tools:
                if tool.lower() == tool_name_lower:
                    return {
                        "name": tool,
                        "category": category.replace("_", " ").title(),
                        "description": self._get_tool_description(tool)
                    }
        
        return None
    
    def _get_tool_description(self, tool: str) -> str:
        """Get description for common tools"""
        descriptions = {
            "Wireshark": "Network protocol analyzer for deep packet inspection",
            "Nmap": "Network mapper and port scanner",
            "Metasploit": "Penetration testing framework",
            "Burp Suite": "Web application security testing platform",
            "OWASP ZAP": "Open source web application security scanner",
            "Volatility": "Memory forensics framework",
            "Splunk": "SIEM and log analysis platform",
            "Nessus": "Vulnerability scanner",
            "sqlmap": "Automated SQL injection tool",
            "John the Ripper": "Password cracking tool",
            "Hashcat": "Advanced password recovery tool",
            "IDA Pro": "Interactive disassembler for reverse engineering",
            "Ghidra": "NSA's reverse engineering framework",
            "YARA": "Pattern matching tool for malware identification"
        }
        return descriptions.get(tool, "Cybersecurity tool")
    
    def recommend_tools(self, use_case: str) -> list:
        """Recommend tools based on use case"""
        use_case_lower = use_case.lower()
        recommendations = []
        
        if "network" in use_case_lower or "packet" in use_case_lower:
            recommendations.extend(["Wireshark", "tcpdump", "nmap"])
        
        if "web" in use_case_lower or "application" in use_case_lower:
            recommendations.extend(["Burp Suite", "OWASP ZAP", "Nikto"])
        
        if "vulnerability" in use_case_lower or "scan" in use_case_lower:
            recommendations.extend(["Nessus", "OpenVAS", "Nmap"])
        
        if "forensics" in use_case_lower or "incident" in use_case_lower:
            recommendations.extend(["Volatility", "Autopsy", "Wireshark"])
        
        if "malware" in use_case_lower:
            recommendations.extend(["YARA", "Cuckoo Sandbox", "IDA Pro", "Ghidra"])
        
        if "password" in use_case_lower or "crack" in use_case_lower:
            recommendations.extend(["John the Ripper", "Hashcat"])
        
        return list(set(recommendations))  # Remove duplicates

