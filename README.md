# General-Purpose Social Media Outreach AI Agent

This project provides an AI-powered tool to create personalized outreach messages for social media. It is designed to be **general-purpose**, allowing users to input their niche, YouTube channel, and the person or creator they want to contact. The tool automatically researches the target and generates a concise, professional, and personalized direct message.

---

## Features

- Researches recent accomplishments and highlights of the target in your chosen niche.
- Generates a concise, personalized DM in the style of Alex Hormozi.
- Fully adaptable to any niche or industry.
- Plug-and-play: ready to use in Google Colab with minimal setup.  

---

## Prerequisites

1. **Google AI API Key** – Free to obtain and use. Tutorial: [https://youtu.be/yZN5a12CZD8](https://youtu.be/yZN5a12CZD8)  
2. **Serper.dev API Key** – Free to obtain and use. Tutorial: [link to be added later]  

---

## Setup

> **Side Note:** All steps assume you are working in a **Google Colab Notebook** for simplicity and speed.

1. Open [Google Colab](https://colab.research.google.com/).  
   [image of Colab homepage here]

2. Create a new notebook.  
   [image of fresh notebook here]

3. Copy and paste the following commands into a cell:

   ```python
   import os
   !uv tool install crewai
   !uv tool run crewai create crew social_media_manager
   ```

   When prompted to "select a provider to set up," type **3** and press Enter.  
   [image here]

   You will then be asked to select a Gemini model. Choose any model for now (we'll update it manually later).  
   [image here]

   Paste your **GEMINI API Key** (from the tutorial above) when prompted.  
   [image here]

   You should see the message: "Crew social_media_manager created successfully!"  
   [image here]

## Configuration

Open the **.env** file and update the model variable:

```
MODEL=gemini/gemini-2.5-flash
```

[image here]

**Note:** The `.env` file might be hidden. Click the eye icon to reveal hidden files.

Add your **Serper API key** for research functionality:

```
SERPER_API_KEY=[Enter your API KEY here]
```

[image here]

Alternatively, you can copy and paste the `.env` file included in this repository.

## Adding Project Files

Copy the following files from this repository into your Google Colab environment:

- `main.py`
- `crew.py`
- `agents.yaml`
- `tasks.yaml`

Paste each file into its respective location in Colab.  
[image here]

## Running the Tool

Run the following commands in a Colab cell:

```bash
%cd /content/social_media_manager
!uv add "crewai[google-genai]"  # only needs to be run once per runtime session
!uv tool run crewai run
```

You will be prompted for three pieces of information:

- Your niche  
- Your YouTube channel name  
- The name of the person/creator you want to contact  

[image here]

The final output will be a personalized DM that you can copy and paste from the terminal or from a file called `generated_dm.txt` in your Google Colab environment directory. You can send this message to the person you are trying to get an interview with.
