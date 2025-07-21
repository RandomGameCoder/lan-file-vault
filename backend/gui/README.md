# 🖥️ Lan File Vault - GUI Backend Server

A desktop GUI application built with Tkinter that provides a graphical interface for managing the Lan File Vault backend server. This application allows users to control Docker containers, manage files, monitor server status, and configure settings without using the command line.

---

## 🚀 Features

- **🏠 Home Dashboard**: Central hub with quick access to all features
- **📊 Server Status**: Monitor server storage, uptime, and connection status
- **📁 File Manager**: Browse, upload, delete, and manage shared files
- **⚙️ Server Configuration**: Configure server settings, ports, and file paths
- **🔧 Settings**: Application preferences and user configurations
- **🐳 Docker Integration**: Start, stop, and manage Docker containers
- **📱 Responsive UI**: Clean, modern interface with emoji icons

---

## 🏗️ Architecture

```text
┌─────────────────────────────────────────┐
│              Main Application           │
│            (main.py - App)              │
├─────────────────────────────────────────┤
│                 Pages                   │
├─────────────────┬───────────────────────┤
│   HomePage      │    StatusPage         │
│   📊 Dashboard  │    💾 Storage Info    │
├─────────────────┼───────────────────────┤
│ FileManagerPage │  ServerConfigPage     │
│ 📁 File Ops     │  ⚙️ Server Settings   │
├─────────────────┼───────────────────────┤
│               SettingsPage              │
│              🔧 App Settings            │
└─────────────────────────────────────────┘
```

## 📁 Project Structure

```
backend/gui/
├── main.py                    # Main application entry point
├── pages/                     # Individual page modules
│   ├── __init__.py
│   ├── home_page.py          # Main dashboard
│   ├── status_page.py        # Server status monitoring
│   ├── file_manager_page.py  # File operations
│   ├── server_config_page.py # Server configuration
│   └── settings_page.py      # Application settings
└── README.md                 # This file
```

## 🎯 Core Components

### Main Application (`main.py`)
- **App Class**: Main Tkinter window with centered positioning
- **Frame Management**: Dynamic page switching using a dictionary-based frame system
- **Navigation**: Central controller for page transitions
- **Window Configuration**: 800x600 responsive layout

### Page Modules

#### 🏠 **HomePage** (`home_page.py`)
- Central dashboard with navigation buttons
- Quick access to all major features
- Status overview button
- File Manager and Server Config shortcuts

#### 📊 **StatusPage** (`status_page.py`)
- Real-time server status monitoring
- Storage usage statistics
- Connection status indicators
- Performance metrics display

#### 📁 **FileManagerPage** (`file_manager_page.py`)
- File browser interface
- Upload/download functionality
- File operations (rename, delete, open)
- Directory navigation

#### ⚙️ **ServerConfigPage** (`server_config_page.py`)
- Docker container management
- Server port configuration
- File path settings
- Service start/stop controls

#### 🔧 **SettingsPage** (`settings_page.py`)
- Application preferences
- User account management
- Theme and UI settings
- Configuration backup/restore

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- Tkinter (usually included with Python)
- Docker (for backend server management)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/RandomGameCoder/lan-file-vault.git
   cd lan-file-vault/backend/gui
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python main.py
   ```

### Quick Start

1. **Launch the GUI**: Run `python main.py`
2. **Check Status**: Click "📊 Status" to verify server connectivity
3. **Configure Server**: Use "⚙️ Server Config" to set up Docker containers
4. **Manage Files**: Access "📁 File Manager" to browse and upload files
5. **Adjust Settings**: Use the "Settings" button for preferences

---

## 🎨 User Interface

### Design Principles
- **Clean & Modern**: Minimalist design with clear visual hierarchy
- **Emoji Icons**: Intuitive visual indicators for different functions
- **Responsive Layout**: Adapts to window resizing
- **Consistent Navigation**: Uniform button placement and styling

### Navigation Flow
```text
Home Page → [Status/FileManager/ServerConfig] → Settings
    ↑                                              ↓
    ←──────────────── Back Navigation ←───────────
```

### Styling Features
- TTK themed widgets for modern appearance
- Custom button styles with increased padding
- Grid-based layout for responsive design
- Arial font family for readability

---

## 🔧 Configuration

### Page Registration
New pages can be added by:
1. Creating a new page class in `pages/`
2. Importing it in `main.py`
3. Adding it to the frames tuple
4. Implementing navigation links

### Frame Structure
Each page follows this pattern:
```python
class NewPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        # Page content and layout
```

---

## 🔌 Integration

### Backend Server Communication
- REST API calls to FastAPI backend
- Docker container status monitoring
- File system operations through shared mounts
- Real-time status updates

### Docker Integration
- Container lifecycle management
- Port configuration
- Volume mounting
- Service discovery

---

## 🛠️ Development

### Adding New Features

1. **Create Page Module**: Add new file in `pages/`
2. **Implement UI**: Use TTK widgets for consistency
3. **Add Navigation**: Link from existing pages
4. **Register Frame**: Update main.py imports and frame list

### Code Style
- Follow PEP 8 guidelines
- Use descriptive variable names
- Comment complex logic
- Maintain consistent indentation

### Testing
- Test page transitions
- Verify Docker integration
- Check file operations
- Validate UI responsiveness

---

## 📋 Features Roadmap

### Current Implementation
- ✅ Basic window and navigation framework
- ✅ Page switching mechanism
- ✅ Home page with navigation buttons
- ✅ Responsive grid layout

### Planned Features
- 🔄 Docker container management
- 🔄 File browser implementation
- 🔄 Server status monitoring
- 🔄 Configuration panels
- 🔄 Settings persistence
- 🔄 Log viewer
- 🔄 System controls (shutdown/reboot)

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Create a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../../LICENSE) file for details.

---

## 👨‍💻 Author

**RandomGameCoder** - [GitHub Profile](https://github.com/RandomGameCoder)

---

## 🔗 Related Documentation

- [Main Project README](../../README.md)
- [Backend Server Documentation](../README.md)
- [Software Design Document](../../docs/software_design_document.md)

---

*Made with ❤️ for secure local file sharing*
