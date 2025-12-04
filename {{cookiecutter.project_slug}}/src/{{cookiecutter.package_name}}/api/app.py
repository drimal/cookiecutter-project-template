"""FastAPI application for {{ cookiecutter.project_name }}

{% if cookiecutter.include_api == "yes" %}
This module provides REST API functionality.
{% endif %}
"""

from fastapi import FastAPI

app = FastAPI(
    title="{{ cookiecutter.project_name }}",
    description="API for {{ cookiecutter.project_name }}",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
