# 🎮 Game

_Astray_ is a dynamic 3D maze game where you steer a rolling ball using either your keyboard or intuitive hand gestures. Built with Three.js for sleek visuals, the game scales in complexity and integrates a powerful ML performance tracking system.

## ✨ Key Highlights

- 🌀 Realistic ball movement within intricate 3D mazes
- ✋ Gesture-based navigation via MediaPipe
- ⌨️ Keyboard support as a fallback control method
- 🚀 Gradually increasing maze complexity
- 👁️ Live hand-tracking feedback overlay
- 🌐 Modern visual style with textured environments
- 📡 Integrated ML observability with Prometheus & Grafana
- 📦 Easy deployment using Docker containers

## 🔧 System Requirements

- 🌍 Up-to-date browser (Chrome, Firefox, Safari, or Edge)
- 📸 Webcam (for gesture control)
- 🐋 Docker & Docker Compose (for ML monitoring)
- 🐍 Python 3.8 or higher
- 🛠️ Basic web dev skills for setup

## 🚀 Quick Start Guide

1. Clone this repo:
```bash
[git clone https://github.com/M/astray.git](https://github.com/MazenFayed/MLOPs-Final-Project.git)
cd astray
```

2. Install required Python libraries:
```bash
pip install -r requirements.txt
```

3. Launch ML monitoring stack:
```bash
docker-compose up -d
```

4. Confirm you have the essential assets:
   - `index.html`
   - `ball.png`, `brick.png`, `concrete.png`

5. Open the game:
```bash
# Python server
python -m http.server 8000

# Or with Node.js
npx serve
```

## 🕹️ Playing the Game

### 🔧 Controls

#### Keyboard:
- Arrows or H/J/K/L to move
- G: Enable/disable gesture control
- I: Show instructions

#### Gestures:
- One finger ☝️ → Up
- Fist ✊ → Down
- Two fingers ✌️ → Left
- Three fingers 🤟 → Right

### 🎯 Objective

- Navigate to the maze's exit
- Levels become harder with larger mazes
- Ball halts on wall impact
- Camera dynamically follows the ball
- Gestures must be held briefly for recognition

## 🛠️ Tech Stack

- 🌐 Three.js (r128) for 3D rendering
- ✋ MediaPipe Hands for gesture input
- 📹 HTML5 Canvas for hand visuals
- 🧠 Vanilla JavaScript game logic
- 📊 Prometheus for collecting metrics
- 📈 Grafana for dashboards
- 🐳 Docker for isolated services
- 🔍 MLflow for model experiment logging

## 🗂️ Project Layout

```
astray/
├── app/                  # Core app logic
├── tests/                # Unit tests
├── grafana/              # Dashboard configs
├── mlruns/               # MLflow tracking logs
├── index.html            # Main web interface
├── ball.png              # Ball texture
├── brick.png             # Wall texture
├── concrete.png          # Floor texture
├── dockerfile            # Docker config
├── docker-compose.yml    # Docker service definitions
├── prometheus.yml        # Prometheus setup
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

## 📊 ML Monitoring Overview

An integrated ML observability suite provides real-time insight into model behavior.

### 🔍 Model Evaluation Pipeline

- 🤖 Compare RandomForest, SVM, and LightGBM
- 📊 Log performance using MLflow
- ⚙️ Choose best model via accuracy & latency
- 🎯 Tune hyperparameters with tracking support

### 🔬 MLflow

- 🔁 Versioning and model registry
- 📈 Metric comparison across runs
- 🗃️ Store artifacts and parameters
- 🌐 Interface: http://localhost:5000

### 📡 Prometheus

- 📊 Monitor metrics in real time
- 🕒 Track inference latency
- 🖥️ Monitor CPU/memory usage
- 🚨 Custom alerts for drift detection
- 🌐 Interface: http://localhost:9090

### 📈 Grafana

- 📊 Dynamic dashboards
- 📉 Compare model metrics
- 🖥️ System performance graphs
- 🚨 Alert triggers for anomalies
- 🌐 Interface: http://localhost:3000
- 🔑 Default login: admin/admin

### 🐳 Docker Setup

```yaml
services:
  - prometheus: For collecting metrics
  - grafana: For real-time dashboards
  - mlflow: For model tracking
  - model-service: Custom inference API
```

### 🔁 Model Lifecycle

1. **Data Logging** 📥
   - Player activity and state tracking
   - Model inference metrics

2. **Model Training** 🎓
   - 🌲 RandomForest
   - 📐 Support Vector Machine
   - ⚡ LightGBM

3. **Performance Insights** 📊
   - Track accuracy, latency, and system load
   - Detect potential model degradation

4. **Deployment** 🚀
   - Automated model selection and deployment
   - Rollback and A/B testing support

## 🤝 Contributions

1. Fork the repo 🍴
2. Create a branch 🌿 (`git checkout -b feature/YourFeature`)
3. Commit changes 💾 (`git commit -m 'Your feature'`)
4. Push updates 📤 (`git push origin feature/YourFeature`)
5. Submit a pull request 🔄

## 📃 License

MIT License – see LICENSE for full details.

## 🙌 Credits

- 🎨 Three.js community
- 🧠 MediaPipe developers
- 🧩 Original Astray maze logic
- 📊 Prometheus & Grafana teams

Have fun exploring Astray! 🌀
