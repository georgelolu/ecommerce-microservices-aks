# E-Commerce Microservices on Azure Kubernetes Service

A cloud-native e-commerce demonstration project that packages application
components into Docker images and deploys them to Azure Kubernetes Service
(AKS) using GitHub Actions.

## Project Overview

The application consists of a static web frontend and three Python FastAPI
microservices:

- **Frontend:** Nginx-based web interface.
- **Product service:** Product-related API.
- **Order service:** Order-related API.
- **Inventory service:** Inventory-related API.

The application images are stored in Azure Container Registry (ACR).
Kubernetes runs the application in the `ecommerce` namespace.

## Architecture

```text
Developer
   |
   v
GitHub Repository
   |
   v
GitHub Actions
   |
   +--> Run Python service tests
   |
   +--> Authenticate to Azure using OIDC
   |
   +--> Build Docker images
   |
   +--> Push images to Azure Container Registry
   |
   +--> Update Kubernetes deployments
   |
   v
Azure Kubernetes Service
   |
   +--> Nginx Frontend
   +--> Product API
   +--> Order API
   +--> Inventory API
Technology Stack
AreaTechnology
Cloud platformMicrosoft Azure
ContainerizationDocker
Container registryAzure Container Registry
OrchestrationAzure Kubernetes Service
CI/CDGitHub Actions
Cloud authenticationMicrosoft Entra ID and OpenID Connect
Application services/Python and FastAPI
FrontendNginx
Testingpytest
Deployment permissionsKubernetes RBAC
Continuous Integration and Deployment
The GitHub Actions workflow is located at
.github/workflows/ci.yml.
The pipeline:
1. Checks out the repository.
2. Installs Python dependencies.
3. Runs tests for the product, order, and inventory services.
4. Authenticates to Azure using OpenID Connect (OIDC).
5. Builds and pushes the frontend and microservice images to ACR.
6. Obtains AKS credentials and verifies deployment permissions.
7. Updates Kubernetes deployments with images tagged to the Git commit.
8. Checks rollout status for the four deployments.
The workflow is configured to run tests on pushes and pull requests targeting
main. Deployment is intended for application or Kubernetes changes pushed
to main, after the tests pass.
Documentation-only changes should not trigger an AKS deployment.
Security
- Uses OIDC federation instead of a long-lived Azure client secret.
- Uses Azure role assignments for registry and cluster access.
- Uses namespace-scoped Kubernetes RBAC for deployment operations.
- Uses Git commit SHA tags to identify built container images.
Repository Structure
.
├── .github/
│   └── workflows/
│       └── ci.yml
├── docs/
│   ├── ARCHITECTURE_AND_INTERVIEW_GUIDE.md
│   └── evidence/
├── frontend/
├── k8s/
│   └── rbac/
├── services/
│   ├── product/
│   ├── order/
│   └── inventory/
└── README.md


Documentation
See Architecture and Interview Guide
for the detailed architecture, deployment workflow, security decisions,
verification notes, limitations, and an interview-ready project walkthrough.
Current Infrastructure Status
The AKS cluster may be stopped when not in use to reduce compute costs.
A deployment job requires the cluster to be running. Documentation changes
do not require starting or modifying Azure infrastructure.
Stopping AKS does not mean every associated Azure resource is free; review
the costs of retained resources such as container registries and networking.
Future Improvements
- Add persistent storage for application data.
- Add integration and end-to-end tests.
- Introduce HTTPS ingress and TLS certificates.
- Add centralized logging, metrics, and alerting.
- Implement autoscaling and stronger image security checks.
- Add deployment approvals and rollback procedures.
Author
George Lolu
- GitHub: https://github.com/georgelolu
