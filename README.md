# 💊 Pharmacy Supply Chain Optimizer

A robust, event-driven **ETL Pipeline** and **Inventory Management System** designed to bridge the gap between clinical pharmacy practice and data engineering. This project automates the tracking of medication stock using **DRAP/GTIN-14** standards and utilizes **PostgreSQL Triggers** for real-time inventory synchronization.

## 🚀 Key Features

* **Clinical Data Modeling:** Implements a normalized schema distinguishing between master medication data and specific stock batches.
* **GTIN-14 Traceability:** Built to accommodate **Drug Regulatory Authority of Pakistan (DRAP)** standards for unique drug identification.
* **Automated Inventory Sync:** A PL/pgSQL Trigger automatically updates total inventory counts whenever a batch is added, updated, or sold.
* **FEFO Optimization:** Advanced SQL queries to prioritize **First-Expired, First-Out (FEFO)** dispensing to minimize pharmaceutical waste.
* **Soft Delete Governance:** Implements "Active/Inactive" flags to preserve historical prescription data while managing the current formulary.

---

## 🏗️ Technical Architecture

### 1. The Database (PostgreSQL)

The system uses a Star Schema approach with the following core entities:

* `med_detail`: The source of truth for drug names, generics, and GTINs.
* `stock_batches`: Tracks granular details like **Batch Number**, **Expiry Date**, and **Unit Cost**.
* `inventory`: An automated summary table providing real-time reorder signals.
* `prescription`: Records all dispensing events for demand forecasting.

### 2. The ETL Process (Python)

* **Extract:** Ingests raw pharmaceutical data from CSV/Staging files.
* **Transform:** Maps brands to generics, calculates reorder points using safety stock formulas, and cleans "messy" GTIN strings.
* **Load:** Utilizes `SQLAlchemy` and `psycopg2` for bulk loading into PostgreSQL.

---

## 🛠️ Installation & Usage

### Prerequisites

* Python 3.12+
* PostgreSQL 15+
* Libraries: `pandas`, `sqlalchemy`, `psycopg2`

### Setup

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/pharmacy-etl-optimizer.git

```


2. **Initialize the Database:**
Run the `schema_setup.sql` script in your PostgreSQL editor to create tables, functions, and triggers.
3. **Run the ETL Pipeline:**
```bash
python bulk_load.py

```



---

## 📊 Sample Insights

The system provides a **Supply Chain Dashboard** via SQL views:
| Brand Name | Total Stock | Status | Recommendation |
| :--- | :--- | :--- | :--- |
| Risek 40mg | 500 | 🟢 OK | Maintain current levels |
| Panadol 500mg | 0 | 🔴 CRITICAL | Reorder immediately |

---

## 👨‍🔬 About the Author

**[Muhammad Nadeem]**
*Final Year Pharm.D Student | Aspiring Data Analyst*
Focused on applying data science to optimize healthcare delivery and pharmaceutical supply chains.

---
