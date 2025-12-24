"""Main Cyber Fellow assistant"""
import sys
from typing import Optional
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import Prompt
from prompt_toolkit import prompt as pt_prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter
from ollama_client import OllamaClient
from cyber_tools import CyberTools

class CyberFellow:
    """Main assistant class"""
    
    def __init__(self):
        self.console = Console()
        self.client = OllamaClient()
        self.tools = CyberTools()
        self.history_path = ".cyber_fellow_history"
        
        # Command completions
        self.commands = [
            "help", "exit", "quit", "clear", "model", "models", "tools",
            "scan", "analyze", "check", "explain", "recommend"
        ]
        self.completer = WordCompleter(self.commands, ignore_case=True)
    
    def print_banner(self):
        """Print welcome banner"""
        banner = """
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║              🛡️  CYBER FELLOW 🛡️                          ║
║                                                           ║
║     Your Personal Cybersecurity AI Assistant              ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
"""
        self.console.print(banner, style="bold cyan")
    
    def print_help(self):
        """Print help information"""
        help_text = """
**Available Commands:**
- `help` - Show this help message
- `exit` or `quit` - Exit the assistant
- `clear` - Clear the screen
- `model` - Show current model
- `models` - List available Ollama models
- `tools` - Show available cybersecurity tools
- `scan <target>` - Perform a security scan (example usage)
- `analyze <item>` - Analyze a security item
- `check <item>` - Check security status
- `explain <concept>` - Explain a cybersecurity concept
- `recommend <scenario>` - Get security recommendations

**Usage:**
Just type your question or use commands. The assistant understands:
- Vulnerability assessments
- Security tool recommendations
- Incident response guidance
- Threat analysis
- Compliance questions
- And much more!

**Examples:**
- "How do I secure my API endpoints?"
- "What tools should I use for network forensics?"
- "Explain SQL injection attacks"
- "Help me with incident response procedures"
"""
        self.console.print(Panel(Markdown(help_text), title="Help", border_style="blue"))
    
    def handle_command(self, user_input: str) -> bool:
        """Handle special commands. Returns True if command was handled."""
        parts = user_input.strip().split(maxsplit=1)
        command = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        
        if command in ["exit", "quit"]:
            self.console.print("\n[bold green]Stay secure! 👋[/bold green]")
            return True
        
        elif command == "help":
            self.print_help()
            return True
        
        elif command == "clear":
            self.console.clear()
            self.print_banner()
            return True
        
        elif command == "model":
            self.console.print(f"[bold]Current model:[/bold] {self.client.model}")
            return True
        
        elif command == "models":
            models = self.client.list_models()
            if models:
                self.console.print("[bold]Available models:[/bold]")
                for model in models:
                    self.console.print(f"  - {model}")
            else:
                self.console.print("[yellow]No models found. Make sure Ollama is running.[/yellow]")
            return True
        
        elif command == "tools":
            self.tools.list_tools()
            return True
        
        elif command.startswith("scan") or command.startswith("analyze") or \
             command.startswith("check") or command.startswith("explain") or \
             command.startswith("recommend"):
            # These are handled as regular queries but with context
            return False
        
        return False
    
    def run(self):
        """Main run loop"""
        self.print_banner()
        
        # Check connection
        if not self.client.check_connection():
            self.console.print(
                "[red]❌ Cannot connect to Ollama![/red]\n"
                "[yellow]Please make sure Ollama is installed and running:[/yellow]\n"
                "  - Install: https://ollama.ai\n"
                f"  - Default URL: {self.client.base_url}\n"
                "  - Or set OLLAMA_BASE_URL environment variable"
            )
            return
        
        self.console.print(f"[green]✓[/green] Connected to Ollama")
        self.console.print(f"[dim]Using model: {self.client.model}[/dim]\n")
        self.console.print("[dim]Type 'help' for commands or ask a question. Type 'exit' to quit.[/dim]\n")
        
        # Main interaction loop
        while True:
            try:
                # Get user input with history and autocomplete
                user_input = pt_prompt(
                    "🛡️  > ",
                    history=FileHistory(self.history_path),
                    auto_suggest=AutoSuggestFromHistory(),
                    completer=self.completer
                ).strip()
                
                if not user_input:
                    continue
                
                # Handle commands
                if self.handle_command(user_input):
                    if user_input.lower() in ["exit", "quit"]:
                        break
                    continue
                
                # Process as AI query
                self.console.print("\n[dim]Thinking...[/dim]\n")
                
                # Stream response
                response_text = ""
                for chunk in self.client.chat(user_input):
                    if chunk:
                        response_text += chunk
                        # Print as markdown for better formatting
                        self.console.print(chunk, end="", style="")
                
                self.console.print("\n")  # New line after response
                
            except KeyboardInterrupt:
                self.console.print("\n[yellow]Interrupted. Type 'exit' to quit.[/yellow]")
            except EOFError:
                break
            except Exception as e:
                self.console.print(f"[red]Error: {e}[/red]")

if __name__ == "__main__":
    assistant = CyberFellow()
    assistant.run()


