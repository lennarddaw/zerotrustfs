import time
import win32clipboard
import re

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from policy_engine.policy_loader import load_policies
from policy_engine.policy_evaluator import is_violation
from alerts.popup import show_block_popup
from auditlog.logger import log_event


def get_clipboard_text():
    win32clipboard.OpenClipboard()
    try:
        data = win32clipboard.GetClipboardData()
    except Exception:
        data = ""
    win32clipboard.CloseClipboard()
    return data


def monitor_clipboard():
    print("[ZeroTrustFS] Clipboard monitor started.")
    last_content = ""

    policies = load_policies()

    while True:
        time.sleep(0.5)
        current = get_clipboard_text()
        if current != last_content and current.strip() != "":
            print("[Clipboard] Detected new content")
            last_content = current

            if is_violation(current, policies):
                print("[Policy] ⚠️ Violation detected in clipboard content")
                show_block_popup("Upload Blocked", "Sensitive content detected and blocked.")
                log_event("clipboard", "blocked", current[:100])  # Log only first 100 chars


if __name__ == "__main__":
    monitor_clipboard()
