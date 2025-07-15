# 🔗 Lan-File-Vault – Secure File Sharing Over Wi-Fi

Lan-File-Vault is a cross-platform application that lets authorized devices upload and view images/videos securely over a local Wi-Fi network. Built with Python and Docker, the server runs only on trusted networks and stores files in a shared location accessible from both Linux and Windows (dual-boot setup). ✨

---

## 🛠️ Features

- 📤 Upload and view files (images, videos) from mobile or desktop
- 🔐 JWT-based authentication for secure access
- 📡 Auto-discovery of server using mDNS (Bonjour/Avahi)
- 📁 Saves files in a common mount directory (shared across dual boot)
- 🐳 Dockerized backend for portability and easy setup
- 🚫 Only runs on trusted Wi-Fi networks (SSID-based control)

---

## 🧱 Architecture Overview

```text
Mobile/Desktop Client
   ↕ HTTP + mDNS
Dockerized FastAPI Server
   ↕ File System
Shared Mount Directory (exFAT/NTFS)
```

## 📦 Tech Stack

| Layer        | Technology                 |
|--------------|----------------------------|
|Backend       | Python, FastAPI, Docker    |
|Auth          | JWT                        |
|Discovery     | Zeroconf (mDNS)            |
|Client UI     | Flutter / Kivy / Electron  |
|File Storage  | Shared NTFS/ExFAT mount    |
|Deploy        | Docker Compose (optional)  |

## 🚀 Getting Started

### 🐳 Run the Server

```bash
docker build -t localshare-server .
docker run -v /mnt/shared:/app/data -p 8000:8000 localshare-server
```

### 🧪 Test Locally (Without Docker)

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
Make sure to mount the shared directory and set environment variables accordingly.
```

## 📱 Client App
*(Work in progress)*

Client will:

- Discover the server using mDNS
- Authenticate using stored credentials
- Upload and view media

Framework options:

- Python + Kivy (if using Python)
- Flutter (if going cross-platform mobile/desktop)
- Electron (for desktop UI)

## 🔐 Authentication

Uses JWT tokens to protect endpoints.
Each device must authenticate before accessing or uploading files.

***TODO: Add user management interface.***

## 🌐 Service Discovery

Using zeroconf, the server advertises itself over the network.
Clients detect and connect without needing to know the IP address.

## 🔒 Wi-Fi Safety Control

The server checks if it's running on an allowed SSID before starting.
This is done via:

- `nmcli` (Linux)
- `netsh wlan show interfaces` (Windows)

## 🗂️ Directory Structure

```text
server/
├── main.py
├── auth.py
├── discovery.py
├── config.py
├── Dockerfile
client/
├── (UI code here)
docs/
├── screenshots/
├── architecture.md
```

## 📸 Screenshots

> Add images or gifs of the UI and upload process here

## 🤝 Contributing

Contributions welcome!
Feel free to open issues, suggest features, or submit pull requests.

## 📄 License

MIT License – see LICENSE for details.

## 🙋‍♂️ Author

Made with 💡 by RandomGameCoder

---

### ✅ Tips

- **Update regularly** as your project grows.
- Add badges (e.g. GitHub stars, CI status) later for polish.
- Include a short demo video or link once the client is ready.
- Write a `docs/architecture.md` file with diagrams (e.g., sequence diagrams or component flow).
