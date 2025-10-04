# Custom Airflow Docker Image

A customized Apache Airflow worker Docker image with additional tools and packages for enhanced functionality.

## Features

- Based on official Apache Airflow 3.0.2 Python 3.11
- Additional system tools: build-essential, git, curl, vim
- Common Python packages: pandas, requests
- Configurable additional Python packages via requirements.txt
- Multi-architecture support (linux/amd64, linux/arm64)
- Automated builds and publishing to GitHub Container Registry

## Quick Start

### Using the Pre-built Image

Pull the latest image from GitHub Container Registry:

```bash
docker pull ghcr.io/speshak/airflow-image:latest
```

### Running Airflow

#### Standalone Mode (for development/testing)

```bash
docker run -p 8080:8080 ghcr.io/speshak/airflow-image:latest airflow standalone
```

Access the Airflow web UI at http://localhost:8080

#### Docker Compose (Recommended)

Create a `docker-compose.yml` file:

```yaml
version: '3.8'

services:
  airflow:
    image: ghcr.io/speshak/airflow-image:latest
    ports:
      - "8080:8080"
    environment:
      - AIRFLOW__CORE__EXECUTOR=LocalExecutor
      - AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=sqlite:////opt/airflow/airflow.db
    volumes:
      - ./dags:/opt/airflow/dags
      - ./logs:/opt/airflow/logs
      - ./plugins:/opt/airflow/plugins
    command: airflow standalone
```

Run with:
```bash
docker-compose up
```

## Customization

### Adding Python Packages

Edit `requirements.txt` to add your required Python packages, then rebuild the image.

### Adding DAGs and Plugins

Mount your local directories to the container:

- DAGs: Mount to `/opt/airflow/dags`
- Plugins: Mount to `/opt/airflow/plugins`
- Configuration: Mount to `/opt/airflow/config`

### Environment Variables

Key environment variables you can set:

- `AIRFLOW__CORE__LOAD_EXAMPLES=False` - Disable example DAGs (default)
- `AIRFLOW__WEBSERVER__EXPOSE_CONFIG=True` - Expose config in web UI (default)
- `AIRFLOW__WEBSERVER__ENABLE_PROXY_FIX=True` - Enable proxy fix (default)

## Building Locally

To build the image locally:

```bash
git clone https://github.com/speshak/airflow-image.git
cd airflow-image
docker build -t my-airflow-image .
```

## CI/CD

This repository includes GitHub Actions workflows that automatically:

- Build Docker images on push to main/develop branches
- Publish images to GitHub Container Registry
- Support semantic versioning via tags
- Build multi-architecture images (AMD64 and ARM64)

### Available Tags

- `latest` - Latest build from main branch
- `main` - Latest build from main branch
- `develop` - Latest build from develop branch
- `v*` - Semantic version tags (e.g., `v1.0.0`, `v1.0`, `v1`)

## Supported Architectures

- linux/amd64
- linux/arm64

## License

This project follows the same license as Apache Airflow.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test the Docker build
5. Submit a pull request
