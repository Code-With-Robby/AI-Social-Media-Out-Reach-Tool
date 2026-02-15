#!/usr/bin/env python

from social_media_manager.crew import SocialMediaManager
from datetime import datetime
import sys

def run():
    print("\n" + "="*70)
    print("General Social Media Outreach DM Generator")
    print("="*70 + "\n")

    # User inputs
    niche = input("Enter your niche (e.g., tech, fitness, cooking): ").strip()
    youtube_channel = input("Enter your YouTube channel name: ").strip()
    target_name = input("Enter the name of the person/creator you want to contact: ").strip()

    if not niche or not youtube_channel or not target_name:
        print("All inputs are required. Exiting.")
        sys.exit(0)

    print(f"\nStarting outreach process for: {target_name} in niche: {niche}")
    print("Researching recent accomplishments...")

    # Inputs passed to Crew
    inputs = {
        "target_name": target_name,
        "niche": niche,
        "youtube_channel": youtube_channel,
        "current_year": str(datetime.now().year),
    }

    try:
        result = SocialMediaManager().crew().kickoff(inputs=inputs)

        print("\n" + "="*70)
        print("Final Output (Personalized DM):")
        print("-"*70)
        print(result)
        print("="*70 + "\n")

    except Exception as e:
        print(f"Error running crew: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run()
