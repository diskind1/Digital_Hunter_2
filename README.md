# Part 2 - Analytics Queries & API

## Setup

### 1. Start MySQL with pre-loaded data

```bash
docker compose -f docker-compose.db.yml up -d
```

### 2. Connection details to the DB
```json
{
  "host": "localhost",
  "port": 3306,
  "user": "root",
  "password": "root",
  "database": "digital_hunter"
}
```

## Files you get

| File | Description                               |
|------|-------------------------------------------|
| `docker-compose.db.yml` | MySQL with pre-loaded data |
| `db/dump.sql` | Database dump (auto-loaded on first start) |
| `requirements.txt` | Python dependencies                       |



לראות את הטבלאות עשיתי פקודה:
docker exec -it mysql mysql -uroot -p digital_hunter -e "SHOW TABLES"

התוצאה:
+--------------------------+
| Tables_in_digital_hunter |
+--------------------------+
| attacks                  |
| damage_assessments       |
| intel_signals            |
| targets                  |
+--------------------------+


ואז ראיתי הכל:
docker exec -it mysql mysql -uroot -p digital_hunter -e "SELECT * FROM attacks"