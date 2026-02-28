/* 
 * Backend API Endpoints Documentation
 * This file documents the recommended backend API structure
 * for the Tunneling Claim Watch AI application
 */

// ============================================
// CLAIMS ENDPOINTS
// ============================================

/**
 * GET /api/claims
 * Retrieve all claims with optional pagination and filtering
 * Query Parameters:
 *   - page: number (default: 1)
 *   - limit: number (default: 10)
 *   - status: string ('pending', 'processing', 'resolved', 'rejected')
 *   - type: string ('medical', 'auto', 'property', 'other')
 *   - sortBy: string ('date', 'amount', 'aiScore')
 *   - sortOrder: string ('asc', 'desc')
 * Response: { success: boolean, data: Claim[], total: number, page: number }
 */

/**
 * POST /api/claims
 * Create a new claim
 * Body: {
 *   customer: string (required),
 *   type: string (required),
 *   amount: number (required),
 *   description: string (required),
 *   attachments?: File[]
 * }
 * Response: { success: boolean, data: ClaimWithId }
 */

/**
 * GET /api/claims/:id
 * Get detailed information about a specific claim
 * Response: { success: boolean, data: DetailedClaim }
 */

/**
 * PUT /api/claims/:id
 * Update a claim's information
 * Body: { status?: string, notes?: string, ... }
 * Response: { success: boolean, data: UpdatedClaim }
 */

/**
 * DELETE /api/claims/:id
 * Delete a claim
 * Response: { success: boolean, message: string }
 */

// ============================================
// AI ANALYSIS ENDPOINTS
// ============================================

/**
 * POST /api/ai/analyze
 * Perform AI analysis on a claim
 * Body: {
 *   claimId: string (required),
 *   includeAnomalyDetection?: boolean,
 *   includeFraudDetection?: boolean
 * }
 * Response: {
 *   success: boolean,
 *   data: {
 *     aiScore: number,
 *     recommendation: string,
 *     confidence: number,
 *     anomalies: string[],
 *     fraudRisk: number
 *   }
 * }
 */

/**
 * GET /api/ai/insights/:claimId
 * Get AI-generated insights for a claim
 * Response: {
 *   success: boolean,
 *   data: {
 *     patterns: string[],
 *     risks: RiskItem[],
 *     recommendations: string[],
 *     relatedClaims: string[]
 *   }
 * }
 */

/**
 * POST /api/ai/model/train
 * Train/retrain the AI model with recent data
 * Body: { dataSource: string, parameters: object }
 * Response: { success: boolean, trainingId: string }
 */

/**
 * GET /api/ai/model/status
 * Get current AI model status and metrics
 * Response: {
 *   success: boolean,
 *   data: {
 *     modelVersion: string,
 *     accuracy: number,
 *     lastTrained: string,
 *     status: string
 *   }
 * }
 */

// ============================================
// TUNNELING ENDPOINTS
// ============================================

/**
 * POST /api/tunnel/create
 * Create a secure tunnel for claim transmission
 * Body: {
 *   claimId: string,
 *   destination: string,
 *   priority?: string
 * }
 * Response: {
 *   success: boolean,
 *   data: {
 *     tunnelId: string,
 *     encryptionKey: string,
 *     token: string,
 *     expiresAt: string
 *   }
 * }
 */

/**
 * GET /api/tunnel/:tunnelId/status
 * Monitor tunnel status
 * Response: {
 *   success: boolean,
 *   data: {
 *     tunnelId: string,
 *     status: string ('active', 'closed', 'error'),
 *     bytesTransferred: number,
 *     createdAt: string,
 *     lastActivity: string
 *   }
 * }
 */

/**
 * POST /api/tunnel/:tunnelId/close
 * Close an active tunnel
 * Response: { success: boolean, message: string }
 */

/**
 * GET /api/tunnel/routes
 * Get available tunneling routes based on claim type
 * Query: { claimType: string }
 * Response: {
 *   success: boolean,
 *   data: {
 *     routes: RouteOption[],
 *     recommended: string
 *   }
 * }
 */

// ============================================
// ANALYTICS ENDPOINTS
// ============================================

/**
 * GET /api/analytics/dashboard
 * Get dashboard analytics data
 * Query: { timeframe: 'day', 'week', 'month', 'year' }
 * Response: {
 *   success: boolean,
 *   data: {
 *     totalClaims: number,
 *     activeClaims: number,
 *     resolvedClaims: number,
 *     averageProcessingTime: number,
 *     aiAccuracy: number
 *   }
 * }
 */

/**
 * GET /api/analytics/trends
 * Get claim trends over time
 * Query: { period: number (days), groupBy: 'day', 'week', 'month' }
 * Response: {
 *   success: boolean,
 *   data: TrendData[]
 * }
 */

/**
 * GET /api/analytics/performance
 * Get performance metrics for claims processing
 * Query: { timeframe: string }
 * Response: {
 *   success: boolean,
 *   data: {
 *     averageProcessingTime: number,
 *     successRate: number,
 *     rejectionRate: number,
 *     reviewRate: number
 *   }
 * }
 */

/**
 * POST /api/analytics/report
 * Generate a detailed analytics report
 * Body: {
 *   reportType: string ('summary', 'detailed', 'custom'),
 *   timeframe: string,
 *   filters: object
 * }
 * Response: {
 *   success: boolean,
 *   data: { reportId: string, downloadUrl: string }
 * }
 */

// ============================================
// USER MANAGEMENT ENDPOINTS
// ============================================

/**
 * GET /api/users/profile
 * Get current user profile
 * Response: { success: boolean, data: UserProfile }
 */

/**
 * PUT /api/users/profile
 * Update user profile
 * Body: { name?: string, email?: string, department?: string }
 * Response: { success: boolean, data: UpdatedUserProfile }
 */

/**
 * GET /api/users/settings
 * Get user settings and preferences
 * Response: { success: boolean, data: UserSettings }
 */

/**
 * PUT /api/users/settings
 * Update user settings
 * Body: { theme?: string, notifications?: object, ... }
 * Response: { success: boolean, data: UpdatedSettings }
 */

// ============================================
// AUTHENTICATION ENDPOINTS
// ============================================

/**
 * POST /api/auth/login
 * User login
 * Body: { email: string, password: string }
 * Response: { success: boolean, token: string, user: User }
 */

/**
 * POST /api/auth/logout
 * User logout
 * Response: { success: boolean }
 */

/**
 * POST /api/auth/refresh
 * Refresh authentication token
 * Body: { refreshToken: string }
 * Response: { success: boolean, token: string }
 */

/**
 * POST /api/auth/register
 * Register new user
 * Body: { email: string, password: string, name: string }
 * Response: { success: boolean, user: User, token: string }
 */

// ============================================
// ERROR RESPONSES
// ============================================

/**
 * All endpoints return error responses in this format:
 * {
 *   success: false,
 *   error: {
 *     code: string,
 *     message: string,
 *     details?: object
 *   }
 * }
 * 
 * Common HTTP Status Codes:
 * - 200 OK: Request succeeded
 * - 201 Created: Resource created successfully
 * - 400 Bad Request: Invalid request format
 * - 401 Unauthorized: Authentication required
 * - 403 Forbidden: Insufficient permissions
 * - 404 Not Found: Resource not found
 * - 429 Too Many Requests: Rate limit exceeded
 * - 500 Internal Server Error: Server error
 * - 503 Service Unavailable: Service temporarily unavailable
 */

// ============================================
// AUTHENTICATION HEADERS
// ============================================

/**
 * All authenticated requests require:
 * Authorization: Bearer <JWT_TOKEN>
 * Content-Type: application/json
 */

// ============================================
// WEBHOOK EVENTS
// ============================================

/**
 * Supported webhook events:
 * - claim.created
 * - claim.updated
 * - claim.resolved
 * - claim.rejected
 * - analysis.completed
 * - tunnel.created
 * - tunnel.closed
 * - error.occurred
 */

// ============================================
// RATE LIMITING
// ============================================

/**
 * Rate limits (per minute):
 * - Authenticated users: 100 requests
 * - Public endpoints: 10 requests
 * - AI analysis endpoints: 20 requests
 * 
 * Headers returned:
 * - X-RateLimit-Limit: Maximum requests allowed
 * - X-RateLimit-Remaining: Requests remaining
 * - X-RateLimit-Reset: Unix timestamp when limit resets
 */
