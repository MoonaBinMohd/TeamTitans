"""
Tunneling Claim Watch AI - Python Backend
Main Flask Application
"""

import os
import sys
from datetime import datetime
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configuration
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['DEBUG'] = os.getenv('FLASK_ENV') == 'development'
app.config['JSON_SORT_KEYS'] = False

# Import blueprints
from routes.claims import claims_bp
from routes.ai import ai_bp
from routes.tunneling import tunneling_bp
from routes.analytics import analytics_bp
from routes.auth import auth_bp
from routes.users import users_bp

# Register blueprints
app.register_blueprint(claims_bp, url_prefix='/api/claims')
app.register_blueprint(ai_bp, url_prefix='/api/ai')
app.register_blueprint(tunneling_bp, url_prefix='/api/tunnel')
app.register_blueprint(analytics_bp, url_prefix='/api/analytics')
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(users_bp, url_prefix='/api/users')

# Global error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': {
            'code': 'NOT_FOUND',
            'message': 'Route not found'
        }
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'success': False,
        'error': {
            'code': 'INTERNAL_ERROR',
            'message': 'Internal server error',
            'details': str(error) if app.debug else None
        }
    }), 500

@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        'success': False,
        'error': {
            'code': 'BAD_REQUEST',
            'message': 'Invalid request format'
        }
    }), 400

# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'success': True,
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    }), 200

# Root endpoint
@app.route('/', methods=['GET'])
def root():
    return jsonify({
        'success': True,
        'message': 'Tunneling Claim Watch AI API',
        'version': '1.0.0',
        'endpoints': {
            'health': '/api/health',
            'claims': '/api/claims',
            'ai': '/api/ai',
            'tunneling': '/api/tunnel',
            'analytics': '/api/analytics',
            'auth': '/api/auth',
            'users': '/api/users'
        }
    }), 200

# Request logging middleware
@app.before_request
def log_request():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {request.method} {request.path}")

@app.after_request
def log_response(response):
    print(f"Response: {response.status_code}")
    return response

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    host = os.getenv('HOST', '0.0.0.0')
    
    print(f"\n{'='*50}")
    print(f"Tunneling Claim Watch AI - Python Backend")
    print(f"{'='*50}")
    print(f"Running on http://{host}:{port}")
    print(f"Environment: {os.getenv('FLASK_ENV', 'development')}")
    print(f"{'='*50}\n")
    
    app.run(host=host, port=port, debug=app.config['DEBUG'])
