---
title: "Snowflake Has 7 Types of Databases Most Architects Only Know 2"
reader_id: "01knqtp68d87esbzbkdntenzfg"
notion_page_id: "3464ebe7-f118-81b1-b2e0-d6ff17b908e0"
category: "article"
source_type: "Readwise web highlighter"
reader_url: "https://read.readwise.io/read/01knqtp68d87esbzbkdntenzfg"
source_url: "https://medium.com/snowflake/snowflake-has-7-types-of-databases-most-architects-only-know-2-70624f6908ad"
author: "Vedprakash"
site: "Medium"
tags: []
published: "2026-04-08"
saved_at: "2026-04-09"
reading_time: "12 mins"
summary: "Snowflake offers seven database types, each with unique features and trade-offs for cost, recovery, and data sharing. Choosing the right type matters to avoid extra costs, data loss, or architectural problems. New options like Iceberg and Hybrid Tables help combine open data lakes and operational workloads in one platform."
content_hash: "a0249aa0ec149c21939c385625ce4d37bf1309e6eb313735a18fb7f5a568d572"
---

_An architect’s guide to every database type in Snowflake, the design decisions behind each, and when choosing the wrong one costs you money, recovery time, or your data sharing strategy._

> _“A database is just a container” every junior developer ever._
>
> _Wrong. In Snowflake, the database type you choose is an_ architectural decision _with real consequences: cost implications, data recovery windows, sharing topology, replication behaviour, and even which compute engines can query your data._

When I onboard new data engineers, I ask them one question: _“How many types of databases does Snowflake have?”_ Most say two: permanent and transient. A few say three if they’ve used data sharing. The real answer, as of today, is **seven** and the differences between them are not cosmetic.

This post breaks down every Snowflake database type from an architect’s lens: what each one is, the mechanics underneath, when to use it, what you trade away, and the mistakes I’ve seen in production that could have been avoided with the right choice upfront.

## The Full Map First

Before we go deep, here’s the full taxonomy:

![](https://miro.medium.com/v2/resize:fit:2000/1*6B5QyXHL-HtaKIowDg3D5Q.png)

Let’s go through each one like we’re designing a system — because that’s exactly what you are doing when you choose.

## 1\. Standard (Permanent) Database

![](https://miro.medium.com/v2/resize:fit:2000/1*tJkDKE3Jq_02FTYdtlyKAA.png)

This is the default. When you run `CREATE DATABASE my_db`, you get a permanent database. Permanent means two things specifically in Snowflake:

  * **Time Travel:** Data changes are retained for up to **90 days** (configurable via `DATA_RETENTION_TIME_IN_DAYS`). You can query historical data with `AT` or `BEFORE` clauses and restore dropped objects.
  * **Fail-safe:** After Time Travel expires, Snowflake holds another **7 days** of data in a Fail-safe layer. This is not user-accessible — it’s emergency infrastructure for Snowflake support to assist with catastrophic recovery.




    -- Create a standard database with maximum time travel
    CREATE DATABASE prod_analytics
      DATA_RETENTION_TIME_IN_DAYS = 90;
    -- Query data as it looked 3 days ago
    SELECT * FROM prod_analytics.sales.orders
      AT (OFFSET => -60 * 60 * 24 * 3);
    -- Restore a dropped table within the time travel window
    UNDROP TABLE prod_analytics.sales.orders;


**The cost reality architects must understand:** Time Travel and Fail-safe are not free. Snowflake stores historical versions of your micro-partitions. For tables with frequent updates or deletes (high change velocity), storage costs multiply. A 1 TB table with heavy DML over 90 days can cost 3–5x more in storage than its current footprint.

**When to use it:** Every production database. If it matters when it’s gone, it goes in a permanent database.

**Architect’s trade-off:** You are paying for safety. That safety has a real dollar value. Size your retention window deliberately — not all tables need 90 days. Finance tables might. Raw event logs probably don’t.

## 2\. Transient Database

Transient databases have **no Fail-safe** and Time Travel limited to a **maximum of 1 day** (0 or 1). That’s it. The storage cost reduction is proportional — no historical micro-partition accumulation beyond 24 hours.


    -- Transient database: zero time travel, no fail-safe
    CREATE TRANSIENT DATABASE staging_db
      DATA_RETENTION_TIME_IN_DAYS = 0;
    -- Everything created inside inherits transient by default
    CREATE SCHEMA staging_db.raw_ingest; -- transient schema
    CREATE TABLE staging_db.raw_ingest.events_raw (...); -- transient table


Note that inheritance flows downward: tables in a transient database are automatically transient. You cannot create a permanent table inside a transient database.

**When to use it:**

  * Staging layers (raw → bronze) where data is re-loadable from the source
  * ETL intermediate scratch tables
  * Dev and sandbox environments
  * Any dataset where loss = re-run a pipeline (not a business incident)



**The mistake I see most often:** Teams create transient staging databases to save cost, then accidentally JOIN those tables into production views that get referenced in BI dashboards. The staging table gets dropped, the view breaks in production, and the on-call engineer scrambles. **Keep transient and permanent schemas in clearly separated databases — never mix them in the same lineage.**

**Architect’s trade-off:** You trade recovery capability for storage cost savings. Quantify the savings before making this call on small datasets. The savings are negligible. On petabyte-scale staging tables with daily full-refreshes, transient can meaningfully cut your storage bill.

![](https://miro.medium.com/v2/resize:fit:2000/1*77pyNlvug2TqxDW67N6y2A.png)

## 3\. Temporary Database

Temporary databases are **session-scoped**. They vanish when your Snowflake session ends. Time Travel is 0 days. No Fail-safe. Not visible to other sessions.


    -- Created in a session, gone when session closes
    CREATE TEMPORARY DATABASE session_scratch;
    -- Only accessible within the current session
    CREATE TABLE session_scratch.work.calc_results AS
      SELECT customer_id, SUM(revenue) AS total_rev
      FROM prod_analytics.sales.orders
      GROUP BY 1;


**When to use it:** Exploratory analysis, complex multi-step queries where you need intermediate materialisation, and testing transformation logic. Think of it as your scratchpad that auto-cleans.

**Architect’s trade-off:** It’s the lowest-cost option for ephemeral work. The risk is that developers start using temporary databases for things that should persist — audit logs, validation outputs, test datasets — and then are surprised when they disappear. Establish a team convention: temporary means throwaway, transient means short-lived pipeline, permanent means it matters.

![](https://miro.medium.com/v2/resize:fit:2000/1*eXz-lqOjvrV4Wi0S3IBYLA.png)

## 4\. Shared Database (Data Sharing / Marketplace)

A Shared Database is a **read-only database** created in a _consumer_ account from a **Share** object published by a _provider_ account. No data is copied. No ETL runs. The consumer’s query engine reads micro-partitions directly from the provider’s storage.

This is one of Snowflake’s most architecturally significant features. It enables zero-copy data sharing across organisations — the provider pays for storage once, the consumer pays only for compute to query it.


    -- PROVIDER ACCOUNT: Create and configure a share
    CREATE SHARE sales_partner_share;
    GRANT USAGE ON DATABASE prod_analytics TO SHARE sales_partner_share;
    GRANT USAGE ON SCHEMA prod_analytics.sales TO SHARE sales_partner_share;
    GRANT SELECT ON TABLE prod_analytics.sales.orders TO SHARE sales_partner_share;
    -- Add the consumer Snowflake account
    ALTER SHARE sales_partner_share ADD ACCOUNTS = <consumer_account_locator>;
    -- CONSUMER ACCOUNT: Create a database from the inbound share
    CREATE DATABASE partner_sales_data FROM SHARE <provider_account>.sales_partner_share;
    -- Query it as if it were local - no data movement
    SELECT * FROM partner_sales_data.sales.orders WHERE order_date >= '2024-01-01';


**The architectural implications are significant:** The consumer database is always **read-only** — no writes, no DDL, no cloning. The provider controls what is shared at the object level. Updates to the provider’s tables are visible to the consumer **instantly** — because there is no copy. This eliminates an entire class of synchronisation problems.

Snowflake Marketplace extends this: providers can publish listings that any Snowflake account in any cloud region can subscribe to. This is how data providers (financial data, weather, demographics) distribute live datasets commercially.

**When to use it:**

  * B2B data monetisation (selling your data to partners)
  * Cross-business-unit data sharing within an enterprise across separate Snowflake accounts
  * Consuming third-party datasets from Snowflake Marketplace
  * Replacing file-based data exchange with partners



**Architect’s trade-off:** Data governance becomes critical. When you share a database, you expose its schema. If your schema changes (column renamed, table dropped), the consumer’s queries break immediately. Treat shared objects like a public API contract — version them and communicate changes with deprecation windows.

![](https://miro.medium.com/v2/resize:fit:2000/1*1OVB4vj4X7tYoTFSg9mZnw.png)

## 5\. Secondary Database (Replication)

A Secondary Database is a **replicated, read-only copy** of a primary database, created in a different Snowflake account — typically in a different cloud region or cloud provider. It is kept in sync with the primary via Snowflake’s replication mechanism.

Unlike a Shared Database (which is a view into someone else’s data), a Secondary Database is a **full copy** of your own data in another location. This matters for disaster recovery, regional query performance, and business continuity.


    -- PRIMARY ACCOUNT: Enable replication on the primary database
    ALTER DATABASE prod_analytics ENABLE REPLICATION TO ACCOUNTS aws_us_east_1.<secondary_account>;
    -- SECONDARY ACCOUNT: Create the secondary database
    CREATE DATABASE prod_analytics_dr
      AS REPLICA OF <primary_account>.aws_eu_west_1.prod_analytics;
    -- Refresh the secondary (can also be automated via Task)
    ALTER DATABASE prod_analytics_dr REFRESH;
    -- Check replication lag
    SELECT SYSTEM$GET_REPLICATION_PROGRESS('prod_analytics_dr');


Modern practice uses **Replication Groups** instead of database-level replication, because a group lets you replicate multiple databases, plus associated objects (roles, warehouses, resource monitors) as a consistent unit — which is what you need for a true failover scenario.


    -- Replication Group approach (recommended for DR)
    CREATE REPLICATION GROUP primary_rg
      OBJECT_TYPES = DATABASES, ROLES, WAREHOUSES, RESOURCE MONITORS
      ALLOWED_DATABASES = prod_analytics, prod_config
      ALLOWED_ACCOUNTS = <secondary_account>
      REPLICATION SCHEDULE = '15 MINUTES';

    -- Failover in a disaster scenario
    ALTER REPLICATION GROUP primary_rg PRIMARY;


**When to use it:**

  * Active-passive DR setup (primary in US-East, secondary in EU-West)
  * Offloading heavy analytical read workloads to a regional replica closer to users
  * Compliance: data residency requirements (EU data must have a replica in EU)



**Architect’s trade-off:** Replication has a cost — both in storage (you pay for the secondary’s storage) and in the replication compute itself. The replication lag is not zero. Know your RPO (Recovery Point Objective) requirement before you set the replication schedule.

![](https://miro.medium.com/v2/resize:fit:2000/1*SaWKbnmnWi7aMMMYQDT5uQ.png)

## 6\. Application Database (Native Apps Framework)

An Application Database is automatically created when a **Native Application** is installed from the Snowflake Marketplace or deployed directly to a consumer account. It runs inside the consumer’s account, accesses their data with explicit permission, and is managed by the application’s logic.

## Get Vedprakash’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

Remember me for faster sign in

This is Snowflake’s distribution model for data applications — not just data, but full applications (stored procedures, Streamlit UIs, Python functions) that run within Snowflake.


    -- APPLICATION PACKAGE (created by the provider/ISV)
    CREATE APPLICATION PACKAGE my_analytics_app_pkg;
    -- CONSUMER ACCOUNT: Install the application
    CREATE APPLICATION my_analytics_app
      FROM APPLICATION PACKAGE provider_account.my_analytics_app_pkg
      USING VERSION v1_0;
    -- Grant the application access to consumer data
    GRANT USAGE ON DATABASE consumer_data TO APPLICATION my_analytics_app;
    GRANT SELECT ON ALL TABLES IN SCHEMA consumer_data.sales
      TO APPLICATION my_analytics_app;


The Application Database is isolated — it has its own schema where the application stores its working data, metadata, and state. The provider cannot see the consumer’s data; the consumer controls what access is granted.

**When to use it:**

  * You are building a SaaS data product distributed via Snowflake Marketplace
  * You want to give customers an analytics application that runs on their own data without it ever leaving their account
  * ISVs building Snowflake-native applications (packaged data pipelines, analytics accelerators)



**Architect’s trade-off:** You must think of your application as a product with a versioned deployment lifecycle. Application upgrades, backward compatibility, and permission grants become first-class concerns. This is a productisation pattern, not just a database type.

![](https://miro.medium.com/v2/resize:fit:2000/1*kxXsMlcjHbv3WBKG024oTw.png)

## 7\. Catalog Database & Iceberg Database (Open Lakehouse)

This is where the architecture gets genuinely interesting for anyone working at the intersection of the data lakehouse and Snowflake.

## Iceberg Tables in Snowflake

Apache Iceberg is an open table format. Iceberg tables store their data as Parquet files in object storage (S3, GCS, ADLS), with a metadata layer (JSON manifests and snapshot files) that enables ACID transactions, schema evolution, and time travel — all independently of the query engine.

In Snowflake, you can create **Iceberg Tables** managed by Snowflake, where Snowflake owns the Iceberg metadata and catalog, but the data lands in your own object storage via an **External Volume**.


    -- Step 1: Create an External Volume pointing to your S3 bucket
    CREATE EXTERNAL VOLUME my_iceberg_vol
      STORAGE_LOCATIONS = (
        (
          NAME = 'primary-s3'
          STORAGE_PROVIDER = 'S3'
          STORAGE_BASE_URL = 's3://my-lakehouse-bucket/iceberg/'
          STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::123456789:role/snowflake-iceberg-role'
        )
      );
    -- Step 2: Create an Iceberg table - data lands in S3, Snowflake owns metadata
    CREATE ICEBERG TABLE prod_analytics.sales.orders_iceberg (
      order_id     STRING,
      customer_id  STRING,
      order_date   DATE,
      total_amount DECIMAL(18, 2)
    )
      CATALOG = 'SNOWFLAKE'
      EXTERNAL_VOLUME = 'my_iceberg_vol'
      BASE_LOCATION = 'sales/orders/';
    -- Time travel works the same way
    SELECT * FROM prod_analytics.sales.orders_iceberg
      AT (TIMESTAMP => '2024-06-01 00:00:00'::TIMESTAMP_NTZ);


## Catalog-Linked Database (Snowflake Open Catalog / Polaris)

**Snowflake Open Catalog** (formerly Project Polaris) is Snowflake’s open-source implementation of the Apache Iceberg REST Catalog spec. It allows multiple query engines — Spark, Flink, Trino, DuckDB, Snowflake — to share the same Iceberg tables via a common catalog.


    -- Create a Catalog Integration to an external REST Catalog (e.g., AWS Glue or Open Catalog)
    CREATE CATALOG INTEGRATION glue_catalog_integration
      CATALOG_SOURCE = GLUE
      CATALOG_NAMESPACE = 'my_lakehouse_db'
      TABLE_FORMAT = ICEBERG
      GLUE_AWS_ROLE_ARN = 'arn:aws:iam::123456789:role/glue-catalog-role'
      GLUE_CATALOG_ID = '123456789012'
      GLUE_REGION = 'us-east-1'
      ENABLED = TRUE;

    -- Create an Iceberg table registered in the external catalog
    CREATE ICEBERG TABLE prod_analytics.lakehouse.clickstream (
      event_id    STRING,
      user_id     STRING,
      event_type  STRING,
      ts          TIMESTAMP_NTZ
    )
      CATALOG = 'glue_catalog_integration'
      EXTERNAL_VOLUME = 'my_iceberg_vol'
      METADATA_FILE_PATH = 'clickstream/metadata/v3.metadata.json';


**The critical architectural distinction:**

Snowflake-Managed Iceberg Catalog-Linked (External Catalog) **Who owns metadata?** Snowflake External catalog (Glue, Open Catalog, Nessie) **Other engines can write?** No (Snowflake is the writer) Yes — Spark, Flink, Trino can all write **DML support in Snowflake?** Full (INSERT, UPDATE, DELETE, MERGE) Read-only in Snowflake (external engine writes) **Use case** Snowflake-primary with open storage True multi-engine lakehouse

**When to use Iceberg / Catalog-Linked:**

  * You need data to be readable by Spark AND Snowflake AND Trino without ETL between them
  * You want to avoid vendor lock-in — Parquet on S3 is universally accessible
  * Your organisation has a data lake (Spark-based) and Snowflake in the same architecture sharing a single table definition
  * Long-term cold data archival where you want storage-layer portability



**Architect’s trade-off:** Iceberg tables are more complex to operate than native Snowflake tables. Maintenance tasks (compaction, snapshot expiry, orphan file cleanup) must be managed explicitly for externally-catalogued tables. Factor in operational overhead from day one.

![](https://miro.medium.com/v2/resize:fit:2000/1*3Ae-1I2TQsNHgbLTSxTHxw.png)

## 8\. Hybrid Tables (Unistore — The OLTP Layer)

Hybrid Tables live inside a regular permanent database but use a **row-store engine** instead of the columnar micro-partition engine. This gives you capabilities that native Snowflake tables cannot provide: **row-level lookups in milliseconds, primary key enforcement, unique constraints, foreign keys, and secondary indexes** — the building blocks of OLTP workloads.


    -- Hybrid table: row-store, indexes, PK enforcement
    CREATE HYBRID TABLE orders (
      order_id     INTEGER PRIMARY KEY,
      customer_id  INTEGER NOT NULL,
      status       VARCHAR(20),
      created_at   TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP(),
      INDEX idx_customer (customer_id),
      INDEX idx_status (status)
    );
    -- Point lookups are fast (milliseconds, not seconds)
    SELECT * FROM orders WHERE order_id = 98765432;
    -- Row-level updates with low latency
    UPDATE orders SET status = 'shipped' WHERE order_id = 98765432;


The same Snowflake account can now serve both a web application’s backend (point lookups, writes) and a data warehouse workload (analytical aggregations) — with JOIN capability between hybrid and standard tables.

**When to use it:**

  * Application state that needs to be JOINed with warehouse data without ETL
  * Lookup tables or reference data with frequent point-read access patterns
  * Operational reporting that requires both fresh row-level data and historical analytics



**Architect’s trade-off:** Hybrid Tables are not a replacement for purpose-built OLTP databases (PostgreSQL, Aurora) at scale. They are best thought of as a bridge — when you want Snowflake to handle operational data tightly coupled to your analytics, without running a separate system.

![](https://miro.medium.com/v2/resize:fit:2000/1*DoevPLSwhTY6K9WWUmnfrQ.png)

## The Architect’s Decision Framework

When a new data domain lands on your desk, ask these four questions in order:


    1. DOES THIS DATA NEED TO SURVIVE ACCIDENTAL LOSS?
       Yes  → Standard (Permanent) Database
       No   → Transient or Temporary
    2. WHO NEEDS TO ACCESS IT?
       Only us, same account            → Standard or Transient
       Another org / partner            → Shared Database (Data Sharing)
       Another region / DR scenario     → Secondary Database (Replication)
       As a deployed application        → Application Database (Native Apps)
    3. DOES IT NEED TO BE READABLE BY NON-SNOWFLAKE ENGINES?
       Yes, multi-engine (Spark, Flink) → Iceberg + External Catalog
       No, Snowflake-primary            → Standard Snowflake tables
    4. DOES IT HAVE OLTP ACCESS PATTERNS (point lookups, row writes)?
       Yes → Hybrid Tables inside a Standard Database
       No  → Standard columnar tables



![](https://miro.medium.com/v2/resize:fit:2000/1*Ky5ShfAuyJg_1wdq_xvm4g.png)

## Storage Cost Comparison at a Glance

Database Type Time Travel Fail-safe Relative Storage Cost Standard 0–90 days 7 days Highest (for high-change tables) Transient 0–1 day None Low Temporary 0 days None Lowest Shared N/A (read-only) N/A Zero (no copy) Secondary Mirrors primary Mirrors primary Additive (full copy) Application Standard internally Standard Standard Iceberg (Snowflake-managed) Yes (metadata) No (your S3) Object storage rates

![](https://miro.medium.com/v2/resize:fit:2000/1*6nC6Xn_sDmWugMIzKOlKHg.png)

## Common Architectural Mistakes to Avoid

**Mistake 1 — Using Standard everywhere out of habit.** Not every dataset needs 90-day time travel. Staging tables, scratch intermediate tables, and dev databases are excellent candidates for transient. Audit your storage bill — you may be paying for recovery windows on data you’d just re-load anyway.

**Mistake 2 — Mixing transient and permanent tables in the same pipeline lineage.** If a permanent prod table is derived from a transient staging table, your lineage is only as recoverable as the weakest link. Design your layers cleanly.

**Mistake 3 — Treating a Shared Database like a permanent local database.** Shared databases are read-only. Teams sometimes CTAS from a shared database into local tables — which is fine — but they forget that this creates a copy with no refresh mechanism. Build explicit refresh pipelines or use the live shared tables directly.

**Mistake 4 — Skipping replication because “we have backups.”** Time Travel and Fail-safe protect against accidental deletion — they don’t protect against a regional AWS outage. Secondary databases in a different region are your actual DR strategy.

**Mistake 5 — Using Iceberg without planning compaction.** Iceberg’s snapshot model accumulates metadata files over time. Without regular maintenance (compaction, snapshot expiry, orphan file cleanup), query planning slows as the engine scans an ever-growing metadata tree. Automate this from day one.

## Key Takeaways

  * Snowflake has seven distinct database types, each encoding a different set of trade-offs around cost, durability, access topology, and engine compatibility.
  * **Standard vs Transient** is fundamentally a question of recoverability vs cost — make this decision per domain, not per account.
  * **Shared and Secondary** databases are your data sharing and DR primitives — design them in from the start, not as afterthoughts.
  * **Iceberg and Catalog-Linked** databases represent Snowflake’s commitment to the open lakehouse — the path to multi-engine interoperability without data duplication.
  * **Hybrid Tables** collapse the OLTP/OLAP divide — use them where operational and analytical data must live together.



The database type is not a setting you configure once and forget. It is a declaration of intent — about who can access the data, how long it must survive, what engines can touch it, and what you are willing to pay for those guarantees.

Choose deliberately.
