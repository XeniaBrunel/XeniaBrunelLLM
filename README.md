# My AI Text Detector

It is an AI text detection system that uses both Llama 3 and Mistral models

Website: https://xeniabrunel.com

## What is this

This is my educational project for detecting AI-generated academic text. It is meant to show how different AI models analyse the same text differently instead of just giving a percentage like GPTZero or other detectors do.

I used two models - Llama 3 and Mistral - because they work locally through Ollama and don't need API keys. They're also open source so I can see what's happening.

## Why I made this

Most AI detectors are 'black boxes'. After you put text in, you just get a percentage such as '85% AI-generated', but there is no explanation about how that conclusion was made. I wanted to make something more transparent for learning, and a detector that can be trained and improved.

## Tech stack

Backend:
- Ollama for running Llama 3 and Mistral locally
- Python + Streamlit for the web interface
- Docker makes it easier to deploy everything together

Infrastructure:
- Nginx Proxy Manager for HTTPS and domain routing
- VPS server running Ubuntu

## How it works

1. You paste text to analyse
2. Both models analyse your text
4. You see side by side results from Llama 3 and Mistral models with explanations
The whole process takes 15-30 seconds because I'm running it on CPU not GPU. GPU would be faster but way more expensive.

## Files

- `.gitignore` - Tells Git to ignore the datasets/ folder (too large for GitHub - 1.1GB)
- `Dockerfile` - Builds the Streamlit container. Sets up Python environment.
- `analyze_data.py` - Python script to analyze the Kaggle dataset.
- `app.py` - Streamlit application
- `docker-compose.yml` - sets up containers
- `requirements.txt` - Python packages
- `datasets/AI_Human.csv` - the big dataset from Kaggle
- `datasets/uploads/` - for new examples you upload
- `npm_data/` - Nginx Proxy Manager configuration and database
- `npm_letsencrypt/` - SSL certificates from Let's Encrypt

## Features

Main page: paste text, get analysis from both models
Brunel Training Lab: password-protected area where you can upload new datasets for further training and improving. Password is `Brunel_2026`

## Why not just use GPTZero or other systems

GPTZero is faster but:
1. It costs money after free tier
2. It's a 'black box' system and gives no explanations
3. Can't add your own training data for further training and improving
4. Sends your text to their servers / unknown how private data is used

You can see how my system works, run it locally, and customise it so I believe it is better for learning.

## Architecture

Browser → Nginx (handles HTTPS) → Streamlit (web UI) → Ollama (runs models)
                                                            ↓
                                                      Dataset (text examples)

All running in Docker containers so it's easy to move between servers.

## Author

Xenia Bugaev, 2026

Educational project for Brunel University, demonstrating AI text detection and AI model comparison.
