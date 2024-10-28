## RedditAlertBot

- This bot monitors a specified subreddit and sends a direct message (DM) to a specified Discord user when a recent post exceeds a defined upvote threshold. It's useful for tracking trending posts on Reddit in real-time.

## Features

- Monitors new posts in a specified subreddit.
- Sends a DM to the user when a post reaches the specified upvote threshold.
- Customizable subreddit, upvote threshold, and notification frequency.

## Getting Started
# Prerequisites
- Python 3.7+

- Ensure you have Python installed. You can download it from python.org.

- Create a bot on the Discord Developer Portal and get your bot token.
- Enable Server Members Intent and Message Content Intent under "Privileged Gateway Intents" in the bot settings.
- Also here in this Developer Portal,  acquire your Discord Bot Token and Reddit API Credentials

Register an application on Reddit's Developer Portal to get your client_id, client_secret, and user_agent.

## Installing Dependencies

    pip install praw discord.py

## Configuration

- Create a .env file (for security) in your project root and add your credentials:
-       REDDIT_CLIENT_ID=your_reddit_client_id
        REDDIT_CLIENT_SECRET=your_reddit_client_secret
        REDDIT_USER_AGENT=your_reddit_user_agent
        DISCORD_TOKEN=your_discord_bot_token
        DISCORD_USER_ID=your_discord_user_id  # Replace with your Discord user ID

- Update the main script to import the credentials from .env instead of hardcoding them directly in the script.

## Running the Bot

- Run the bot with:
-     python bot.py
- The bot will now monitor your chosen subreddit and DM you when a post reaches the specified upvote threshold.




