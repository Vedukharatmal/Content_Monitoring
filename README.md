# Content Monitoring & Flagging System
A backend system built using Django and Django REST Framework that monitors external content against user-defined keywords, generates match scores, and supports a human review workflow with suppression logic.

This project demonstrates backend engineering fundamentals including data modeling, API design, business logic separation, and handling edge cases like suppression of irrelevant content.

Tech stack 
- Python
- Django
- Django REST Framework
- SQLite
- drf-yasg (Swagger documentation)

---

# FEATURES
- Add keywords to monitor
- Import/mock external content
- Keyword-based scoring system:
  - Exact match in title → 100
  - Partial match in title → 70
  - Match in body → 40
- Flag generation for matched content
- Review workflow:
  - pending
  - relevant
  - irrelevant
- Suppression logic:
  - Irrelevant flags are not resurfaced unless content changes
- Swagger API documentation

---

# SUPPRESSION LOGIC
If a flag is marked as `irrelevant`, it will not be recreated in future scans unless the associated content item has been updated.

This is implemented by comparing:
- `ContentItem.last_updated`
- `Flag.reviewed_at`

If:
ContentItem.last_updated <= Flag.reviewed_at

→ The flag is suppressed

If:
ContentItem.last_updated > Flag.reviewed_at

→ The content is considered updated and can be flagged again

---

# API ENDPOINTS
| Method | Endpoint           | Description                  |
|--------|--------------------|------------------------------|
| POST   | /api/keywords/     | Create a keyword             |
| POST   | /api/scan/         | Trigger content scan         |
| GET    | /api/flags/        | List all flags               |
| PATCH  | /api/flags/{id}/   | Update flag status           |

---

# I have used a dummy data

curl -X POST http://127.0.0.1:8000/api/keywords/ \
-H "Content-Type: application/json" \
-d '{"name": "django"}'

# Run Scan

curl -X POST http://127.0.0.1:8000/api/scan/

# Get flags

curl http://127.0.0.1:8000/api/flags/

# Update flag

curl -X PATCH http://127.0.0.1:8000/api/flags/1/ \
-H "Content-Type: application/json" \
-d '{"status": "irrelevant"}'

---
# SETUP INSTRUCTIONS

1. Clone the repository
git clone <your-repo-link>

2. Navigate to project
cd content_monitoring

3. Create virtual environment
python -m venv venv

4. Activate virtual environment
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

5. Install dependencies
pip install -r requirements.txt

6. Run migrations
python manage.py makemigrations
python manage.py migrate

7. Start server
python manage.py runserver

# API DOCUMENTATION

Swagger UI:
http://127.0.0.1:8000/swagger/

ReDoc:
http://127.0.0.1:8000/redoc/

---

# DESIGN DECISIONS

- Keyword matching is case-insensitive
- One flag per keyword-content pair (enforced via unique constraint)
- Mock data is used instead of external API for simplicity and deterministic testing
- `update_or_create` is used to simulate content updates
- Business logic is separated into a service layer for maintainability

---

# POSSIBLE IMPROVEMENTS

- Keyword matching is case-insensitive
- One flag per keyword-content pair (enforced via unique constraint)
- Mock data is used instead of external API for simplicity and deterministic testing
- `update_or_create` is used to simulate content updates
- Business logic is separated into a service layer for maintainability