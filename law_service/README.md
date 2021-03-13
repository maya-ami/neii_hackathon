# Tracking changes in social legislation. Проверка изменения законодательства

Idea:

- The service parses the website containing legal documents once a week.
- Vectorize an updated and a local versions of the document.
- Compute the distance between the two document vectors.
- Unless the distance equals 1, notify a social worker about the changes.

## Usage

python3 detect_document_changes.py local.txt updated.txt
