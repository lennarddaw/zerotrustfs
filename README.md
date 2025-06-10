# ZeroTrustFS

**ZeroTrustFS** is a secure, role-based virtual filesystem for controlling GPT/LLM access to sensitive enterprise data. It prevents unauthorized data exposure by enforcing Zero Trust principles for file-level access – especially in environments where employees use generative AI tools like ChatGPT, Copilot, or Claude.

---

## 🔐 Why ZeroTrustFS?

GPTs and other LLMs often see more than they should – especially when employees paste internal documents into AI tools out of laziness or unawareness.

**ZeroTrustFS prevents this by:**
- Providing GPTs access **only through a mounted virtual filesystem**
- Enforcing **policy- and role-based access control**
- Scanning contents for **PII or sensitive terms**
- Logging and blocking any unauthorized or risky attempt

---

## 🚀 Features

- ✅ FUSE-based virtual filesystem (Linux/macOS/Windows via Dokan)
- ✅ Role-based file access via `gpt_read()` API
- ✅ YAML/JSON policy engine (include/deny patterns, file types)
- ✅ NLP content filtering (PII, finance, HR, source code)
- ✅ Full audit logging & replay system
- ✅ REST API & Python SDK
- ✅ Admin dashboard for policy editing & access monitoring
- ✅ Optional clipboard/file upload agent

---

## 🧱 Project Structure

```plaintext
zerotrustfs/
├── fuse_layer/                 # FUSE filesystem implementation
│   ├── __init__.py
│   └── virtual_fs.py
│
├── policy_engine/             # Policy and role rules
│   ├── __init__.py
│   ├── policy_loader.py
│   └── policy_evaluator.py
│
├── content_filter/            # PII & content scanning
│   ├── __init__.py
│   └── filter_engine.py
│
├── access_api/                # GPT SDK and REST access API
│   ├── __init__.py
│   ├── gpt_read.py
│   └── server.py
│
├── auditlog/                  # Logging and query system
│   ├── __init__.py
│   ├── logger.py
│   └── log_reader.py
│
├── web_admin/                 # Web interface (admin UI)
│   ├── backend/
│   │   └── main.py
│   └── frontend/
│       └── (React/Vite setup)
│
├── endpoint_agent/            # Optional local user agent
│   └── agent.py
│
├── config/
│   ├── policies.yaml
│   └── roles.json
│
├── tests/
│   └── test_fuse.py
│
├── README.md
├── LICENSE
├── .gitignore
└── setup.py
