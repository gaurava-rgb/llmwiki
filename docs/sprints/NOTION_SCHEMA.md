# Notion Schema

Created on 2026-04-20 with `python3 notion_schema.py --apply`.

## Databases

| Role | Notion name | ID |
| --- | --- | --- |
| Raw Sources | Export via Reader | `3464ebe7-f118-8086-ae21-fa8b46f294ec` |
| Control Page | LLM Wiki Control Center | `3484ebe7-f118-81cf-aa1e-c87efef41174` |
| Wiki Pages | LLM Wiki - Wiki Pages | `3484ebe7-f118-81b6-b8b4-ff8291b5ddd2` |
| Claims / Evidence | LLM Wiki - Claims / Evidence | `3484ebe7-f118-812f-a0fd-d1e1bd372cd2` |
| Ops Log | LLM Wiki - Ops Log | `3484ebe7-f118-81c0-ab3f-e64b6707979b` |

## Raw Sources

`Export via Reader` remains the canonical raw-source database.

Required properties:

- `Name` title
- `Author` rich text
- `Category` select
- `Cover Image URL` URL
- `Location` select
- `Notes` rich text
- `Published Date` date
- `Reader URL` URL
- `Reading Progress` number
- `Reading Time` rich text
- `Saved At` date
- `Site` select
- `Source` rich text
- `Source URL` URL
- `Summary` rich text
- `Tags` multi-select
- `Word Count` number
- `Reader ID` rich text
- `Source Type` select
- `Status` select
- `Local Markdown Path` rich text
- `Local Asset Paths` rich text
- `Content Hash` rich text
- `Last Synced At` date
- `Sync Run ID` rich text
- `Processing Notes` rich text
- `Related Wiki Pages` relation to Wiki Pages

## Wiki Pages

Required properties:

- `Name` title
- `Page Type` select
- `Slug` rich text
- `Summary` rich text
- `Lifecycle` select
- `Confidence` select
- `Related Raw Sources` relation to Raw Sources
- `Local Path` rich text
- `GitHub URL` URL
- `Last Updated` date
- `Tags` multi-select

## Claims / Evidence

Required properties:

- `Claim` title
- `Evidence Quote` rich text
- `Confidence` select
- `Raw Source` relation to Raw Sources
- `Wiki Page` relation to Wiki Pages
- `Entity / Concept` rich text
- `Image Reference` rich text
- `Source URL` URL
- `Date Observed` date

## Ops Log

Required properties:

- `Name` title
- `Timestamp` date
- `Operation` select
- `Status` select
- `Run ID` rich text
- `Summary` rich text
- `Notes` rich text
- `Touched Sources` relation to Raw Sources
- `Touched Wiki Pages` relation to Wiki Pages
- `Git Commit` rich text

## Verification

Verification command:

```bash
python3 -m unittest discover -s tests
```

Last local result: 10 tests passed.
