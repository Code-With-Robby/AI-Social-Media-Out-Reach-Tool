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
2. **Serper.dev API Key** – Free to obtain and use. Tutorial: Go to serper.dev -> sign up/in -> get FREE API KEY  

---

## Setup

> **Side Note:** All steps assume you are working in a **Google Colab Notebook** for simplicity and speed.

1. Open [Google Colab](https://colab.research.google.com/).  

2. Create a new notebook.  

3. Copy and paste the following commands into a cell:

   ```python
   import os
   !uv tool install crewai
   !uv tool run crewai create crew social_media_manager
   ```

   When prompted to "select a provider to set up," type **3** and press Enter.  
 <img width="1406" height="674" alt="Screenshot 2026-02-15 at 3 43 51 PM" src="https://github.com/user-attachments/assets/1725969b-3d56-425f-8092-bdb69cda8835" />


   You will then be asked to select a Gemini model. Choose any model for now (we'll update it manually later).  
<img width="1406" height="674" alt="Screenshot 2026-02-15 at 3 45 22 PM" src="https://github.com/user-attachments/assets/dce9d7dc-57a2-4ae4-86f6-b587c2380610" />

   Paste your **GEMINI API Key** (from the tutorial above) when prompted.  
<img width="1406" height="674" alt="Screenshot 2026-02-15 at 3 46 26 PM" src="https://github.com/user-attachments/assets/86a77c23-1705-4f69-a722-863ec5fa87d3" />

   You should see the message: "Crew social_media_manager created successfully!"  
<img width="1102" height="674" alt="Screenshot 2026-02-15 at 3 50 06 PM" src="https://github.com/user-attachments/assets/bae8f430-6adf-4024-b70b-af0a3cbb14d7" />

## Configuration

Open the **.env** file and update the model variable:

```
MODEL=gemini/gemini-2.5-flash
```

<img width="534" height="530" alt="Screenshot 2026-02-15 at 3 53 46 PM" src="https://github.com/user-attachments/assets/7777a567-4324-4edf-9b69-83a04768d33b" />

**Note:** The `.env` file might be hidden. Click the eye icon to reveal hidden files.

Add your **Serper API key** for research functionality:

```
SERPER_API_KEY=[Enter your API KEY here]
```

<img width="1546" height="530" alt="image" src="https://github.com/user-attachments/assets/b68d2489-2928-46dd-b97f-01a4d64c2fd8" />

Alternatively, you can copy and paste the `.env` file included in this repository.

## Adding Project Files

Copy the following files from this repository into your Google Colab environment:

- `main.py`
- `crew.py`
- `agents.yaml`
- `tasks.yaml`

Paste each file into its respective location in Colab.  
<img width="414" height="902" alt="image" src="https://github.com/user-attachments/assets/cafd9f55-30b6-4cc2-8059-dd017a203929" />

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

<img width="814" height="261" alt="Screenshot 2026-02-15 at 4 13 21 PM" src="https://github.com/user-attachments/assets/af4e8895-e058-47f3-97bb-dccf0056564f" />

The final output will be a personalized DM that you can copy and paste from the terminal or from a file called `generated_dm.txt` in your Google Colab environment directory. You can send this message to the person you are trying to get an interview with.

<img width="1818" height="753" alt="Screenshot 2026-02-15 at 4 28 25 PM" src="https://github.com/user-attachments/assets/ca7352fd-f753-448a-aff6-ac14ff677a20" />

