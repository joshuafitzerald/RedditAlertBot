import praw
import discord
import asyncio

# Reddit credentials
REDDIT_CLIENT_ID = 'YOUR CLIENT ID'
REDDIT_CLIENT_SECRET = 'YOUR CLIENT SECRET'
REDDIT_USER_AGENT = 'Redditdev scraper by YOUR USERNAME'

# Discord credentials
DISCORD_TOKEN = 'YOUR DISCORD TOKEN'
DISCORD_USER_ID = 404069977788907550  # Replace with your Discord user ID

# Set up Reddit client
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

# Set up Discord client with required intents
intents = discord.Intents.default()
intents.messages = True
intents.members = True  # Added to allow fetching users
client = discord.Client(intents=intents)

async def check_reddit():
    await client.wait_until_ready()
    while not client.is_closed():
        subreddit = reddit.subreddit('YOUR DESIRED SUBREDDIT')
        for submission in subreddit.new(limit=10):  # Check the latest 10 posts
            print(f"Checking post: {submission.title} with upvotes: {submission.score}")
            if submission.score > 100:  # Change this to 1 for testing
                message = (f"New post in r/Goodasssub!\n"
                           f"Title: {submission.title}\n"
                           f"Upvotes: {submission.score}\n"
                           f"URL: {submission.url}")
                user = await client.fetch_user(DISCORD_USER_ID)
                await user.send(message)
                print(f"Sent DM to user with post: {submission.title}")

        await asyncio.sleep(60)  # Check every minute

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

async def main():
    await client.start(DISCORD_TOKEN)

asyncio.run(main())
