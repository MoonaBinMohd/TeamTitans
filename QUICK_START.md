# Quick Start Guide - Tunneling Claim Watch AI

## 🚀 Running the Application

### Option 1: Using Python (Recommended for quick start)
```bash
python -m http.server 8000
```
Then open: `http://localhost:8000`

### Option 2: Using Node.js HTTP Server
```bash
npx http-server
```
Then open: `http://localhost:8080`

### Option 3: Using Node.js with NPM
```bash
npm install
npm start
```
Then open: `http://localhost:8000`

---

## 📋 Backend Setup (Optional - For Full Stack)

### Prerequisites
- Node.js 14+
- MongoDB (or remove DB integration for in-memory storage)

### Step 1: Install Dependencies
```bash
npm install express cors dotenv mongoose
```

### Step 2: Create .env file
```bash
echo "PORT=3000" > .env
echo "MONGO_URI=mongodb://localhost:27017/claims_db" >> .env
```

### Step 3: Run Backend Server
```bash
node src/server.js
```

Backend will run at: `http://localhost:3000`

### Step 4: Update API Base URL
Edit `config.json` and change:
```json
"api": {
  "baseUrl": "http://localhost:3000/api"
}
```

---

## 📁 Project Structure Overview

```
projectAI2/
├── index.html              # Main application
├── config.json            # Configuration file
├── package.json           # Project metadata
├── README.md              # Full documentation
├── API_ENDPOINTS.md       # Backend API specs
├── QUICK_START.md         # This file
├── .gitignore            # Git ignore rules
│
├── css/
│   ├── styles.css        # Main styles
│   └── dashboard.css     # Dashboard specific
│
├── js/
│   ├── app.js            # Main app logic
│   ├── dashboard.js      # Dashboard features
│   └── claims.js         # Claims management
│
├── src/
│   └── server.js         # Backend example
│
└── assets/
    └── logo.svg          # Logo file
```

---

## 🎯 Features Demo

### Dashboard
1. Open http://localhost:8000
2. Click "Dashboard" in navigation
3. View real-time metrics and charts

### Create a Claim
1. Click "+ New Claim" button
2. Fill in claim details
3. Submit claim
4. View in Claims table

### Search & Filter
1. Go to Claims section
2. Use search box to find claims
3. Filter by status dropdown

### AI Analysis
- Claims automatically get AI scores (0-100)
- Red flag for low scores
- Recommendations shown in insights

### Settings
1. Click "Settings" in navigation
2. Adjust AI threshold
3. Toggle notifications
4. Save changes

---

## 🔧 Configuration

Edit `config.json` to customize:

```json
{
  "ai": {
    "thresholds": {
      "approval": 0.85,
      "review": 0.60,
      "rejection": 0.30
    }
  },
  "tunneling": {
    "enabled": true,
    "protocol": "tls"
  }
}
```

---

## 🧪 Testing

### Mock Data
- Application generates 12 sample claims on first load
- Data persists in browser's localStorage

### Test Analytics
- Navigate to Analytics section
- View performance metrics
- Download sample reports

### Test Workflows
1. Create claim → Processing
2. Click View on any claim
3. Create multiple claims
4. Use search/filter features

---

## 🐛 Troubleshooting

### Claims Table Empty
- Clear browser cache (Ctrl+Shift+Delete or Cmd+Shift+Delete)
- Reset localStorage:
  ```javascript
  localStorage.clear()
  location.reload()
  ```

### Server Not Found
- Check if server is running on correct port
- Verify firewall allows port 8000 or 3000
- Try `localhost` or `127.0.0.1`

### Charts Not Showing
- Charts are rendered as SVG elements
- Check console for errors (F12 → Console)
- Ensure JavaScript is enabled

### Data Not Persisting
- localStorage must be enabled
- Try different browser if issues persist
- Check privacy/incognito mode

---

## 📊 Database Connection (MongoDB Example)

If using MongoDB:

```javascript
// In server.js
const mongoose = require('mongoose');

mongoose.connect(process.env.MONGO_URI);

// Define schema
const claimSchema = new mongoose.Schema({
  id: String,
  customer: String,
  amount: Number,
  status: String,
  aiScore: Number,
  createdAt: { type: Date, default: Date.now }
});

const Claim = mongoose.model('Claim', claimSchema);
```

---

## 🚀 Production Deployment

### Frontend (Static Files)
- Upload to AWS S3 + CloudFront
- Or: Netlify, Vercel, GitHub Pages
- Or: Traditional web hosting

### Backend (Node.js)
- Deploy to: Heroku, AWS EC2, DigitalOcean, Vercel
- Use PM2 for process management
- Set up SSL/TLS certificates

### Database
- MongoDB Atlas (cloud)
- AWS RDS
- Firebase Firestore

### Example Heroku Deployment
```bash
heroku login
heroku create tunneling-claim-watch-ai
heroku config:set MONGO_URI=mongodb://...
git push heroku main
```

---

## 📱 Mobile Testing

The app is fully responsive. Test on mobile:
1. Chrome DevTools: F12 → Toggle device toolbar
2. Or access from actual phone: `http://yourip:8000`

---

## 🔐 Security Checklist

Before production:

- [ ] Enable HTTPS
- [ ] Implement authentication
- [ ] Add CORS restrictions
- [ ] Rate limiting enabled
- [ ] Valid SSL certificates
- [ ] Environment variables (.env)
- [ ] Remove debug logs
- [ ] Enable HSTS headers
- [ ] Input validation
- [ ] SQL injection prevention

---

## 📚 Additional Resources

- [Express.js Documentation](https://expressjs.com/)
- [MongoDB Documentation](https://docs.mongodb.com/)
- [MDN Web Docs](https://developer.mozilla.org/)
- [Web Security Best Practices](https://owasp.org/)

---

## 💡 Tips & Tricks

### Browser Developer Tools
```javascript
// Check app state in console
window.app.claims
window.app.currentUser

// Access managers
window.dashboardManager
window.claimsManager
window.aiInsights
```

### Simulate API Calls
```javascript
// Fetch claims from API
fetch('http://localhost:3000/api/claims')
  .then(r => r.json())
  .then(data => console.log(data));
```

### Export Data
- Use DevTools → Application → LocalStorage
- Copy JSON data for backup/analysis

---

## 🎓 Learning Path

1. **Understand the UI** - Explore all features
2. **Review HTML** - Understand structure (index.html)
3. **Learn CSS** - Check styling (css/styles.css)
4. **Study JavaScript** - Core logic (js/app.js)
5. **Explore Backend** - API example (src/server.js)
6. **Deploy** - Follow production guide above

---

## ❓ FAQ

**Q: Can I use this without a backend?**
A: Yes! The frontend works standalone with localStorage.

**Q: How do I connect my real API?**
A: Update `config.json` baseUrl and modify API calls in js/app.js

**Q: Is this production-ready?**
A: It's a foundation. Add authentication, validation, and error handling before production.

**Q: Can I modify the UI?**
A: Absolutely! Edit CSS and HTML to match your brand.

**Q: Do I need Docker?**
A: Not required, but helpful for consistent environments.

---

**Happy coding! 🎉**

For questions or issues, check the README.md or open an issue on GitHub.
