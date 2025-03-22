import json
import os

badge_ok = """<svg xmlns="http://www.w3.org/2000/svg" width="170" height="20">
  <rect width="100%" height="100%" fill="#2d2d2d"/>
  <rect width="120" height="20" fill="#555"/>
  <rect x="120" width="50" height="20" fill="#4c1"/>
  <text x="60" y="14" fill="#fff" font-family="Verdana" font-size="11" text-anchor="middle">Security Scan</text>
  <text x="145" y="14" fill="#fff" font-family="Verdana" font-size="11">OK</text>
</svg>"""

badge_ko = """<svg xmlns="http://www.w3.org/2000/svg" width="190" height="20">
  <rect width="100%" height="100%" fill="#2d2d2d"/>
  <rect width="140" height="20" fill="#555"/>
  <rect x="140" width="50" height="20" fill="#e05d44"/>
  <text x="70" y="14" fill="#fff" font-family="Verdana" font-size="11" text-anchor="middle">Security Scan</text>
  <text x="165" y="14" fill="#fff" font-family="Verdana" font-size="11">Issues</text>
</svg>"""

def has_issues(path, keyword=""):
    try:
        with open(path) as f:
            data = json.load(f)
            if isinstance(data, list):
                return len(data) > 0
            elif isinstance(data, dict):
                return any(data.get(k) for k in ["Results", "Findings"])
    except:
        return False
    return False

found_issues = (
    has_issues("scans/gitleaks/report.json") or
    has_issues("scans/trivy/report.json") or
    has_issues("scans/semgrep/report.json")
)

os.makedirs("assets", exist_ok=True)
with open("assets/badge.svg", "w") as f:
    f.write(badge_ko if found_issues else badge_ok)

