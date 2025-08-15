# AI Consulting Company Website

A modern full-stack web application built with FastAPI (backend) and Next.js (frontend) for an AI consulting company.

## Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: Next.js 15 with TypeScript
- **Styling**: Tailwind CSS
- **Development**: Docker & Docker Compose
- **Deployment**: Heroku

## Getting Started

### Prerequisites

- Node.js 18+
- Python 3.11+
- Docker & Docker Compose

### Local Development

1. **Clone and navigate to the project:**
   ```bash
   cd website
   ```

2. **Option A: Using Docker (Recommended)**
   ```bash
   # Build and start all services
   cd docker
   docker-compose -f docker-compose.dev.yml up --build
   ```

3. **Option B: Manual setup**

   **Backend:**
   ```bash
   cd backend
   pip install -r requirements.txt
   python main.py
   ```

   **Frontend:**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

### Access the Application

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## Project Structure

```
website/
├── backend/              # FastAPI backend
│   ├── app/
│   │   ├── api/         # API routes
│   │   ├── core/        # Configuration
│   │   └── models/      # Data models
│   ├── main.py          # Application entry point
│   ├── requirements.txt # Python dependencies
│   └── Dockerfile
├── frontend/            # Next.js frontend
│   ├── src/
│   │   ├── app/        # App router pages
│   │   ├── lib/        # Utilities and API client
│   │   └── components/ # React components
│   ├── package.json
│   └── Dockerfile
├── docker/              # Docker configuration
│   ├── docker-compose.yml
│   └── docker-compose.dev.yml
└── .docs/              # Documentation
    └── TODO.md         # Development roadmap
```

## Development Stages

This project is being developed in stages:

1. ✅ **Stage 1**: Skeleton Application Setup
2. 🔄 **Stage 2**: Core Website Structure
3. ⏳ **Stage 3**: Component Migration
4. ⏳ **Stage 4**: AI-Powered Features
5. ⏳ **Stage 5**: Performance & Production

See `.docs/TODO.md` for detailed development plan.

## API Endpoints

### Current Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /api/info` - Company information

### Frontend Features

- **System Status**: Real-time backend connection status
- **Service Display**: Dynamic service listing from API
- **Responsive Design**: Mobile-first approach
- **Dark Mode**: Automatic dark mode support

## Next Steps

1. Add more API endpoints for services
2. Implement contact form
3. Add service detail pages
4. Integrate AI-powered features
5. Deploy to Heroku

## Contributing

1. Follow the development stages outlined in TODO.md
2. Ensure all tests pass before committing
3. Use conventional commits for version control
4. Update documentation as needed

## Deployment

Instructions for Heroku deployment will be added in Stage 1 completion.
