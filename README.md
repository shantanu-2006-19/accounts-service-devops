# DevOps Capstone Project - Accounts Service

[![CI Build](https://github.com/shantanu-2006-19/accounts-service-devops/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/shantanu-2006-19/accounts-service-devops/actions/workflows/ci-build.yaml)

A RESTful microservice for managing user accounts, built as part of the IBM DevOps and Software Engineering Professional Certificate capstone project.

## Project Overview

This repository demonstrates the end-to-end development, testing, and deployment lifecycle of a cloud-native microservice:
- **Test-Driven Development (TDD)** using `nosetests` and Python `coverage`.
- **Linting & Code Quality** enforced via `flake8` and `pylint`.
- **Security & Headers** configured via `Flask-Talisman` and `Flask-CORS`.
- **Continuous Integration (CI)** pipeline powered by GitHub Actions.
- **Containerization** with Docker running `gunicorn` under a non-root user.

---

## REST API Endpoints

| Method | Endpoint | Description | Status Codes |
| :--- | :--- | :--- | :--- |
| **GET** | `/` | Root URL / Health check | `200 OK` |
| **GET** | `/accounts` | List all accounts | `200 OK` |
| **POST** | `/accounts` | Create a new account | `201 Created`, `400 Bad Request` |
| **GET** | `/accounts/<id>` | Read an account by ID | `200 OK`, `404 Not Found` |
| **PUT** | `/accounts/<id>` | Update an account by ID | `200 OK`, `404 Not Found` |
| **DELETE**| `/accounts/<id>` | Delete an account by ID | `204 No Content` |
