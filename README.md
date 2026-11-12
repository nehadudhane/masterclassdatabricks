# Databricks Masterclass — PySpark, Azure Storage, Delta Lake & Auto Loader

Hands-on Databricks notebook exports exploring **Spark DataFrames**, **Azure Data Lake Storage Gen2**, **Databricks widgets and secrets**, **Delta Lake**, and **Auto Loader streaming ingestion**.

## Technologies

- Azure Databricks, PySpark, and Databricks SQL
- Azure Data Lake Storage Gen2 (`abfss://`)
- Delta Lake managed and external tables
- Databricks widgets and secret scopes
- Databricks Auto Loader (`cloudFiles`) and Structured Streaming

## Repository structure

```text
masterclassdatabricks/
├── README.md
├── 01_pyspark_and_azure/
│   └── Tutorial1.py
├── 02_delta_lake_and_autoloader/
│   └── DeltaLake.py
└── 03_practice_notebooks/
    ├── Notebook 1.py
    └── Notebook 2.py
```

## Notebook guide

| Notebook | Topics |
| --- | --- |
| [`Tutorial1.py`](01_pyspark_and_azure/Tutorial1.py) | Building Spark DataFrames; reading CSV; DataFrame transformations; Azure storage access; Databricks widgets and secret scope usage |
| [`DeltaLake.py`](02_delta_lake_and_autoloader/DeltaLake.py) | Delta writes; managed and external tables; DML operations; history and restore; `OPTIMIZE` and `ZORDER`; Auto Loader streaming Parquet to Delta |
| [`Notebook 1.py`](03_practice_notebooks/Notebook%201.py) | Introductory Python output |
| [`Notebook 2.py`](03_practice_notebooks/Notebook%202.py) | Introductory Python output |

## Example data flow

```text
Azure storage (CSV / Parquet)
             |
             v
Databricks PySpark / Auto Loader
             |
             v
Delta Lake tables / streaming Delta sink
             |
             v
Table history, restore, OPTIMIZE, ZORDER
```

## Running the notebooks

These are Databricks Python notebook exports. Import them into a compatible workspace to use the `%sql`, `%md`, and `%run` cells. The `DeltaLake.py` notebook begins with `%run "/masterclassdatabricks/Tutorial1"`, a **workspace notebook path from the original project**. Moving the notebooks into GitHub folders does not update that Databricks workspace dependency. If importing under a different workspace path, adapt that path in your *workspace copy* before execution.

The notebooks also reference environment-specific ABFSS storage paths, schemas, secret scopes, and checkpoints. You need your own configured storage access and compatible Databricks permissions to reproduce the exercises. Some cells rely on state created by earlier cells, and several are exploratory; successful execution has not been independently verified.

## Public repository security note

The original `Tutorial1.py` export contained a **commented-out Azure OAuth client secret**. This public-sharing edition replaces only the secret value with `REDACTED_FOR_PUBLIC_REPOSITORY`; all other notebook content remains exactly as exported. A commented credential is still sensitive. If that client secret was genuine, revoke or rotate it in Azure. Never commit usable credentials to GitHub.

## Author

**Neha Dudhane** — [GitHub](https://github.com/nehadudhane)
