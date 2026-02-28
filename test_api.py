"""
Test Script - Test all API endpoints
Run this after starting the backend: python test_api.py
"""

import requests
import json
import time
from pprint import pprint

BASE_URL = "http://localhost:5000/api"

class APITester:
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = {"Content-Type": "application/json"}
        self.test_token = None
        self.test_claim_id = None
    
    def test_health(self):
        """Test health check"""
        print("\n" + "="*50)
        print("Testing: Health Check")
        print("="*50)
        
        response = requests.get(f"{self.base_url.split('/api')[0]}/api/health")
        print(f"Status: {response.status_code}")
        pprint(response.json())
        return response.status_code == 200
    
    def test_get_claims(self):
        """Test getting claims"""
        print("\n" + "="*50)
        print("Testing: Get All Claims")
        print("="*50)
        
        response = requests.get(f"{self.base_url}/claims")
        print(f"Status: {response.status_code}")
        data = response.json()
        print(f"Total claims: {data['data'][0] if data['data'] else 0}")
        if data['data']:
            self.test_claim_id = data['data'][0]['id']
            print(f"First claim ID: {self.test_claim_id}")
        return response.status_code == 200
    
    def test_create_claim(self):
        """Test creating a claim"""
        print("\n" + "="*50)
        print("Testing: Create Claim")
        print("="*50)
        
        payload = {
            "customer": "Test Customer",
            "claim_type": "medical",
            "amount": 5000,
            "description": "This is a test claim for API testing"
        }
        
        response = requests.post(
            f"{self.base_url}/claims",
            headers=self.headers,
            json=payload
        )
        print(f"Status: {response.status_code}")
        data = response.json()
        pprint(data)
        
        if data['success']:
            self.test_claim_id = data['data']['id']
            print(f"Created claim: {self.test_claim_id}")
        
        return response.status_code == 201
    
    def test_get_claim_details(self):
        """Test getting specific claim"""
        if not self.test_claim_id:
            print("Skipping: No claim ID")
            return False
        
        print("\n" + "="*50)
        print(f"Testing: Get Claim Details ({self.test_claim_id})")
        print("="*50)
        
        response = requests.get(f"{self.base_url}/claims/{self.test_claim_id}")
        print(f"Status: {response.status_code}")
        pprint(response.json())
        return response.status_code == 200
    
    def test_ai_analyze(self):
        """Test AI analysis"""
        if not self.test_claim_id:
            print("Skipping: No claim ID")
            return False
        
        print("\n" + "="*50)
        print("Testing: AI Analysis")
        print("="*50)
        
        payload = {"claim_id": self.test_claim_id}
        response = requests.post(
            f"{self.base_url}/ai/analyze",
            headers=self.headers,
            json=payload
        )
        print(f"Status: {response.status_code}")
        pprint(response.json())
        return response.status_code == 200
    
    def test_ai_insights(self):
        """Test AI insights"""
        if not self.test_claim_id:
            print("Skipping: No claim ID")
            return False
        
        print("\n" + "="*50)
        print("Testing: AI Insights")
        print("="*50)
        
        response = requests.get(f"{self.base_url}/ai/insights/{self.test_claim_id}")
        print(f"Status: {response.status_code}")
        pprint(response.json())
        return response.status_code == 200
    
    def test_tunnel_create(self):
        """Test tunnel creation"""
        if not self.test_claim_id:
            print("Skipping: No claim ID")
            return False
        
        print("\n" + "="*50)
        print("Testing: Create Tunnel")
        print("="*50)
        
        payload = {"claim_id": self.test_claim_id}
        response = requests.post(
            f"{self.base_url}/tunnel/create",
            headers=self.headers,
            json=payload
        )
        print(f"Status: {response.status_code}")
        data = response.json()
        pprint(data)
        return response.status_code == 201
    
    def test_analytics_dashboard(self):
        """Test analytics dashboard"""
        print("\n" + "="*50)
        print("Testing: Analytics Dashboard")
        print("="*50)
        
        response = requests.get(f"{self.base_url}/analytics/dashboard")
        print(f"Status: {response.status_code}")
        pprint(response.json())
        return response.status_code == 200
    
    def test_analytics_trends(self):
        """Test analytics trends"""
        print("\n" + "="*50)
        print("Testing: Analytics Trends")
        print("="*50)
        
        response = requests.get(f"{self.base_url}/analytics/trends")
        print(f"Status: {response.status_code}")
        data = response.json()
        print(f"Trend data points: {len(data['data'])}")
        print("Sample data:")
        pprint(data['data'][:3])
        return response.status_code == 200
    
    def test_auth_register(self):
        """Test user registration"""
        print("\n" + "="*50)
        print("Testing: User Registration")
        print("="*50)
        
        payload = {
            "email": "testuser@example.com",
            "password": "testpass123",
            "name": "Test User"
        }
        
        response = requests.post(
            f"{self.base_url}/auth/register",
            headers=self.headers,
            json=payload
        )
        print(f"Status: {response.status_code}")
        pprint(response.json())
        return response.status_code in [201, 409]  # 409 if already exists
    
    def test_auth_login(self):
        """Test user login"""
        print("\n" + "="*50)
        print("Testing: User Login")
        print("="*50)
        
        payload = {
            "email": "user@example.com",
            "password": "password123"
        }
        
        response = requests.post(
            f"{self.base_url}/auth/login",
            headers=self.headers,
            json=payload
        )
        print(f"Status: {response.status_code}")
        data = response.json()
        pprint(data)
        
        if data['success']:
            self.test_token = data['data']['token']
            print(f"Login token: {self.test_token[:20]}...")
        
        return response.status_code == 200
    
    def test_search_claims(self):
        """Test claim search"""
        print("\n" + "="*50)
        print("Testing: Search Claims")
        print("="*50)
        
        response = requests.get(
            f"{self.base_url}/claims/search",
            params={"q": "medical"}
        )
        print(f"Status: {response.status_code}")
        data = response.json()
        print(f"Results found: {data['total']}")
        return response.status_code == 200

    def test_users_get_profile(self):
        """Test getting current user profile"""
        if not self.test_token:
            print("Skipping: No auth token")
            return False

        print("\n" + "=" * 50)
        print("Testing: Get User Profile")
        print("=" * 50)

        headers = {**self.headers, "Authorization": f"Bearer {self.test_token}"}
        response = requests.get(f"{self.base_url}/users/profile", headers=headers)
        print(f"Status: {response.status_code}")
        pprint(response.json())
        return response.status_code == 200

    def test_users_get_settings(self):
        """Test getting user settings"""
        if not self.test_token:
            print("Skipping: No auth token")
            return False

        print("\n" + "=" * 50)
        print("Testing: Get User Settings")
        print("=" * 50)

        headers = {**self.headers, "Authorization": f"Bearer {self.test_token}"}
        response = requests.get(f"{self.base_url}/users/settings", headers=headers)
        print(f"Status: {response.status_code}")
        pprint(response.json())
        return response.status_code == 200
    
    def run_all_tests(self):
        """Run all tests"""
        print("\n" + "🚀"*25)
        print("RUNNING ALL API TESTS")
        print("🚀"*25)
        
        tests = [
            ("Health Check", self.test_health),
            ("Get Claims", self.test_get_claims),
            ("Create Claim", self.test_create_claim),
            ("Get Claim Details", self.test_get_claim_details),
            ("AI Analyze", self.test_ai_analyze),
            ("AI Insights", self.test_ai_insights),
            ("Create Tunnel", self.test_tunnel_create),
            ("Analytics Dashboard", self.test_analytics_dashboard),
            ("Analytics Trends", self.test_analytics_trends),
            ("User Login", self.test_auth_login),
            ("Get User Profile", self.test_users_get_profile),
            ("Get User Settings", self.test_users_get_settings),
            ("Search Claims", self.test_search_claims),
        ]
        
        results = []
        passed = 0
        failed = 0
        
        for test_name, test_func in tests:
            try:
                result = test_func()
                results.append((test_name, "✅ PASSED" if result else "❌ FAILED"))
                passed += 1 if result else 0
                failed += 1 if not result else 0
            except Exception as e:
                results.append((test_name, f"❌ ERROR: {str(e)[:50]}"))
                failed += 1
            
            time.sleep(0.5)  # Small delay between requests
        
        # Print summary
        print("\n" + "="*50)
        print("TEST SUMMARY")
        print("="*50)
        for test_name, result in results:
            print(f"{test_name:.<40} {result}")
        
        print(f"\nTotal: {passed + failed} | Passed: {passed} | Failed: {failed}")
        print("="*50)

if __name__ == "__main__":
    print("\n⏳ Starting API tests...")
    print("Make sure the backend is running: python main.py\n")
    
    tester = APITester()
    
    try:
        tester.run_all_tests()
    except requests.exceptions.ConnectionError:
        print("\n❌ ERROR: Could not connect to backend!")
        print("Make sure to run: python main.py")
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
