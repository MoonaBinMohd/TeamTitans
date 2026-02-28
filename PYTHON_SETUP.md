# Python Backend Setup Guide

## Overview

The application now includes a complete Python backend using Flask. The frontend remains the same HTML/CSS/JS application, which can communicate with this Python API.

## Project Structure

```
projectAI2/
├── main.py                      # Flask application entry point
├── requirements.txt             # Python dependencies
├── .env.example                # Environment variables template
├── config.json                 # Configuration file
│
├── routes/                     # API endpoints
│   ├── claims.py              # Claims management endpoints
│   ├── ai.py                  # AI analysis endpoints
│   ├── tunneling.py           # Secure tunneling endpoints
│   ├── analytics.py           # Analytics endpoints
│   └── auth.py                # Authentication endpoints
│
├── models/                     # Data models
│   └── claim.py               # Claim, AIAnalysis, Tunnel models
│
├── services/                   # Business logic
│   ├── ai_service.py          # AI analysis service
│   ├── tunneling_service.py   # Tunneling service
│   └── storage_service.py     # Data storage service
│
├── utils/                      # Utility functions
├── css/                        # Frontend styles
├── js/                         # Frontend JavaScript
├── assets/                     # Frontend assets
└── index.html                 # Frontend HTML
```

## Installation

### 1. Prerequisites

Ensure you have Python 3.8+ installed:

```bash
python --version
```

### 2. Clone/Setup Project

```bash
cd c:\Users\MOONA BIN MOHD\Desktop\projectAI2
```

### 3. Create Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Create Environment File

```bash
copy .env.example .env
```

Edit `.env` and set your configuration:

```env
FLASK_ENV=development
FLASK_DEBUG=True
HOST=0.0.0.0
PORT=5000
SECRET_KEY=your-secret-key-here
```

## Running the Application

### Start the Python Backend

```bash
python main.py
```

Output:
```
==================================================
Tunneling Claim Watch AI - Python Backend
==================================================
Running on http://0.0.0.0:5000
Environment: development
==================================================
```

### In Another Terminal: Start the Frontend

Option 1: Using Python HTTP Server
```bash
python -m http.server 8000
```

Option 2: Using PowerShell
```powershell
python -m http.server 8000
```

### Access the Application

- **Frontend:** http://localhost:8000
- **Backend API:** http://localhost:5000
- **API Health:** http://localhost:5000/api/health

## API Endpoints

### Claims Management
- `GET /api/claims` - Get all claims
- `POST /api/claims` - Create new claim
- `GET /api/claims/<id>` - Get specific claim
- `PUT /api/claims/<id>` - Update claim
- `DELETE /api/claims/<id>` - Delete claim

### AI Analysis
- `POST /api/ai/analyze` - Analyze a claim
- `GET /api/ai/insights/<claim_id>` - Get AI insights
- `GET /api/ai/model/status` - Get model status
- `GET /api/ai/anomalies` - Detect anomalies
- `GET /api/ai/fraud-detection` - Get fraud risks

### Tunneling
- `POST /api/tunnel/create` - Create secure tunnel
- `GET /api/tunnel/<tunnel_id>/status` - Get tunnel status
- `POST /api/tunnel/<tunnel_id>/close` - Close tunnel
- `GET /api/tunnel/routes` - Get routing options
- `GET /api/tunnel/stats` - Get tunneling stats

### Analytics
- `GET /api/analytics/dashboard` - Dashboard stats
- `GET /api/analytics/trends` - Claims trends
- `GET /api/analytics/performance` - Performance metrics
- `POST /api/analytics/report` - Generate report
- `GET /api/analytics/by-type` - Claims by type
- `GET /api/analytics/by-status` - Claims by status

### Authentication
- `POST /api/auth/register` - Register user
- `POST /api/auth/login` - User login
- `POST /api/auth/logout` - User logout
- `POST /api/auth/refresh` - Refresh token
- `GET /api/auth/me` - Get current user

## Testing API Endpoints

### Using PowerShell

```powershell
# Get all claims
$response = Invoke-WebRequest -Uri "http://localhost:5000/api/claims" -Method GET
$response.Content | ConvertFrom-Json | ConvertTo-Json

# Create a claim
$body = @{
    customer = "John Doe"
    claim_type = "medical"
    amount = 5000
    description = "Test claim"
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:5000/api/claims" `
  -Method POST `
  -Headers @{"Content-Type" = "application/json"} `
  -Body $body

# Get dashboard analytics
Invoke-WebRequest -Uri "http://localhost:5000/api/analytics/dashboard" -Method GET
```

### Using curl (Git Bash)

```bash
# Get all claims
curl http://localhost:5000/api/claims

# Create a claim
curl -X POST http://localhost:5000/api/claims \
  -H "Content-Type: application/json" \
  -d '{"customer":"John Doe","claim_type":"medical","amount":5000,"description":"Test claim"}'

# Get dashboard
curl http://localhost:5000/api/analytics/dashboard
```

### Using Python requests

```python
import requests

# Get all claims
response = requests.get('http://localhost:5000/api/claims')
print(response.json())

# Create a claim
data = {
    'customer': 'John Doe',
    'claim_type': 'medical',
    'amount': 5000,
    'description': 'Test claim'
}
response = requests.post('http://localhost:5000/api/claims', json=data)
print(response.json())
```

## Frontend-Backend Integration

Update `config.json` to point to Python backend:

```json
{
  "api": {
    "baseUrl": "http://localhost:5000/api",
    "timeout": 30000,
    "retries": 3
  }
}
```

Then modify `js/app.js` to use the API:

```javascript
// Example API call
fetch('http://localhost:5000/api/claims')
  .then(response => response.json())
  .then(data => console.log(data));
```

## Database Setup (Optional)

### SQLite (Default)

Already configured - no setup needed!

### MongoDB

1. Install MongoDB:
```bash
# Using Homebrew (macOS)
brew install mongodb-community

# Windows: Download from mongodb.com
```

2. Start MongoDB:
```bash
mongod
```

3. Update `.env`:
```env
MONGO_URI=mongodb://localhost:27017/claims_db
```

### PostgreSQL

1. Install PostgreSQL and create database:
```bash
createdb claims_db
```

2. Update `.env`:
```env
DATABASE_URL=postgresql://user:password@localhost/claims_db
```

## Troubleshooting

### Port Already in Use

```bash
# Windows: Kill process on port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# macOS/Linux:
lsof -ti:5000 | xargs kill -9
```

### Module Not Found Errors

```bash
# Verify virtual environment is activated
pip list

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Connection Refused

- Check if backend is running: `http://localhost:5000/api/health`
- Verify port in `.env` matches
- Check firewall settings

### CORS Errors

Already configured in `main.py` with:
```python
CORS(app)
```

If needed, restrict origins in `.env`:
```env
CORS_ORIGINS=http://localhost:8000,http://localhost:3000
```

## Production Deployment

### Using Gunicorn

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 main:app
```

### Using Docker

Create `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_ENV=production
ENV PORT=5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "main:app"]
```

Build and run:

```bash
docker build -t claim-watch-ai .
docker run -p 5000:5000 claim-watch-ai
```

### Using Heroku

```bash
heroku login
heroku create your-app-name
heroku config:set FLASK_ENV=production
git push heroku main
```

## Development Tips

### Enable Debug Mode

```env
FLASK_DEBUG=True
```

### View Logs

```bash
# Python server logs visible in terminal
# Check any exceptions or errors
```

### Mock Data

Auto-generated on startup:
- 12 sample claims
- Various statuses and types
- Random AI scores

### Reset Data

```python
# In Python shell
from routes.claims import storage
storage.claims = []
storage.users = []
```

## Architecture Overview

```
Frontend (HTML/CSS/JS)
        ↓
    HTTP/REST
        ↓
    Flask Backend
    ├── Routes (API endpoints)
    ├── Services (Business logic)
    │   ├── AIService (Analysis)
    │   ├── TunnelingService (Secure transmission)
    │   └── StorageService (Data management)
    ├── Models (Data structures)
    └── Database (Storage)
```

## Key Features

✅ **RESTful API** - Standard REST endpoints
✅ **AI Analysis** - Claim scoring and anomaly detection
✅ **Secure Tunneling** - Safe claim transmission
✅ **Analytics** - Comprehensive dashboard data
✅ **Authentication** - JWT-based auth (ready for production)
✅ **Error Handling** - Comprehensive error responses
✅ **Logging** - Built-in request logging
✅ **CORS Enabled** - Frontend can communicate
✅ **Mock Data** - Auto-generated for testing

## Next Steps

1. **Connect Frontend**: Update API calls to use Python backend
2. **Database**: Implement real database (MongoDB/PostgreSQL)
3. **Authentication**: Add proper JWT verification
4. **Validation**: Add request validation and sanitization
5. **Testing**: Add unit and integration tests
6. **Deployment**: Deploy to production (AWS, Heroku, etc.)

## Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [REST API Best Practices](https://restfulapi.net/)
- [JWT Authentication](https://jwt.io/)
- [Python Requests Library](https://requests.readthedocs.io/)

---

**Happy coding with Python! 🐍**
