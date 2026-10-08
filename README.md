# DevOps Pipeline

A containerized Flask web application with a complete CI/CD workflow using Docker, Docker Compose, GitHub Actions, automated testing, environment variables, health checks, monitoring, and cloud deployment.

## Technologies Used

- Python
- Flask
- Docker
- Docker Compose
- Nginx
- Git & GitHub
- GitHub Actions
- Pytest
- Render

## Project Features

- Containerized Flask web application using Docker
- Multi-container setup using Docker Compose
- Nginx configured as a reverse proxy
- Automated testing using Pytest
- CI/CD pipeline using GitHub Actions
- Environment variable configuration
- Docker container health checks
- Application monitoring and logging
- Cloud deployment on Render

## Project Setup

### Clone the Repository

```bash
git clone https://github.com/JavariaAfzal/devops-pipeline.git
cd devops-pipeline
```

### Build and Start the Application

```bash
docker compose up -d --build
```

The application is available locally at:

```text
http://localhost:5002
```

## Testing

Automated tests can be run using:

```bash
pytest
```

The same tests are also executed automatically through the GitHub Actions CI/CD pipeline.

## Environment Variables

The application supports the `APP_MESSAGE` environment variable.

Example:

```text
APP_MESSAGE=DevOps Pipeline Application is Running!
```

## Health Check

The application provides a health endpoint:

```text
http://localhost:5002/health
```

The Docker container also includes an automatic health check.

To verify the container status:

```bash
docker compose ps
```

The application container should show:

```text
healthy
```

## Monitoring and Logging

Application and container logs can be viewed using:

```bash
docker compose logs
```

The project also includes a monitoring service for the application.

## CI/CD Pipeline

The GitHub Actions workflow automatically:

- Checks out the repository
- Sets up Python
- Installs project dependencies
- Runs automated tests
- Completes the CI workflow

The workflow configuration is located at:

```text
.github/workflows/ci-cd.yml
```

## Deployment

The application is deployed using Docker on Render.

Live application:

https://devops-pipeline-fft0.onrender.com

## Repository

GitHub repository:

https://github.com/JavariaAfzal/devops-pipeline