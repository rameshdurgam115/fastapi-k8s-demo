from fastapi import FastAPI
import os
import psycopg2

# 1. Create the FastAPI "app" object
app = FastAPI()

# 2. Read DATABASE_URL from env, or fall back to a default
DB_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@db:5432/postgres"
)

# 3. Define a GET endpoint at "/"
@app.get("/")
def read_root():
    # 4. Connect to Postgres
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    # 5. Run a simple query
    cur.execute("SELECT version();")
    version = cur.fetchone()[0]
    cur.close()
    conn.close()
    # 6. Return JSON with the Postgres version
    return {"postgres_version": version}
