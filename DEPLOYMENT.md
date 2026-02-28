# Deployment Guide - Tunneling Claim Watch AI

## 📦 Pre-Deployment Checklist

### Frontend Optimization
- [ ] Minify CSS files
- [ ] Minify JavaScript files
- [ ] Optimize images/SVG
- [ ] Update config.json with production URLs
- [ ] Test all browser compatibility
- [ ] Run lighthouse audit
- [ ] Test on mobile devices
- [ ] Check accessibility (A11y)

### Backend Optimization
- [ ] Add input validation
- [ ] Implement error handling
- [ ] Add logging middleware
- [ ] Enable Rate limiting
- [ ] Add API documentation
- [ ] Set up monitoring
- [ ] Configure CORS properly
- [ ] Enable compression

---

## 🌐 Deployment Options

### Option 1: Netlify (Recommended for Frontend)

```bash
# 1. Install Netlify CLI
npm install -g netlify-cli

# 2. Deploy
netlify deploy --prod --dir=.

# 3. Set environment variables in Netlify UI
```

### Option 2: Vercel

```bash
# 1. Install Vercel CLI
npm install -g vercel

# 2. Deploy
vercel --prod

# 3. Configure API routes in vercel.json
```

### Option 3: GitHub Pages

```bash
# 1. Create gh-pages branch
git checkout -b gh-pages

# 2. Push to GitHub
git push origin gh-pages

# 3. Enable GitHub Pages in repository settings
```

### Option 4: AWS (Full Stack)

#### Frontend on S3 + CloudFront
```bash
# 1. Create S3 bucket (static-website)
aws s3 mb s3://your-domain-name

# 2. Enable static website hosting
aws s3 website s3://your-domain-name \
  --index-document index.html \
  --error-document error.html

# 3. Upload files
aws s3 sync . s3://your-domain-name --exclude ".git*"

# 4. Set up CloudFront distribution for CDN
```

#### Backend on EC2 with Node.js
```bash
# 1. Launch EC2 instance
# 2. SSH into instance
ssh -i your-key.pem ec2-user@your-instance-ip

# 3. Install Node.js
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install node

# 4. Clone repository
git clone your-repo
cd projectAI2

# 5. Install dependencies
npm install

# 6. Create .env file
echo "PORT=3000" > .env
echo "MONGO_URI=your-mongodb-connection-string" >> .env

# 7. Start with PM2
npm install -g pm2
pm2 start src/server.js
pm2 startup
pm2 save

# 8. Set up Nginx reverse proxy
# See Nginx configuration below
```

### Option 5: Heroku (Quick Backend Deployment)

```bash
# 1. Install Heroku CLI
npm install -g heroku

# 2. Login
heroku login

# 3. Create app
heroku create your-app-name

# 4. Set environment variables
heroku config:set MONGO_URI=mongodb+srv://...

# 5. Deploy
git push heroku main

# 6. View logs
heroku logs --tail
```

---

## 🔐 Security Configuration

### HTTPS/SSL Setup

#### Using Let's Encrypt (Free)
```bash
# 1. Install Certbot
sudo apt-get install certbot python3-certbot-nginx

# 2. Get certificate
sudo certbot certonly --nginx -d your-domain.com

# 3. Auto-renewal
sudo systemctl enable certbot.timer
```

#### Using AWS Certificate Manager
```bash
# 1. Request certificate in ACM
# 2. Validate domain ownership
# 3. Associate with CloudFront/ALB
```

---

## 🚀 Nginx Configuration (Reverse Proxy)

Create `/etc/nginx/sites-available/default`:

```nginx
server {
    listen 80;
    server_name your-domain.com;
    
    # Redirect to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name your-domain.com;
    
    # SSL certificates
    ssl_certificate /etc/letsencrypt/live/your-domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/your-domain.com/privkey.pem;
    
    # Security headers
    add_header Strict-Transport-Security "max-age=31536000" always;
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header Referrer-Policy "no-referrer-when-downgrade" always;
    add_header Content-Security-Policy "default-src 'self' https: data: 'unsafe-inline'" always;
    
    # Gzip compression
    gzip on;
    gzip_vary on;
    gzip_types text/plain text/css text/javascript application/json application/javascript;
    
    # Frontend static files
    location / {
        alias /var/www/html/;
        try_files $uri /index.html;
    }
    
    # Backend API
    location /api/ {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

Enable config:
```bash
sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

---

## 📊 Monitoring & Logging

### Application Monitoring (PM2)
```bash
# 1. Install PM2
npm install -g pm2

# 2. Start app
pm2 start src/server.js --name "claims-api"

# 3. Monitor
pm2 monit

# 4. View logs
pm2 logs

# 5. Setup auto-restart
pm2 save
pm2 startup
```

### Error Tracking (Sentry)
```javascript
// In server.js
const Sentry = require("@sentry/node");

Sentry.init({ 
  dsn: process.env.SENTRY_DSN,
  tracesSampleRate: 1.0 
});

app.use(Sentry.Handlers.errorHandler());
```

### Logging (Winston)
```bash
npm install winston

# In server.js
const winston = require('winston');

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.json(),
  transports: [
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
    new winston.transports.File({ filename: 'combined.log' })
  ]
});
```

---

## 🚁 Database Deployment

### MongoDB Atlas (Cloud)
```bash
# 1. Create account at mongodb.com/cloud/atlas
# 2. Create cluster
# 3. Get connection string
# 4. Set in .env
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/dbname

# 5. Create indexes for performance
db.claims.createIndex({ status: 1 })
db.claims.createIndex({ customerId: 1 })
```

### PostgreSQL on AWS RDS
```bash
# 1. Create RDS instance in AWS Console
# 2. Get endpoint
# 3. Connect via psql or Prisma
# 4. Set in .env
DATABASE_URL=postgresql://user:pass@instance.rds.amazonaws.com:5432/dbname
```

---

## 🔄 CI/CD Pipeline (GitHub Actions)

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to Production

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Setup Node.js
      uses: actions/setup-node@v2
      with:
        node-version: '16'
    
    - name: Install dependencies
      run: npm ci
    
    - name: Run tests
      run: npm test
    
    - name: Deploy to production
      run: |
        echo "Deploying..."
        # Add your deployment command here
      env:
        DEPLOY_KEY: ${{ secrets.DEPLOY_KEY }}
```

---

## ⚡ Performance Optimization

### CDN Configuration
- Use CloudFront for AWS
- Use Cloudflare for DNS + CDN
- Cache static assets aggressively
- Set cache-control headers

### Database Optimization
```javascript
// Add indexes
db.claims.createIndex({ createdAt: -1 });
db.claims.createIndex({ status: 1, customerId: 1 });

// Use pagination
app.get('/api/claims', (req, res) => {
  const page = req.query.page || 1;
  const limit = 20;
  const skip = (page - 1) * limit;
  
  return Claim.find().skip(skip).limit(limit);
});
```

### Caching Strategy
```javascript
// Redis caching
const redis = require('redis');
const client = redis.createClient();

app.get('/api/analytics/dashboard', async (req, res) => {
  const cached = await client.get('dashboard-analytics');
  if (cached) return res.json(JSON.parse(cached));
  
  const data = await generateAnalytics();
  await client.setex('dashboard-analytics', 300, JSON.stringify(data));
  res.json(data);
});
```

---

## 📞 Post-Deployment

### Testing Checklist
- [ ] Test all features in production
- [ ] Check API response times
- [ ] Monitor error rates
- [ ] Verify SSL certificate
- [ ] Test on various devices
- [ ] Check SEO (meta tags)
- [ ] Performance audit (Lighthouse)
- [ ] Load test with k6 or JMeter

### Monitoring Setup
```bash
# 1. Setup uptime monitoring (UptimeRobot)
# 2. Setup error tracking (Sentry)
# 3. Setup performance monitoring (New Relic)
# 4. Setup logs aggregation (ELK Stack)
```

---

## 🆘 Rollback Procedure

```bash
# Using Git
git revert <commit-hash>
git push heroku main

# Using PM2
pm2 start old-version/src/server.js
pm2 delete new-version

# Using Docker
docker pull your-image:old-tag
docker stop current-container
docker run -d your-image:old-tag
```

---

## 💰 Cost Estimation (AWS)

| Service | Cost | Estimate |
|---------|------|----------|
| EC2 (t2.micro) | $0.0116/hour | ~$8.45/month |
| RDS (db.t2.micro) | $0.017/hour | ~$12.45/month |
| S3 Storage | $0.023/GB | Minimal |
| CloudFront | $0.085/GB | Depends on traffic |
| Total (startup) | - | ~$30-50/month |

---

**Deployment completed! Monitor your application regularly.**
