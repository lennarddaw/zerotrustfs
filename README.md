# ZeroTrustFS

**ZeroTrustFS** is a local monitoring agent that prevents unauthorized data leakage to generative AI systems (like ChatGPT or Microsoft Copilot) by intercepting clipboard actions and file uploads. It enforces company-wide policies through file type rules, content scanning, and role-based restrictions – before sensitive data leaves the endpoint.

---

## 🛡️ Key Idea

Employees often copy and paste or upload sensitive company documents into LLMs out of convenience. ZeroTrustFS prevents this at the source – on their local machine – before the data even reaches the internet.

---

## 🚀 Features

- ✅ Agent runs silently on employee endpoints
- ✅ Blocks clipboard copy/paste of sensitive files
- ✅ Blocks file uploads to AI tools (via browser or app)
- ✅ YAML/JSON-based role & policy system
- ✅ Alert popups to educate users in real-time
- ✅ Full local logging and audit trail
- ✅ (Optional) Browser extension or API proxy for Copilot

---

## 📁 Project Structure

```plaintext
zerotrustfs/
├── agent/                   # Main logic for detection and enforcement
│   ├── monitor.py           # Monitors clipboard, file access, window focus
│   ├── policy_enforcer.py   # Evaluates policies and roles
│   └── windows_hooks.py     # Low-level OS hooking
│
├── alerts/                  # User notifications
│   └── popup.py
│
├── policy_engine/           # Loads and applies policy rules
│   ├── policy_loader.py
│   └── policy_evaluator.py
│
├── auditlog/                # Logging of all events
│   ├── logger.py
│   └── log_reader.py
│
├── integration/             # Optional Copilot/Browser integrations
│   ├── browser_extension/
│   │   └── manifest.json
│   └── copilot_proxy.py
│
├── config/                  # YAML policies, roles, and exclusions
│   ├── policies.yaml
│   └── roles.json
│
├── tests/                   # Unit tests
│   └── test_policy.py
│
├── README.md
├── LICENSE
├── .gitignore
└── setup.py
