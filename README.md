
# Access Management Service

This repository contains the **Notification Management Service**, an independent microservice implemented as a [Fission](https://fission.io/) function. It notification capabilities and is designed following **Domain-Driven Design (DDD)** principles along with the **Repository** and **Service** patterns.

---

## 📁 Project Structure

``` bash
notification_management/
├── application/        # Commands and service logic
├── domain/             # Aggregates, value objects, domain events
├── handlers/           # Command and event handlers
├── infrastructure/     # ORM models and other infra details, repositories
├── interfaces/         # Interfaces for external interactions
├── main.py             # Entry point for the function
├── requirements.txt    # Dependencies
shared/                 # Shared abstractions (DB, messaging, etc.)
specs/                  # Fission deployment configs and routes
```

---

## Architecture patterns used

### Domain-Driven Design (DDD)

* Domain layer contains aggregates, entities, value objects, and events.
* Business logic is encapsulated in aggregates like `Notification`.

### Repository Pattern

* Abstracts data access via repository interfaces and implementations like `notification_repository.py`.

### Service Pattern

* Encapsulates application-specific logic in `services/notification_service.py`.

---

## 🚀 Fission Deployment

The `specs/` directory contains the YAML specifications to deploy this service as a Fission function:

* `function-notification-management-consumer.yaml`: Registers the function.
* `mqtrigger-notification-trigger.yaml`: Triggers consumer function from response topic
* `fission-deployment-config.yaml`: Additional deployment configuration.

Deploy all resources using:
> ***Note***: Its already been automated in `deploy.sh`file. Just run `deploy.sh` from project's root directory.
```bash
fission spec apply --specdir specs
```

## 📄 Example Event Flow (Sending Notification)

1. Handler receives the event as http request body in fission main function.
2. Handler delegates to `NotificationService`
3. Service constructs and persists domain aggregate

## Deployment

For deployment, go to the shared submodule and check document [running_locally](./shared/docs/running_locally.md) file.

---
