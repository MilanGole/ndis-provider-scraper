# NDIS Providers Scraper

A high-performance Python-based data scraper designed to extract registered service provider details from the Australian National Disability Insurance Scheme (NDIS) portal. 

This project uses an advanced hybrid architecture: it leverages **Playwright** to seamlessly bypass Cloudflare anti-bot protection, and then intercepts the underlying JavaScript network requests (`cURL` / API responses) to capture the raw JSON payload. This eliminates the need for brittle HTML parsing and ensures fast, resilient data collection.

---

## 🚀 Features

* **Anti-Bot Bypass:** Utilizes Playwright's automated browser engine to handle Cloudflare challenges that completely block standard `requests` scripts.
* **Network Interception:** Captures the raw JSON network payloads directly from the browser background, providing highly accurate data extraction.
* **Data Handling & Structured Output:** Leverages a secondary Pandas pipeline `data_cleaning.ipynb` to clean raw JSON payloads, handle missing records, deduplicate fields and export final provider lists into production-ready Excel and CSV formats.
* **Isolated Environment:** Fully self-contained configuration with zero global package dependencies.

---

## 🛠️ Installation & Setup

Follow these steps to set up and run the scraper on your local machine:

### Prerequisites

Make sure you have **Python 3.10+** installed on your system.

### 1. Open the Project Folder

Open your terminal (or VS Code) directly in the project directory:

```powershell
git clone https://github.com/MilanGole/ndis-provider-scraper.git
cd ndis-provider-scraper
```
### 2. Set Up a Virtual Environment

Create a clean, isolated virtual environment inside the project directory so the scraper's packages do not interfere with your system-wide Python installation:

```powershell
python -m venv .venv
```
### 3. Activate the Environment

Tell your terminal to start using your newly created virtual environment:

On Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```
On Mac/Linux:

```Bash
source .venv/bin/activate
```

⚠️ Windows Troubleshooting Note: If you encounter an error stating that script execution is disabled on your system, run the following command in PowerShell before running the activation script:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

### 4. Install Dependencies

Ensure your local pip package manager is updated and install the required libraries from the requirements.txt file:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 5. Install Playwright Browsers

Download the required Chromium engine used by the automated browser to handle the Cloudflare handshake:

```powershell
python -m playwright install chromium
```

## 💻 Usage

### Step 1: Run the Extractor

Execute the core script to bypass defenses and extract the raw network API data:

```powershell
python scraper.py
```
### Step 2: Run the Data Cleaning Pipeline

Open the Jupyter Notebook to clean the extracted raw data and export it to Microsoft Excel/CSV:

```powershell
jupyter notebook data_cleaning.ipynb
```
(Note: Ensure you have Jupyter installed via your requirements.txt to run the processing file).

## 📂 Project Structure

```text
ndis-provider-scraper/
├── .venv/                  # Local Python virtual environment (ignored by Git)
├── scraper.py              # Script 1: Playwright API interception
├── data_cleaning.ipynb     # Script 2: Pandas data cleaning pipeline
├── requirements.txt        # Project dependencies (Playwright, pandas, etc.)
├── README.md               # Project documentation
└── .gitignore              # Tells Git to ignore .venv and cached files
```
## 🛡️ License
This project is licensed under the MIT License.
