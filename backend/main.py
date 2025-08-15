"""
FastAPI backend for AI Consulting Company website
"""
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="AI Consulting API",
    description="Backend API for AI Consulting Company website",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Next.js dev server
        "https://your-frontend-app.herokuapp.com",  # Production frontend
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "AI Consulting API is running"}

@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    return {
        "status": "healthy",
        "service": "ai-consulting-api",
        "version": "1.0.0"
    }

@app.get("/api/info")
async def get_info():
    """Basic info endpoint"""
    return {
        "company": "AI Consulting Company",
        "services": [
            "AI Strategy Consulting",
            "Custom AI Solutions",
            "AI Implementation",
            "Data Analytics"
        ],
        "api_version": "1.0.0",
        "environment": os.getenv("ENVIRONMENT", "development")
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
