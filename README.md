# StudyHelp

A Django-based web app for study help, featuring user authentication, an admin panel, help videos, and a YourGuide module for expert lookup by app/topic. Uses Bootstrap for UI and pandas for CSV handling.

## Features
- User login/logout
- Admin panel for managing help videos
- Homepage with app cards (Workato, Alteryx, AWS, etc.)
- Help videos per app (title + video link)
- Sidebar with "Help Videos" and "YourGuide"
- YourGuide: select app/topic, see expert developers (from CSV)

## Setup
1. Create and activate a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
2. Install dependencies:
   ```powershell
   pip install django pandas streamlit bootstrap4
   ```
3. Run migrations:
   ```powershell
   python manage.py migrate
   ```
4. Create a superuser:
   ```powershell
   python manage.py createsuperuser
   ```
5. Start the server:
   ```powershell
   python manage.py runserver
   ```

## CSV Format for YourGuide
Place your CSV in `media/yourguide.csv` with columns: `app,topic,dev1,dev2,dev3,...` (1=expert, 0=not expert).

## Streamlit
If you want to use Streamlit for the YourGuide module, run:
```powershell
streamlit run yourguide_streamlit.py
```

---

Replace placeholder data and extend as needed for your organization.
