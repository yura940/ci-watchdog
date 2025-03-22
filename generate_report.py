import json
import os

OUTPUT = "report.html"

def load_json(path):
    try:
        with open(path) as f:
            return json.load(f)
    except Exception:
        return []

def section(title, content):
    return f"<h2>{title}</h2>\n<pre>{content}</pre>"

def main():
    gitleaks_data = load_json("scans/gitleaks/report.json")
    trivy_data = load_json("scans/trivy/report.json")
    semgrep_data = load_json("scans/semgrep/report.json")

    html = "<html><head><meta charset='utf-8'><title>CI-Watchdog Report</title></head><body>"
    html += "<h1>🔐 CI-Watchdog - Security Scan Report</h1>"

    # Gitleaks
    html += section("Gitleaks", json.dumps(gitleaks_data, indent=2))

    # Trivy
    trivy_vulns = []
    for res in trivy_data if isinstance(trivy_data, list) else trivy_data.get("Results", []):
        trivy_vulns.extend(res.get("Vulnerabilities", []))
    html += section("Trivy", json.dumps(trivy_vulns, indent=2))

    # Semgrep
    semgrep_results = semgrep_data.get("results", []) if isinstance(semgrep_data, dict) else []
    html += section("Semgrep", json.dumps(semgrep_results, indent=2))

    html += "</body></html>"

    with open(OUTPUT, "w") as f:
        f.write(html)

    print(f"✅ HTML report generated at {OUTPUT}")

if __name__ == "__main__":
    main()

