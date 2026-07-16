# NDIS Providers Scraper

A high-performance Python-based data scraper designed to extract registered service provider details from the Australian National Disability Insurance Scheme (NDIS) portal. 

This project uses a advanced hybrid architecture: it leverages **Playwright** to seamlessly bypass Cloudflare anti-bot protection, and then intercepts the underlying JavaScript network requests (`cURL` / API responses) to capture the raw JSON payload. This eliminates the need for brittle HTML parsing and ensures fast, resilient data collection.

---

## 🚀 Features

* **Anti-Bot Bypass:** Utilizes Playwright's automated browser engine to handle Cloudflare challenges that completely block standard `requests` scripts.
* **Network Interception:** Captures the raw JSON network payloads directly from the browser background, providing highly accurate data extraction.
* **Structured Output:** Automatically parses the backend API data and exports provider details (Names, Emails, Phone Numbers, Addresses, and Services) into structured formats (CSV/JSON).
* **Isolated Environment:** Fully self-contained configuration with zero global package dependencies.

---

## 🛠️ Installation & Setup

Follow these steps to set up and run the scraper on your local machine:

### Prerequisites
Make sure you have **Python 3.10+** installed on your system.

### 1. Open the Project Folder
Open your terminal (or VS Code) directly in the project directory:
```powershell
cd C:\PythonProjects\ndis-provider-scraper
```
2. Set Up a Virtual Environment
Create a clean, isolated virtual environment inside the project directory so the scraper's packages do not interfere with your system-wide Python installation:
```PowerShell
python -m venv .venv
```
3. Activate the Environment
Tell your terminal to start using your newly created virtual environment:

On Windows (PowerShell):

```PowerShell
.\.venv\Scripts\Activate.ps1
```
On Mac/Linux:

```Bash
source .venv/bin/activate
```
4. Install Dependencies
Ensure your local pip package manager is updated and install the required libraries from the requirements.txt file:

```PowerShell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```
5. Install Playwright Browsers
Download the required Chromium engine used by the automated browser to handle the Cloudflare handshake:

```PowerShell
python -m playwright install chromium
```
💻 Usage
To launch the scraper, make sure your virtual environment is active and run the main Python script:

```PowerShell
python scraper.py
```
(Note: If your main script is named differently, replace scraper.py with your file name.)
---
📂 Project Structure
Plaintext
ndis-provider-scraper/
├── .venv/                 # Local Python virtual environment (ignored by Git)
├── scraper.py             # Main scraper script execution file
├── requirements.txt       # Project dependencies (Playwright, pandas, etc.)
├── README.md              # Project documentation
└── .gitignore             # Tells Git to ignore .venv and cached files
---
🛡️ License
This project is licensed under the MIT License.