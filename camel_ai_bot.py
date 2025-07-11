import discord
import os

intents = discord.Intents.default()
intents.members = True  # Needed for member join events
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_member_join(member):
    if member.bot:
        return

    embed = discord.Embed(
        title="👋 Welcome to CAMEL-AI!",
        description=(
            "We're thrilled to have you join us! 🚀\n\n"
            "**Useful Links**\n"
            "• [Main Website](https://www.camel-ai.org/)\n"
            "• [Docs](https://docs.camel-ai.org/)\n\n"
            "**Get Involved**\n"
            "• Introduce yourself in #introductions\n"
            "• Need help? Reply to this DM or tag @Staff in the server.\n\n"
            "**🗓️ Weekly Community Meeting**\n"
            "We host a meeting every week—everyone’s welcome!\n"
            "[Add to your calendar](https://calendar.google.com/calendar/render?action=TEMPLATE&text=CAMEL-AI+Developer+Meeting-US&timezone=friendly&dates=20250708T030000Z/20250708T043000Z&details=Join+with+Google+Meet:+https://meet.google.com/sez-aomy-ebm)\n\n"
            "*Tip: Set it as recurring (weekly) so you never miss out!*"
        ),
        color=0x7B68EE
    )
    embed.set_footer(text="— Team CAMEL-AI")
    embed.set_thumbnail(url="https://media.licdn.com/dms/image/v2/D560BAQEtrzetpWj9RQ/company-logo_200_200/company-logo_200_200/0/1710385275126?e=2147483647&v=beta&t=NJW25EpK_pOIRCWKZWg8UrujmCF2Nye4M8PaqAEPbtY")  # Optional

    try:
        await member.send(embed=embed)
    except Exception as e:
        print(f"Could not DM {member}: {e}")

client.run(TOKEN)
