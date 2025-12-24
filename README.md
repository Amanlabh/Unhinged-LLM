# 🛡️ Cyber Fellow

Your personal cybersecurity AI assistant powered by Ollama. Cyber Fellow is an intelligent assistant that understands cybersecurity concepts, tools, techniques, and best practices.

## Features

- **Cybersecurity Expertise**: Deep knowledge of security domains, tools, and frameworks
- **Local AI**: Powered by Ollama for privacy and offline use
- **Interactive CLI**: Rich terminal interface with command history and autocomplete
- **Comprehensive Knowledge**: Covers network security, application security, forensics, compliance, and more
- **Tool Recommendations**: Get suggestions for the right security tools for your needs
- **MITRE ATT&CK Awareness**: Understands attack techniques and defense strategies

## Prerequisites

1. **Python 3.8+**
2. **Ollama** - Install from [ollama.ai](https://ollama.ai)

## Installation

1. **Install Ollama** (if not already installed):
   ```bash
   # macOS/Linux
   curl -fsSL https://ollama.ai/install.sh | sh
   
   # Or download from https://ollama.ai
   ```

2. **Pull a model** (choose one):
   ```bash
   ollama pull llama3.2        # Recommended: Fast and capable
   ollama pull mistral         # Alternative
   ollama pull codellama       # Good for code-related security
   ollama pull llama3.1        # Larger, more capable
   ```

3. **Install Python dependencies**:
   ```bash
   cd cyber-fellow
   pip install -r requirements.txt
   ```

## Configuration

Create a `.env` file (optional) to customize settings:

```env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2
```

## Usage

Run the assistant:

```bash
python main.py
```

Or make it executable:

```bash
chmod +x main.py
./main.py
```

## Commands

- `help` - Show help message
- `exit` or `quit` - Exit the assistant
- `clear` - Clear the screen
- `model` - Show current model
- `models` - List available Ollama models
- `tools` - Show available cybersecurity tools

## Examples

Ask questions like:

- "How do I secure my API endpoints?"
- "What tools should I use for network forensics?"
- "Explain SQL injection attacks and how to prevent them"
- "Help me with incident response procedures"
- "What are the OWASP Top 10 vulnerabilities?"
- "Recommend tools for penetration testing"
- "How do I implement proper authentication?"
- "Explain the MITRE ATT&CK framework"

## Knowledge Areas

Cyber Fellow understands:

- **Network Security**: Firewalls, IDS/IPS, VPN, network segmentation
- **Application Security**: OWASP Top 10, secure coding, authentication
- **Cloud Security**: IAM, container security, cloud compliance
- **Incident Response**: SIEM, threat hunting, forensics, malware analysis
- **Cryptography**: Encryption, hashing, PKI, TLS/SSL
- **Vulnerability Management**: Penetration testing, scanning, patch management
- **Compliance**: GDPR, HIPAA, PCI DSS, SOC 2, ISO 27001, NIST
- **Threat Intelligence**: Threat modeling, APT groups, attack vectors

## Security Tools Coverage

- Network analysis tools (Wireshark, nmap, tcpdump)
- Vulnerability scanners (Nessus, OpenVAS, Burp Suite)
- Penetration testing tools (Metasploit, sqlmap, Hydra)
- Forensics tools (Volatility, Autopsy, FTK)
- Malware analysis tools (IDA Pro, Ghidra, YARA)
- Log analysis tools (Splunk, ELK Stack, Graylog)

## Troubleshooting

**Cannot connect to Ollama:**
- Make sure Ollama is running: `ollama serve`
- Check if the URL is correct (default: http://localhost:11434)
- Verify Ollama is installed: `ollama --version`

**Model not found:**
- Pull the model: `ollama pull llama3.2`
- List available models: `ollama list`
- Change model in `.env` or use `models` command

**Slow responses:**
- Use a smaller/faster model (llama3.2 is recommended)
- Ensure you have enough RAM (models need 4-8GB typically)
- Close other applications to free up resources

## License

MIT License - Feel free to use and modify for your needs.

## Contributing

Contributions welcome! Areas for improvement:
- Additional security knowledge domains
- More tool integrations
- Better context management
- Web interface option
- Plugin system for custom tools

---

**Stay secure! 🛡️**



# Unhinged-LLM
