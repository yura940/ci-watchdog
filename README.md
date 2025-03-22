# 🐶 CI-Watchdog

**CI-Watchdog** is an automated DevSecOps agent designed to monitor and enhance the security of CI/CD pipelines, with a primary focus on **GitHub Actions**.

## 🚀 Project Goals

- Detect vulnerabilities in code, dependencies, and infrastructure
- Catch hardcoded secrets and misconfigurations
- Generate a centralized, structured security report
- Display a dynamic security badge in the README
- Plug easily into any GitHub Actions workflow

## 🔧 Tools Used

- [🔍 Trivy](https://github.com/aquasecurity/trivy) — vulnerability & dependency scanning  
- [🕵️‍♂️ Gitleaks](https://github.com/gitleaks/gitleaks) — secrets detection  
- [📜 Semgrep](https://semgrep.dev) — static code analysis (SAST)  
- [🏗️ Checkov](https://www.checkov.io/) — Infrastructure as Code (IaC) scanning *(coming soon)*

## 📂 Project Structure

```bash
.github/workflows/ci.yml       # CI workflow definition  
scans/                         # Scan tool configs & outputs  
report/                        # Generated security reports  
assets/                        # Visuals and SVG badge  
```

## 📈 Security Badge (coming soon)

*A security score badge will be generated and displayed here to reflect the latest CI pipeline scan results.*

## ⚙️ GitHub Actions Pipeline

A GitHub Actions workflow is being implemented to run security scans automatically on each push or pull request.

---

## 🛣️ Roadmap

- [ ] Integrate security scanners (Trivy, Gitleaks, Semgrep, etc.)
- [ ] Collect and aggregate scan results
- [ ] Generate a comprehensive report + SVG badge
- [ ] Publish reports via GitHub Pages or downloadable releases

---

## 👨‍💻 Author

Made with ❤️ by [Sami Brahimi](https://github.com/yura940) — Cybersecurity Engineer. 
