# 🎨 Text-to-Image Generator  

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)  
[![Flask](https://img.shields.io/badge/Flask-Web_Framework-black?logo=flask)](https://flask.palletsprojects.com/)  
[![Diffusers](https://img.shields.io/badge/Diffusers-Stable_Diffusion-orange?logo=huggingface)](https://huggingface.co/docs/diffusers/index)  
[![License](https://img.shields.io/badge/License-MIT-green)](https://github.com/zinoos/text-to-image-generator/main/LICENSE)  

A simple and elegant **Flask web app** that lets you generate images from text prompts using the **SDXL Turbo** model from Stability AI.  
The app features a clean UI with modern styling and smooth interactions.  

---

## 🧠 Features

✅ Generate images instantly from any text prompt  
✅ Uses **Stable Diffusion XL Turbo** for fast inference  
✅ Simple web interface — type, click, and view  
✅ Automatically saves and displays the last generated image  
✅ Works on both **CPU** and **GPU (CUDA)**  



## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/text-to-image-generator.git
cd text-to-image-generator

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install flask torch diffusers
```

## Structure

```bash

text-to-image-generator/
│
├── main.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── img/
    └── (generated images)

