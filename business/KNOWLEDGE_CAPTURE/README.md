# Knowledge Capture Inbox

Use this folder for information Axis OS should remember and retrieve later.

Each captured note should include:

- title
- date captured
- source
- tags
- confidence level
- summary
- original detail or link
- follow-up needed

After adding or editing notes, rebuild the local knowledge index:

```powershell
python tools/rag/kb_ingest.py
```

Then test retrieval:

```powershell
python tools/rag/kb_search.py "your question"
```

