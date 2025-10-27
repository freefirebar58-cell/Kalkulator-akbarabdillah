DEPLOY TO RENDER (quick)
1. Create a GitHub repo named 'kalkulator-akbar' and push this project (or upload files via GitHub web).
2. Log in to https://dashboard.render.com and connect your GitHub account.
3. Create a new Web Service → Select the 'kalkulator-akbar' repo → Branch main.
4. Build Command: (leave blank)  Start Command: `gunicorn app:app`
5. Render will build and provide a public URL after deploy.

NOTES:
- Scientific functions use Python's math module (angles in radians).
- You can use 'pi' via the π button.
