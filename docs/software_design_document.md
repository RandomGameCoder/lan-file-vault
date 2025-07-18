# 🧾 Software Design Document: lan-file-vault

## 1. Overview

### Purpose:

A secure, cross-platform application to upload and view media files (images/videos) over local Wi-Fi. The backend runs on a laptop and only starts on trusted networks. Clients auto-discover the server, authenticate, and interact with the shared storage.

### Goals:

- Fast and secure file sharing within local networks
- Device authentication
- Shared mount support across Linux and Windows
- Developer-friendly (Docker, REST API)
- Open-source and modular

## 2. System Architecture

```text
+------------------+         mDNS         +------------------+
|  Client (Mobile) | <------------------> |  Server (FastAPI)|
| or Desktop App   |       HTTP+JWT       |     (Dockerized) |
+------------------+                     +------------------+
        |                                         |
        |       Media File Upload/Download       |
        +------------------------>---------------+
                                 Shared Mount (/mnt/shared)
```

## 3. Core Modules

**A. Server (FastAPI + Docker)**

| Component           | Description                                    |
|---------------------|------------------------------------------------|
| `main.py`           | App entrypoint, routes, startup hooks          |
| `auth.py`           | JWT token generation, login, registration      |
| `upload.py`         | File upload and listing endpoints              |
| `discovery.py`      | mDNS (zeroconf) server advertisement           |
| `network_check.py`  | Verifies SSID (runs only on trusted networks)  |
| `config.py`         | App configs, env vars, path settings           |
| `Dockerfile`        | Containerizes the server                       |
| `requirements.txt`  | Python dependencies                            |

**B. Client (Flutter)**

| Module               | File / Folder                           | Description                                                 |
|----------------------|-----------------------------------------|-------------------------------------------------------------|
| **Main App Entry**   | `main.dart`                             | Initializes app, routing, theme                             |
| **Authentication**   | `lib/screens/login_screen.dart`         | Login form + API call to get JWT                            |
|                      | `lib/services/auth_service.dart`        | Handles login, token storage, headers                       |
| **Server Discovery** | `lib/services/discovery_service.dart`   | Uses mDNS to find the server IP                             |
| **API Client**       | `lib/services/api_client.dart`          | Handles all REST API calls (login, upload, list, download)  |
| **Upload**           | `lib/screens/upload_screen.dart`        | UI to pick and upload media files                           |
|                      | `lib/services/file_picker_service.dart` | Abstracts file picking logic                                |
| **Media Listing**    | `lib/screens/home_screen.dart`          | Shows list of uploaded media (GET `/files`)                 |
|                      | `lib/models/file_model.dart`            | Model class for media files                                 |
| **Media Viewer**     | `lib/screens/media_viewer.dart`         | View full image/video using Flutter widgets                 |
| **Config**           | `lib/config.dart`                       | App-level constants (e.g. port, mDNS type, file size limit) |
| **Token Storage**    | `shared_preferences` package            | Securely store JWT token across sessions                    |
| **Utils / Helpers**  | `lib/utils/logger.dart` *(optional)*    | Simple logging or error parsing                             |
| **Routing**          | `lib/app_router.dart` *(optional)*      | Centralize app navigation routes                            |


## 4. Data Flow

- Client starts and discovers server via mDNS
- Client sends login credentials → receives JWT
- Client uploads media files via POST /upload/
- Server saves file to shared mount
- Clients can list and view media from GET /files/

## 5. Endpoints (REST API)

|Method  | Endpoint         | Description              | Auth  |
|--------|------------------|--------------------------|-------|
|`POST`  |`/auth/login`     | Login with credentials   | ❌    |
|`POST`  |`/auth/register`  | Create a new user        | ❌    |
|`GET`   |`/files/`         | List all uploaded files  | ✅    |
|`POST`  |`/upload/`        | Upload a new file        | ✅    |
|`GET`   |`/files/{id}`     | Download a file          | ✅    |

## 6. Security Design

- JWT-based auth with expiry + refresh token support
- Basic password hashing (bcrypt)
- Files saved outside web root (non-public paths)
- Optional: Role-based access (viewer/uploader)

## 7. Local Network Behavior

- On startup, server checks current SSID.
- If SSID is not in whitelist, server exits.
- Otherwise, server launches and advertises via mDNS.
- Clients scan mDNS records for _lanvault._tcp.local. to find IP/port.

## 8. Future Enhancements

- Lossless media compression module
- Thumbnail generation for videos
- Admin panel (web-based)
- Desktop sync client (auto-backup folders)

## 9. Work Breakdown (Suggested Milestones)

### Phase 1: Backend Setup

- Project skeleton with FastAPI + Docker
- JWT auth system
- Upload + list endpoints
- Shared directory mounting
- mDNS advertisement

### Phase 2: Setup + Networking
- Initialize Flutter project
- Setup base routing and screens
- Write api_client.dart for login/upload

### Phase 3: Core Features

- Implement login + JWT storage
- Add mDNS service to discover server
- File picker + upload
- Media list with preview

## Phase 4: Polish

- UI styling + file previews
- SSID whitelist enforcement
- Create README, diagrams, video demo
- Open-source launch on GitHub