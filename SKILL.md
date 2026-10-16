---
name: python-sqlite-manager
description: Manage databases, create tables, and perform CRUD operations (insert, update, delete) using Python's built-in sqlite3 module. Use when the user asks to connect to databases, create tables, or update/delete records in Python.
---

# Python SQLite Manager

A guide and workflow for managing databases, creating tables, and executing updates and deletions using Python.

## Workflow Steps
1. **Connect:** Use `sqlite3.connect('filename.db')` to establish a connection and create a cursor.
2. **Schema:** Execute `CREATE TABLE IF NOT EXISTS` statements.
3. **Modify:** Run parameterized `UPDATE` and `DELETE` queries safely.
4. **Persist & Close:** Always call `conn.commit()` to save changes and `conn.close()` to release resources.