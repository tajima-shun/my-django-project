# Course Project: Web Application Development

## 1. Project Outline (プロジェクト概要)
This repository contains the course project for Web Application Development. 
The goal of this project is to develop a robust web application using Python and Django, ensuring high code quality, reproducibility, and comprehensive test coverage.

(本リポジトリは、Webアプリケーション開発の講義プロジェクト用です。PythonとDjangoを使用し、コード品質、再現性、および包括的なテストカバー率を保証した堅牢なWebアプリケーションの開発を目指します。)

---

## 2. Development Environment (開発環境)
The development environment is fully isolated and managed using `uv` to ensure reproducibility across different machines.

- **Python Interpreter**: Version 3.11.8
- **Environment Manager**: `uv` (by Astral)
- **Virtual Environment**: Python venv managed under `.venv/`

### Setup Instructions
To reproduce this environment on your machine, ensure you have `uv` installed, then run the following command in the project root folder:
```bash
# Sync and install all required dependencies listed in pyproject.toml
uv sync
```

### OpenSpec documentation
This project uses OpenSpec for authoritative runtime and domain documentation. See `openspec/specs/` for the canonical project specification and agent guidance.