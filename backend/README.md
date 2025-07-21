# 🧠 OVERVIEW

### Components:

1. **FastAPI server (in Docker)**: File API, auth, mDNS
1. **Tkinter GUI (on host)**: File manager, Docker control
1. **Shared folder**: Persistent mount for files

## 🧩 MODULE 1: GUI STARTUP

### Pseudocode:

```python
on_app_launch():
    check_docker_installed()
    check_server_status()
    load_config_file()
    show_main_window()
```

### Tasks:

- Detect Docker
- Read .env or config.json
- Poll server container status
- Launch dashboard

## 🧩 MODULE 2: FILE BROWSER (IN GUI)

### Pseudocode:

```python
refresh_file_list():
    for file in SHARED_DIRECTORY:
        display_file_info(file)

on_file_delete(filename):
    confirm_user()
    delete_file(filename)

on_file_rename(old, new):
    rename_file(old, new)

on_open_file(filename):
    open_with_default_app(filename)
```

### Tasks:

- List files
- Open, delete, rename
- Use os and subprocess

## 🧩 MODULE 3: SERVER CONTROL (GUI to Docker)

### Pseudocode:

```python
on_start_server():
    subprocess.run("docker compose up -d")

on_stop_server():
    subprocess.run("docker compose down")

on_restart_server():
    subprocess.run("docker compose restart")

get_server_status():
    subprocess.check_output("docker ps")
```

### Tasks:

- Start/stop FastAPI backend container
- Show status

## 🧩 MODULE 4: CONFIGURATION PANEL

### Pseudocode:

```python
load_config():
    read_json("config.json")

save_config(new_config):
    write_json("config.json", new_config)
    notify_restart_required()
```

### Editable Settings:

- Mount path
- Allowed file types
- Max file size
- Server port

## 🧩 MODULE 5: DISK USAGE MONITORING

### Pseudocode:

```python
check_disk_usage():
    total, used, free = shutil.disk_usage(SHARED_DIRECTORY)
    if used / total > 0.9:
        warn_user_low_space()
```

## 🧩 MODULE 6: LOGS (Optional)

### Pseudocode:

```python
on_view_logs():
    read_file("logs/upload.log")
    display_in_textbox()
```

## 🧩 MODULE 7: SYSTEM CONTROL (Optional, sudo)

```python
on_shutdown():
    subprocess.run(["systemctl", "poweroff"])

on_reboot():
    subprocess.run(["systemctl", "reboot"])
```

## 📊 FLOWCHART

```
    +---------------------------+
    |      Launch GUI App       |
    +------------+--------------+
                 |
                 v
      +-----------------------+
      | Check Docker Status   |
      +-----------------------+
                 |
                 v
      +-----------------------+
      | Check Server Running? |
      +-----------------------+
         | Yes           | No
         v               v
     Show "Running"   Show "Stopped"
         |               |
         +---------------+
                 |
                 v
     +-----------------------+
     |     GUI Main Menu     |
     +-----------------------+
        |         |       |
        v         v       v
   File Browser  Config   Server Control
        |           |       |
        v           v       v
  Open/Del/Rename  Edit    Start/Stop
        |        Save       |
        v          |        v
  View Media     Restart?  Show Logs
        |
        v
   Disk Usage
```

## ✅ What You Can Do From GUI

- Browse/manage uploaded files
- Start/stop/restart Docker backend
- Edit config without terminal
- Monitor disk space
- Optional: shutdown/reboot system