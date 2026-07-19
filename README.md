# ISEMS – Intelligent Surveillance Event Management System

> **Turning Surveillance Footage into Actionable Security Intelligence.**

ISEMS is an enterprise surveillance event management platform currently under active development. Its mission is to transform raw surveillance footage into structured security intelligence by detecting incidents, preserving evidence, managing events, and supporting security operations through a modern desktop application.

This repository contains the foundational prototype of ISEMS, focusing on motion detection and evidence capture using Python and OpenCV. The project is being developed incrementally, with each milestone building toward a fully featured enterprise surveillance platform.

---

# Current Development Status

**Project Phase:** Foundation Prototype

### Implemented Features

* ✅ Live video processing
* ✅ Motion detection using frame differencing
* ✅ Real-time motion highlighting with bounding boxes
* ✅ Timestamp overlay on live video
* ✅ Automatic evidence snapshot capture
* ✅ Timestamp burned onto captured evidence
* ✅ Modular Python project structure
* ✅ Support for webcam and recorded CCTV footage

### Currently Under Development

* Event Model
* Incident Management
* SQLite Database Integration
* Camera Abstraction Layer
* Event Bus Architecture
* Evidence Management Service

### Planned Enterprise Features

* Multi-camera monitoring
* Camera management
* Incident dashboard
* Evidence browser
* Searchable incident history
* Video playback
* Reporting
* User authentication
* Notifications
* AI-powered analytics
* Person, vehicle and fire detection
* RTSP/IP Camera support
* ONVIF integration

---

# Why Build This?

Many surveillance systems simply record video, leaving security personnel to manually review hours of footage after an incident has occurred.

ISEMS is being designed to reduce that workload by automatically detecting security events, preserving evidence, and organizing incidents into actionable information for investigators and operators.

The long-term vision is to build a professional surveillance platform suitable for environments such as:

* Banks
* Government institutions
* Hospitals
* Universities
* Corporate offices
* Industrial facilities
* Commercial properties

---

# Technology Stack

* Python
* OpenCV
* SQLite *(planned)*
* Object-Oriented Programming
* Git & GitHub

Future versions will incorporate additional technologies as the platform evolves.

---

# Repository Structure

```text
video-motion-detection-event-logging-system/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── motion_detector.py
│   └── event_logger.py
│
├── assets/
│   └── cctv_sample.mp4
│
├── events/
│   └── event_*.jpg
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

# Current System Workflow

```text
Video Source
      │
      ▼
Frame Capture
      │
      ▼
Motion Detection
      │
      ▼
Motion Detected?
      │
      ├── No → Continue Monitoring
      │
      └── Yes
             │
             ▼
Evidence Snapshot
             │
             ▼
Timestamp Overlay
             │
             ▼
Save Image to Events Folder
```

---

# Planned Enterprise Architecture

```text
        Camera Pipeline
              │
              ▼
       Detection Engine
              │
              ▼
        Event Builder
              │
              ▼
          Event Bus
              │
 ┌────────────┼──────────────┐
 ▼            ▼              ▼
Incident   Evidence        Audit
Service    Service        Service

───────────────┼───────────────
               ▼
       SQLite Database
               │
               ▼
      Operations Dashboard
```

This architecture has been designed to support scalable deployments ranging from a single camera to large enterprise surveillance installations.

---

# Getting Started

## Clone the repository

```bash
git clone https://github.com/MrLongwe/video-motion-detection-event-logging-system.git
cd video-motion-detection-event-logging-system
```

## Create a virtual environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Configure the video source

Edit `app/config.py`.

For a webcam:

```python
VIDEO_SOURCE = 0
```

For a recorded CCTV video:

```python
VIDEO_SOURCE = r"assets/cctv_sample.mp4"
```

## Run the application

```bash
python app/main.py
```

Press **ESC** to exit.

Captured evidence images will be saved automatically in the `events/` directory whenever motion is detected.

---

# Project Roadmap

### Version 0.1

* Motion Detection Prototype ✅

### Version 0.2

* Evidence Capture System ✅

### Version 0.3

* Event Model

### Version 0.4

* Incident Management

### Version 0.5

* SQLite Persistence

### Version 0.6

* Camera Framework

### Version 0.7

* Multi-Camera Monitoring

### Version 0.8

* Operations Dashboard

### Version 0.9

* Reports & Analytics

### Version 1.0

* Enterprise Surveillance Event Management Platform

---

# Documentation

The project is accompanied by a Software Engineering Manual documenting the architecture, engineering decisions, and future design of ISEMS.

Documentation includes:

* Product Vision
* System Architecture
* Architecture Decision Records (ADRs)
* Camera Framework
* Detection Engine
* Incident Management
* Database Design
* User Interface
* Deployment

---

# License

This project is released under the MIT License.

---

# Author

**Mbeki Peter Longwe**

BSc Computer Network Engineering

GitHub: https://github.com/MrLongwe

---

## Project Vision

ISEMS is more than a motion detection application.

It is the foundation of an enterprise surveillance platform designed to transform surveillance footage into actionable security intelligence through intelligent event detection, evidence management, and scalable software architecture.
