import datetime
starttime = datetime.datetime.now()

# Discord Imports
import disnake as discord
import disnake
from disnake.ext import commands, tasks
from disnake.ui import View
from disnake import ButtonStyle
intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="b.", intents=intents)
bot.remove_command("help")

# Memory Lists
# Leave all empty, bot will modify when necessary

jdsupervisors = []
jdmembers = []
seniorstaff = []
staff = []
staffintraining = []
lastxp = {}

# Settings

# Charges List
charges = {
    "Pedophilia": 30,
    "Jailbaiting": 30,
    "Doxxing": 30,
    "IP Grabbing": 25,
    "Info Leaking": 25,
    "DDoSing": 25,
    "Tech Leaking": 15,
    "Account Compromising": 15,
    "Admin Abusing": 15,
    "Theft": 15
}

# this system is so weak, but honestly, idgaf
# Server IDs
mainid = 890352746803376148
jdid = 901558113616924693

# Role IDs
# Main Server
raidrequestid = 901089364904390676
snrstaffid = 901081321982541834
staffid = 890353236165406720
staffitid = 909891995915415582
devid = 901248201154256906
mutedid = 902341042207092736
verifiedid = 901081474470649867
attachmentsid = 901290240227041320

# JD Server
supervisorid = 903357155552415834
justiceid = 903352065852579850
jdverifiedid = 903351930397552681

# Channel IDs
# Main Server
clannewsid = 890352878588399646
generalid = 890352746803376153
botcmdsid = 901080264619491418
recruitmentid = 904486522856812565
suggestionsid = 901272994259812422
resourceannouncementid = 901473336150851664
logsid = 890353977647054909
modlogsid = 905537482542706718

# JD Server
newcasesid = 903359607513186344
caselookupid = 903358269668589700

# Emoji IDs
upvoteid = 932333038296252457
downvoteid = 932333037906190377

# Lists

# Activities
# Sub-lists must have 2 values; discord.ActivityType and a string
activities = [
    [discord.ActivityType.playing, "with a boop noodle | b.help"],
    [discord.ActivityType.watching, "over you | b.help"],
    [discord.ActivityType.listening, "the hisses of danger ropes | b.help"],
    [discord.ActivityType.playing, "with fire | b.help"],
    [discord.ActivityType.playing, "with puppies | b.help"],
    [discord.ActivityType.watching, "your montages | b.help"],
    [discord.ActivityType.listening, "the list of my war crimes | b.help"],
    [discord.ActivityType.listening, "your packing sessions | b.help"],
    [discord.ActivityType.watching, "over the Shadow Realm | b.help"],
    [discord.ActivityType.playing, "Circle Reach Simulator | b.help"],
    [discord.ActivityType.playing, "with your heart | b.help"],
    [discord.ActivityType.watching, "anime | b.help"],
    [discord.ActivityType.watching, "hentai | b.help"],
    [discord.ActivityType.playing, "Florida Simulator | b.help"],
    [discord.ActivityType.playing, "with bombs | b.help"],
    [discord.ActivityType.playing, "War Crime Simulator | b.help"],
    [discord.ActivityType.listening, "to the crackles of a campfire | b.help"]
]

# Clan News Messages
# Each value must be a string
clannewsmessages = [
    f"There is a new post in <#{clannewsid}>, check it out!",
    f"Spotlight uh, moonlight uh, someone posted in <#{clannewsid}> check it out uh!",
    f"It appears another member of this community has posted in <#{clannewsid}>. If you seek enlightenment, do not hesitate to feast your eyes upon the channel!",
    f"There's a new post in <#{clannewsid}>! Did Valax finally shutdown? Did SCAR takeover? Well, there's only one way to find out!",
    f"There's new clanning news! Better go check <#{clannewsid}>!",
    f"New clanning news in <#{clannewsid}>! There is a 99.8295298% chance that it is cool!"
]

# Safe Text
# Each must be a single word that isn't filtered by Roblox
# the roblox filter can suck it
safetext = [
    "hello",
    "hi",
    "howdy",
    "welcome",
    "hey",
    "good",
    "pardon",
    "happy",
    "flower",
    "sunny",
    "rainbow",
    "clouds",
    "friend",
    "epic",
    "devforums",
    "build",
    "gamer",
    "staff",
    "egg",
    "jelly",
    "job",
    "funny",
    "moo",
    "glass",
    "groups",
    "birdy",
    "haha",
    "manager",
    "pizza",
    "yellow",
    "code",
    "command",
    "api",
    "bird",
    "candy",
    "quality",
    "development",
    "general",
    "plane",
    "college",
    "visual",
    "dog",
    "tail",
    "time",
    "roblox",
    "verify"
]

# Auto Responses
# Sub-lists must have 2 strings; trigger and response
autoresponses = [
    ["invite", "https://discord.gg/EpNJmEK6KY"],
    ["jd", "https://discord.gg/Batz4VaJpm"],
    ["sorry", "tf you mean, you aint sorry"],
    ["fuck you", "THATS MY JOB"],
    ["lovely", "the built different canadian"],
    ["lancer", "forever 17"],
    ["newgen", "ay bro why is this not anti ft heal 5v5 static subs"],
    ["oldgen", "the future is here old man"]
]

# Blacklisted Links
# Each value must be a URL without protocol
# absolute blast trying to find these
blacklistedlinks = [
    "pornhub.com",
    "hanime.tv",
    "theporndude.com",
    "animeidhentai.com",
    "hentai.tv",
    "rule34video.com",
    "muchohentai.com",
    "hentaimama.io",
    "ohentai.org",
    "hentaiworld.tv",
    "hentaigasm.com",
    "hentaistream.com",
    "hentaiplay.net",
    "xvideos.com",
    "underhentai.net",
    "xanimeporn.com",
    "hentaihaven.com",
    "hentaitube.online",
    "hentai-moon.com",
    "miohentai.com",
    "hentaicore.org",
    "hentais.tube",
    "hentaifreak.org",
    "hentaicloud.com",
    "erotic-hentai.com",
    "hentaiyes.com",
    "hentaifox.tv",
    "animestigma.com",
    "xhamster.com",
    "xnxx.com",
    "beeg.com",
    "daftsex.com",
    "spankbang.com",
    "discorcl.click",
    "discordgift.link",
    "grabify.link",
    "gyazo.nl",
    "v3rmillion.net",
    "iplogger.org",
    "whatstheirip.com",
    "dlscord-claim.com",
    "discord-claim.com",
    "discorcl.gift",
    "steamdiscord.com",
    "discord-app.net",
    "discrod.xyz",
    "steamdlscords.com",
    "dlscord.org",
    "disocrd.gifts",
    "discorde.gift",
    "bit.ly",
    "doxbin.com",
    "dischrdapp.com"
]

# Blacklisted Text
# Each value must be a string
# automod be like
blacklistedtext = [
    "nigga",
    "nigger",
    "nibba",
    "faggot",
    "chink chonk"
]

# Asyncio Imports
import asyncio
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# SQLite3 Imports + Initialization
import db
from sqlite3 import Error
connection = db.connection

# ro.py Imports
import roblox as ro_py
from roblox.utilities import exceptions
RoClient = ro_py.Client()

# aiohttp Imports
import aiohttp
bloxlinkrequests = 0
roverrequests = 0

# Pastebin Imports
import pbwrap
pastebin = pbwrap.Pastebin("VymtFkEC4e_8SDMauphVAOK7RSaqhZHa")
pastebin.authenticate("BDJD", "Aar0n2007bladejd")
# planned on detecting nsfw images, but discord does a good enough job
"""
# Nudenet Imports
from nudenet import NudeDetector
nsfwdetect = NudeDetector()
imgformats = [
    "jpg",
    "png",
    "jpeg",
    "webp",
    "jfif",
    "pjpeg",
    "pjp"
]
nsfwdetections = [
    "EXPOSED_ANUS",
    "EXPOSED_BUTTOCKS",
    "EXPOSED_BREAST_F",
    "COVERED_GENITALIA_F",
    "EXPOSED_GENITALIA_F",
    "EXPOSED_GENITALIA_M"
]
"""

# RegEx Imports
import re
durationpattern = re.compile(r"^([0-9]+)([smhdw])$")
invitepattern = re.compile(r"(?:https?://)?(?:www\.)?(?:discord(?:app)?)?[\. ]?(?<!. )(?:gg|com)[\/ ](?:invite[\/ ])?([\w\-]{2,})(?! ?.)")
mentionpattern = re.compile(r"<@!?(\d+)>")
usernamepattern = re.compile(r"(\w+)#\d{4,}")
linkpattern = re.compile(r"(\w+\.\w+)")

# Logging Imports
import logging
logger = logging.Logger(__name__, level=logging.DEBUG)
fh = logging.FileHandler(filename="/discordbot/current.log", mode="a", encoding="utf-8")
formatter = logging.Formatter(fmt="[%(asctime)s] %(levelname)s: %(message)s", datefmt="%d/%m/%Y %H:%M:%S")
fh.setFormatter(formatter)
logger.addHandler(fh)

# Misc Imports
import random
import traceback
import uuid
import shortuuid
import aioschedule
import os
import pathlib
import typing
import math

# Utility Functions

async def parse_duration(duration: str | datetime.timedelta=None, mode: str=None, startdt: datetime.datetime=None) -> str | datetime.datetime: # type: ignore
    if duration == None:
        raise TypeError("A duration string was not provided")
    if mode == None:
        raise TypeError("A mode was not provided")
    if mode == "string":
        if isinstance(duration, str):
            if duration[0].isnumeric() == True:
                found = durationpattern.search(duration)
                if isinstance(found, re.Match):
                    time = found.group(1)
                    dtype = found.group(2)
                    match dtype:
                        case "s":
                            return f"{str(time)} seconds"
                        case "m":
                            return f"{str(time)} minutes"
                        case "h":
                            return f"{str(time)} hours"
                        case "d":
                            return f"{str(time)} days"
                        case "w":
                            return f"{str(time)} weeks"
                        case _:
                            raise ValueError("The given duration type is invalid")
                else:
                    raise ValueError("The given duration is invalid")
        else:
            raise ValueError("The given duration is invalid")
    elif mode == "enddatetime":
        if isinstance(duration, str):
            if duration[0].isnumeric() == True:
                if not isinstance(startdt, datetime.datetime):
                    startdt = datetime.datetime.now()
                found = durationpattern.search(duration)
                if isinstance(found, re.Match):
                    time = int(found.group(1))
                    dtype = found.group(2)
                    match dtype:
                        case "s":
                            return startdt + datetime.timedelta(seconds=time)
                        case "m":
                            return startdt + datetime.timedelta(minutes=time)
                        case "h":
                            return startdt + datetime.timedelta(hours=time)
                        case "d":
                            return startdt + datetime.timedelta(days=time)
                        case "w":
                            return startdt + datetime.timedelta(weeks=time)
                        case _:
                            raise ValueError("The given duration is invalid")
                else:
                    raise ValueError("The given duration is invalid")
            else:
                raise ValueError("The given duration is invalid")
    else:
        raise ValueError("The passed mode to parse the duration to is invalid")

async def punishment(member: discord.Member | discord.User=None, ptype: str=None, duration: datetime.datetime=None, punishmentid: str=None) -> None:
    if not isinstance(member, discord.Member) and not isinstance(member, discord.User):
        raise TypeError("Member argument is not a user or member")
    if not isinstance(ptype, str):
        raise TypeError("Punishment type argument is not a string")
    if not isinstance(duration, datetime.datetime) and duration != None:
        raise TypeError("Duration argument is not a datetime or None")
    if not isinstance(punishmentid, str):
        raise TypeError("Punishment ID argument is not a string")
    server = await bot.fetch_guild(mainid)
    match ptype:
        case "ban":
            if duration == None:
                return
            await discord.utils.sleep_until(when=duration)
            try:
                server = await bot.fetch_guild(mainid)
                await server.unban(member, reason="Auto Unban")
            except discord.Forbidden:
                logger.error(f"Failed to unban {member.name}#{member.discriminator} ({member.id})")
            logs = await server.fetch_channel(modlogsid)
            embed = await create_log(member, await server.fetch_member(bot.user.id), "Auto Unban", "unban", punishmentid)
            if isinstance(logs, discord.TextChannel):
                await logs.send(embed=embed)
        case _:
            raise ValueError("Punishment type is invalid")

async def create_embed(embedtype: str) -> discord.Embed:
    embed = discord.Embed()
    embed.set_footer(text="Created by FireMaster", icon_url="https://i.imgur.com/0tfjipc.png")
    match embedtype:
        case "jd":
            embed.set_footer(text="Created by FireMaster", icon_url="https://i.imgur.com/IhJheJc.png")
            embed.color = discord.Color.dark_blue()
        case "roblox":
            embed.set_footer(text="Created by FireMaster", icon_url="https://i.imgur.com/znSP2w1.png")
            embed.color = discord.Color.red()
        case "red":
            embed.color = discord.Color.red()
        case "green":
            embed.color = discord.Color.green()
        case "blue":
            embed.color = discord.Color.blue()
        case "yellow":
            embed.color = discord.Color.yellow()
        case _:
            embed.color = discord.Color.from_rgb(255, 255, 255)
    embed.timestamp = datetime.datetime.now()
    return embed

async def create_safetext(number: int) -> str:
    text = ""
    last = False
    for i in range(1, number+1):
        chc = random.choice(safetext)
        if last:
            text = text + str(chc)
        else:
            text = text + str(chc) + " "
        if i == number-1:
            last = True
    return text

async def create_log(user: discord.Member | discord.User, punisher: discord.Member | discord.User, reason: str, ptype: str, punishmentid: str=None, duration: str=None) -> discord.Embed:
    embed = await create_embed("global")
    match ptype:
        case "kick":
            embed.title = "User Kicked"
        case "ban":
            embed.title = "User Banned"
        case "unban":
            embed.title = "User Unbanned"
        case "mute":
            embed.title = "User Muted"
        case "unmute":
            embed.title = "User Unmuted"
        case "warn":
            embed.title = "User Warned"
        case _:
            embed.title = "User Received Punishment"
    embed.add_field(name="User", value=f"{user.mention} | {user.name}#{user.discriminator} | {user.id}", inline=False)
    embed.add_field(name="Punisher", value=f"{punisher.mention} | {punisher.name}#{punisher.discriminator} | {punisher.id}", inline=False)
    embed.add_field(name="Reason", value=reason, inline=False)
    if duration != None:
        embed.add_field(name="Duration", value=await parse_duration(duration, "string"), inline=True)
    if punishmentid != None:
        embed.add_field(name="Punishment ID", value=punishmentid, inline=True)
    return embed

# should i have consolidated these into one function? yes. am i going to fix it? fuck no.
async def is_supervisor(ctx: commands.Context | discord.Message | discord.CommandInteraction | discord.MessageInteraction=None) -> bool:
    if ctx == None:
        raise TypeError("A context object was not provided when checking for Supervisor permissions")
    if isinstance(ctx, discord.MessageInteraction | discord.CommandInteraction) and isinstance(ctx.user, discord.Member | discord.User):
        return ctx.user.id in jdsupervisors
    return ctx.author.id in jdsupervisors

async def is_justice(ctx: commands.Context | discord.Message | discord.CommandInteraction | discord.MessageInteraction=None) -> bool:
    if ctx == None:
        raise TypeError("A context object was not provided when checking for Justice permissions")
    if isinstance(ctx, discord.MessageInteraction | discord.CommandInteraction) and isinstance(ctx.user, discord.Member | discord.User):
        return ctx.user.id in jdmembers
    return ctx.author.id in jdmembers

async def is_snr_staff(ctx: commands.Context | discord.Message | discord.CommandInteraction | discord.MessageInteraction=None) -> bool:
    if ctx == None:
        raise TypeError("A context object was not provided when checking for Senior Staff permissions")
    if isinstance(ctx, discord.MessageInteraction | discord.CommandInteraction) and isinstance(ctx.user, discord.Member | discord.User):
        return ctx.user.id in seniorstaff
    return ctx.author.id in seniorstaff

async def is_staff(ctx: commands.Context | discord.Message | discord.CommandInteraction | discord.MessageInteraction=None) -> bool:
    if ctx == None:
        raise TypeError("A context object was not provided when checking for Staff permissions")
    if isinstance(ctx, discord.MessageInteraction | discord.CommandInteraction) and isinstance(ctx.user, discord.Member | discord.User):
        return ctx.user.id in staff
    return ctx.author.id in staff

async def is_staffit(ctx: commands.Context | discord.Message | discord.CommandInteraction | discord.MessageInteraction=None) -> bool:
    if ctx == None:
        raise TypeError("A context object was not provided when checking for Staff in Training permissions")
    if isinstance(ctx, discord.MessageInteraction | discord.CommandInteraction) and isinstance(ctx.user, discord.Member | discord.User):
        return ctx.user.id in staffintraining
    return ctx.author.id in staffintraining

async def is_mod(ctx: commands.Context | discord.Message | discord.CommandInteraction | discord.MessageInteraction=None) -> bool:
    if ctx == None:
        raise TypeError("A context object was not provided when checking for Moderator permissions")
    if isinstance(ctx, discord.MessageInteraction | discord.CommandInteraction) and isinstance(ctx.user, discord.Member | discord.User):
        return ctx.user.id in staffintraining or ctx.user.id in staff or ctx.user.id in seniorstaff
    return ctx.author.id in staffintraining or ctx.author.id in staff or ctx.author.id in seniorstaff

# actual pain in the ass to write
async def is_developer(ctx: commands.Context | discord.Message | discord.CommandInteraction | discord.MessageInteraction=None) -> typing.Tuple[bool, str]:
    if ctx == None:
        raise TypeError("A context object was not provided when checking for Developer permissions")
    if isinstance(ctx, discord.MessageInteraction | discord.CommandInteraction) and ctx.guild != None:
        if isinstance(ctx.user, discord.Member):
            if ctx.guild.id == mainid:
                if ctx.user.get_role(devid) == None:
                    return False, "role"
            else:
                bh = await bot.fetch_guild(mainid)
                if bh in ctx.user.mutual_guilds:
                    mem = await bh.fetch_member(ctx.user.id)
                    if mem.get_role(devid) == None:
                        return False, "role"
                else:
                    return False, "server"
        else:
            if isinstance(ctx.user, discord.User):
                bh = await bot.fetch_guild(mainid)
                if bh in ctx.user.mutual_guilds:
                    mem = await bh.fetch_member(ctx.user.id)
                    if mem.get_role(devid) == None:
                        return False, "role"
                else:
                    return False, "server"
    elif isinstance(ctx.author, discord.Member) and ctx.guild != None:
        if ctx.guild.id == mainid:
            if ctx.author.get_role(devid) == None:
                return False, "role"
        else:
            bh = await bot.fetch_guild(mainid)
            if bh in ctx.author.mutual_guilds:
                mem = await bh.fetch_member(ctx.author.id)
                if mem.get_role(devid) == None:
                    return False, "role"
            else:
                return False, "server"
    else:
        bh = await bot.fetch_guild(mainid)
        if bh in ctx.author.mutual_guilds:
            mem = await bh.fetch_member(ctx.author.id)
            if mem.get_role(devid) == None:
                return False, "role"
        else:
            return False, "server"
    return True, "dev"

# View Item Classes
# views are so weird, and i wish i didnt have to use them. these also wouldve been great as just one function.
class casepageselect(discord.ui.Select):
    def __init__(self, options):
        id = uuid.uuid4().hex
        super().__init__(placeholder="Select case to view", custom_id=str(id), min_values=1, max_values=1, options=options)
        self.pressed = False
    async def callback(self, interaction: discord.MessageInteraction):
        self.pressed = True
        if self.view != None:
            self.view.stop()

class closebutton(discord.ui.Button):
    def __init__(self):
        super().__init__(label="Close", custom_id="close", style=ButtonStyle.danger)
        self.pressed = False
    async def callback(self, interaction: discord.MessageInteraction):
        await interaction.message.delete()
        self.pressed = True

class chargeselect(discord.ui.Select):
    def __init__(self):
        id = uuid.uuid4().hex
        super().__init__(placeholder="Please select at least 1 charge", custom_id=str(id), min_values=1, max_values=13, options=[
            discord.SelectOption(label="Pedophilia", description="Having sexual interactions with minor(s).", value="Pedophilia"),
            discord.SelectOption(label="Jailbaiting", description="Lying about age to trick other(s) into Pedophilia.", value="Jailbaiting"),
            discord.SelectOption(label="Doxxing", description="Obtaining someone's personal information.", value="Doxxing"),
            discord.SelectOption(label="IP Grabbing", description="Obtaining or attempting to obtain a person's IP.", value="IP Grabbing"),
            discord.SelectOption(label="Info Leaking", description="Reposting a dox/expanding the audience of private information", value="Info Leaking"),
            discord.SelectOption(label="DDoSing", description="Knocking a person(s) offline.", value="DDoSing"),
            discord.SelectOption(label="Tech Leaking", description="Distributing private assets without permission.", value="Tech Leaking"),
            discord.SelectOption(label="Account Compromising", description="Compromising the accounts of others.", value="Account Compromising"),
            discord.SelectOption(label="Admin Abusing", description="Abusing a position's permissions to harm property.", value="Admin Abusing"),
            discord.SelectOption(label="Theft", description="Stealing content that is not rightfully owned.", value="Theft"),
            discord.SelectOption(label="Malicious Distribution", description="Distributing/selling malicious programs/scripts.", value="Malicious Distribution"),
            discord.SelectOption(label="Exploiting", description="Using an external program to exploit issues within game code", value="Exploiting"),
            discord.SelectOption(label="Scamming", description="Getting something of value and not giving payment.", value="Scamming")
        ])
        self.pressed = False
    async def callback(self, interaction: discord.MessageInteraction):
        self.pressed = True
        if self.view != None:
            self.view.stop()

class skipbutton(discord.ui.Button):
    def __init__(self):
        id = uuid.uuid4().hex
        super().__init__(label="Skip", custom_id=str(id), style=ButtonStyle.danger)
        self.pressed = False
    async def callback(self, interaction: discord.MessageInteraction):
        self.pressed = True
        await interaction.response.defer()
        if self.view != None:
            self.view.stop()

class donebutton(discord.ui.Button):
    def __init__(self):
        id = uuid.uuid4().hex
        super().__init__(label="Done", custom_id=str(id), style=ButtonStyle.green)
        self.pressed = False
        async def done(interaction: discord.MessageInteraction):
            self.pressed = True
        self.callback = done
    async def wait(self):
        while self.pressed == False:
            await asyncio.sleep(0.03)
        return True

class confirmbutton(discord.ui.Button):
    def __init__(self):
        id = uuid.uuid4().hex
        super().__init__(label="Confirm", custom_id=str(id), style=ButtonStyle.green)
        self.pressed = False
    async def callback(self, interaction: discord.MessageInteraction):
        self.pressed = True
        await interaction.response.defer()
        if self.view != None:
            self.view.stop()

class editbutton(discord.ui.Button):
    def __init__(self):
        id = uuid.uuid4().hex
        super().__init__(label="Edit", custom_id=str(id), style=ButtonStyle.danger)
        self.pressed = False
    async def callback(self, interaction: discord.MessageInteraction):
        self.pressed = True
        if self.view != None:
            self.view.stop()

class jpeditselect(discord.ui.Select):
    def __init__(self, caseinfo: typing.Dict[str, str]):
        id = uuid.uuid4().hex
        for field in caseinfo:
            field = field.replace("|", "\n")
            if field.__len__() > 100:
                newstr = ""
                for i in range(0, 98):
                    newstr = newstr + field[i]
                field = newstr + "..."
        super().__init__(placeholder="Please select the fields you would like to edit", custom_id=str(id), min_values = 1, max_values = 7, options = [
            discord.SelectOption(label="Charges", description=caseinfo['charge'], value="charges"),
            discord.SelectOption(label="Proof", description=caseinfo['proof'], value="proof"),
            discord.SelectOption(label="Discord ID(s)", description=caseinfo['did'], value="did"),
            discord.SelectOption(label="Discord Username(s)", description=caseinfo['dusername'], value="dusername"),
            discord.SelectOption(label="Roblox ID(s)", description=caseinfo['rid'], value="rid"),
            discord.SelectOption(label="Roblox Username(s)", description=caseinfo['rusername'], value="rusername"),
            discord.SelectOption(label="Notes", description=caseinfo['notes'], value="notes")
        ])
        self.pressed = False
    async def callback(self, interaction: discord.MessageInteraction):
        self.pressed = True
        if self.view != None:
            self.view.stop()

class bloxlinkbutton(discord.ui.Button):
    def __init__(self):
        id = uuid.uuid4().hex
        super().__init__(label="Bloxlink", custom_id=str(id), style=ButtonStyle.primary)
        self.pressed = False
    async def callback(self, interaction: discord.MessageInteraction):
        self.pressed = True
        if self.view != None:
            self.view.stop()

class rbxboltbutton(discord.ui.Button):
    def __init__(self):
        id = uuid.uuid4().hex
        super().__init__(label="RBXBolt", custom_id=str(id), style=ButtonStyle.primary)
        self.pressed = False
    async def callback(self, interaction: discord.MessageInteraction):
        self.pressed = True
        if self.view != None:
            self.view.stop()

class roverbutton(discord.ui.Button):
    def __init__(self):
        id = uuid.uuid4().hex
        super().__init__(label="RoVer", custom_id=str(id), style=ButtonStyle.primary)
        self.pressed = False
    async def callback(self, interaction: discord.MessageInteraction):
        self.pressed = True
        if self.view != None:
            self.view.stop()

class bhbutton(discord.ui.Button):
    def __init__(self):
        id = uuid.uuid4().hex
        super().__init__(label="BH", custom_id=str(id), style=ButtonStyle.primary)
        self.pressed = False
    async def callback(self, interaction: discord.MessageInteraction):
        self.pressed = True
        if self.view != None:
            self.view.stop()

class verifybutton(discord.ui.Button):
    def __init__(self):
        id = uuid.uuid4().hex
        super().__init__(label="Verify", custom_id=str(id), style=ButtonStyle.green)
        self.pressed = False
    async def callback(self, interaction: discord.MessageInteraction):
        self.pressed = True
        if self.view != None:
            self.view.stop()

class caselookupbutton(discord.ui.Button):
    def __init__(self):
        super().__init__(label="Case Lookup", style=ButtonStyle.blurple, url="discord://discordapp.com/channels/901558113616924693/903358269668589700")

class resourcetypeselect(discord.ui.Select):
    def __init__(self):
        id = uuid.uuid4().hex
        super().__init__(placeholder="Please select a resource type", custom_id=str(id), min_values=1, max_values=1, options=[
            discord.SelectOption(label="Sword", description="A sword or sword system.", value="Sword"),
            discord.SelectOption(label="Objective", description="Terminal, payload, etc.", value="Objective"),
            discord.SelectOption(label="Utility", description="Team counter, deployment system, doesn't fit into other categories.", value="Utility"),
            discord.SelectOption(label="Guide", description="How to build something, collection of tips, etc.", value="Guide"),
            discord.SelectOption(label="Building", description="Fort, training facility, map assets, etc.", value="Building"),
            discord.SelectOption(label="Anti Exploit", description="Prevents exploiting in some capacity.", value="Anti Exploit"),
            discord.SelectOption(label="GFX", description="Logo, uniform, etc.", value="GFX"),
            discord.SelectOption(label="Mini Script", description="Not in model form.", value="Mini Script")
        ])
        self.pressed = False
    async def callback(self, interaction: discord.MessageInteraction):
        self.pressed = True
        if self.view != None:
            self.view.stop()

class resourceeditselect(discord.ui.Select):
    def __init__(self, resourceinfo):
        id = uuid.uuid4().hex
        for field in resourceinfo:
            if field.__len__() > 100:
                newstr = ""
                for i in range(0, 98):
                    newstr = newstr + field[i]
                field = newstr + "..."
        super().__init__(placeholder="Please select the fields you would like to edit", custom_id=str(id), min_values = 1, max_values = 4, options = [
            discord.SelectOption(label="Type", description=f"Current Type: {resourceinfo['type']}", value="type"),
            discord.SelectOption(label="Name", description=f"Current Name: {resourceinfo['name']}", value="name"),
            discord.SelectOption(label="Description", description=f"Current Description: {resourceinfo['description']}", value="description"),
            discord.SelectOption(label="Link", description=f"Current Link: {resourceinfo['link']}", value="link")
        ])
        self.pressed = False
    async def callback(self, interaction: discord.MessageInteraction):
        self.pressed = True
        if self.view != None:
            self.view.stop()

class resourcesearchfilterselect(discord.ui.Select):
    def __init__(self):
        id = uuid.uuid4().hex
        super().__init__(placeholder="Filter by..", custom_id=str(id), min_values = 1, max_values = 1, options = [
            discord.SelectOption(label="Vouches High-Low", description=f"How popular the resource is", value="vouchesdesc"),
            discord.SelectOption(label="Vouches Low-High", description=f"How unpopular the resource is", value="vouchesasc"),
            discord.SelectOption(label="Alphabetical A-Z", description=f"Alphabetical by name, from A-Z", value="alphasc"),
            discord.SelectOption(label="Alphabetical Z-A", description=f"Alphabetical by name, from Z-A", value="alphdesc")
        ])
        self.pressed = False
    async def callback(self, interaction: discord.MessageInteraction):
        self.pressed = True
        if self.view != None:
            self.view.stop()

class resourcesearchpageselect(discord.ui.Select):
    def __init__(self, pages, currentpage):
        id = uuid.uuid4().hex
        options = []
        i = 1
        for page in pages:
            if currentpage != i:
                options.append(discord.SelectOption(label=f"Page {i}", value=str(i-1)))
            i = sum((i, 1))
        super().__init__(placeholder="View page..", custom_id=str(id), min_values = 1, max_values = 1, options = options)
        self.pressed = False
    async def callback(self, interaction: discord.MessageInteraction):
        self.pressed = True
        if self.view != None:
            self.view.stop()

class resourcelinkbutton(discord.ui.Button):
    def __init__(self):
        super().__init__(label="Open Resource", style=ButtonStyle.blurple, url="https://google.com")

class resourcevouchbutton(discord.ui.Button):
    def __init__(self, rid):
        id = uuid.uuid4().hex
        super().__init__(label="Vouch", custom_id=str(id), style=ButtonStyle.primary)
        self.pressed = False
        self.resourceid = rid
    async def callback(self, interaction: discord.MessageInteraction):
        await interaction.response.defer(ephemeral=True)
        if connection != None:
            cursor = connection.cursor()
            cursor.execute("select vouches from resources where id=?", (self.resourceid))
            rows = cursor.fetchall()
            if rows.__len__() >= 1:
                if rows[0][7].find(f"{interaction.author.id}|") == -1:
                    rows[0][7] = rows[0][7] + f"{interaction.author.id}|"
                    embed = await create_embed("global")
                    embed.title = "BH Open Resource"
                    embed.description = "Vouch given!"
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                    return
                else:
                    embed = await create_embed("global")
                    embed.title = "BH Open Resource"
                    embed.description = "You've already vouched for this resource!"
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                    return
            else:
                embed = await create_embed("global")
                embed.title = "BH Open Resource"
                embed.description = "Uh oh! An error occured when vouching. Please try again later, and contact <@464096668879683594> if the issue persists!"
                await interaction.response.send_message(embed=embed, ephemeral=True)
                return
        else:
            embed = await create_embed("global")
            embed.title = "BH Open Resource"
            embed.description = "The database is currently inaccessible."
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return

class upvotebutton(discord.ui.Button):
    def __init__(self):
        id = uuid.uuid4().hex
        super().__init__(label="Upvote", custom_id=str(id), style=ButtonStyle.green)
        self.pressed = False
    async def callback(self, interaction: discord.MessageInteraction):
        if await is_justice(interaction) == True:
            self.pressed = True
            if self.view != None:
                self.view.stop()
        else:
            await interaction.response.send_message(content="You don't have permission to upvote!", ephemeral=True)
            
class downvotebutton(discord.ui.Button):
    def __init__(self):
        id = uuid.uuid4().hex
        super().__init__(label="Downvote", custom_id=str(id), style=ButtonStyle.red)
        self.pressed = False
    async def callback(self, interaction: discord.MessageInteraction):
        if await is_justice(interaction) == True:
            self.pressed = True
            if self.view != None:
                self.view.stop()
        else:
            await interaction.response.send_message(content="You don't have permission to downvote!", ephemeral=True)

class view(View):
    def __init__(self, timeout: float=180):
        super().__init__(timeout=timeout)

# Database Classes

class Case():
    def __init__(
        self,
        caseid: int,
        charges: str,
        status: str,
        proof: str,
        postdate: datetime.datetime | str,
        expiredate: datetime.datetime | str,
        dusername: str,
        did: str,
        rusername: str,
        rid: str,
        notes: str,
        severity: int
    ):
        self.caseid = caseid
        self.charges = charges
        self.status = status
        self.proof = proof
        self.postdate = postdate
        self.expiredate = expiredate
        self.dusername = dusername
        self.did = did
        self.rusername = rusername
        self.rid = rid
        self.notes = notes
        self.severity = severity
    async def edit(self, fields: typing.Dict[str, str | int]) -> None:
        cursor = connection.cursor()
        values = ""
        for i, v in fields.items():
            match i:
                case "id":
                    if not isinstance(v, int):
                        raise TypeError("Attempted to edit case ID with non-integer")
                    if values != "":
                        values = f"{values}, id = {str(v)}"
                    else:
                        values = f"id = {str(v)}"
                    self.caseid = v
                case "charges":
                    if not isinstance(v, str):
                        raise TypeError("Attempted to edit case charges with non-string")
                    if values != "":
                        values = f"{values}, charge = '{v}'"
                    else:
                        values = f"charge = '{v}'"
                    self.charges = v
                case "status":
                    if not isinstance(v, str):
                        raise TypeError("Attempted to edit case status with non-string")
                    if values != "":
                        values = f"{values}, status = '{v}'"
                    else:
                        values = f"status = '{v}'"
                    self.status = v
                case "proof":
                    if not isinstance(v, str):
                        raise TypeError("Attempted to edit case proof with non-string")
                    if values != "":
                        values = f"{values}, proof = '{v}'"
                    else:
                        values = f"proof = '{v}'"
                    self.proof = v
                case "postdate":
                    if not isinstance(v, datetime.datetime):
                        raise TypeError("Attempted to edit case post date with non-datetime")
                    if values != "":
                        values = f"{values}, postdate = '{v.strftime('%d/%m/%Y')}'"
                    else:
                        values = f"postdate = '{v.strftime('%d/%m/%Y')}'"
                    self.postdate = v
                case "expiredate":
                    if not isinstance(v, datetime.datetime):
                        raise TypeError("Attempted to edit case expire date with non-datetime")
                    if values != "":
                        values = f"{values}, expiredate = '{v.strftime('%d/%m/%Y')}'"
                    else:
                        values = f"expiredate = '{v.strftime('%d/%m/%Y')}'"
                    self.expiredate = v
                case "dusername":
                    if not isinstance(v, str):
                        raise TypeError("Attempted to edit case Discord username with non-string")
                    if values != "":
                        values = f"{values}, dusername = '{v}'"
                    else:
                        values = f"dusername = '{v}'"
                    self.dusername = v
                case "did":
                    if not isinstance(v, str):
                        raise TypeError("Attempted to edit case Discord ID with non-string")
                    if values != "":
                        values = f"{values}, did = '{v}'"
                    else:
                        values = f"did = '{v}'"
                    self.did = v
                case "rusername":
                    if not isinstance(v, str):
                        raise TypeError("Attempted to edit case Roblox username with non-string")
                    if values != "":
                        values = f"{values}, rusername = '{v}'"
                    else:
                        values = f"rusername = '{v}'"
                    self.rusername = v
                case "rid":
                    if not isinstance(v, str):
                        raise TypeError("Attempted to edit case Roblox ID with non-string")
                    if values != "":
                        values = f"{values}, rid = '{v}'"
                    else:
                        values = f"rid = '{v}'"
                    self.rid = v
                case "notes":
                    if not isinstance(v, str):
                        raise TypeError("Attempted to edit case notes with non-string")
                    if values != "":
                        values = f"{values}, notes = '{v}'"
                    else:
                        values = f"notes = '{v}'"
                    self.notes = v
                case "severity":
                    if not isinstance(v, int):
                        raise TypeError("Attempted to edit case severity with non-integer")
                    if values != "":
                        values = f"{values}, severity = {str(v)}"
                    else:
                        values = f"severity = {str(v)}"
                    self.severity = v
                case _:
                    raise ValueError(f"Attempted to set case field that doesn't exist\nField: {str(i)}")
        cursor.execute(f"update cases set {values} where id = ?", (str(self.caseid),)) # ah yes, the good ol days of manual queries
        return
    async def delete(self) -> None:
        cursor = connection.cursor()
        self.charges = "N/A"
        self.status = "DELETED"
        self.proof = "N/A"
        self.postdate = None
        self.expiredate = None
        self.dusername = "N/A"
        self.did = "N/A"
        self.rusername = "N/A"
        self.rid = "N/A"
        self.notes = "N/A"
        self.severity = 0
        cursor.execute("update cases set charge='N/A|', status='DELETED', proof='N/A|', postdate='N/A', expiredate='N/A', dusername='N/A|', did='|N/A', rusername='N/A|', rid='|N/A', notes='N/A' where id=?", (int(self.caseid),))
        return
    @classmethod
    def from_id(cls, id: int):
        if not isinstance(id, int):
            raise TypeError("Attempted to create case from ID with non-integer")
        cursor = connection.cursor()
        cursor.execute("select * from cases where id = ?", (id,))
        case = cursor.fetchall()
        if case.__len__() >= 1:
            postdate = "NONE"
            expiredate = "NONE"
            try:
                postdate = datetime.datetime.strptime(case[0][4], "%d/%m/%Y")
            except ValueError:
                pass
            try:
                postdate = datetime.datetime.strptime(case[0][5], "%d/%m/%Y")
            except ValueError:
                pass
            return Case(
                id,
                case[0][1],
                case[0][2],
                case[0][3],
                postdate,
                expiredate,
                case[0][6],
                case[0][7],
                case[0][8],
                case[0][9],
                case[0][10],
                case[0][11]
            )
        else:
            raise KeyError("Attempted to create case from ID, but the ID was invalid")

class Resource():
    def __init__(
        self,
        id: int,
        resourcetype: str,
        name: str,
        description: str,
        date: datetime.datetime,
        creator: str,
        vouches: int
    ):
        self.id = id
        self.type = resourcetype
        self.name = name
        self.description = description
        self.date = date
        self.creator = creator
        self.vouches = vouches
    async def edit(self, fields: typing.Dict[str, str | int]) -> None:
        cursor = connection.cursor()
        values = ""
        for i, v in fields.items():
            match i:
                case "id":
                    if not isinstance(v, int):
                        raise TypeError("Attempted to edit case ID with non-integer")
                    if values != "":
                        values = f"{values}, id = {str(v)}"
                    else:
                        values = f"id = {str(v)}"
                    self.caseid = v
                case "type":
                    if not isinstance(v, str):
                        raise TypeError("Attempted to edit case charges with non-string")
                    if values != "":
                        values = f"{values}, charge = '{v}'"
                    else:
                        values = f"charge = '{v}'"
                    self.charges = v
                case "name":
                    if not isinstance(v, str):
                        raise TypeError("Attempted to edit case status with non-string")
                    if values != "":
                        values = f"{values}, status = '{v}'"
                    else:
                        values = f"status = '{v}'"
                    self.status = v
                case "description":
                    if not isinstance(v, str):
                        raise TypeError("Attempted to edit case proof with non-string")
                    if values != "":
                        values = f"{values}, proof = '{v}'"
                    else:
                        values = f"proof = '{v}'"
                    self.proof = v
                case "date":
                    if not isinstance(v, datetime.datetime):
                        raise TypeError("Attempted to edit case post date with non-datetime")
                    if values != "":
                        values = f"{values}, postdate = '{v.strftime('%d/%m/%Y')}'"
                    else:
                        values = f"postdate = '{v.strftime('%d/%m/%Y')}'"
                    self.postdate = v
                case "creator":
                    if not isinstance(v, datetime.datetime):
                        raise TypeError("Attempted to edit case expire date with non-datetime")
                    if values != "":
                        values = f"{values}, expiredate = '{v.strftime('%d/%m/%Y')}'"
                    else:
                        values = f"expiredate = '{v.strftime('%d/%m/%Y')}'"
                    self.expiredate = v
                case "vouches":
                    if not isinstance(v, str):
                        raise TypeError("Attempted to edit case Discord username with non-string")
                    if values != "":
                        values = f"{values}, dusername = '{v}'"
                    else:
                        values = f"dusername = '{v}'"
                    self.dusername = v
                case _:
                    raise ValueError(f"Attempted to set case field that doesn't exist\nField: {str(i)}")
        cursor.execute(f"update cases set {values} where id = ?", (str(self.caseid),))
        return
    async def delete(self) -> None:
        cursor = connection.cursor()
        self.type = "N/A"
        self.name = "N/A"
        self.description = "N/A"
        self.date = None
        self.creator = "N/A"
        self.vouches = 0
        cursor.execute("update cases set type='N/A', name='N/A', description='N/A', date='N/A', creator='N/A', vouches=0 where id=?", (int(self.caseid),))
        return
    @classmethod
    def from_id(cls, id: int):
        if not isinstance(id, int):
            raise TypeError("Attempted to create case from ID with non-integer")
        cursor = connection.cursor()
        cursor.execute("select * from cases where id = ?", (id,))
        case = cursor.fetchall()
        if case.__len__() >= 1:
            return Case(
                id,
                case[0][1],
                case[0][2],
                case[0][3],
                datetime.datetime.strptime(case[0][4], "%d/%m/%Y"),
                datetime.datetime.strptime(case[0][5], "%d/%m/%Y"),
                case[0][6],
                case[0][7],
                case[0][8],
                case[0][9],
                case[0][10],
                case[0][11]
            )
        else:
            raise KeyError("Attempted to create case from ID, but the ID was invalid")

# Loops

lastchoice = None
@tasks.loop(seconds=15)
async def changepres():
    global lastchoice
    def pick():
        choice = random.choice(activities)
        if lastchoice != None:
            if choice == lastchoice:
                return pick()
        return choice
    chc = pick()
    lastchoice = chc
    if chc != None:
        try:
            await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=chc[0], name=chc[1]))
        except:
            logger.error("Failed to change bot presence")
@changepres.before_loop
async def before_changepres():
    await bot.wait_until_ready()

# could the scc do THIS??????
async def expirecases():
    i = 0
    cursor = connection.cursor()
    cursor.execute("select * from cases where status='ACTIVE' and not expiredate='NONE'")
    rows = cursor.fetchall()
    dt = datetime.datetime.today()
    dt = dt.strftime("%d/%m/%Y")
    for row in rows:
        if row[5] == dt:
            cursor.execute("update cases set status = 'CLEARED' where caseid = ?", (row[0],))
            i = sum((i, 1))
            logger.info(f"Low case {row[0]} was cleared for expiration")
            continue
    logger.info(f"Completed case expiration check. Total cases expired: {str(i)}")
aioschedule.every(1).day.at("01:00").do(expirecases)

# Events

@bot.event
async def on_ready():
    cursor = connection.cursor()
    asyncio.create_task(db.commitloop())
    try:
        await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.playing, name="startup noises"))
    except:
        logger.error("Failed to set presence to startup presence!")
    logger.info("Registering supervisors..")
    try:
        privatejp = await bot.fetch_guild(jdid)
        logger.info("Fetched Private JP guild")
        async for member in privatejp.fetch_members():
            if member.get_role(supervisorid) != None:
                jdsupervisors.append(member.id)
                logger.info(f"{member.name}#{member.discriminator} has been registered as a Supervisor!")
    except discord.Forbidden:
        logger.error("Warning: Bot is not in JD Server, Supervisor commands will not be available!")
    logger.info("Registering senior staff..")
    try:
        main = await bot.fetch_guild(mainid)
        async for member in main.fetch_members():
            if member.get_role(snrstaffid) != None:
                seniorstaff.append(member.id)
                logger.info(f"{member.name}#{member.discriminator} has been registered as a Senior Staff!")
            if member.get_role(staffid) != None:
                staff.append(member.id)
                logger.info(f"{member.name}#{member.discriminator} has been registered as a Staff!")
            if member.get_role(staffitid) != None:
                staffintraining.append(member.id)
                logger.info(f"{member.name}#{member.discriminator} has been registered as a Staff in Training!")
    except discord.Forbidden:
        logger.error("Warning: Bot is not in Main server, Moderator commands will not be available!")
    startpunishments = False
    try:
        server = await bot.fetch_guild(mainid)
        role = server.get_role(raidrequestid)
        if role != None:
            await role.edit(mentionable=True, reason="Outage recovery")
            logger.info("Raids role re-enabled!")
            startpunishments = True
        else:
            logger.error("Unable to re-enable raids role!")
    except:
        logger.error("Unable to re-enable raids role!")
    def pick():
        choice = random.choice(activities)
        if lastchoice != None:
            if choice == lastchoice:
                return pick()
        return choice
    chc = pick()
    if chc != None:
        try:
            await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=chc[0], name=chc[1]))
        except:
            logger.error("Failed to change bot presence!")
    cursor.execute("select * from punishments")
    rows = cursor.fetchall()
    if startpunishments == True:
        try:
            server = await bot.fetch_guild(mainid)
            for row in rows:
                startdt = datetime.datetime.strptime(row[3], "%d/%m/%Y %H:%M:%S")
                enddt = datetime.datetime.strptime(row[4], "%d/%m/%Y %H:%M:%S")
                duration = enddt - startdt
                if duration.total_seconds() > 0:
                    member = await server.fetch_member(row[2])
                    roles = []
                    for role in row[5].split("|"):
                        if role.isnumeric():
                            roles.append(server.get_role(int(role)))
                    asyncio.create_task(punishment(member, row[1], enddt, row[0]))
        except discord.Forbidden:
            logger.error("Bot is not in main server; punishments have not been restarted!")
    else:
        logger.error("Bot is not in main server; punishments have not been restarted!")
    stoptime = datetime.datetime.now()
    logger.info(f"Bot is fully loaded under {str(bot.user.name)}#{bot.user.discriminator} ({str(bot.user.id)}). Total load time was {str((stoptime - starttime).total_seconds())}")
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

@bot.event
async def on_command_error(ctx: commands.Context, err):
    match err:
        case commands.CommandOnCooldown():
            embed = await create_embed("global")
            embed.title = "Cooldown"
            embed.description = f"Slow down there! You need to wait {err.retry_after: .0f} seconds before you can use this!"
            try:
                return await ctx.reply(embed=embed, delete_after=15)
            except discord.HTTPException:
                return await ctx.send(embed=embed, delete_after=15)
        case commands.CommandNotFound():
            return
        case NotImplementedError():
            embed = await create_embed("global")
            embed.title = "Unimplemented Command"
            embed.description = "Uh oh! It looks like this command is currently unimplemented!"
            try:
                return await ctx.reply(embed=embed, delete_after=15)
            except discord.HTTPException:
                return await ctx.send(embed=embed, delete_after=15)
        case discord.Forbidden():
            embed = await create_embed("global")
            embed.title = "Error 403"
            embed.description = "Uh oh! It looks like I was rate limited or forbidden from doing that! Please wait a minute, then try again! If the issue persists, please contact <@464096668879683594>."
            try:
                return await ctx.reply(embed=embed, delete_after=15)
            except discord.HTTPException:
                return await ctx.send(embed=embed, delete_after=15)
        case discord.HTTPException():
            embed = await create_embed("global")
            embed.title = "HTTP Error"
            embed.description = f"Uh oh! Discord returned an HTTPException! Please try again later.\n```\nCode: {err.code}\nText: {err.text}```"
            try:
                return await ctx.reply(embed=embed)
            except discord.HTTPException:
                return await ctx.send(embed=embed)
        case _:
            print("_")
            logger.error(f"Error occured when command {str(ctx.command)} was invoked\nLine {err.__traceback__.tb_lineno}\n{str(err)}")
            embed = await create_embed("global")
            embed.title = "Error"
            embed.description = f"Uh oh, an internal error occured! Try again, and if the issue persists, please contact <@464096668879683594>.\n```{str(err)}```"
            try:
                return await ctx.reply(embed=embed)
            except discord.HTTPException:
                return await ctx.send(embed=embed)

@bot.event
async def on_slash_command_error(interaction: discord.ApplicationCommandInteraction, err):
    match err:
        case commands.CommandOnCooldown():
            embed = await create_embed("global")
            embed.title = "Cooldown"
            embed.description = f"Slow down there! You need to wait {err.retry_after: .0f} seconds before you can use this!"
            await interaction.edit_original_message(embed=embed)
            return await interaction.delete_original_message(delay=15)
        case NotImplementedError():
            embed = await create_embed("global")
            embed.title = "Unimplemented Command"
            embed.description = "Uh oh! It looks like this command is currently unimplemented!"
            await interaction.edit_original_message(embed=embed)
            return await interaction.delete_original_message(delay=15)
        case discord.Forbidden():
            embed = await create_embed("global")
            embed.title = "Error 403"
            embed.description = "Uh oh! It looks like I was rate limited or forbidden from doing that! Please wait a minute, then try again! If the issue persists, please contact <@464096668879683594>."
            await interaction.edit_original_message(embed=embed)
            return await interaction.delete_original_message(delay=15)
        case discord.HTTPException():
            embed = await create_embed("global")
            embed.title = "HTTP Error"
            embed.description = f"Uh oh! Discord returned an HTTPException! Please try again later.\n```\nCode: {err.code}\nText: {err.text}```"
            return await interaction.edit_original_message(embed=embed)
        case _:
            logger.error(f"Error occured when command {str(interaction.application_command.name)} was invoked\nLine {err.__traceback__.tb_lineno}\n{str(err)}")
            embed = await create_embed("global")
            embed.title = "Error"
            embed.description = f"Uh oh, an internal error occured! Try again, and if the issue persists, please contact <@464096668879683594>.\n```{str(err)}```"
            return await interaction.edit_original_message(embed=embed)

@bot.event
async def on_message(message: discord.Message):
    if message.author.id == bot.user.id:
        return
    if isinstance(message.guild, discord.Guild) and isinstance(message.author, discord.Member) and message.guild.id == mainid:
        if await is_snr_staff(message) == False:
            if ( # Anti Invite; actual nightmare to make
                issubclass(type(message.channel), discord.abc.Messageable) and 
                issubclass(type(message.channel), discord.abc.GuildChannel) and 
                not isinstance(message.channel, discord.DMChannel) and
                message.channel.id != recruitmentid
            ):
                if captured := invitepattern.search(message.content):
                    if isinstance(captured, re.Match):
                        code = captured.group(1)
                        try:
                            invite = await bot.fetch_invite(f"https://discord.gg/{code}")
                            if isinstance(invite.guild, discord.PartialInviteGuild):
                                if discord.utils.get(bot.guilds, id=invite.guild.id) == None:
                                    try:
                                        await message.delete()
                                    except discord.Forbidden:
                                        logger.error(f"Forbidden to delete invite in {message.channel.name} ({message.channel.id}\nMessage Link: https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}")
                                    except discord.HTTPException:
                                        logger.error(f"Unable to delete invite in {message.channel.name} ({message.channel.id}\nMessage Link: https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}")
                                    embed = await create_embed("red")
                                    embed.title = "Invite Posted"
                                    logs = await bot.fetch_channel(logsid)
                                    embed.add_field(name="Server", value=f"{invite.guild.name} ({invite.guild.id})", inline=False)
                                    embed.add_field(name="Description", value=invite.guild.description, inline=False)
                                    if isinstance(invite.guild.icon, discord.Asset):
                                        embed.set_thumbnail(url=invite.guild.icon.url)
                                    if isinstance(invite.guild.banner, discord.Asset):
                                        embed.set_image(url=invite.guild.banner.url)
                                    if isinstance(invite.inviter, discord.User):
                                        embed.add_field(name="Inviter", value=f"{invite.inviter.name}#{invite.inviter.discriminator} ({invite.inviter.id})", inline=True)
                                    if isinstance(invite.channel, discord.PartialInviteChannel):
                                        embed.add_field(name="Channel", value=invite.channel.name, inline=True)
                                    if isinstance(invite.approximate_member_count, int) and isinstance(invite.approximate_presence_count, int):
                                        embed.add_field(name="Members", value=f"{invite.approximate_presence_count}/{invite.approximate_member_count}", inline=True)
                                    if isinstance(invite.created_at, datetime.datetime):
                                        embed.add_field(name="Creation Date", value=f"{discord.utils.format_dt(invite.created_at, style='R')} | {discord.utils.format_dt(invite.created_at)}")
                                    await logs.send(embed=embed) # type: ignore
                                    return
                        except discord.NotFound:
                            pass
        for link in blacklistedlinks:
            if message.content.lower().find(link) != -1:
                try:
                    await message.delete()
                except discord.Forbidden:
                    embed = await create_embed("global")
                    embed.title = "Blacklisted Link"
                    embed.description = "A blacklisted link was detected in this message, but I was unable to delete it!"
                    await message.reply(content="<@&890353236165406720>", embed=embed, delete_after=10)
                try:
                    await message.author.ban(reason=f"Posting blacklisted link\n{link}")
                except discord.Forbidden:
                    embed = await create_embed("global")
                    embed.title = "Blacklisted Link"
                    embed.description = f"A blacklisted link was detected in a message sent by {message.author.mention}, but I was unable to ban them!"
                    await message.channel.send(content="<@&890353236165406720>", embed=embed)
                return
        for text in blacklistedtext:
            if message.content.lower().find(text) != -1:
                try:
                    await message.delete()
                    embed = await create_embed("global")
                    embed.title = "Blacklisted Text"
                    embed.description = "Blacklisted text was detected in your message!"
                    await message.channel.send(content=f"{message.author.mention}", embed=embed, delete_after=10)
                except discord.Forbidden:
                    embed = await create_embed("global")
                    embed.title = "Blacklisted Text"
                    embed.description = "Blacklisted text was detected in this message, but I was unable to delete it!"
                    await message.reply(content="<@&890353236165406720>", embed=embed)
                return
        if message.author.bot == False:
            cursor = connection.cursor()
            cursor.execute("select * from xp where id = ?", (message.author.id,))
            rows = cursor.fetchall()
            if rows.__len__() >= 1:
                try:
                    if lastxp[message.author.id] < message.created_at:
                        gained = random.randint(7, 15)
                        neededxp = math.floor(((rows[0][2]+1)/0.07)**2)
                        level = rows[0][2]
                        if neededxp <= gained+rows[0][1]:
                            level += 1
                        cursor.execute("update xp set xp = ?, level = ? where id = ?", (gained+rows[0][1], level, message.author.id))
                        lastxp[message.author.id] = message.created_at + datetime.timedelta(seconds=30)
                        if rows[0][2] < level:
                            embed = await create_embed("global")
                            embed.title = "Level Up"
                            if level == 10 and rows[0][2] != 10:
                                roles = message.author.roles
                                attachments = message.guild.get_role(attachmentsid)
                                if isinstance(attachments, discord.Role):
                                    roles.append(attachments)
                                    await message.author.edit(roles=roles)
                                    embed.description = f"Congratulations! You've reached level {str(level)}!\nYou've unlocked attachment and embed perms!"
                            else:
                                embed.description = f"Congratulations! You've reached level {str(level)}!"
                            await message.reply(embed=embed)
                except KeyError:
                    gained = random.randint(7, 15)
                    neededxp = math.floor(((rows[0][2]+1)/0.07)**2)
                    level = rows[0][2]
                    if neededxp <= gained+rows[0][1]:
                        level += 1
                    cursor.execute("update xp set xp = ?, level = ? where id = ?", (gained+rows[0][1], level, message.author.id))
                    lastxp[message.author.id] = message.created_at + datetime.timedelta(seconds=30)
                    if rows[0][2] < level:
                        embed = await create_embed("global")
                        embed.title = "Level Up"
                        if level == 10 and rows[0][2] != 10:
                            roles = message.author.roles
                            attachments = message.guild.get_role(attachmentsid)
                            if isinstance(attachments, discord.Role):
                                roles.append(attachments)
                                await message.author.edit(roles=roles)
                                embed.description = f"Congratulations! You've reached level {str(level)}!\nYou've unlocked attachment and embed perms!"
                        else:
                            embed.description = f"Congratulations! You've reached level {str(level)}!"
                        await message.reply(embed=embed)
            else:
                gained = random.randint(7, 15)
                cursor.execute("insert into xp values (?, ?, ?)", (message.author.id, gained, 0))
                lastxp[message.author.id] = message.created_at + datetime.timedelta(seconds=30)
    # oh hey, its that nsfw detector again
    """
    if message.attachments.__len__() >= 1:
        if not isinstance(message.channel, discord.DMChannel) and not isinstance(message.author, discord.User) and isinstance(message.guild, discord.Guild):
            for image in message.attachments:
                if image.filename.split(".")[image.filename.split(".").__len__()-1] in imgformats:
                    path = pathlib.PurePath(f"nsfwimages/{str(image.id)}.{image.filename.split('.')[image.filename.split('.').__len__()-1]}")
                    await image.save(path, use_cached=True)
                    nsfw = nsfwdetect.detect(path)
                    for detected in nsfw:
                        if detected["label"] in nsfwdetections:
                            try:
                                await message.delete()
                            except discord.Forbidden:
                                logger.error(f"Forbidden to delete NSFW in {message.channel.name} ({message.channel.id}\nMessage Link: https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}")
                            except discord.HTTPException:
                                logger.error(f"Unable to delete NSFW in {message.channel.name} ({message.channel.id}\nMessage Link: https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}")
                            try:
                                await message.author.ban(reason="NSFW")
                            except discord.Forbidden:
                                logger.error(f"Forbidden to ban {message.author.name}#{message.author.discriminator} for posting NSFW")
                            except discord.HTTPException:
                                logger.error(f"Unable to ban {message.author.name}#{message.author.discriminator} for posting NSFW")
                    try:
                        os.remove(f"nsfwimages/{str(image.id)}.{image.filename.split('.')[image.filename.split('.').__len__()-1]}")
                    except:
                        pass
    """
    for role in message.role_mentions:
        if role.id == raidrequestid:
            await role.edit(mentionable=False, reason="10 minute cooldown")
            embed = await create_embed("global")
            embed.title = "Raid Request"
            embed.description = "Raids Request pings disabled for 10 minutes!"
            await message.reply(embed=embed)
            await asyncio.sleep(600)
            await role.edit(mentionable=True, reason="10 minute cooldown expired")
            embed = await create_embed("global")
            embed.title = "Raid Request"
            embed.description = "Raids Request pings enabled!"
            try:
                await message.reply(embed=embed)
            except discord.errors.HTTPException as e:
                if e.status == 400:
                    await message.channel.send(embed=embed)
    if message.channel.id == clannewsid and message.content.__len__() >= 70:
        def pick():
            choice = random.choice(clannewsmessages)
            if choice != None:
                return choice
            else:
                return pick()
        chc = pick()
        embed = await create_embed("global")
        embed.title = "Clanning News"
        embed.description = str(chc)
        general = await bot.fetch_channel(generalid)
        if isinstance(general, discord.abc.Messageable):
            await general.send(embed=embed)
        return
    for ar in autoresponses:
        if message.content.lower() == ar[0]:
            return await message.reply(content=ar[1])
    return await bot.process_commands(message)

@bot.event
async def on_member_join(member: discord.Member):
    if member.guild.id == mainid:
        # did the scc do this either??? didnt think so
        cursor = connection.cursor()
        cursor.execute("select id from cases where status='ACTIVE' and did like :sarg or did=:sarg2", {"sarg": "%|" + str(member.id) + "|%", "sarg2": "|" + str(member.id)})
        rows = cursor.fetchall()
        if rows.__len__() >= 1:
            try:
                try:
                    embed = await create_embed("global")
                    embed.title = "Blade Hub Punishment"
                    embed.description = f"You have been banned from Blade Hub for the reason:\nBH Low {rows[0][0]}"
                    await member.send(embed=embed)
                except discord.Forbidden:
                    pass
                await member.ban(reason=f"BH Low {rows[0][0]}")
                logs = await bot.fetch_channel(modlogsid)
                punishmentid = shortuuid.uuid()
                embed = await create_log(member, await member.guild.fetch_member(bot.user.id), f"BH Low {rows[0][0]}", "ban", punishmentid)
                if isinstance(logs, discord.TextChannel):
                    await logs.send(embed=embed)
                date = datetime.datetime.now()
                enddate = date + datetime.timedelta(weeks=521)
                cursor.execute("insert into punishments values (?, ?, ?, ?, ?, ?, ?)", (punishmentid, "ban", member.id, bot.user.id, date.strftime("%d/%M/%Y %H:%M:%S"), enddate.strftime("%d/%M/%Y %H:%M:%S"), f"BH Low {rows[0][0]}"))
            except discord.Forbidden:
                logger.debug(f"Unable to ban {member.name}#{str(member.discriminator)} who is BH Low {rows[0][0]}")
            return
        after6weeks = member.created_at + datetime.timedelta(weeks=6)
        if after6weeks > datetime.datetime.now(after6weeks.tzinfo):
            try:
                try:
                    embed = await create_embed("global")
                    embed.title = "Blade Hub Punishment"
                    embed.description = "You have been kicked from Blade Hub for the reason:\nAccount too young"
                    await member.send(embed=embed)
                except discord.Forbidden:
                    pass
                await member.kick(reason="Account too young")
                logs = await bot.fetch_channel(modlogsid)
                punishmentid = shortuuid.uuid()
                embed = await create_log(member, await member.guild.fetch_member(bot.user.id), "Account too young", "kick", punishmentid)
                if isinstance(logs, discord.TextChannel):
                    await logs.send(embed=embed)
                date = datetime.datetime.now().strftime("%d/%M/%Y %H:%M:%S")
                cursor.execute("insert into punishments values (?, ?, ?, ?, ?, ?, ?)", (punishmentid, "kick", member.id, bot.user.id, date, date, f"Account too young"))
            except discord.Forbidden:
                logger.debug(f"Unable to kick {member.name}#{str(member.discriminator)} who is too young")
            return
        logs = await bot.fetch_channel(logsid)
        embed = await create_embed("green")
        embed.title = "Member Joined"
        embed.add_field(name="Username", value=f"{member.name}#{member.discriminator}", inline=True)
        embed.add_field(name="ID", value=str(member.id), inline=True)
        embed.add_field(name="Mention", value=member.mention, inline=False)
        embed.add_field(name="Created", value=f"{discord.utils.format_dt(member.created_at.timestamp(), style='R')} | {discord.utils.format_dt(member.created_at.timestamp())}", inline=False)
        if isinstance(member.avatar, discord.Asset):
            embed.set_thumbnail(url=member.avatar.url)
        if isinstance(logs, discord.TextChannel):
            return await logs.send(embed=embed)
        cursor.execute("select * from users where did = ?", (member.id,))
        rows = cursor.fetchall()
        if rows.__len__() >= 1:
            try:
                verified = member.guild.get_role(verifiedid)
                if isinstance(verified, discord.Role):
                    await member.edit(roles=[verified])
            except discord.Forbidden:
                pass
    elif member.guild.id == jdid:
        cursor = connection.cursor()
        cursor.execute("select * from users where did = ?", (member.id,))
        rows = cursor.fetchall()
        if rows.__len__() >= 1:
            try:
                verified = member.guild.get_role(jdverifiedid)
                if isinstance(verified, discord.Role):
                    await member.edit(roles=[verified])
            except discord.Forbidden:
                pass

@bot.event
async def on_member_update(before: discord.Member, after: discord.Member):
    if isinstance(before.guild, discord.Guild):
        if before.nick != after.nick and before.guild.id == mainid:
            logs = await bot.fetch_channel(logsid)
            embed = await create_embed("yellow")
            embed.title = "Member Edited"
            embed.add_field(name="Member", value=f"{before.mention} | {before.name}#{before.discriminator} | {before.id}", inline=False)
            embed.add_field(name="Nickname Before", value=before.nick or "None", inline=False)
            embed.add_field(name="Nickname After", value=after.nick or "None", inline=False)
            if isinstance(logs, discord.TextChannel):
                await logs.send(embed=embed)
            if isinstance(after.nick, str):
                for text in blacklistedtext:
                    if after.nick.find(text):
                        try:
                            await after.edit(nick=None)
                        except discord.Forbidden:
                            embed = await create_embed("yellow")
                            embed.title = "Blacklisted Text in Nickname"
                            embed.description = f"Blacklisted text was found in {after.mention}'s nickname, but I was unable to reset it!"
                            if isinstance(logs, discord.TextChannel):
                                await logs.send(embed=embed)
        if before.roles != after.roles and before.guild.id == mainid:
            broles = ""
            for role in before.roles:
                if role != before.guild.default_role:
                    broles = broles + role.mention
            if broles == "":
                broles = "None"
            aroles = ""
            for role in after.roles:
                if role != after.guild.default_role:
                    aroles = aroles + role.mention
            if aroles == "":
                aroles = "None"
            logs = await bot.fetch_channel(logsid)
            embed = await create_embed("yellow")
            embed.title = "Member Edited"
            embed.add_field(name="Member", value=f"{before.mention} | {before.name}#{before.discriminator} | {before.id}", inline=False)
            embed.add_field(name="Roles Before", value=broles, inline=False)
            embed.add_field(name="Roles After", value=aroles, inline=False)
            if isinstance(logs, discord.TextChannel):
                await logs.send(embed=embed)

@bot.event
async def on_member_leave(member: discord.Member):
    print("leave")
    if member.guild.id == mainid:
        server = await bot.fetch_guild(mainid)
        async for log in server.audit_logs(action=discord.AuditLogAction.kick):
            if isinstance(log.target, discord.Member):
                if isinstance(log.user, discord.Member) and log.target.id == member.id:
                    if log.user.id == bot.user.id:
                        return
                    logs = await bot.fetch_channel(modlogsid)
                    embed = None
                    punishmentid = shortuuid.uuid()
                    if isinstance(log.reason, str):
                        embed = await create_log(member, log.user, log.reason, "kick", punishmentid)
                    else:
                        embed = await create_log(member, log.user, "No reason", "kick", punishmentid)
                    if isinstance(logs, discord.TextChannel):
                        await logs.send(embed=embed)
                    return
        logs = await bot.fetch_channel(logsid)
        embed = await create_embed("red")
        embed.title = "Member Left"
        embed.add_field(name="Username", value=f"{member.name}#{member.discriminator}", inline=True)
        embed.add_field(name="ID", value=str(member.id), inline=True)
        embed.add_field(name="Mention", value=member.mention, inline=False)
        embed.add_field(name="Created", value=f"{discord.utils.format_dt(datetime.datetime.now().timestamp(), style='R')} | {discord.utils.format_dt(datetime.datetime.now().timestamp())}", inline=False)
        print("log")
        if isinstance(member.avatar, discord.Asset):
            embed.set_thumbnail(url=member.avatar.url)
        if isinstance(logs, discord.TextChannel):
            return await logs.send(embed=embed)

@bot.event
async def on_message_delete(message: discord.Message):
    if message.author.bot == False:
        if isinstance(message.guild, discord.Guild):
            if message.channel.id != logsid and message.channel.id != modlogsid and message.guild.id == mainid and isinstance(message.channel, discord.TextChannel):
                logs = await bot.fetch_channel(logsid)
                embed = await create_embed("red")
                embed.title = "Message Deleted"
                embed.add_field(name="Author", value=f"{message.author.mention} | {message.author.name}#{message.author.discriminator} | {message.author.id}", inline=False)
                embed.add_field(name="Text", value=message.content, inline=False)
                embed.add_field(name="Channel", value=message.channel.mention, inline=False)
                embed.add_field(name="Send Time", value=discord.utils.format_dt(datetime.datetime.now().timestamp()))
                file = None
                if message.attachments.__len__() >= 1:
                    file = open(f"attachments/{str(message.id)}.txt", "a")
                    for attachment in message.attachments:
                        file.write(f"{attachment.proxy_url}\n")
                    file.close()
                    file = discord.File(open(f"attachments/{str(message.id)}.txt", "rb"))
                    embed.description = "The message had attachments; links to them are provided in a text file attached to this log"
                if isinstance(file, discord.File):
                    if isinstance(logs, discord.TextChannel):
                        return await logs.send(embed=embed, file=file)
                else:
                    if isinstance(logs, discord.TextChannel):
                        return await logs.send(embed=embed)

@bot.event
async def on_message_edit(before: discord.Message, after: discord.Message):
    if isinstance(before.guild, discord.Guild):
        if before.content != after.content and before.guild.id == mainid and isinstance(before.channel, discord.TextChannel) and isinstance(after.author, discord.Member):
            logs = await bot.fetch_channel(logsid)
            embed = await create_embed("yellow")
            embed.title = "Message Edited"
            embed.description = f"The message can be found [here](https://discord.com/channels/{mainid}/{before.channel.id}/{before.id})."
            embed.add_field(name="Author", value=f"{before.author.mention} | {before.author.name}#{before.author.discriminator} | {before.author.id}", inline=False)
            embed.add_field(name="Channel", value=before.channel.mention, inline=False)
            embed.add_field(name="Before", value=before.content, inline=False)
            embed.add_field(name="After", value=after.content, inline=False)
            for link in blacklistedlinks:
                if after.content.lower().find(link) != -1:
                    try:
                        await after.delete()
                    except discord.Forbidden:
                        embed = await create_embed("global")
                        embed.title = "Blacklisted Link"
                        embed.description = "A blacklisted link was detected in this message, but I was unable to delete it!"
                        await after.reply(content="<@&890353236165406720>", embed=embed, delete_after=10)
                    try:
                        await after.author.ban(reason=f"Posting blacklisted link\n{link}")
                    except discord.Forbidden:
                        embed = await create_embed("global")
                        embed.title = "Blacklisted Link"
                        embed.description = f"A blacklisted link was detected in a message sent by {after.author.mention}, but I was unable to ban them!"
                        await after.channel.send(content="<@&890353236165406720>", embed=embed)
            for text in blacklistedtext:
                if after.content.lower().find(text) != -1:
                    try:
                        await after.delete()
                        embed = await create_embed("global")
                        embed.title = "Blacklisted Text"
                        embed.description = "Blacklisted text was detected in your message!"
                        await after.channel.send(content=f"{after.author.mention}", embed=embed, delete_after=10)
                    except discord.Forbidden:
                        embed = await create_embed("global")
                        embed.title = "Blacklisted Text"
                        embed.description = "Blacklisted text was detected in this message, but I was unable to delete it!"
                        await after.reply(content="<@&890353236165406720>", embed=embed)
            if isinstance(logs, discord.TextChannel):
                return await logs.send(embed=embed)

@bot.event
async def on_member_ban(guild: discord.Guild, user: discord.User | discord.Member):
    if isinstance(guild, discord.Guild):
        if guild.id == mainid:
            async for log in guild.audit_logs(action=discord.AuditLogAction.ban):
                if isinstance(log.target, discord.Member | discord.User):
                    if isinstance(log.user, discord.Member) and log.target.id == user.id:
                        if log.user.id == bot.user.id:
                            return
                        logs = await bot.fetch_channel(modlogsid)
                        embed = None
                        punishmentid = shortuuid.uuid()
                        if isinstance(log.reason, str):
                            embed = await create_log(user, log.user, log.reason, "ban", punishmentid)
                        else:
                            embed = await create_log(user, log.user, "No reason", "ban", punishmentid)
                        if isinstance(logs, discord.TextChannel):
                            return await logs.send(embed=embed)

# Commands
# ah yes, text commands. how ancient
@bot.group()
async def jd(ctx: commands.Context):
    async with ctx.typing():
        if ctx.invoked_subcommand == None:
            embed = await create_embed("jd")
            embed.title = "Invalid Command Syntax"
            embed.description = "Please pass a valid subcommand! Use `b.help jd` for a list of subcommands."
            return await ctx.reply(embed=embed, delete_after=15)

@bot.command()
async def refreshperms(ctx: commands.Context):
    if ctx.author.id != 464096668879683594:
        embed = await create_embed("global")
        embed.title = "Refresh Permissions"
        embed.description = "You do not have permission to use this command."
        return await ctx.reply(embed=embed)
    jdsupervisors.clear()
    seniorstaff.clear()
    staff.clear()
    staffintraining.clear()
    try:
        privatejp = await bot.fetch_guild(jdid)
        async for member in privatejp.fetch_members():
            if member.get_role(supervisorid) != None:
                jdsupervisors.append(member.id)
                logger.info(f"{member.name}#{member.discriminator} has been registered as a Supervisor!")
    except discord.Forbidden:
        logger.error("Warning: Bot is not in JD Server, Supervisor commands will not be available!")
    try:
        main = await bot.fetch_guild(mainid)
        async for member in main.fetch_members():
            if member.get_role(snrstaffid) != None:
                seniorstaff.append(member.id)
                logger.info(f"{member.name}#{member.discriminator} has been registered as a Senior Staff!")
            if member.get_role(staffid) != None:
                staff.append(member.id)
                logger.info(f"{member.name}#{member.discriminator} has been registered as a Staff!")
            if member.get_role(staffitid) != None:
                staffintraining.append(member.id)
                logger.info(f"{member.name}#{member.discriminator} has been registered as a Staff in Training!")
    except discord.Forbidden:
        logger.error("Warning: Bot is not in Main server, Moderator commands will not be available!")
    embed = await create_embed("global")
    embed.title = "Refresh Permissions"
    embed.description = "Permissions successfully refreshed!"
    return await ctx.reply(embed=embed)

# one time use commands be like
@bot.command()
async def banlows(ctx: commands.Context):
    async with ctx.typing():
        if ctx.author.id != 464096668879683594:
            embed = await create_embed("global")
            embed.title = "Ban All Lows"
            embed.description = "You do not have permission to use this command."
            return await ctx.reply(embed=embed)
        cursor = connection.cursor()
        cursor.execute("select id, did from cases where status='ACTIVE'")
        rows = cursor.fetchall()
        try:
            server = await bot.fetch_guild(mainid)
        except discord.Forbidden:
            embed = await create_embed("global")
            embed.title = "Ban All Lows"
            embed.description = "Unable to get main server."
            return await ctx.reply(embed=embed)
        count = 0
        for row in rows:
            ids = row[1].split("|")
            for id in ids:
                if id.isnumeric():
                    try:
                        user = await bot.fetch_user(int(id))
                    except:
                        continue
                    try:
                        await server.ban(user, reason=f"BH Low {row[0]}")
                        count += 1
                    except discord.Forbidden:
                        pass
                    await asyncio.sleep(1)
        embed = await create_embed("global")
        embed.title = "Ban All Lows"
        embed.description = f"Banned {count} Lows"
        return await ctx.reply(embed=embed)

# die die die die die die die die die die
@commands.cooldown(2, 15, commands.BucketType.user)
@bot.command(aliases=["jdcase"])
async def case(ctx: commands.Context, arg=None):
    cursor = connection.cursor()
    if arg == None or arg == "UNKNOWN" or arg == "N/A":
        embed = await create_embed("jd")
        embed.title = "BH JD Case Search"
        embed.description = "Please enter a search argument"
        await ctx.reply(embed=embed, delete_after=15)
        if isinstance(ctx.command, commands.Command):
            ctx.command.reset_cooldown(ctx)
        return
    if ctx.guild != None:
        if ctx.guild.id == mainid and await is_snr_staff(ctx) == False:
            embed = await create_embed("jd")
            embed.title = "BH JD Case Search"
            embed.description = "This command is not supported here"
            await ctx.reply(embed=embed, delete_after=15)
            if isinstance(ctx.command, commands.Command):
                ctx.command.reset_cooldown(ctx)
            return
    async with ctx.typing():
        if str(arg).isnumeric():
            try:
                cursor.execute("select * from cases where id=:iarg or rid like :sarg or rid=:sarg2 or did like :sarg or did=:sarg2 order by id DESC", {"iarg": int(arg), "sarg": "%|" + arg + "|%", "sarg2": "|" + arg})
                rows = cursor.fetchall()
                if rows.__len__() <= 0:
                    embed = await create_embed("jd")
                    embed.title = "BH JD Case Search"
                    embed.description = "No results found"
                    return await ctx.reply(embed=embed, delete_after=15)
                def mcheck(msg: discord.Message):
                    return msg.author.id == bot.user.id
                async def generatecase(index: int, originalmessage: discord.Message):
                    mainview = view()
                    close = closebutton()
                    caseselect = None
                    if rows.__len__() > 1:
                        options = []
                        optionindex = 0
                        for rec in rows:
                            if rec[0] == rows[index][0]:
                                continue
                            options.append(discord.SelectOption(label=f"Low Case {rec[0]}", description=f"**STATUS: {rec[2]}**", value=str(optionindex)))
                            optionindex = sum((optionindex, 1))
                        caseselect = casepageselect(options)
                        mainview.add_item(caseselect)
                    mainview.add_item(close)
                    embed = await create_embed("jd")
                    embed.title = f"Case ID: {str(rows[index][0])}"
                    embed.description = f"[Requested by {ctx.author.mention}] | STATUS: {str(rows[index][2])}"
                    embed.set_author(name=f"Result Found: {index+1} of {rows.__len__()}")
                    embed.add_field(name="CREATION DATE (dd/mm/yyyy):", value=str(rows[index][4]), inline=False)
                    charge = str(rows[index][1]).replace('|', '\n')
                    embed.add_field(name="CHARGE(s):", value=f"```\n{charge}```", inline=False)
                    proof = str(rows[index][3]).replace('|', '\n')
                    if proof.__len__() > 1024:
                        pastes = pastebin.get_user_pastes()
                        if isinstance(pastes, str) == True:
                            url = pastebin.create_paste(api_paste_code=proof, api_paste_name=f"{rows[index][0]}_{str(rows[index][2])}")
                            proof = url
                        else:
                            found = False
                            for paste in pastes:
                                if paste.title == f"{rows[index][0]}_{str(rows[index][2])}":
                                    if paste.get_raw_text() == proof: # type: ignore
                                        proof = paste.url # type: ignore
                                        found = True
                                        break
                                    else:
                                        pastebin.delete_user_paste(paste.key) # type: ignore
                                        url = pastebin.create_paste(api_paste_code=proof, api_paste_name=f"{rows[index][0]}_{str(rows[index][2])}")
                                        proof = url
                            if found == False:
                                url = pastebin.create_paste(api_paste_code=proof, api_paste_name=f"{rows[index][0]}_{str(rows[index][2])}")
                                proof = url
                    embed.add_field(name="PROOF:", value=f"```\n{proof}```", inline=False)
                    discordids = str(rows[index][7]).replace('|', '\n')
                    embed.add_field(name="DISCORD ID(s):", value=f"```\n{discordids}```", inline=False)
                    discordnames = str(rows[index][6]).replace('|', '\n')
                    embed.add_field(name="DISCORD NAME(s):", value=f"```\n{discordnames}```", inline=False)
                    robloxids = str(rows[index][9]).replace('|', '\n')
                    embed.add_field(name="ROBLOX ID(s):", value=f"```\n{robloxids}```", inline=False)
                    robloxnames = str(rows[index][8]).replace('|', '\n')
                    embed.add_field(name="ROBLOX NAME(s):", value=f"```\n{robloxnames}```", inline=False)
                    notes = str(rows[index][10]).replace('|', '\n')
                    embed.add_field(name="ADDITIONAL NOTE(s):", value=f"```\n{notes}```", inline=False)
                    await originalmessage.edit(embed=embed, view=mainview)
                    if caseselect != None:
                        done, pending = await asyncio.wait([mainview.wait(), bot.wait_for("message_delete", check=mcheck)], return_when=asyncio.FIRST_COMPLETED)
                        for task in pending:
                            task.cancel()
                        if caseselect.pressed == True:
                            await generatecase(int(caseselect.values[0]), originalmessage)
                            return
                        else:
                            return
                embed = await create_embed("jd")
                embed.title = "Loading"
                embed.description = "Please wait.."
                originalmessage = await ctx.reply(embed=embed, delete_after=50)
                await generatecase(0, originalmessage)
            except Error as e:
                logger.debug("An error occured while searching the case database: " + str(e))
                embed = await create_embed("jd")
                embed.title = "BH JD Case Search"
                embed.description = f"An error occured while searching the case database:\n```{str(e)}```"
                return await ctx.reply(embed=embed)
        else:
            try:
                cursor.execute("select * from cases where rusername like :ruser or dusername like :duser order by id DESC", {"ruser": arg + "|%", "duser": arg + "#%"})
                rows = cursor.fetchall()
                if rows.__len__() < 1:
                    embed = await create_embed("jd")
                    embed.title = "BH JD Case Search"
                    embed.description = "No results found"
                    return await ctx.reply(embed=embed, delete_after=15)
                mainview = None
                def mcheck(msg: discord.Message):
                    return msg.author.id == bot.user.id
                async def generatecase(index: int, originalmessage: discord.Message):
                    mainview = view()
                    close = closebutton()
                    caseselect = None
                    if rows.__len__() > 1:
                        options = []
                        optionindex = 0
                        for rec in rows:
                            if rec[0] == rows[index][0]:
                                continue
                            options.append(discord.SelectOption(label=f"Low Case {rec[0]}", description=f"**STATUS: {rec[2]}**", value=str(optionindex)))
                            optionindex = sum((optionindex, 1))
                        caseselect = casepageselect(options)
                        mainview.add_item(caseselect)
                    mainview.add_item(close)
                    embed = await create_embed("jd")
                    embed.title = f"Case ID: {str(rows[index][0])}"
                    embed.description = f"[Requested by {ctx.author.mention}] | STATUS: {str(rows[index][2])}"
                    embed.set_author(name=f"Result Found: {index+1} of {rows.__len__()}")
                    embed.add_field(name="CREATION DATE (dd/mm/yyyy):", value=str(rows[index][5]), inline=False)
                    charge = str(rows[index][1]).replace('|', '\n')
                    embed.add_field(name="CHARGE(s):", value=f"```\n{charge}```", inline=False)
                    proof = str(rows[index][3]).replace('|', '\n')
                    if proof.__len__() > 1024:
                        pastes = pastebin.get_user_pastes()
                        if isinstance(pastes, str) == True:
                            url = pastebin.create_paste(api_paste_code=proof, api_paste_name=f"{rows[index][0]}_{str(rows[index][2])}")
                            proof = url
                        else:
                            found = False
                            for paste in pastes:
                                if paste.title == f"{rows[index][0]}_{str(rows[index][2])}":
                                    if paste.get_raw_text() == proof: # type: ignore
                                        proof = paste.url # type: ignore
                                        found = True
                                        break
                                    else:
                                        pastebin.delete_user_paste(paste.key) # type: ignore
                                        url = pastebin.create_paste(api_paste_code=proof, api_paste_name=f"{rows[index][0]}_{str(rows[index][2])}")
                                        proof = url
                            if found == False:
                                url = pastebin.create_paste(api_paste_code=proof, api_paste_name=f"{rows[index][0]}_{str(rows[index][2])}")
                                proof = url
                    embed.add_field(name="PROOF:", value=f"```\n{proof}```", inline=False)
                    discordids = str(rows[index][7]).replace('|', '\n')
                    embed.add_field(name="DISCORD IDS:", value=f"```\n{discordids}```", inline=False)
                    discordnames = str(rows[index][6]).replace('|', '\n')
                    embed.add_field(name="DISCORD NAMES:", value=f"```\n{discordnames}```", inline=False)
                    robloxids = str(rows[index][9]).replace('|', '\n')
                    embed.add_field(name="ROBLOX IDS:", value=f"```\n{robloxids}```", inline=False)
                    robloxnames = str(rows[index][8]).replace('|', '\n')
                    embed.add_field(name="ROBLOX NAMES:", value=f"```\n{robloxnames}```", inline=False)
                    notes = str(rows[index][10]).replace('|', '\n')
                    embed.add_field(name="ADDITIONAL NOTES:", value=f"```\n{notes}```", inline=False)
                    await originalmessage.edit(embed=embed, view=mainview)
                    if caseselect != None:
                        done, pending = await asyncio.wait([mainview.wait(), bot.wait_for("message_delete", check=mcheck)], return_when=asyncio.FIRST_COMPLETED)
                        for task in pending:
                            task.cancel()
                        if caseselect.pressed == True:
                            await generatecase(int(caseselect.values[0]), originalmessage)
                            return
                        else:
                            return
                embed = await create_embed("jd")
                embed.title = "Loading"
                embed.description = "Please wait.."
                originalmessage = await ctx.reply(embed=embed, delete_after=50)
                await generatecase(0, originalmessage)
            except Error as e:
                logger.debug("An error occured while searching the case database: " + str(e))
                embed = await create_embed("jd")
                embed.title = "BH JD Case Search"
                embed.description = f"An error occured while searching the case database:\n```{str(e)}```"
                return await ctx.reply(embed=embed)

@commands.cooldown(2, 15, commands.BucketType.user)
@bot.slash_command(
    name="case",
    description="Fetches a case from the JD case database via case ID/username/user ID"
)
async def slashcase(interaction: discord.ApplicationCommandInteraction, query: str):
    arg = query
    cursor = connection.cursor()
    if arg == "" or arg == "UNKNOWN" or arg == "N/A":
        embed = await create_embed("jd")
        embed.title = "BH JD Case Search"
        embed.description = "Please enter a search argument"
        await interaction.response.send_message(embed=embed, delete_after=15)
        return interaction.application_command.reset_cooldown(interaction)   
    if interaction.guild != None:
        if interaction.guild.id == mainid and await is_snr_staff(interaction) == False:
            embed = await create_embed("jd")
            embed.title = "BH JD Case Search"
            embed.description = "This command is not supported here"
            await interaction.response.send_message(embed=embed, delete_after=15)
            return interaction.application_command.reset_cooldown(interaction)
    if not isinstance(interaction.user, discord.User | discord.Member):
        return
    await interaction.response.defer()
    if str(arg).isnumeric():
        try:
            cursor.execute("select * from cases where id=:iarg or rid like :sarg or rid=:sarg2 or did like :sarg or did=:sarg2 order by id DESC", {"iarg": int(arg), "sarg": "%|" + arg + "|%", "sarg2": "|" + arg})
            rows = cursor.fetchall()
            if rows.__len__() <= 0:
                embed = await create_embed("jd")
                embed.title = "BH JD Case Search"
                embed.description = "No results found"
                await interaction.edit_original_message(embed=embed)
                return await interaction.delete_original_message(delay=15)
            def mcheck(msg: discord.Message):
                return msg.author.id == bot.user.id
            async def generatecase(index: int, originalmessage: discord.Message):
                assert isinstance(interaction.user, discord.User | discord.Member)
                mainview = view()
                close = closebutton()
                caseselect = None
                if rows.__len__() > 1:
                    options = []
                    optionindex = 0
                    for rec in rows:
                        if rec[0] == rows[index][0]:
                            continue
                        options.append(discord.SelectOption(label=f"Low Case {rec[0]}", description=f"**STATUS: {rec[2]}**", value=str(optionindex)))
                        optionindex = sum((optionindex, 1))
                    caseselect = casepageselect(options)
                    mainview.add_item(caseselect)
                mainview.add_item(close)
                embed = await create_embed("jd")
                embed.title = f"Case ID: {str(rows[index][0])}"
                embed.description = f"[Requested by {interaction.user.mention}] | STATUS: {str(rows[index][2])}"
                embed.set_author(name=f"Result Found: {index+1} of {rows.__len__()}")
                embed.add_field(name="CREATION DATE (dd/mm/yyyy):", value=str(rows[index][4]), inline=False)
                charge = str(rows[index][1]).replace('|', '\n')
                embed.add_field(name="CHARGE(s):", value=f"```\n{charge}```", inline=False)
                proof = str(rows[index][3]).replace('|', '\n')
                if proof.__len__() > 1024:
                    pastes = pastebin.get_user_pastes()
                    if isinstance(pastes, str) == True:
                        url = pastebin.create_paste(api_paste_code=proof, api_paste_name=f"{rows[index][0]}_{str(rows[index][2])}")
                        proof = url
                    else:
                        found = False
                        for paste in pastes:
                            if paste.title == f"{rows[index][0]}_{str(rows[index][2])}":
                                if paste.get_raw_text() == proof: # type: ignore
                                    proof = paste.url # type: ignore
                                    found = True
                                    break
                                else:
                                    pastebin.delete_user_paste(paste.key) # type: ignore
                                    url = pastebin.create_paste(api_paste_code=proof, api_paste_name=f"{rows[index][0]}_{str(rows[index][2])}")
                                    proof = url
                        if found == False:
                            url = pastebin.create_paste(api_paste_code=proof, api_paste_name=f"{rows[index][0]}_{str(rows[index][2])}")
                            proof = url
                embed.add_field(name="PROOF:", value=f"```\n{proof}```", inline=False)
                discordids = str(rows[index][7]).replace('|', '\n')
                embed.add_field(name="DISCORD ID(s):", value=f"```\n{discordids}```", inline=False)
                discordnames = str(rows[index][6]).replace('|', '\n')
                embed.add_field(name="DISCORD NAME(s):", value=f"```\n{discordnames}```", inline=False)
                robloxids = str(rows[index][9]).replace('|', '\n')
                embed.add_field(name="ROBLOX ID(s):", value=f"```\n{robloxids}```", inline=False)
                robloxnames = str(rows[index][8]).replace('|', '\n')
                embed.add_field(name="ROBLOX NAME(s):", value=f"```\n{robloxnames}```", inline=False)
                notes = str(rows[index][10]).replace('|', '\n')
                embed.add_field(name="ADDITIONAL NOTE(s):", value=f"```\n{notes}```", inline=False)
                await originalmessage.edit(embed=embed, view=mainview)
                if caseselect != None:
                    done, pending = await asyncio.wait([mainview.wait(), bot.wait_for("message_delete", check=mcheck)], return_when=asyncio.FIRST_COMPLETED)
                    for task in pending:
                        task.cancel()
                    if caseselect.pressed == True:
                        await generatecase(int(caseselect.values[0]), originalmessage)
                        return
                    else:
                        return
            embed = await create_embed("jd")
            embed.title = "Loading"
            embed.description = "Please wait.."
            await interaction.edit_original_message(embed=embed)
            originalmessage = await interaction.original_message()
            await originalmessage.delete(delay=50)
            await generatecase(0, originalmessage)
        except Error as e:
            logger.debug("An error occured while searching the case database: " + str(e))
            embed = await create_embed("jd")
            embed.title = "BH JD Case Search"
            embed.description = f"An error occured while searching the case database:\n```{str(e)}```"
            return await interaction.edit_original_message(embed=embed)
    else:
        try:
            cursor.execute("select * from cases where rusername like :ruser or dusername like :duser order by id DESC", {"ruser": arg + "|%", "duser": arg + "#%"})
            rows = cursor.fetchall()
            if rows.__len__() < 1:
                embed = await create_embed("jd")
                embed.title = "BH JD Case Search"
                embed.description = "No results found"
                await interaction.edit_original_message(embed=embed)
                originalmessage = await interaction.original_message()
                return await originalmessage.delete(delay=15)
            mainview = None
            def mcheck(msg: discord.Message):
                return msg.author.id == bot.user.id
            async def generatecase(index: int, originalmessage: discord.Message):
                assert isinstance(interaction.user, discord.User | discord.Member)
                mainview = view()
                close = closebutton()
                caseselect = None
                if rows.__len__() > 1:
                    options = []
                    optionindex = 0
                    for rec in rows:
                        if rec[0] == rows[index][0]:
                            continue
                        options.append(discord.SelectOption(label=f"Low Case {rec[0]}", description=f"**STATUS: {rec[2]}**", value=str(optionindex)))
                        optionindex = sum((optionindex, 1))
                    caseselect = casepageselect(options)
                    mainview.add_item(caseselect)
                mainview.add_item(close)
                embed = await create_embed("jd")
                embed.title = f"Case ID: {str(rows[index][0])}"
                embed.description = f"[Requested by {interaction.user.mention}] | STATUS: {str(rows[index][2])}"
                embed.set_author(name=f"Result Found: {index+1} of {rows.__len__()}")
                embed.add_field(name="CREATION DATE (dd/mm/yyyy):", value=str(rows[index][5]), inline=False)
                charge = str(rows[index][1]).replace('|', '\n')
                embed.add_field(name="CHARGE(s):", value=f"```\n{charge}```", inline=False)
                proof = str(rows[index][3]).replace('|', '\n')
                if proof.__len__() > 1024:
                    pastes = pastebin.get_user_pastes()
                    if isinstance(pastes, str) == True:
                        url = pastebin.create_paste(api_paste_code=proof, api_paste_name=f"{rows[index][0]}_{str(rows[index][2])}")
                        proof = url
                    else:
                        found = False
                        for paste in pastes:
                            if paste.title == f"{rows[index][0]}_{str(rows[index][2])}":
                                if paste.get_raw_text() == proof: # type: ignore
                                    proof = paste.url # type: ignore
                                    found = True
                                    break
                                else:
                                    pastebin.delete_user_paste(paste.key) # type: ignore
                                    url = pastebin.create_paste(api_paste_code=proof, api_paste_name=f"{rows[index][0]}_{str(rows[index][2])}")
                                    proof = url
                        if found == False:
                            url = pastebin.create_paste(api_paste_code=proof, api_paste_name=f"{rows[index][0]}_{str(rows[index][2])}")
                            proof = url
                embed.add_field(name="PROOF:", value=f"```\n{proof}```", inline=False)
                discordids = str(rows[index][7]).replace('|', '\n')
                embed.add_field(name="DISCORD IDS:", value=f"```\n{discordids}```", inline=False)
                discordnames = str(rows[index][6]).replace('|', '\n')
                embed.add_field(name="DISCORD NAMES:", value=f"```\n{discordnames}```", inline=False)
                robloxids = str(rows[index][9]).replace('|', '\n')
                embed.add_field(name="ROBLOX IDS:", value=f"```\n{robloxids}```", inline=False)
                robloxnames = str(rows[index][8]).replace('|', '\n')
                embed.add_field(name="ROBLOX NAMES:", value=f"```\n{robloxnames}```", inline=False)
                notes = str(rows[index][10]).replace('|', '\n')
                embed.add_field(name="ADDITIONAL NOTES:", value=f"```\n{notes}```", inline=False)
                await originalmessage.edit(embed=embed, view=mainview)
                if caseselect != None:
                    done, pending = await asyncio.wait([mainview.wait(), bot.wait_for("message_delete", check=mcheck)], return_when=asyncio.FIRST_COMPLETED)
                    for task in pending:
                        task.cancel()
                    if caseselect.pressed == True:
                        await generatecase(int(caseselect.values[0]), originalmessage)
                        return
                    else:
                        return
            embed = await create_embed("jd")
            embed.title = "Loading"
            embed.description = "Please wait.."
            await interaction.edit_original_message(embed=embed)
            originalmessage = await interaction.original_message()
            await originalmessage.delete(delay=50)
            await generatecase(0, originalmessage)
        except Error as e:
            logger.debug("An error occured while searching the case database: " + str(e))
            embed = await create_embed("jd")
            embed.title = "BH JD Case Search"
            embed.description = f"An error occured while searching the case database:\n```{str(e)}```"
            return await interaction.edit_original_message(embed=embed)

@commands.cooldown(1, 180, commands.BucketType.user)
@bot.command()
async def suggest(ctx: commands.Context, *, suggestion: str):
    if not isinstance(ctx.guild, discord.Guild) or ctx.guild.id != mainid or not isinstance(ctx.author, discord.Member):
        embed = await create_embed("global")
        embed.title = "BH Suggestions"
        embed.description = "This command can only be executed in the Blade Hub server!"
        return await ctx.reply(embed=embed)
    if not isinstance(suggestion, str):
        embed = await create_embed("global")
        embed.title = "BH Suggestions"
        embed.description = "Please provide a suggestion to give!"
        return await ctx.reply(embed=embed)
    embed = await create_embed("global")
    embed.add_field(name="Suggester", value=f"{ctx.author.name}#{ctx.author.discriminator}", inline=False)
    embed.add_field(name="Suggestion", value=suggestion, inline=False)
    suggestions = await bot.fetch_channel(suggestionsid)
    if isinstance(suggestions, discord.TextChannel):
        message = await suggestions.send(embed=embed)
        try:
            upvote = await ctx.guild.fetch_emoji(upvoteid)
            downvote = await ctx.guild.fetch_emoji(downvoteid)
        except discord.NotFound:
            embed = await create_embed("global")
            embed.title = "BH Suggestions"
            embed.description = "I couldn't get the voting emojis! Please try again later!"
            return await ctx.reply(embed=embed)
        await message.add_reaction(upvote)
        await message.add_reaction(downvote)
    embed = await create_embed("global")
    embed.title = "BH Suggestions"
    embed.description = "Your suggestion has been submitted!"
    return await ctx.reply(embed=embed)

@commands.cooldown(1, 180, commands.BucketType.user)
@bot.slash_command(
    name="suggest",
    description="Submits a suggestion to the suggestions channel"
)
async def slashsuggest(interaction: discord.ApplicationCommandInteraction, suggestion: str):
    if not isinstance(interaction.guild, discord.Guild) or interaction.guild.id != mainid or not isinstance(interaction.author, discord.Member):
        embed = await create_embed("global")
        embed.title = "BH Suggestions"
        embed.description = "This command can only be executed in the Blade Hub server!"
        return await interaction.send(embed=embed, delete_after=15)
    if not isinstance(suggestion, str):
        embed = await create_embed("global")
        embed.title = "BH Suggestions"
        embed.description = "Please provide a suggestion to give!"
        return await interaction.send(embed=embed, delete_after=15)
    embed = await create_embed("global")
    embed.add_field(name="Suggester", value=f"{interaction.author.name}#{interaction.author.discriminator}", inline=False)
    embed.add_field(name="Suggestion", value=suggestion, inline=False)
    suggestions = await bot.fetch_channel(suggestionsid)
    if isinstance(suggestions, discord.TextChannel):
        message = await suggestions.send(embed=embed)
        try:
            upvote = await interaction.guild.fetch_emoji(upvoteid)
            downvote = await interaction.guild.fetch_emoji(downvoteid)
        except discord.NotFound:
            embed = await create_embed("global")
            embed.title = "BH Suggestions"
            embed.description = "I couldn't get the voting emojis! Please try again later!"
            return await interaction.send(embed=embed, delete_after=15)
        await message.add_reaction(upvote)
        await message.add_reaction(downvote)
    embed = await create_embed("global")
    embed.title = "BH Suggestions"
    embed.description = "Your suggestion has been submitted!"
    return await interaction.send(embed=embed)

@commands.cooldown(1, 30, commands.BucketType.user)
@bot.command()
async def level(ctx: commands.Context, member: typing.Optional[discord.Member]):
    if not isinstance(ctx.guild, discord.Guild) or ctx.guild.id != mainid or not isinstance(ctx.author, discord.Member):
        embed = await create_embed("global")
        embed.title = "BH Level"
        embed.description = "This command can only be executed in the Blade Hub server!"
        return await ctx.reply(embed=embed)
    cursor = connection.cursor()
    if not isinstance(member, discord.Member):
        cursor.execute("select * from xp where id = ?", (ctx.author.id,))
        rows = cursor.fetchall()
        if rows.__len__() >= 1:
            embed = await create_embed("global")
            embed.title = "BH Level"
            embed.add_field(name="User", value=f"{ctx.author.name}#{ctx.author.discriminator}", inline=False)
            embed.add_field(name="Level", value=str(rows[0][2]), inline=False)
            embed.add_field(name="XP", value=f"{str(rows[0][1])}/{str(math.floor(((rows[0][2]+1)/0.07)**2))}", inline=False)
            attachments = ctx.guild.get_role(attachmentsid)
            if rows[0][2] >= 10 and isinstance(attachments, discord.Role) and attachments not in ctx.author.roles:
                roles = ctx.author.roles
                roles.append(attachments)
                await ctx.author.edit(roles=roles)
            return await ctx.reply(embed=embed, delete_after=30)
        else:
            embed = await create_embed("global")
            embed.title = "BH Level"
            embed.add_field(name="User", value=f"{ctx.author.name}#{ctx.author.discriminator}", inline=False)
            embed.add_field(name="Level", value="0", inline=False)
            embed.add_field(name="XP", value="0", inline=False)
            return await ctx.reply(embed=embed, delete_after=30)
    else:
        cursor.execute("select * from xp where id = ?", (member.id,))
        rows = cursor.fetchall()
        if rows.__len__() >= 1:
            embed = await create_embed("global")
            embed.title = "BH Level"
            embed.add_field(name="User", value=f"{member.name}#{member.discriminator}", inline=False)
            embed.add_field(name="Level", value=str(rows[0][2]), inline=False)
            embed.add_field(name="XP", value=f"{str(rows[0][1])}/{str(math.floor(((rows[0][2]+1)/0.07)**2))}", inline=False)
            attachments = ctx.guild.get_role(attachmentsid)
            if rows[0][2] >= 10 and isinstance(attachments, discord.Role) and attachments not in member.roles:
                roles = member.roles
                roles.append(attachments)
                await member.edit(roles=roles)
            return await ctx.reply(embed=embed, delete_after=30)
        else:
            embed = await create_embed("global")
            embed.title = "BH Level"
            embed.add_field(name="User", value=f"{member.name}#{member.discriminator}", inline=False)
            embed.add_field(name="Level", value="0", inline=False)
            embed.add_field(name="XP", value="0", inline=False)
            return await ctx.reply(embed=embed, delete_after=30)

@commands.cooldown(1, 30, commands.BucketType.user)
@bot.slash_command(
    name="level",
    description="Gets the level and XP of the calling user (or specified user)"
)
async def slashlevel(interaction: discord.ApplicationCommandInteraction, member: discord.Member=None):
    if not isinstance(interaction.guild, discord.Guild) or interaction.guild.id != mainid or not isinstance(interaction.author, discord.Member):
        embed = await create_embed("global")
        embed.title = "BH Level"
        embed.description = "This command can only be executed in the Blade Hub server!"
        return await interaction.send(embed=embed, delete_after=15)
    cursor = connection.cursor()
    await interaction.response.defer()
    if not isinstance(member, discord.Member):
        cursor.execute("select * from xp where id = ?", (interaction.author.id,))
        rows = cursor.fetchall()
        if rows.__len__() >= 1:
            embed = await create_embed("global")
            embed.title = "BH Level"
            embed.add_field(name="User", value=f"{interaction.author.name}#{interaction.author.discriminator}", inline=False)
            embed.add_field(name="Level", value=str(rows[0][2]), inline=False)
            embed.add_field(name="XP", value=f"{str(rows[0][1])}/{str(math.floor(((rows[0][2]+1)/0.07)**2))}", inline=False)
            attachments = interaction.guild.get_role(attachmentsid)
            if rows[0][2] >= 10 and isinstance(attachments, discord.Role) and attachments not in interaction.author.roles:
                roles = interaction.author.roles
                roles.append(attachments)
                await interaction.author.edit(roles=roles)
            await interaction.edit_original_message(embed=embed)
            return await interaction.delete_original_message(delay=30)
        else:
            embed = await create_embed("global")
            embed.title = "BH Level"
            embed.add_field(name="User", value=f"{interaction.author.name}#{interaction.author.discriminator}", inline=False)
            embed.add_field(name="Level", value="0", inline=False)
            embed.add_field(name="XP", value="0", inline=False)
            await interaction.edit_original_message(embed=embed)
            return await interaction.delete_original_message(delay=30)
    else:
        cursor.execute("select * from xp where id = ?", (member.id,))
        rows = cursor.fetchall()
        if rows.__len__() >= 1:
            embed = await create_embed("global")
            embed.title = "BH Level"
            embed.add_field(name="User", value=f"{member.name}#{member.discriminator}", inline=False)
            embed.add_field(name="Level", value=str(rows[0][2]), inline=False)
            embed.add_field(name="XP", value=f"{str(rows[0][1])}/{str(math.floor(((rows[0][2]+1)/0.07)**2))}", inline=False)
            attachments = interaction.guild.get_role(attachmentsid)
            if rows[0][2] >= 10 and isinstance(attachments, discord.Role) and attachments not in member.roles:
                roles = member.roles
                roles.append(attachments)
                await member.edit(roles=roles)
            await interaction.edit_original_message(embed=embed)
            return await interaction.delete_original_message(delay=30)
        else:
            embed = await create_embed("global")
            embed.title = "BH Level"
            embed.add_field(name="User", value=f"{member.name}#{member.discriminator}", inline=False)
            embed.add_field(name="Level", value="0", inline=False)
            embed.add_field(name="XP", value="0", inline=False)
            await interaction.edit_original_message(embed=embed)
            return await interaction.delete_original_message(delay=30)

# is this necessary? absolutely not.
@commands.cooldown(3, 30, commands.BucketType.user)
@bot.command()
async def membercount(ctx: commands.Context):
    if not isinstance(ctx.guild, discord.Guild):
        embed = await create_embed("global")
        embed.title = "Member Count"
        embed.description = "This command can only be used from within a server!"
        return await ctx.reply(embed=embed, delete_after=15)
    embed = await create_embed("global")
    embed.title = f"{ctx.guild.name} ({str(ctx.guild.id)})"
    embed.description = f"{ctx.guild.approximate_presence_count}/{ctx.guild.approximate_member_count}"
    return await ctx.reply(embed=embed, delete_after=30)

# DIEEEEEEEE!!!!!!!!!!
@commands.cooldown(1, 40, commands.BucketType.user)
@jd.command(aliases=["createcase", "newcase"])
async def create(ctx: commands.Context):
    sup = await is_supervisor(ctx)
    if sup == False:
        embed = await create_embed("jd")
        embed.title = "BH Justice Department"
        embed.description = "You do not have permission to use JD commands."
        if isinstance(ctx.command, commands.Command):
            ctx.command.reset_cooldown(ctx)
        return await ctx.reply(embed=embed, delete_after=15)
    cursor = connection.cursor()
    originalmessage = None
    async with ctx.typing():
        if isinstance(ctx.channel, discord.TextChannel) or isinstance(ctx.channel, discord.Thread):
            try:
                originalmessage = await ctx.author.send(embed=discord.Embed(title="Loading"))
            except discord.Forbidden as e:
                embed = embed = await create_embed("jd")
                embed.title = "BH JD Case Creation"
                embed.description = "I was unable to DM you, please make sure your DMs are open for me!"
                embed.set_image(url="https://i.gyazo.com/4a34ad7a3b7daa1da12010c11ee840b5.gif")
                await ctx.reply(embed=embed, delete_after=30)
                if isinstance(ctx.command, commands.Command):
                    ctx.command.reset_cooldown(ctx)
                return
        else:
            originalmessage = await ctx.send(embed=discord.Embed(title="Loading"))
    caseinfo = {}
    mainview = view()
    embed = await create_embed("jd")
    embed.title = "BH JD Case Creation"
    embed.description = "Please select charges"
    selectmenu = chargeselect()
    mainview.add_item(selectmenu)
    await originalmessage.edit(embed=embed, view=mainview)
    await mainview.wait()
    caseinfo["charge"] = ""
    for charge in selectmenu.values:
        caseinfo["charge"] = caseinfo["charge"] + str(charge) + "|"
    if "Exploiting" in selectmenu.values:
        def mcheck(msg: discord.Message):
            return msg.author == ctx.author and msg.channel == originalmessage.channel
        async def getevents(failed=False):
            embed = await create_embed("jd")
            embed.title = "BH JD Case Creation"
            if failed == False:
                embed.description = "Please send how many events the perpetrator exploited at"
            else:
                embed.description = "Uh oh, that isn't a number! Please send how many events this individual exploited at"
            await originalmessage.edit(embed=embed, view=None)
            message = await bot.wait_for("message", check=mcheck)
            if message.content.isnumeric() == True:
                if caseinfo["charge"].find("Exploiting") != -1:
                    caseinfo["charge"] = caseinfo["charge"].replace("Exploiting", f"Exploiting x{message.content}")
                else:
                    return
            else:
                return await getevents(failed=True)
        await getevents(failed=False)
    if "Malicious Distribution" in selectmenu.values:
        def mcheck(msg: discord.Message):
            return msg.author == ctx.author and msg.channel == originalmessage.channel
        async def getlevel(failed=False):
            embed = await create_embed("jd")
            embed.title = "BH JD Case Creation"
            if failed == False:
                embed.description = "Please send the Severity level of the Malicious Distribution"
            else:
                embed.description = "Uh oh, that isn't a number! Please send the Severity level of the Malicious Distribution"
            await originalmessage.edit(embed=embed, view=None)
            message = await bot.wait_for("message", check=mcheck)
            if message.content.isnumeric() == True:
                if caseinfo["charge"].find("Malicious Distribution") != -1:
                    caseinfo["charge"] = caseinfo["charge"].replace("Malicious Distribution", f"Malicious Distribution ({message.content})")
                else:
                    return
            else:
                return await getlevel(failed=True)
        await getlevel(failed=False)
    if "Scamming" in selectmenu.values:
        def mcheck(msg: discord.Message):
            return msg.author == ctx.author and msg.channel == originalmessage.channel
        async def getlevel(failed=False):
            embed = await create_embed("jd")
            embed.title = "BH JD Case Creation"
            if failed == False:
                embed.description = "Please send the Severity level of the Scamming"
            else:
                embed.description = "Uh oh, that isn't a number! Please send the Severity level of the Scamming"
            await originalmessage.edit(embed=embed, view=None)
            message = await bot.wait_for("message", check=mcheck)
            if message.content.isnumeric() == True:
                if caseinfo["charge"].find("Scamming") != -1:
                    caseinfo["charge"] = caseinfo["charge"].replace("Scamming", f"Scamming ({message.content})")
                else:
                    return
            else:
                return await getlevel(failed=True)
        await getlevel(failed=False)
    mainview = view()
    embed = await create_embed("jd")
    embed.title = "BH JD Case Creation"
    embed.description = "Please send proof as links, separating each link as a new message"
    await originalmessage.edit(embed=embed, view=None)
    def mcheck(msg: discord.Message):
        return msg.author == ctx.author and msg.channel == originalmessage.channel
    message = await bot.wait_for("message", check=mcheck)
    caseinfo["proof"] = message.content
    async def acceptinput():
        mainview = view()
        embed = await create_embed("jd")
        embed.title = "BH JD Case Creation"
        embed.description = "Please send proof as links, separating each link as a new message, and press \"Confirm\" when you have inputted all proof"
        confirm = confirmbutton()
        mainview.add_item(confirm)
        await originalmessage.edit(embed=embed, view=mainview)
        done, pending = await asyncio.wait([mainview.wait(), bot.wait_for("message", check=mcheck)], return_when=asyncio.FIRST_COMPLETED)
        for task in pending:
            task.cancel()
        for task in done:
            msg = await task
            if isinstance(msg, discord.Message):
                caseinfo["proof"] = caseinfo["proof"] + "|" + msg.content
                return await acceptinput()
            elif isinstance(msg, bool):
                return
    await acceptinput()
    mainview = view()
    caseinfo["identityfound"] = False
    embed = await create_embed("jd")
    embed.title = "BH JD Case Creation"
    embed.description = "Please send the perpetrator's Discord ID, separated by new messages, or press \"Skip\" if it is unknown"
    skip = skipbutton()
    mainview.add_item(skip)
    await originalmessage.edit(embed=embed, view=mainview)
    done, pending = await asyncio.wait([mainview.wait(), bot.wait_for("message", check=mcheck)], return_when=asyncio.FIRST_COMPLETED)
    getmore = True
    for task in pending:
        task.cancel()
    for task in done:
        msg = await task
        if isinstance(msg, discord.Message):
            caseinfo["did"] = "|" + msg.content
            getmore = True
            caseinfo["identityfound"] = True
        elif isinstance(msg, bool):
            caseinfo["did"] = "|UNKNOWN"
            getmore = False
    if getmore == True:
        async def acceptinput():
            mainview = view()
            embed = await create_embed("jd")
            embed.title = "BH JD Case Creation"
            embed.description = "Please send the perpetrator's Discord ID(s), separated by new messages, and press \"Confirm\" when you have inputted all Discord ID(s)"
            confirm = confirmbutton()
            mainview.add_item(confirm)
            await originalmessage.edit(embed=embed, view=mainview)
            done, pending = await asyncio.wait([mainview.wait(), bot.wait_for("message", check=mcheck)], return_when=asyncio.FIRST_COMPLETED)
            for task in pending:
                task.cancel()
            for task in done:
                msg = await task
                if isinstance(msg, discord.Message):
                    caseinfo["did"] = caseinfo["did"] + "|" + msg.content
                    return await acceptinput()
                elif isinstance(msg, bool):
                    return
        await acceptinput()
    mainview = view()
    embed = await create_embed("jd")
    embed.title = "BH JD Case Creation"
    embed.description = "Please send the perpetrator's Discord username, separated by new messages, or press \"Skip\" if it is unknown"
    skip = skipbutton()
    mainview.add_item(skip)
    await originalmessage.edit(embed=embed, view=mainview)
    done, pending = await asyncio.wait([mainview.wait(), bot.wait_for("message", check=mcheck)], return_when=asyncio.FIRST_COMPLETED)
    getmore = True
    for task in pending:
        task.cancel()
    for task in done:
        msg = await task
        if isinstance(msg, discord.Message):
            caseinfo["dusername"] = msg.content + "|"
            getmore = True
            caseinfo["identityfound"] = True
        elif isinstance(msg, bool):
            caseinfo["dusername"] = "UNKNOWN|"
            getmore = False
    if getmore == True:
        async def acceptinput():
            mainview = view()
            embed = await create_embed("jd")
            embed.title = "BH JD Case Creation"
            embed.description = "Please send the perpetrator's Discord username(s), separated by new messages, and press \"Confirm\" when you have inputted all Discord username(s)"
            confirm = confirmbutton()
            mainview.add_item(confirm)
            await originalmessage.edit(embed=embed, view=mainview)
            done, pending = await asyncio.wait([mainview.wait(), bot.wait_for("message", check=mcheck)], return_when=asyncio.FIRST_COMPLETED)
            for task in pending:
                task.cancel()
            for task in done:
                msg = await task
                if isinstance(msg, discord.Message):
                    caseinfo["dusername"] = caseinfo["dusername"] + "|" + msg.content
                    return await acceptinput()
                elif isinstance(msg, bool):
                    return
        await acceptinput()
    mainview = view()
    embed = await create_embed("jd")
    embed.title = "BH JD Case Creation"
    embed.description = "Please send the perpetrator's Roblox ID, separated by this character: | or press \"Skip\" if it is unknown"
    skip = skipbutton()
    mainview.add_item(skip)
    await originalmessage.edit(embed=embed, view=mainview)
    done, pending = await asyncio.wait([mainview.wait(), bot.wait_for("message", check=mcheck)], return_when=asyncio.FIRST_COMPLETED)
    getmore = True
    for task in pending:
        task.cancel()
    for task in done:
        msg = await task
        if isinstance(msg, discord.Message):
            caseinfo["rid"] = "|" + msg.content
            getmore = True
            caseinfo["identityfound"] = True
        elif isinstance(msg, bool):
            caseinfo["rid"] = "|UNKNOWN"
            getmore = False
    if getmore == True:
        async def acceptinput():
            mainview = view()
            embed = await create_embed("jd")
            embed.title = "BH JD Case Creation"
            embed.description = "Please send the perpetrator's Roblox ID(s), separated by new messages, and press \"Confirm\" when you have inputted all Roblox ID(s)"
            confirm = confirmbutton()
            mainview.add_item(confirm)
            await originalmessage.edit(embed=embed, view=mainview)
            done, pending = await asyncio.wait([mainview.wait(), bot.wait_for("message", check=mcheck)], return_when=asyncio.FIRST_COMPLETED)
            for task in pending:
                task.cancel()
            for task in done:
                msg = await task
                if isinstance(msg, discord.Message):
                    caseinfo["rid"] = caseinfo["rid"] + "|" + msg.content
                    return await acceptinput()
                elif isinstance(msg, bool):
                    return
        await acceptinput()
    mainview = view()
    if caseinfo["identityfound"] == True:
        async def getrusername(warn=False):
            if warn == False:
                embed = await create_embed("jd")
                embed.title = "BH JD Case Creation"
                embed.description = "Please send the perpetrator's Roblox username, separated by new messages, or press \"Skip\" if it is unknown"
                skip = skipbutton()
                mainview.add_item(skip)
                await originalmessage.edit(embed=embed, view=mainview)
                def mcheck(msg: discord.Message):
                    return msg.author == ctx.author and msg.channel == originalmessage.channel
                done, pending = await asyncio.wait([mainview.wait(), bot.wait_for("message", check=mcheck)], return_when=asyncio.FIRST_COMPLETED)
                getmore = True
                for task in pending:
                    task.cancel()
                for task in done:
                    msg = await task
                    if isinstance(msg, discord.Message):
                        if msg.content.__len__() < 3:
                            await getrusername(warn=True)
                        else:
                            caseinfo["rusername"] = msg.content + "|"
                            getmore = True
                            caseinfo["identityfound"] = True
                    elif isinstance(msg, bool):
                        caseinfo["rusername"] = "UNKNOWN|"
                        getmore = False
            else:
                embed = await create_embed("jd")
                embed.title = "BH JD Case Creation"
                embed.description = "Username too short! Please send the perpetrator's Roblox username, separated by new messages, or press \"Skip\" if it is unknown"
                skip = skipbutton()
                mainview.add_item(skip)
                await originalmessage.edit(embed=embed, view=mainview)
                def mcheck(msg: discord.Message):
                    return msg.author == ctx.author and msg.channel == originalmessage.channel
                done, pending = await asyncio.wait([mainview.wait(), bot.wait_for("message", check=mcheck)], return_when=asyncio.FIRST_COMPLETED)
                getmore = True
                for task in pending:
                    task.cancel()
                for task in done:
                    msg = await task
                    if isinstance(msg, discord.Message):
                        if msg.content.__len__() < 3:
                            await getrusername(warn=True)
                        else:
                            caseinfo["rusername"] = msg.content + "|"
                            getmore = True
                            caseinfo["identityfound"] = True
                    elif isinstance(msg, bool):
                        caseinfo["rusername"] = "UNKNOWN|"
                        getmore = False
        await getrusername(warn=False)
        if getmore == True:
            async def acceptinput():
                mainview = view()
                embed = await create_embed("jd")
                embed.title = "BH JD Case Creation"
                embed.description = "Please send the perpetrator's Roblox username(s), separated by new messages, and press \"Confirm\" when you have inputted all Roblox username(s)"
                confirm = confirmbutton()
                mainview.add_item(confirm)
                await originalmessage.edit(embed=embed, view=mainview)
                done, pending = await asyncio.wait([mainview.wait(), bot.wait_for("message", check=mcheck)], return_when=asyncio.FIRST_COMPLETED)
                for task in pending:
                    task.cancel()
                for task in done:
                    msg = await task
                    if isinstance(msg, discord.Message):
                        caseinfo["rusername"] = caseinfo["rusername"] + "|" + msg.content
                        await acceptinput()
                    elif isinstance(msg, bool):
                        return
            await acceptinput()
    else:
        async def acceptinput():
            mainview = view()
            embed = await create_embed("jd")
            embed.title = "BH JD Case Creation"
            embed.description = "Please send the perpetrator's Roblox username(s), separated by new messages, and press \"Confirm\" when you have inputted all Roblox username(s)"
            confirm = confirmbutton()
            mainview.add_item(confirm)
            await originalmessage.edit(embed=embed, view=mainview)
            done, pending = await asyncio.wait([mainview.wait(), bot.wait_for("message", check=mcheck)], return_when=asyncio.FIRST_COMPLETED)
            for task in pending:
                task.cancel()
            for task in done:
                msg = await task
                if isinstance(msg, discord.Message):
                    caseinfo["rusername"] = caseinfo["rusername"] + "|" + msg.content
                    await acceptinput()
                elif isinstance(msg, bool):
                    return
        embed = await create_embed("jd")
        embed.title = "BH JD Case Creation"
        embed.description = "Please send the perpetrator's Roblox username(s)"
        await originalmessage.edit(embed=embed, view=None)
        msg = await bot.wait_for("message", check=mcheck)
        caseinfo["rusername"] = msg.content + "|"
        await acceptinput()
    mainview = view()
    embed = await create_embed("jd")
    embed.title = "BH JD Case Creation"
    embed.description = "Please send any notes on this case or press \"Skip\" if there are none"
    skip = skipbutton()
    mainview.add_item(skip)
    await originalmessage.edit(embed=embed, view=mainview)
    done, pending = await asyncio.wait([mainview.wait(), bot.wait_for("message",check=mcheck)], return_when=asyncio.FIRST_COMPLETED)
    for task in pending:
        task.cancel()
    context = None
    for task in done:
        context = await task
    if isinstance(context, discord.Message):
        caseinfo["notes"] = context.content
    if isinstance(context, bool) == True:
        caseinfo["notes"] = "NONE"
    mainview.clear_items()
    async def showcaseinfo():
        mainview = view()
        embed = await create_embed("jd")
        embed.title = "BH JD Case Creation"
        embed.description = "Please review the case information inputted to make sure it is correct:"
        charge = str(caseinfo["charge"]).replace("|", "\n")
        embed.add_field(name="CHARGE(s)", value=f"```\n{charge}```", inline=False)
        proof = str(caseinfo["proof"]).replace("|", "\n")
        embed.add_field(name="PROOF", value=f"```\n{proof}```", inline=False)
        did = str(caseinfo['did']).replace('|', '\n')
        embed.add_field(name="DISCORD ID(s)", value=f"```\n{did}```", inline=False)
        dusername = str(caseinfo['dusername']).replace('|', '\n')
        embed.add_field(name="DISCORD USERNAME(s)", value=f"```\n{dusername}```", inline=False)
        rid = str(caseinfo['rid']).replace('|', '\n')
        embed.add_field(name="ROBLOX ID(s)", value=f"```\n{rid}```", inline=False)
        rusername = str(caseinfo['rusername']).replace('|', '\n')
        embed.add_field(name="ROBLOX USERNAME(s)", value=f"```\n{rusername}```", inline=False)
        embed.add_field(name="NOTES", value=f"```\n{str(caseinfo['notes'])}```", inline=False)
        confirm = confirmbutton()
        edit = editbutton()
        mainview.add_item(confirm)
        mainview.add_item(edit)
        await originalmessage.edit(embed=embed, view=mainview)
        await mainview.wait()
        if edit.pressed == True:
            async def editcase():
                mainview = view()
                embed = await create_embed("jd")
                embed.title = "BH JD Case Creation"
                embed.description = "Please select the fields you would like to edit"
                menu = jpeditselect(caseinfo)
                mainview.add_item(menu)
                await originalmessage.edit(embed=embed, view=mainview)
                await mainview.wait()
                
                for field in menu.values:
                    def mcheck(msg: discord.Message):
                        return msg.author == ctx.author and msg.channel == originalmessage.channel
                    mainview = view()
                    if field == "charges":
                        embed = await create_embed("jd")
                        embed.title = "BH JD Case Creation"
                        embed.description = "Please select charges"
                        selectmenu = chargeselect()
                        mainview.add_item(selectmenu)
                        await originalmessage.edit(embed=embed, view=mainview)
                        await mainview.wait()
                        caseinfo["charge"] = ""
                        for charge in selectmenu.values:
                            caseinfo["charge"] = caseinfo["charge"] + str(charge) + "|"
                        if "Exploiting" in selectmenu.values:
                            async def getevents(failed=False):
                                embed = await create_embed("jd")
                                embed.title = "BH JD Case Creation"
                                if failed == False:
                                    embed.description = "Please send how many events the perpetrator exploited at"
                                else:
                                    embed.description = "Uh oh, that isn't a number! Please send how many events this individual exploited at"
                                await originalmessage.edit(embed=embed, view=None)
                                message = await bot.wait_for("message", check=mcheck)
                                if message.content.isnumeric() == True:
                                    if message.content.find("Exploiting") != -1:
                                        caseinfo["charge"].replace("Exploiting", f"Exploiting x{message.content}")
                                    else:
                                        return
                                else:
                                    return await getevents(failed=True)
                            await getevents(failed=False)
                        else:
                            continue
                    elif field == "did":
                        embed = await create_embed("jd")
                        embed.title = "BH JD Case Creation"
                        embed.description = "Please send the perpetrator's Discord ID(s), separated by new messages"
                        await originalmessage.edit(embed=embed, view=None)
                        msg = await bot.wait_for("message", check=mcheck)
                        caseinfo["did"] = "|" + msg.content
                        async def acceptinput():
                            mainview = view()
                            embed = await create_embed("jd")
                            embed.title = "BH JD Case Creation"
                            embed.description = "Please send the perpetrator's Discord ID(s), separated by new messages, and press \"Confirm\" when you have inputted all Discord ID(s)"
                            confirm = confirmbutton()
                            mainview.add_item(confirm)
                            await originalmessage.edit(embed=embed, view=mainview)
                            done, pending = await asyncio.wait([mainview.wait(), bot.wait_for("message", check=mcheck)], return_when=asyncio.FIRST_COMPLETED)
                            for task in pending:
                                task.cancel()
                            for task in done:
                                msg = await task
                                if isinstance(msg, discord.Message):
                                    caseinfo["did"] = caseinfo["did"] + "|" + msg.content
                                    await acceptinput()
                                elif isinstance(msg, bool):
                                    return
                        await acceptinput()
                    elif field == "dusername":
                        embed = await create_embed("jd")
                        embed.title = "BH JD Case Creation"
                        embed.description = "Please send the perpetrator's Discord username(s), separated by new messages"
                        await originalmessage.edit(embed=embed, view=None)
                        msg = await bot.wait_for("message", check=mcheck)
                        caseinfo["dusername"] = msg.content
                        async def acceptinput():
                            mainview = view()
                            embed = await create_embed("jd")
                            embed.title = "BH JD Case Creation"
                            embed.description = "Please send the perpetrator's Discord username(s), separated by new messages, and press \"Confirm\" when you have inputted all Discord username(s)"
                            confirm = confirmbutton()
                            mainview.add_item(confirm)
                            await originalmessage.edit(embed=embed, view=mainview)
                            done, pending = await asyncio.wait([mainview.wait(), bot.wait_for("message", check=mcheck)], return_when=asyncio.FIRST_COMPLETED)
                            for task in pending:
                                task.cancel()
                            for task in done:
                                msg = await task
                                if isinstance(msg, discord.Message):
                                    caseinfo["dusername"] = caseinfo["dusername"] + "|" + msg.content
                                    await acceptinput()
                                elif isinstance(msg, bool):
                                    return
                        await acceptinput()
                    elif field == "rid":
                        embed = await create_embed("jd")
                        embed.title = "BH JD Case Creation"
                        embed.description = "Please send the perpetrator's Roblox ID(s), separated by new messages"
                        await originalmessage.edit(embed=embed, view=None)
                        msg = await bot.wait_for("message", check=mcheck)
                        caseinfo["rid"] = "|" + msg.content
                        async def acceptinput():
                            mainview = view()
                            embed = await create_embed("jd")
                            embed.title = "BH JD Case Creation"
                            embed.description = "Please send the perpetrator's Roblox ID(s), separated by new messages, and press \"Confirm\" when you have inputted all Roblox ID(s)"
                            confirm = confirmbutton()
                            mainview.add_item(confirm)
                            await originalmessage.edit(embed=embed, view=mainview)
                            done, pending = await asyncio.wait([mainview.wait(), bot.wait_for("message", check=mcheck)], return_when=asyncio.FIRST_COMPLETED)
                            for task in pending:
                                task.cancel()
                            for task in done:
                                msg = await task
                                if isinstance(msg, discord.Message):
                                    caseinfo["rid"] = caseinfo["rid"] + "|" + msg.content
                                    await acceptinput()
                                elif isinstance(msg, bool):
                                    return
                        await acceptinput()
                    elif field == "rusername":
                        embed = await create_embed("jd")
                        embed.title = "BH JD Case Creation"
                        embed.description = "Please send the perpetrator's Roblox username(s), separated by new messages"
                        await originalmessage.edit(embed=embed, view=None)
                        msg = await bot.wait_for("message", check=mcheck)
                        caseinfo["rusername"] = msg.content
                        async def acceptinput():
                            mainview = view()
                            embed = await create_embed("jd")
                            embed.title = "BH JD Case Creation"
                            embed.description = "Please send the perpetrator's Roblox username(s), separated by new messages, and press \"Confirm\" when you have inputted all Roblox username(s)"
                            confirm = confirmbutton()
                            mainview.add_item(confirm)
                            await originalmessage.edit(embed=embed, view=mainview)       
                            done, pending = await asyncio.wait([mainview.wait(), bot.wait_for("message", check=mcheck)], return_when=asyncio.FIRST_COMPLETED)
                            for task in pending:
                                task.cancel()
                            for task in done:
                                msg = await task
                                if isinstance(msg, discord.Message):
                                    caseinfo["rusername"] = caseinfo["rusername"] + "|" + msg.content
                                    await acceptinput()
                                elif isinstance(msg, bool):
                                    return
                        await acceptinput()
                    elif field == "notes":
                        embed = await create_embed("jd")
                        embed.title = "BH JD Case Creation"
                        embed.description = "Please send any notes on this case"
                        await originalmessage.edit(embed=embed, view=None)
                        msg = await bot.wait_for("message", check=mcheck)
                        caseinfo["notes"] = msg.content
                await showcaseinfo()
            await editcase()
    await showcaseinfo()
    date = datetime.date.today()
    try:
        severity = 0
        expiredate = ""
        for charge in caseinfo["charge"].split("|"):
            if charge == "":
                continue
            if charge in charges:
                severity = sum((severity, charges[charge]))
                continue
            if charge.find("Exploiting") != -1:
                severity = sum((severity, int(charge.split("x")[2] * 2))) # type: ignore
                continue
            elif charge.find("Malicious Distribution") != -1:
                severity = sum((severity, int(charge.split("(")[1]))) # type: ignore
                continue
            elif charge.find("Scamming") != -1:
                severity = sum((severity, int(charge.split("(")[1]))) # type: ignore
                continue
        pedocharge = False
        for charge in caseinfo["charge"].split("|"):
            if charge == "Pedophilia" or charge == "Jailbaiting":
                pedocharge = True
                expiredate = "NONE"
        if severity >= 20 and pedocharge == False:
            exp = date + datetime.timedelta(days=730)
            for charge in caseinfo["charge"].split("|"):
                if charge.find("Exploiting") != -1:
                    exp += datetime.timedelta(days=60*int(charge.split("x")[2]))
                    break
            expiredate = exp.strftime("%d/%m/%Y")
        elif severity >= 10 and pedocharge == False:
            exp = date + datetime.timedelta(days=365)
            for charge in caseinfo["charge"].split("|"):
                if charge.find("Exploiting") != -1:
                    exp = exp + datetime.timedelta(days=60*int(charge.split("x")[2]))
                    break
            expiredate = exp.strftime("%d/%m/%Y")
        elif pedocharge == False:
            exp = date
            for charge in caseinfo["charge"].split("|"):
                if charge.find("Exploiting") != -1:
                    exp = exp + datetime.timedelta(days=60*int(charge.split("x")[2]))
                    break
            expiredate = exp.strftime("%d/%m/%Y")
        date = date.strftime("%d/%m/%Y")
        cursor.execute("select * from cases")
        rows = cursor.fetchall()
        caseid = rows.__len__() + 1
        cursor.execute("insert into cases values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (caseid, str(caseinfo["charge"]), "ACTIVE", str(caseinfo["proof"]), str(date), str(expiredate), str(caseinfo["dusername"]), str(caseinfo["did"]), str(caseinfo["rusername"]), str(caseinfo["rid"]), str(caseinfo["notes"]), severity))
        embed = await create_embed("jd")
        embed.title = "BH JD Case Creation"
        embed.description = f"Case successfully created! ID is {caseid}."
        await originalmessage.edit(embed=embed, view=None)
        linkview = view()
        linkview.add_item(caselookupbutton())
        embed = await create_embed("jd")
        embed.title = f"NEW LOW CASE"
        embed.description = f"`b.case {str(caseid)}` in <#{caselookupid}> to see details!"
        newcases = await bot.fetch_channel(newcasesid)
        try:
            msg = await newcases.send(embed=embed, view=linkview) # type: ignore
            try:
                await msg.publish()
            except:
                logger.debug("Unable to publish new case message")
            return
        except:
            embed = await create_embed("jd")
            embed.title = "BH JD Case Creation"
            embed.description = "Unable to announce case creation"
            await ctx.reply(embed=embed)
            return
    except Error as e:
        logger.debug("Error when adding case, traceback in logs.txt")
        traceback.print_exc(file=open("logs.txt", "a"))
        embed = await create_embed("jd")
        embed.title = "BH JD Case Creation"
        embed.description = "Error while adding case: " + str(e)
        await originalmessage.edit(embed=embed, view=None)
        return

# now lets do it again
@commands.cooldown(1, 40, commands.BucketType.user)
@jd.command(aliases=["editcase"])
async def edit(ctx: commands.Context, caseid: str=None):
    sup = await is_supervisor(ctx)
    if sup == False:
        embed = await create_embed("jd")
        embed.title = "BH Justice Department"
        embed.description = "You do not have permission to use JD commands."
        if isinstance(ctx.command, commands.Command):
            ctx.command.reset_cooldown(ctx)
        return await ctx.reply(embed=embed, delete_after=15)
    async with ctx.typing():
        if isinstance(caseid, str):
            if caseid.isnumeric() == False:
                embed = await create_embed("jd")
                embed.title = "BH JD Case Editing"
                embed.description = "Please enter a valid case ID"
                await ctx.reply(embed=embed)
                if isinstance(ctx.command, commands.Command):
                    ctx.command.reset_cooldown(ctx)
                return
        else:
            embed = await create_embed("jd")
            embed.title = "BH JD Case Editing"
            embed.description = "Please enter a valid case ID"
            await ctx.reply(embed=embed)
            if isinstance(ctx.command, commands.Command):
                ctx.command.reset_cooldown(ctx)
            return
    if str(caseid).isnumeric():
        async with ctx.typing():
            case = Case.from_id(int(caseid))
            caseinfo = {}
            embed = await create_embed("global")
            embed.title = "Loading"
            originalmessage = None
            try:
                originalmessage = await ctx.author.send(embed=embed)
            except discord.Forbidden:
                embed = embed = await create_embed("jd")
                embed.title = "BH JD Case Editing"
                embed.description = "I was unable to DM you, please make sure your DMs are open for me!"
                embed.set_image(url="https://i.gyazo.com/4a34ad7a3b7daa1da12010c11ee840b5.gif")
                await ctx.reply(embed=embed)
                return
            caseinfo["charge"] = str(case.charges)
            if caseinfo["charge"].__len__() > 100:
                new = ""
                for i in range(0, caseinfo["charge"].__len__()+1):
                    if i < 81:
                        new = new + caseinfo["charge"][i]
                    else:
                        new = new + "..."
                        caseinfo["charge"] = new
                        break
            caseinfo["proof"] = str(case.proof)
            if caseinfo["proof"].__len__() > 100:
                new = ""
                for i in range(0, caseinfo["proof"].__len__()+1):
                    if i < 83:
                        new = new + caseinfo["proof"][i]
                    else:
                        new = new + "..."
                        caseinfo["proof"] = new
                        break
            caseinfo["did"] = str(case.did)
            if caseinfo["did"].__len__() > 100:
                new = ""
                for i in range(0, caseinfo["did"].__len__()+1):
                    if i < 75:
                        new = new + caseinfo["did"][i]
                    else:
                        new = new + "..."
                        caseinfo["did"] = new
                        break
            caseinfo["dusername"] = str(case.dusername)
            if caseinfo["dusername"].__len__() > 100:
                new = ""
                for i in range(0, caseinfo["dusername"].__len__()+1):
                    if i < 69:
                        new = new + caseinfo["dusername"][i]
                    else:
                        new = new + "..."
                        caseinfo["dusername"] = new
                        break
            caseinfo["rid"] = str(case.rid)
            if caseinfo["rid"].__len__() > 100:
                new = ""
                for i in range(0, caseinfo["rid"].__len__()+1):
                    if i < 76:
                        new = new + caseinfo["rid"][i]
                    else:
                        new = new + "..."
                        caseinfo["rid"] = new
                        break
            caseinfo["rusername"] = str(case.rusername)
            if caseinfo["rusername"].__len__() > 100:
                new = ""
                for i in range(0, caseinfo["rusername"].__len__()+1):
                    if i < 70:
                        new = new + caseinfo["rusername"][i]
                    else:
                        new = new + "..."
                        caseinfo["rusername"] = new
                        break
            caseinfo["notes"] = str(case.notes)
            if caseinfo["notes"].__len__() > 100:
                new = ""
                for i in range(0, caseinfo["notes"].__len__()+1):
                    if i < 83:
                        new = new + caseinfo["notes"][i]
                    else:
                        new = new + "..."
                        caseinfo["notes"] = new
                        break
        async def showcaseinfo(first=True):
            async def editcase():
                def mcheck(msg: discord.Message):
                    return msg.author == ctx.author and msg.channel == originalmessage.channel
                mainview = view()
                embed = await create_embed("jd")
                embed.title = "BH JD Case Editing"
                embed.description = "Please select the fields you would like to edit"
                menu = jpeditselect(caseinfo)
                mainview.add_item(menu)
                await originalmessage.edit(embed=embed, view=mainview)
                await mainview.wait()
                for field in menu.values:
                    mainview = view()
                    if field == "charges":
                        embed = await create_embed("jd")
                        embed.title = "BH JD Case Creation"
                        embed.description = "Please select charges"
                        selectmenu = chargeselect()
                        mainview.add_item(selectmenu)
                        await originalmessage.edit(embed=embed, view=mainview)
                        await mainview.wait()
                        caseinfo["charge"] = ""
                        for charge in selectmenu.values:
                            caseinfo["charge"] = caseinfo["charge"] + str(charge) + "|"
                        if "Exploiting" in selectmenu.values:
                            def mcheck(msg: discord.Message):
                                return msg.author == ctx.author and msg.channel == originalmessage.channel
                            async def getevents(failed=False):
                                embed = await create_embed("jd")
                                embed.title = "BH JD Case Creation"
                                if failed == False:
                                    embed.description = "Please send how many events the perpetrator exploited at"
                                else:
                                    embed.description = "Uh oh, that isn't a number! Please send how many events this individual exploited at"
                                await originalmessage.edit(embed=embed, view=None)
                                message: discord.Message = await bot.wait_for("message", check=mcheck)
                                if message.content.isnumeric() == True:
                                    if message.content.find("Exploiting") != -1:
                                        caseinfo["charge"].replace("Exploiting", f"Exploiting x{message.content}")
                                    else:
                                        return
                                else:
                                    return await getevents(failed=True)
                            await getevents(failed=False)
                    elif field == "did":
                        embed = await create_embed("jd")
                        embed.title = "BH JD Case Editing"
                        embed.description = "Please send the perpetrator's Discord ID(s), separated by new messages"
                        await originalmessage.edit(embed=embed, view=None)
                        def mcheck(msg: discord.Message):
                            return msg.author == ctx.author and msg.channel == originalmessage.channel
                        msg: discord.Message = await bot.wait_for("message", check=mcheck)
                        caseinfo["did"] = "|" + msg.content
                        async def acceptinput():
                            mainview = view()
                            embed = await create_embed("jd")
                            embed.title = "BH JD Case Editing"
                            embed.description = "Please send the perpetrator's Discord ID(s), separated by new messages, and press \"Confirm\" when you have inputted all Discord ID(s)"
                            confirm = confirmbutton()
                            mainview.add_item(confirm)
                            await originalmessage.edit(embed=embed, view=mainview)
                            done, pending = await asyncio.wait([mainview.wait(), bot.wait_for("message", check=mcheck)], return_when=asyncio.FIRST_COMPLETED)
                            for task in pending:
                                task.cancel()
                            for task in done:
                                msg = await task
                                if isinstance(msg, discord.Message):
                                    caseinfo["did"] = caseinfo["did"] + "|" + msg.content
                                    await acceptinput()
                                elif isinstance(msg, bool):
                                    return
                        await acceptinput()
                    elif field == "dusername":
                        embed = await create_embed("jd")
                        embed.title = "BH JD Case Editing"
                        embed.description = "Please send the perpetrator's Discord username(s), separated by new messages"
                        await originalmessage.edit(embed=embed, view=None)
                        def mcheck(msg: discord.Message):
                            return msg.author == ctx.author and msg.channel == originalmessage.channel
                        msg = await bot.wait_for("message", check=mcheck)
                        caseinfo["dusername"] = msg.content
                        async def acceptinput():
                            mainview = view()
                            embed = await create_embed("jd")
                            embed.title = "BH JD Case Editing"
                            embed.description = "Please send the perpetrator's Discord username(s), separated by new messages, and press \"Confirm\" when you have inputted all Discord username(s)"
                            confirm = confirmbutton()
                            mainview.add_item(confirm)
                            await originalmessage.edit(embed=embed, view=mainview)
                            done, pending = await asyncio.wait([mainview.wait(), bot.wait_for("message", check=mcheck)], return_when=asyncio.FIRST_COMPLETED)
                            for task in pending:
                                task.cancel()
                            for task in done:
                                msg = await task
                                if isinstance(msg, discord.Message):
                                    caseinfo["dusername"] = caseinfo["dusername"] + "|" + msg.content
                                    await acceptinput()
                                elif isinstance(msg, bool):
                                    return
                        await acceptinput()
                    elif field == "rid":
                        embed = await create_embed("jd")
                        embed.title = "BH JD Case Editing"
                        embed.description = "Please send the perpetrator's Roblox ID(s), separated by new messages"
                        await originalmessage.edit(embed=embed, view=None)
                        def mcheck(msg: discord.Message):
                            return msg.author == ctx.author and msg.channel == originalmessage.channel
                        msg = await bot.wait_for("message", check=mcheck)
                        caseinfo["rid"] = "|" + msg.content
                        async def acceptinput():
                            mainview = view()
                            embed = await create_embed("jd")
                            embed.title = "BH JD Case Editing"
                            embed.description = "Please send the perpetrator's Roblox ID(s), separated by new messages, and press \"Confirm\" when you have inputted all Roblox ID(s)"
                            confirm = confirmbutton()
                            mainview.add_item(confirm)
                            await originalmessage.edit(embed=embed, view=mainview)
                            done, pending = await asyncio.wait([mainview.wait(), bot.wait_for("message", check=mcheck)], return_when=asyncio.FIRST_COMPLETED)
                            for task in pending:
                                task.cancel()
                            for task in done:
                                msg = await task
                                if isinstance(msg, discord.Message):
                                    caseinfo["rid"] = caseinfo["rid"] + "|" + msg.content
                                    await acceptinput()
                                elif isinstance(msg, bool):
                                    return
                        await acceptinput()
                    elif field == "rusername":
                        embed = await create_embed("jd")
                        embed.title = "BH JD Case Editing"
                        embed.description = "Please send the perpetrator's Roblox username(s), separated by new messages"
                        mainview.clear_items()
                        await originalmessage.edit(embed=embed, view=None)
                        msg = await bot.wait_for("message", check=mcheck)
                        caseinfo["rusername"] = msg.content
                        async def acceptinput():
                            embed = await create_embed("jd")
                            embed.title = "BH JD Case Editing"
                            embed.description = "Please send the perpetrator's Roblox username(s), separated by new messages, and press \"Confirm\" when you have inputted all Roblox username(s)"
                            mainview.clear_items()
                            confirm = confirmbutton()
                            mainview.add_item(confirm)
                            await originalmessage.edit(embed=embed, view=mainview)
                            done, pending = await asyncio.wait([mainview.wait(), bot.wait_for("message", check=mcheck)], return_when=asyncio.FIRST_COMPLETED)
                            for task in pending:
                                task.cancel()
                            for task in done:
                                msg = await task
                                if isinstance(msg, discord.Message):
                                    caseinfo["rusername"] = caseinfo["rusername"] + "|" + msg.content
                                    await acceptinput()
                                elif isinstance(msg, bool):
                                    return
                        await acceptinput()
                    elif field == "notes":
                        embed = await create_embed("jd")
                        embed.title = "BH JD Case Editing"
                        embed.description = "Please send any notes on this case"
                        mainview.clear_items()
                        await originalmessage.edit(embed=embed, view=None)
                        msg = await bot.wait_for("message", check=mcheck)
                        caseinfo["notes"] = msg.content
                await showcaseinfo(first=False)
            if first == False:
                mainview = view()
                embed = await create_embed("jd")
                embed.title = "BH JD Case Editing"
                embed.description = "Please review the case information inputted to make sure it is correct:"
                charge = str(caseinfo["charge"]).replace("|", "\n")
                embed.add_field(name="CHARGE(s)", value="```\n" + charge + "```", inline=False)
                proof = str(caseinfo["proof"]).replace("|", "\n")
                embed.add_field(name="PROOF", value="```\n" + proof + "```", inline=False)
                did = str(caseinfo["did"]).replace("|", "\n")
                embed.add_field(name="DISCORD ID(s)", value="```\n" + did + "```", inline=False)
                dusername = str(caseinfo["dusername"]).replace("|", "\n")
                embed.add_field(name="DISCORD USERNAME(s)", value="```\n" + dusername + "```", inline=False)
                rid = str(caseinfo["rid"]).replace("|", "\n")
                embed.add_field(name="ROBLOX ID(s)", value="```\n" + rid + "```", inline=False)
                rusername = str(caseinfo["rusername"]).replace("|", "\n")
                embed.add_field(name="ROBLOX USERNAME(s)", value="```\n" + rusername + "```", inline=False)
                embed.add_field(name="NOTES", value="```\n" + str(caseinfo["notes"]) + "```", inline=False)
                confirm = confirmbutton()
                edit = editbutton()
                mainview.add_item(confirm)
                mainview.add_item(edit)
                await originalmessage.edit(embed=embed, view=mainview)
                await mainview.wait()
                if confirm.pressed == True:
                    try:
                        await case.edit({
                            "charges": caseinfo["charge"], 
                            "proof": caseinfo["proof"], 
                            "dusername": caseinfo["dusername"], 
                            "did": caseinfo["did"], 
                            "rusername": caseinfo["rusername"], 
                            "rid": caseinfo["rid"], 
                            "notes": caseinfo["notes"]
                        })
                        embed = await create_embed("jd")
                        embed.title = "BH JD Case Editing"
                        embed.description = "Case successfully edited!"
                        return await originalmessage.edit(embed=embed, view=None)
                    except Error as e:
                        logger.debug("Error while adding case to database: " + str(e))
                        embed = await create_embed("jd")
                        embed.title = "BH JD Case Editing"
                        embed.description = "Error while editing case: " + str(e)
                        return await originalmessage.edit(embed=embed, view=None)
                elif edit.pressed == True:
                    return await editcase()
                await showcaseinfo(False)
            else:
                await editcase()
        await showcaseinfo(True)

@commands.cooldown(2, 30, commands.BucketType.user)
@jd.command(aliases=["clearcase"])
async def clear(ctx: commands.Context, caseid: str=None):
    sup = await is_supervisor(ctx)
    if sup == False:
        embed = await create_embed("jd")
        embed.title = "BH Justice Department"
        embed.description = "You do not have permission to use JD commands."
        if isinstance(ctx.command, commands.Command):
            ctx.command.reset_cooldown(ctx)
        return await ctx.reply(embed=embed, delete_after=15)
    async with ctx.typing():
        if not isinstance(caseid, str):
            embed = await create_embed("jd")
            embed.title = "BH JD Case Clearing"
            embed.description = "Please enter a case ID"
            await ctx.reply(embed=embed)
            if isinstance(ctx.command, commands.Command):
                ctx.command.reset_cooldown(ctx)
            return
    try:
        case = Case.from_id(int(caseid))
        if case.status != "CLEARED":
            await case.edit({"status": "CLEARED"})
            embed = await create_embed("jd")
            embed.title = "BH JD Case Clearing"
            embed.description = "Case successfully cleared!"
            return await ctx.reply(embed=embed)
        elif case.status == "DELETED":
            embed = await create_embed("jd")
            embed.title = "BH JD Case Clearing"
            embed.description = "Case is deleted!"
            return await ctx.reply(embed=embed)
        else:
            embed = await create_embed("jd")
            embed.title = "BH JD Case Clearing"
            embed.description = "Case already cleared!"
            return await ctx.reply(embed=embed)
    except KeyError:
        embed = await create_embed("jd")
        embed.title = "BH JD Case Clearing"
        embed.description = "No case found!"
        return await ctx.reply(embed=embed)

@commands.cooldown(2, 30, commands.BucketType.user)
@jd.command(aliases=["activatecase"])
async def activate(ctx: commands.Context, caseid: str=None):
    sup = await is_supervisor(ctx)
    if sup == False:
        embed = await create_embed("jd")
        embed.title = "BH Justice Department"
        embed.description = "You do not have permission to use JD commands."
        if isinstance(ctx.command, commands.Command):
            ctx.command.reset_cooldown(ctx)
        return await ctx.reply(embed=embed, delete_after=15)
    async with ctx.typing():
        if not isinstance(caseid, str) or caseid.isnumeric() == False:
            embed = await create_embed("jd")
            embed.title = "BH JD Case Activation"
            embed.description = "Please enter a case ID"
            await ctx.reply(embed=embed)
            if isinstance(ctx.command, commands.Command):
                ctx.command.reset_cooldown(ctx)
            return
    try:
        case = Case.from_id(int(caseid))
        if case.status != "ACTIVE":
            await case.edit({"status": "ACTIVE"})
            embed = await create_embed("jd")
            embed.title = "BH JD Case Activation"
            embed.description = "Case successfully activated!"
            return await ctx.reply(embed=embed)
        elif case.status == "DELETED":
            embed = await create_embed("jd")
            embed.title = "BH JD Case Activation"
            embed.description = "Case is deleted!"
            return await ctx.reply(embed=embed)
        else:
            embed = await create_embed("jd")
            embed.title = "BH JD Case Activation"
            embed.description = "Case already active!"
            return await ctx.reply(embed=embed)
    except KeyError:
        embed = await create_embed("jd")
        embed.title = "BH JD Case Activation"
        embed.description = "No case found!"
        return await ctx.reply(embed=embed)

@commands.cooldown(2, 30, commands.BucketType.user)
@jd.command(aliases=["deletecase", "remove", "removecase"])
async def delete(ctx: commands.Context, caseid: str=None):
    sup = await is_supervisor(ctx)
    if sup == False:
        embed = await create_embed("jd")
        embed.title = "BH Justice Department"
        embed.description = "You do not have permission to use JD commands."
        if isinstance(ctx.command, commands.Command):
            ctx.command.reset_cooldown(ctx)
        return await ctx.reply(embed=embed, delete_after=15)
    async with ctx.typing():
        if not isinstance(caseid, str) or caseid.isnumeric() == False:
            embed = await create_embed("jd")
            embed.title = "BH JD Case Deletion"
            embed.description = "Please enter a valid case ID!"
            await ctx.reply(embed=embed)
            if isinstance(ctx.command, commands.Command):
                ctx.command.reset_cooldown(ctx)
            return
    try:
        case = Case.from_id(int(caseid))
        await case.delete()
        embed = await create_embed("jd")
        embed.title = "BH JD Case Deletion"
        embed.description = "Case successfully deleted!"
        await ctx.reply(embed=embed)
        return
    except KeyError:
        embed = await create_embed("jd")
        embed.title = "BH JD Case Activation"
        embed.description = "No case found!"
        await ctx.reply(embed=embed)
        return

@commands.cooldown(1, 60, commands.BucketType.user)
@jd.command()
async def vote(ctx: commands.Context):
    raise NotImplementedError()
    cursor = connection.cursor()
    originalmessage = None
    async with ctx.typing():
        if isinstance(ctx.channel, discord.TextChannel) or isinstance(ctx.channel, discord.Thread):
            try:
                originalmessage = await ctx.author.send(embed=discord.Embed(title="Loading"))
            except discord.Forbidden as e:
                embed = embed = await create_embed("jd")
                embed.title = "BH JD Voting"
                embed.description = "I was unable to DM you, please make sure your DMs are open for me!"
                embed.set_image(url="https://i.gyazo.com/4a34ad7a3b7daa1da12010c11ee840b5.gif")
                await ctx.reply(embed=embed, delete_after=30)
                if isinstance(ctx.command, commands.Command):
                    ctx.command.reset_cooldown(ctx)
                return
        else:
            originalmessage = await ctx.send(embed=discord.Embed(title="Loading"))
    voteinfo = {}
    embed = await create_embed("jd")
    embed.title = "BH JD Vote"
    embed.description = "Who is this vote for?"
    await originalmessage.edit(embed=embed)
    def mcheck(msg: discord.Message):
            return msg.author == ctx.author and msg.channel == originalmessage.channel
    message: discord.Message = await bot.wait_for("message", check=mcheck)
    voteinfo["suspect"] = message.content
    embed = await create_embed("jd")
    embed.title = "BH JD Vote"
    embed.description = "What are they accused of?"
    await originalmessage.edit(embed=embed)
    message: discord.Message = await bot.wait_for("message", check=mcheck)
    voteinfo["charges"] = message.content
    embed = await create_embed("jd")
    embed.title = "BH JD Vote"
    embed.description = "Please send evidence as links, separating each link as a new message"
    await originalmessage.edit(embed=embed, view=None)
    message = await bot.wait_for("message", check=mcheck)
    voteinfo["evidence"] = message.content
    async def acceptinput():
        mainview = view()
        embed = await create_embed("jd")
        embed.title = "BH JD Vote"
        embed.description = "Please send proof as links, separating each link as a new message, and press \"Confirm\" when you have inputted all proof"
        confirm = confirmbutton()
        mainview.add_item(confirm)
        await originalmessage.edit(embed=embed, view=mainview)
        done, pending = await asyncio.wait([mainview.wait(), bot.wait_for("message", check=mcheck)], return_when=asyncio.FIRST_COMPLETED)
        for task in pending:
            task.cancel()
        for task in done:
            msg = await task
            if isinstance(msg, discord.Message):
                voteinfo["evidence"] = voteinfo["evidence"] + "|" + msg.content
                return await acceptinput()
            elif isinstance(msg, bool):
                return
    await acceptinput()
    embed = await create_embed("jd")
    embed.title = "BH JD Vote"
    embed.description = "What is the ID of the discussion channel?"
    await originalmessage.edit(embed=embed)
    message: discord.Message = await bot.wait_for("message", check=mcheck)
    voteinfo["channel"] = message.content
    
@commands.cooldown(3, 15, commands.BucketType.user)
@bot.command()
async def previewembed(ctx: commands.Context, embed="global"):
    async with ctx.typing():
        emb = await create_embed(embed)
        emb.title = "Title"
        emb.description = "Description"
        return await ctx.reply(embed=emb, delete_after=30)

# blargh
@commands.cooldown(1, 180, commands.BucketType.user)
@bot.command(aliases=["gcheck", "lowcheck", "groupcheck"])
async def check(ctx: commands.Context, arg: str=None):
    cursor = connection.cursor()
    WebClient = aiohttp.ClientSession()
    if arg == None:
        embed = await create_embed("global")
        embed.title = "BH Group Check"
        embed.description = "Please specify a group ID to check"
        await ctx.reply(embed=embed, delete_after=30)
        if isinstance(ctx.command, commands.Command):
            ctx.command.reset_cooldown(ctx)
        return
    if ctx.guild != None:
        if ctx.guild.id == mainid and await is_snr_staff(ctx) == False:
            embed = await create_embed("global")
            embed.title = "BH Group Check"
            embed.description = "This command is not supported here"
            await ctx.reply(embed=embed, delete_after=15)
            if isinstance(ctx.command, commands.Command):
                ctx.command.reset_cooldown(ctx)
            return
    if arg.isnumeric():
        async with ctx.typing():
            try:
                foundusers = ""
                extrastrings = []
                group = await RoClient.get_group(int(arg))
                if group.member_count > 200000:
                    embed = await create_embed("global")
                    embed.title = "BH Group Check"
                    embed.description = "Too many members"
                    await ctx.reply(embed=embed, delete_after=30)
                    if isinstance(ctx.command, commands.Command):
                        ctx.command.reset_cooldown(ctx)
                    return
                members = group.get_members()
                async for member in members:
                    if member != None:
                        cursor = connection.cursor()
                        cursor.execute("select status, id from cases where rid = ? or rid like ?", (f"|{str(member.id)}", f"|{str(member.id)}|"))
                        record = cursor.fetchone()
                        if record != None:
                            if record[0] == "ACTIVE":
                                if foundusers.__len__() < 4000:
                                    foundusers = foundusers + f"[{member.name}](https://roblox.com/users/{str(member.id)}/profile) ({member.id}) | Low {record[1]}\n"
                                else:
                                    if extrastrings.__len__() == 0:
                                        extrastrings.append(f"[{member.name}](https://roblox.com/users/{str(member.id)}/profile) ({member.id}) | Low {record[1]}\n")
                                    else:
                                        index = 0
                                        found = False
                                        for string in extrastrings:
                                            if string.__len__() < 4000:
                                                found = True
                                                break
                                            else:
                                                index = sum((index, 1))
                                        if found == True:
                                            extrastrings[index] = extrastrings[index] + f"[{member.name}(https://roblox.com/users/{str(member.id)}/profile) ({member.id})] | Low {record[0]}\n"
                                        else:
                                            extrastrings.append(f"[{member.name}(https://roblox.com/users/{str(member.id)}/profile) ({member.id})] | Low {record[0]}\n")
                re = await WebClient.get(url=f"https://thumbnails.roblox.com/v1/groups/icons?groupIds={group.id}&size=420x420&format=Png&isCircular=false")
                js = await re.json()
                if foundusers != "":
                    embeds = []
                    embed = await create_embed("global")
                    embed.title = "BH Group Check"
                    embed.set_author(name=group.name, url=f"https://roblox.com/groups{group.id}")
                    embed.description = foundusers
                    embed.set_thumbnail(url=js["data"][0]["imageUrl"])
                    embeds.append(embed)
                    if extrastrings.__len__() > 1:
                        for i in range(0, 11):
                            embed2 = await create_embed("global")
                            embed2.title = "BH Group Check"
                            embed2.set_author(name=group.name, url=f"https://roblox.com/groups{group.id}")
                            embed2.description = extrastrings[i]
                            embed2.set_thumbnail(url=js["data"][0]["imageUrl"])
                            embeds.append(embed2)
                    await ctx.reply(embeds=embeds, delete_after=180)
                    return
                else:
                    embed = await create_embed("global")
                    embed.title = "BH Group Check"
                    embed.set_author(name=group.name, url=f"https://roblox.com/groups{group.id}")
                    embed.description = "No Lows found"
                    embed.set_thumbnail(url=js["data"][0]["imageUrl"])
                    await ctx.reply(embed=embed, delete_after=30)
                    return
            except exceptions.GroupNotFound:
                embed = await create_embed("global")
                embed.title = "BH Group Check"
                embed.description = "Group not found"
                await ctx.reply(embed=embed, delete_after=30)
                if isinstance(ctx.command, commands.Command):
                    ctx.command.reset_cooldown(ctx)
                return
    else:
        embed = await create_embed("global")
        embed.title = "BH Group Check"
        embed.description = "Please use an ID, not a name"
        await ctx.reply(embed=embed, delete_after=30)
        if isinstance(ctx.command, commands.Command):
            ctx.command.reset_cooldown(ctx)
        return

@commands.cooldown(1, 60, commands.BucketType.guild)
@bot.command()
async def setpresence(ctx: commands.Context, activitytype: str=None, *, message: str=None):
    async with ctx.typing():
        if await is_snr_staff(ctx) == False:
            embed = await create_embed("global")
            embed.title = "Set Presence"
            embed.description = "You do not have permission to set the bot presence"
            await ctx.reply(embed=embed, delete_after=30)
            if isinstance(ctx.command, commands.Command):
                ctx.command.reset_cooldown(ctx)
            return
        if activitytype == None:
            embed = await create_embed("global")
            embed.title = "Set Presence"
            embed.description = "Please pass an activity type! The following are accepted:\n```p - Playing\nl - Listening\ns - Streaming\nw - Watching\n```"
            await ctx.reply(embed=embed, delete_after=30)
            if isinstance(ctx.command, commands.Command):
                ctx.command.reset_cooldown(ctx)
            return
        if message == None:
            embed = await create_embed("global")
            embed.title = "Set Presence"
            embed.description = "Please pass a message!"
            await ctx.reply(embed=embed, delete_after=30)
            if isinstance(ctx.command, commands.Command):
                ctx.command.reset_cooldown(ctx)
            return
        act = discord.ActivityType.playing
        if activitytype == "p":
            act = discord.ActivityType.playing
        elif activitytype == "l":
            act = discord.ActivityType.listening
        elif activitytype == "s":
            act = discord.ActivityType.streaming
        elif activitytype == "w":
            act = discord.ActivityType.watching
        else:
            embed = await create_embed("global")
            embed.title = "Set Presence"
            embed.description = "Please pass a valid activity type! The following are accepted:\n```p - Playing\nl - Listening\ns - Streaming\nw - Watching\n```"
            await ctx.reply(embed=embed, delete_after=30)
            if isinstance(ctx.command, commands.Command):
                ctx.command.reset_cooldown(ctx)
            return
        await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=act, name=f"{message} | b.help"))
        embed = await create_embed("global")
        embed.title = "Set Presence"
        embed.description = "Successfully set presence!"
        await ctx.reply(embed=embed, delete_after=180)
        return changepres.restart()

@bot.group()
async def dev(ctx: commands.Context):
    if ctx.invoked_subcommand == None:
        embed = await create_embed("global")
        embed.title = "Invalid Command Syntax"
        embed.description = "Please pass a valid subcommand! Use `b.help dev` for a list of subcommands."
        await ctx.reply(embed=embed, delete_after=30)

# this code looks familiar...
@commands.cooldown(1, 40, commands.BucketType.user)
@dev.command(aliases=["create", "newresource"])
async def createresource(ctx: commands.Context):
    cursor = connection.cursor()
    rows = None
    async with ctx.typing():
        isdev, reason = await is_developer(ctx)
        if isdev == False:
            if reason == "role":
                embed = await create_embed("global")
                embed.title = "BH Open Resource Creation"
                embed.description = f"Please request the <@&{devid}> role to create an open resource!"
                await ctx.reply(embed=embed, delete_after=30)
                if isinstance(ctx.command, commands.Command):
                    ctx.command.reset_cooldown(ctx)
                return
            else:
                embed = await create_embed("global")
                embed.title = "BH Open Resource Creation"
                embed.description = f"Please join Blade Hub and request the Developer role to create an open resource!\nhttps://discord.gg/EpNJmEK6KY"
                await ctx.reply(embed=embed, delete_after=30)
                if isinstance(ctx.command, commands.Command):
                    ctx.command.reset_cooldown(ctx)
                return
        cursor.execute("select * from users where did=?", (ctx.author.id,))
        rows = cursor.fetchall()
    creator = None
    if rows.__len__() < 1:
        embed = await create_embed("global")
        embed.title = "BH Open Resource Creation"
        embed.description = "Please verify to create a resource! You can verify by using `b.ro verify`"
        await ctx.reply(embed=embed, delete_after=30)
        return
    else:
        creator = f"<@{ctx.author.id}>"
    originalmessage = None
    if isinstance(ctx.channel, discord.TextChannel) or isinstance(ctx.channel, discord.Thread):
        try:
            originalmessage = await ctx.author.send(embed=discord.Embed(title="Loading"))
        except discord.Forbidden as e:
            embed = embed = await create_embed("global")
            embed.title = "BH Open Resource Creation"
            embed.description = "I was unable to DM you, please make sure your DMs are open for me!"
            embed.set_image(url="https://i.gyazo.com/4a34ad7a3b7daa1da12010c11ee840b5.gif")
            await ctx.reply(embed=embed, delete_after=30)
            if isinstance(ctx.command, commands.Command):
                ctx.command.reset_cooldown(ctx)
            return
    else:
        originalmessage = await ctx.send(embed=discord.Embed(title="Loading"))
    embed = await create_embed("global")
    embed.title = "BH Open Resource Creation"
    embed.description = "Please select the resource type."
    resourceinfo = {}
    mainview = view()
    rtype = resourcetypeselect()
    mainview.add_item(rtype)
    await originalmessage.edit(embed=embed, view=mainview)
    await mainview.wait()
    resourceinfo["type"] = rtype.values[0]
    embed = await create_embed("global")
    embed.title = "BH Open Resource Creation"
    embed.description = "Please send the name of the resource."
    await originalmessage.edit(embed=embed, view=None)
    def mcheck(msg: discord.Message):
        return msg.author == ctx.author and msg.channel == originalmessage.channel
    message: discord.Message = await bot.wait_for("message", check=mcheck)
    if message.content.__len__() > 256:
        async def getname():
            def mcheck(msg: discord.Message):
                return msg.author == ctx.author and msg.channel == originalmessage.channel
            embed = await create_embed("global")
            embed.title = "BH Open Resource Creation"
            embed.description = "Uh oh! Your name exceeds 256 characters! Please send a version of the resource name shorter than 256 characters."
            await originalmessage.edit(embed=embed, view=None)
            message = await bot.wait_for("message", check=mcheck)
            if message.content.__len__() > 256:
                return await getname()
            else:
                resourceinfo["name"] = message.content
                return
        await getname()
    else:
        resourceinfo["name"] = message.content
    mainview = view()
    embed = await create_embed("global")
    embed.title = "BH Open Resource Creation"
    embed.description = "Please send a description of this resource, or press \"Skip\" if you do not have one."
    skip = skipbutton()
    mainview.add_item(skip)
    await originalmessage.edit(embed=embed, view=mainview)
    done, pending = await asyncio.wait([mainview.wait(), bot.wait_for("message", check=mcheck)], return_when=asyncio.FIRST_COMPLETED)
    for task in pending:
        task.cancel()
    for task in done:
        msg = await task # type: ignore
        if isinstance(msg, discord.Message):
            resourceinfo["description"] = msg.content
        elif isinstance(msg, bool):
            resourceinfo["description"] = "None"
    embed = await create_embed("global")
    embed.title = "BH Open Resource Creation"
    embed.description = "Please send the link to this resource"
    await originalmessage.edit(embed=embed, view=None)
    message = await bot.wait_for("message", check=mcheck)
    if message.content.__len__() > 1024:
        async def getlink():
            def mcheck(msg: discord.Message):
                return msg.author == ctx.author and msg.channel == originalmessage.channel
            embed = await create_embed("global")
            embed.title = "BH Open Resource Creation"
            embed.description = "Uh oh! Your link exceeds 1024 characters! Please send a version of the resource link shorter than 1024 characters."
            await originalmessage.edit(embed=embed, view=None)
            message = await bot.wait_for("message", check=mcheck)
            if message.content.__len__() > 256:
                return await getlink()
            else:
                resourceinfo["link"] = message.content
                return
        await getlink()
    else:
        resourceinfo["link"] = message.content
    async def showresourceinfo():
        mainview = view()
        embed = await create_embed("global")
        embed.title = "BH Open Resource Creation"
        embed.description = "Please review the resource information inputted to make sure it is correct:"
        embed.add_field(name="Type", value=resourceinfo["type"], inline=False)
        embed.add_field(name="Name", value=resourceinfo["name"], inline=False)
        embed.add_field(name="Description", value=resourceinfo["description"], inline=False)
        embed.add_field(name="Link", value=resourceinfo["link"], inline=False)
        confirm = confirmbutton()
        edit = editbutton()
        mainview.add_item(confirm)
        mainview.add_item(edit)
        await originalmessage.edit(embed=embed, view=mainview)
        await mainview.wait()
        if edit.pressed == True:
            async def editresource():
                mainview = view()
                embed = await create_embed("global")
                embed.title = "BH Open Resource Creation"
                embed.description = "Please select the fields you would like to edit"
                menu = resourceeditselect(resourceinfo)
                mainview.add_item(menu)
                await originalmessage.edit(embed=embed, view=mainview)
                await mainview.wait()
                for field in menu.values:
                    mainview = view()
                    if field == "type":
                        embed = await create_embed("global")
                        embed.title = "BH Open Resource Creation"
                        embed.description = "Please select the resource type"
                        rtype = resourcetypeselect()
                        mainview.add_item(rtype)
                        await originalmessage.edit(embed=embed, view=mainview)
                        await mainview.wait()
                        resourceinfo["type"] = rtype.values[0]
                    elif field == "name":
                        embed = await create_embed("global")
                        embed.title = "BH Open Resource Creation"
                        embed.description = "Please send a name"
                        await originalmessage.edit(embed=embed, view=None)
                        message = await bot.wait_for("message", check=mcheck)
                        if message.content.__len__() > 256:
                            async def getname():
                                def mcheck(msg: discord.Message):
                                    return msg.author == ctx.author and msg.channel == originalmessage.channel
                                embed = await create_embed("global")
                                embed.title = "BH Open Resource Creation"
                                embed.description = "Uh oh! Your name exceeds 256 characters! Please send a version of the resource name shorter than 256 characters."
                                await originalmessage.edit(embed=embed, view=None)
                                message = await bot.wait_for("message", check=mcheck)
                                if message.content.__len__() > 256:
                                    return await getname()
                                else:
                                    resourceinfo["name"] = message.content
                                    return
                            await getname()
                        else:
                            resourceinfo["name"] = message.content
                    elif field == "description":
                        embed = await create_embed("global")
                        embed.title = "BH Open Resource Creation"
                        embed.description = "Please send a description"
                        await originalmessage.edit(embed=embed, view=None)
                        msg = await bot.wait_for("message", check=mcheck)
                        resourceinfo["description"] = msg.content
                    elif field == "link":
                        embed = await create_embed("global")
                        embed.title = "BH Open Resource Creation"
                        embed.description = "Please send a link to the resource"
                        await originalmessage.edit(embed=embed, view=None)
                        msg = await bot.wait_for("message", check=mcheck)
                        if msg.content.__len__() > 1024:
                            async def getlink():
                                def mcheck(msg: discord.Message):
                                    return msg.author == ctx.author and msg.channel == originalmessage.channel
                                embed = await create_embed("global")
                                embed.title = "BH Open Resource Creation"
                                embed.description = "Uh oh! Your link exceeds 1024 characters! Please send a version of the resource link shorter than 1024 characters."
                                await originalmessage.edit(embed=embed, view=None)
                                message = await bot.wait_for("message", check=mcheck)
                                if message.content.__len__() > 256:
                                    return await getlink()
                                else:
                                    resourceinfo["link"] = message.content
                                    return
                            await getlink()
                        else:
                            resourceinfo["link"] = msg.content
                return await showresourceinfo()
            return await editresource()
    await showresourceinfo()
    date = datetime.date.today()
    date = date.strftime("%d/%m/%Y")
    try:
        cursor.execute("select * from resources")
        rows = cursor.fetchall()
        resourceid = rows.__len__() + 1
        cursor.execute("insert into resources values (?, ?, ?, ?, ?, ?, ?, ?)", (resourceinfo["type"], resourceid, resourceinfo["name"], resourceinfo["description"], resourceinfo["link"], creator, date, 0))
        embed = await create_embed("global")
        embed.title = "BH Open Resource Creation"
        embed.description = f"Resource successfully created! Name is {resourceinfo['name']} and ID is {resourceid}."
        await originalmessage.edit(embed=embed, view=None)
        embed = await create_embed("global")
        embed.title = f"New {resourceinfo['type']} Resource"
        embed.description = f"`b.dev resource {resourceid}` in <#{botcmdsid}> to see details!"
        newcases = await bot.fetch_channel(resourceannouncementid)
        try:
            msg: discord.Message = await newcases.send(embed=embed, view=None) # type: ignore
            try:
                await msg.publish()
            except:
                logger.debug("Unable to publish new resource message")
            return
        except:
            embed = await create_embed("global")
            embed.title = "BH Open Resource Creation"
            embed.description = "Unable to announce resource creation"
            await ctx.reply(embed=embed)
            return
    except Error as e:
        logger.debug("Error when adding resource, traceback in logs.txt")
        traceback.print_exc(file=open("logs.txt", "a"))
        embed = await create_embed("global")
        embed.title = "BH Open Resource Creation"
        embed.description = "Error while adding resource: " + str(e)
        await originalmessage.edit(embed=embed, view=None)
        return

@commands.cooldown(1, 40, commands.BucketType.user)
@dev.command(aliases=["edit"])
async def editresource(ctx: commands.Context, id: str):
    cursor = connection.cursor()
    rows = None
    async with ctx.typing():
        isdev, reason = await is_developer(ctx)
        if isdev == False:
            if reason == "role":
                embed = await create_embed("global")
                embed.title = "BH Open Resource Editing"
                embed.description = f"Please request the <@&{devid}> role to edit an open resource!"
                await ctx.reply(embed=embed, delete_after=30)
                if isinstance(ctx.command, commands.Command):
                    ctx.command.reset_cooldown(ctx)
                return
            else:
                embed = await create_embed("global")
                embed.title = "BH Open Resource Editing"
                embed.description = f"Please join Blade Hub and request the Developer role to edit an open resource!\nhttps://discord.gg/EpNJmEK6KY"
                await ctx.reply(embed=embed, delete_after=30)
                if isinstance(ctx.command, commands.Command):
                    ctx.command.reset_cooldown(ctx)
                return
        cursor.execute("select * from users where did=?", (ctx.author.id,))
        rows = cursor.fetchall()
    if rows.__len__() < 1:
        embed = await create_embed("global")
        embed.title = "BH Open Resource Editing"
        embed.description = "Please verify to edit a resource! You can verify by using `b.ro verify`"
        await ctx.reply(embed=embed, delete_after=30)
        return
    if id.isnumeric() == False:
        embed = await create_embed("global")
        embed.title = "BH Open Resource Editing"
        embed.description = "Please provide a number ID."
        await ctx.reply(embed=embed, delete_after=30)
        return
    cursor.execute("select * from resources where id=?", (id))
    rows = cursor.fetchall()
    if rows.__len__() >= 1:
        if rows[0][5] == f"<@{ctx.author.id}>" == False:
            embed = await create_embed("global")
            embed.title = "BH Open Resource Editing"
            embed.description = "You do not own this resource."
            await ctx.reply(embed=embed, delete_after=30)
            return
        originalmessage = None
        if isinstance(ctx.channel, discord.TextChannel) or isinstance(ctx.channel, discord.Thread):
            try:
                originalmessage = await ctx.author.send(embed=discord.Embed(title="Loading"))
            except discord.Forbidden as e:
                embed = embed = await create_embed("global")
                embed.title = "BH Open Resource Editing"
                embed.description = "I was unable to DM you, please make sure your DMs are open for me!"
                embed.set_image(url="https://i.gyazo.com/4a34ad7a3b7daa1da12010c11ee840b5.gif")
                await ctx.reply(embed=embed, delete_after=30)
                return
        else:
            originalmessage = await ctx.send(embed=discord.Embed(title="Loading"))
        resourceinfo = {"type": rows[0][0], "name": rows[0][2], "description": rows[0][3], "link": rows[0][4]}
        async def showresourceinfo(skipreview=False):
            if skipreview == False:
                mainview = view()
                embed = await create_embed("global")
                embed.title = "BH Open Resource Editing"
                embed.description = "Please review the resource information inputted to make sure it is correct:"
                embed.add_field(name="Type", value=resourceinfo["type"], inline=False)
                embed.add_field(name="Name", value=resourceinfo["name"], inline=False)
                embed.add_field(name="Description", value=resourceinfo["description"], inline=False)
                embed.add_field(name="Link", value=resourceinfo["link"], inline=False)
                confirm = confirmbutton()
                edit = editbutton()
                mainview.add_item(confirm)
                mainview.add_item(edit)
                await originalmessage.edit(embed=embed, view=mainview)
                await mainview.wait()
                if edit.pressed == True:
                    async def editresource():
                        def mcheck(msg: discord.Message):
                            return msg.author == ctx.author and msg.channel == originalmessage.channel
                        mainview = view()
                        embed = await create_embed("global")
                        embed.title = "BH Open Resource Creation"
                        embed.description = "Please select the fields you would like to edit"
                        menu = resourceeditselect(resourceinfo)
                        mainview.add_item(menu)
                        await originalmessage.edit(embed=embed, view=mainview)
                        await mainview.wait()
                        for field in menu.values:
                            mainview = view()
                            if field == "type":
                                embed = await create_embed("global")
                                embed.title = "BH Open Resource Creation"
                                embed.description = "Please select the resource type"
                                rtype = resourcetypeselect()
                                mainview.add_item(rtype)
                                await originalmessage.edit(embed=embed, view=mainview)
                                await mainview.wait()
                                resourceinfo["type"] = rtype.values[0]
                            elif field == "name":
                                embed = await create_embed("global")
                                embed.title = "BH Open Resource Creation"
                                embed.description = "Please send a name"
                                await originalmessage.edit(embed=embed, view=None)
                                message = await bot.wait_for("message", check=mcheck)
                                if message.content.__len__() > 256:
                                    async def getname():
                                        
                                        embed = await create_embed("global")
                                        embed.title = "BH Open Resource Creation"
                                        embed.description = "Uh oh! Your name exceeds 256 characters! Please send a version of the resource name shorter than 256 characters."
                                        await originalmessage.edit(embed=embed, view=None)
                                        message = await bot.wait_for("message", check=mcheck)
                                        if message.content.__len__() > 256:
                                            return await getname()
                                        else:
                                            resourceinfo["name"] = message.content
                                            return
                                    await getname()
                                else:
                                    resourceinfo["name"] = message.content
                            elif field == "description":
                                embed = await create_embed("global")
                                embed.title = "BH Open Resource Creation"
                                embed.description = "Please send a description"
                                await originalmessage.edit(embed=embed, view=None)
                                msg = await bot.wait_for("message", check=mcheck)
                                resourceinfo["description"] = msg.content
                            elif field == "link":
                                embed = await create_embed("global")
                                embed.title = "BH Open Resource Creation"
                                embed.description = "Please send a link to the resource"
                                await originalmessage.edit(embed=embed, view=None)
                                msg = await bot.wait_for("message", check=mcheck)
                                if msg.content.__len__() > 1024:
                                    async def getlink():
                                        def mcheck(msg: discord.Message):
                                            return msg.author == ctx.author and msg.channel == originalmessage.channel
                                        embed = await create_embed("global")
                                        embed.title = "BH Open Resource Creation"
                                        embed.description = "Uh oh! Your link exceeds 1024 characters! Please send a version of the resource link shorter than 1024 characters."
                                        await originalmessage.edit(embed=embed, view=None)
                                        message = await bot.wait_for("message", check=mcheck)
                                        if message.content.__len__() > 256:
                                            return await getlink()
                                        else:
                                            resourceinfo["link"] = message.content
                                            return
                                    await getlink()
                                else:
                                    resourceinfo["link"] = msg.content
                        return await showresourceinfo()
                    return await editresource()
                elif confirm.pressed == True:
                    async with ctx.typing():
                        cursor.execute("update resources set type = ?, name = ?, description = ?, link = ? where id=?", (resourceinfo["type"], resourceinfo["name"], resourceinfo["description"], resourceinfo["link"], id))
                        embed = await create_embed("global")
                        embed.title = "BH Open Resource Editing"
                        embed.description = "Resource successfully edited."
                        await originalmessage.edit(embed=embed, view=None)
                        return
            else:
                async def editresource():
                    def mcheck(msg: discord.Message):
                        return msg.author == ctx.author and msg.channel == originalmessage.channel
                    mainview = view()
                    embed = await create_embed("global")
                    embed.title = "BH Open Resource Creation"
                    embed.description = "Please select the fields you would like to edit"
                    menu = resourceeditselect(resourceinfo)
                    mainview.add_item(menu)
                    await originalmessage.edit(embed=embed, view=mainview)
                    await mainview.wait()
                    for field in menu.values:
                        mainview = view()
                        if field == "type":
                            embed = await create_embed("global")
                            embed.title = "BH Open Resource Creation"
                            embed.description = "Please select the resource type"
                            rtype = resourcetypeselect()
                            mainview.add_item(rtype)
                            await originalmessage.edit(embed=embed, view=mainview)
                            await mainview.wait()
                            resourceinfo["type"] = rtype.values[0]
                        elif field == "name":
                            embed = await create_embed("global")
                            embed.title = "BH Open Resource Creation"
                            embed.description = "Please send a name"
                            await originalmessage.edit(embed=embed, view=None)
                            message = await bot.wait_for("message", check=mcheck)
                            if message.content.__len__() > 256:
                                async def getname():
                                    def mcheck(msg: discord.Message):
                                        return msg.author == ctx.author and msg.channel == originalmessage.channel
                                    embed = await create_embed("global")
                                    embed.title = "BH Open Resource Creation"
                                    embed.description = "Uh oh! Your name exceeds 256 characters! Please send a version of the resource name shorter than 256 characters."
                                    await originalmessage.edit(embed=embed, view=None)
                                    message = await bot.wait_for("message", check=mcheck)
                                    if message.content.__len__() > 256:
                                        return await getname()
                                    else:
                                        resourceinfo["name"] = message.content
                                        return
                                await getname()
                            else:
                                resourceinfo["name"] = message.content
                        elif field == "description":
                            embed = await create_embed("global")
                            embed.title = "BH Open Resource Creation"
                            embed.description = "Please send a description"
                            await originalmessage.edit(embed=embed, view=None)
                            msg = await bot.wait_for("message", check=mcheck)
                            resourceinfo["description"] = msg.content
                        elif field == "link":
                            embed = await create_embed("global")
                            embed.title = "BH Open Resource Creation"
                            embed.description = "Please send a link to the resource"
                            await originalmessage.edit(embed=embed, view=None)
                            msg = await bot.wait_for("message", check=mcheck)
                            if msg.content.__len__() > 1024:
                                async def getlink():
                                    def mcheck(msg: discord.Message):
                                        return msg.author == ctx.author and msg.channel == originalmessage.channel
                                    embed = await create_embed("global")
                                    embed.title = "BH Open Resource Creation"
                                    embed.description = "Uh oh! Your link exceeds 1024 characters! Please send a version of the resource link shorter than 1024 characters."
                                    await originalmessage.edit(embed=embed, view=None)
                                    message = await bot.wait_for("message", check=mcheck)
                                    if message.content.__len__() > 256:
                                        return await getlink()
                                    else:
                                        resourceinfo["link"] = message.content
                                        return
                                await getlink()
                            else:
                                resourceinfo["link"] = msg.content
                    return await showresourceinfo()
                return await editresource()
        await showresourceinfo(skipreview=True)
    else:
        embed = await create_embed("global")
        embed.title = "BH Open Resource Editing"
        embed.description = "No resource was found with that ID."
        await ctx.reply(embed=embed, delete_after=30)
        return

@commands.cooldown(1, 40, commands.BucketType.user)
@dev.command(aliases=["delete", "remove", "removeresource"])
async def deleteresource(ctx: commands.Context, id: str):
    cursor = connection.cursor()
    rows = None
    async with ctx.typing():
        isdev, reason = await is_developer(ctx)
        if isdev == False:
            if reason == "role":
                embed = await create_embed("global")
                embed.title = "BH Open Resource Deletion"
                embed.description = f"Please request the <@&{devid}> role to delete an open resource!"
                await ctx.reply(embed=embed, delete_after=30)
                if isinstance(ctx.command, commands.Command):
                    ctx.command.reset_cooldown(ctx)
                return
            else:
                embed = await create_embed("global")
                embed.title = "BH Open Resource Deletion"
                embed.description = f"Please join Blade Hub and request the Developer role to delete an open resource!\nhttps://discord.gg/EpNJmEK6KY"
                await ctx.reply(embed=embed, delete_after=30)
                if isinstance(ctx.command, commands.Command):
                    ctx.command.reset_cooldown(ctx)
                return
        cursor.execute("select * from users where did=?", (ctx.author.id,))
        rows = cursor.fetchall()
    if rows.__len__() < 1:
        embed = await create_embed("global")
        embed.title = "BH Open Resource Deletion"
        embed.description = "Please verify to delete an open resource! You can verify by using `b.ro verify`"
        await ctx.reply(embed=embed, delete_after=30)
        return
    if id.isnumeric() == False:
        embed = await create_embed("global")
        embed.title = "BH Open Resource Deletion"
        embed.description = "Please provide a number ID."
        await ctx.reply(embed=embed, delete_after=30)
        return
    cursor.execute("select * from resources where id=?", (id))
    rows = cursor.fetchall()
    if rows.__len__() >= 1:
        if rows[0][5] == f"<@{ctx.author.id}>" == False:
            embed = await create_embed("global")
            embed.title = "BH Open Resource Deletion"
            embed.description = "You do not own this resource."
            await ctx.reply(embed=embed, delete_after=30)
            return
        cursor.execute("update resources set type = 'N/A', name = 'N/A', description = 'N/A', link = 'N/A', creator = 'N/A', creationdate = 'N/A', vouches = 0 where id=?", (id,))
        embed = await create_embed("global")
        embed.title = "BH Open Resource Deletion"
        embed.description = "Resource successfully deleted!"
        await ctx.reply(embed=embed, delete_after=30)
        return

@commands.cooldown(1, 60, commands.BucketType.user)
@dev.command(aliases=["getresources", "listresources"])
async def resources(ctx: commands.Context, rtype: str=None):
    cursor = connection.cursor()
    async def filter(mainview: discord.ui.View, selectedfilter: resourcesearchfilterselect, selectedpage: resourcesearchpageselect, closetask: asyncio.Task, currentpage: int, currentfilter: str, cpages: list, retype: str=None):
        await mainview.wait()
        if selectedfilter.pressed == True:
            if selectedfilter.values[0] == "vouchesasc" and currentfilter != "vouchesasc":
                currentfilter = "vouches"
                closetask.cancel()
                embed = await create_embed("global")
                embed.title = "BH Open Resource Search"
                embed.description = f"Requested by: <@{str(ctx.author.id)}>\nPage: {str(currentpage+1)}\nSorted by: Vouches Ascending"
                if retype == None:
                    pages = constructpages("vouches")
                else:
                    pages = constructpages("vouches", retype)
                for resource in pages[currentpage]:
                    embed.add_field(name=f"{resource[0]} ({resource[3]})", value=f"Resource ID: {resource[1]}\nResource Type: {resource[2]}", inline=True)
                mainview = view()
                selectedfilter = resourcesearchfilterselect()
                selectedpage = resourcesearchpageselect(pages, currentpage+1)
                mainview.add_item(selectedpage)
                mainview.add_item(selectedfilter)
                mainview.add_item(closebutton())
                await originalmessage.edit(embed=embed, view=mainview)
                closetask = asyncio.create_task(originalmessage.delete(delay=100))
                return await filter(mainview, selectedfilter, selectedpage, closetask, currentpage, currentfilter, pages)
            if selectedfilter.values[0] == "vouchesdesc" and currentfilter != "vouchesdesc":
                currentfilter = "vouches DESC"
                closetask.cancel()
                embed = await create_embed("global")
                embed.title = "BH Open Resource Search"
                embed.description = f"Requested by: <@{str(ctx.author.id)}>\nPage: {str(currentpage+1)}\nSorted by: Vouches Descending"
                if retype == None:
                    pages = constructpages("vouches DESC")
                else:
                    pages = constructpages("vouches DESC", retype)
                for resource in pages[currentpage]:
                    embed.add_field(name=f"{resource[0]} ({resource[3]})", value=f"Resource ID: {resource[1]}\nResource Type: {resource[2]}", inline=True)
                mainview = view()
                selectedfilter = resourcesearchfilterselect()
                selectedpage = resourcesearchpageselect(pages, currentpage+1)
                mainview.add_item(selectedpage)
                mainview.add_item(selectedfilter)
                mainview.add_item(closebutton())
                await originalmessage.edit(embed=embed, view=mainview)
                closetask = asyncio.create_task(originalmessage.delete(delay=100))
                return await filter(mainview, selectedfilter, selectedpage, closetask, currentpage, currentfilter, pages)
            elif selectedfilter.values[0] == "alphasc" and currentfilter != "alphasc":
                currentfilter = "name"
                closetask.cancel()
                embed = await create_embed("global")
                embed.title = "BH Open Resource Search"
                embed.description = f"Requested by: <@{str(ctx.author.id)}>\nPage: {str(currentpage+1)}\nSorted by: Alphabetical Ascending"
                if retype == None:
                    pages = constructpages("name")
                else:
                    pages = constructpages("name", retype)
                for resource in pages[currentpage]:
                    embed.add_field(name=f"{resource[0]} ({resource[3]})", value=f"Resource ID: {resource[1]}\nResource Type: {resource[2]}", inline=True)
                mainview = view()
                selectedfilter = resourcesearchfilterselect()
                selectedpage = resourcesearchpageselect(pages, currentpage+1)
                mainview.add_item(selectedpage)
                mainview.add_item(selectedfilter)
                mainview.add_item(closebutton())
                await originalmessage.edit(embed=embed, view=mainview)
                closetask = asyncio.create_task(originalmessage.delete(delay=100))
                return await filter(mainview, selectedfilter, selectedpage, closetask, currentpage, currentfilter, pages)
            elif selectedfilter.values[0] == "alphdesc" and currentfilter != "alphdesc":
                currentfilter = "name DESC"
                closetask.cancel()
                embed = await create_embed("global")
                embed.title = "BH Open Resource Search"
                embed.description = f"Requested by: <@{str(ctx.author.id)}>\nPage: {str(currentpage+1)}\nSorted by: Alphabetical Descending"
                if retype == None:
                    pages = constructpages("name DESC")
                else:
                    pages = constructpages("name DESC", retype)
                for resource in pages[currentpage]:
                    embed.add_field(name=f"{resource[0]} ({resource[3]})", value=f"Resource ID: {resource[1]}\nResource Type: {resource[2]}", inline=True)
                mainview = view()
                selectedfilter = resourcesearchfilterselect()
                selectedpage = resourcesearchpageselect(pages, currentpage+1)
                mainview.add_item(selectedpage)
                mainview.add_item(selectedfilter)
                mainview.add_item(closebutton())
                await originalmessage.edit(embed=embed, view=mainview)
                closetask = asyncio.create_task(originalmessage.delete(delay=100))
                return await filter(mainview, selectedfilter, selectedpage, closetask, currentpage, currentfilter, pages)
            else:
                mainview = view()
                selectedfilter = resourcesearchfilterselect()
                if retype == None:
                    pages = constructpages(currentfilter)
                else:
                    pages = constructpages(currentfilter, retype)
                selectedpage = resourcesearchpageselect(pages, currentpage+1)
                mainview.add_item(selectedpage)
                mainview.add_item(selectedfilter)
                mainview.add_item(closebutton())
                await originalmessage.edit(embed=originalmessage.embeds[0], view=mainview)
                return await filter(mainview, selectedfilter, selectedpage, closetask, currentpage, currentfilter, pages)
        elif selectedpage.pressed == True:
            currentpage = int(selectedpage.values[0])
            embed = await create_embed("global")
            embed.title = "BH Open Resource Search"
            cfilter = "Vouches High-Low"
            if currentfilter == "vouches DESC":
                cfilter = "Vouches Low-High"
            elif currentfilter == "name":
                cfilter = "Alphabetical A-Z"
            elif currentfilter == "name DESC":
                cfilter = "Alphabetical Z-A"
            embed.description = f"Requested by: <@{str(ctx.author.id)}>\nPage: {str(currentpage+1)}\nSorted by: {cfilter}"
            for resource in cpages[currentpage]:
                embed.add_field(name=f"{resource[0]} ({resource[3]})", value=f"Resource ID: {resource[1]}\nResource Type: {resource[2]}", inline=True)
            mainview = view()
            selectedfilter = resourcesearchfilterselect()
            selectedpage = resourcesearchpageselect(cpages, currentpage+1)
            mainview.add_item(selectedpage)
            mainview.add_item(selectedfilter)
            mainview.add_item(closebutton())
            await originalmessage.edit(embed=embed, view=mainview)
            return await filter(mainview, selectedfilter, selectedpage, closetask, currentpage, currentfilter, cpages)
        else:
            try:
                await originalmessage.delete()
                return
            except:
                return
    def constructpages(method: str, retype: str=""):
        cursor.execute(f"select * from resources {retype} order by {method}")
        rows = cursor.fetchall()
        pages = [[]]
        for row in rows:
            appended = False
            for page in pages:
                if page.__len__() < 25:
                    page.append([row[2], row[1], row[0], row[7]])
                    appended = True
                    break
            if appended == False:
                pages.append([[row[2], row[1], row[0], row[7]]])
        return pages
    if rtype == None:
        async with ctx.typing():
            currentpage = 0
            embed = await create_embed("global")
            embed.title = "BH Open Resource Search"
            embed.description = f"Requested by: <@{str(ctx.author.id)}>\nPage: {str(currentpage+1)}\nSorted by: Vouches Descending"
            currentfilter = "vouches"
            pages = constructpages("vouches DESC")
            for resource in pages[0]:
                embed.add_field(name=f"{resource[0]} ({resource[3]})", value=f"Resource ID: {resource[1]}\nResource Type: {resource[2]}", inline=True)
            mainview = view()
            selectedfilter = resourcesearchfilterselect()
            selectedpage = resourcesearchpageselect(pages, currentpage+1)
            if pages.__len__() > 1:
                mainview.add_item(selectedpage)
            mainview.add_item(selectedfilter)
            mainview.add_item(closebutton())
            originalmessage = await ctx.reply(embed=embed, view=mainview)
        closetask = asyncio.create_task(originalmessage.delete(delay=100))
        await filter(mainview, selectedfilter, selectedpage, closetask, currentpage, currentfilter, pages)
    match rtype:
        case "sword":
            async with ctx.typing():
                currentpage = 0
                embed = await create_embed("global")
                embed.title = "BH Open Resource Search"
                embed.description = f"Requested by: <@{str(ctx.author.id)}>\nPage: {str(currentpage+1)}\nSorted by: Vouches Descending"
                currentfilter = "vouches"
                pages = constructpages("vouches DESC", "where type = 'Sword'")
                for resource in pages[0]:
                    embed.add_field(name=f"{resource[0]} ({resource[3]})", value=f"Resource ID: {resource[1]}\nResource Type: {resource[2]}", inline=True)
                mainview = view()
                selectedfilter = resourcesearchfilterselect()
                selectedpage = resourcesearchpageselect(pages, currentpage+1)
                if pages.__len__() > 1:
                    mainview.add_item(selectedpage)
                mainview.add_item(selectedfilter)
                mainview.add_item(closebutton())
                originalmessage = await ctx.reply(embed=embed, view=mainview)
            closetask = asyncio.create_task(originalmessage.delete(delay=100))
            await filter(mainview, selectedfilter, selectedpage, closetask, currentpage, currentfilter, pages, "where type = 'Sword'")
        case "objective":
            async with ctx.typing():
                currentpage = 0
                embed = await create_embed("global")
                embed.title = "BH Open Resource Search"
                embed.description = f"Requested by: <@{str(ctx.author.id)}>\nPage: {str(currentpage+1)}\nSorted by: Vouches Descending"
                currentfilter = "vouches"
                pages = constructpages("vouches DESC", "where type = 'Objective'")
                for resource in pages[0]:
                    embed.add_field(name=f"{resource[0]} ({resource[3]})", value=f"Resource ID: {resource[1]}\nResource Type: {resource[2]}", inline=True)
                mainview = view()
                selectedfilter = resourcesearchfilterselect()
                selectedpage = resourcesearchpageselect(pages, currentpage+1)
                if pages.__len__() > 1:
                    mainview.add_item(selectedpage)
                mainview.add_item(selectedfilter)
                mainview.add_item(closebutton())
                originalmessage = await ctx.reply(embed=embed, view=mainview)
            closetask = asyncio.create_task(originalmessage.delete(delay=100))
            await filter(mainview, selectedfilter, selectedpage, closetask, currentpage, currentfilter, pages, "where type = 'Objective'")
        case "utility":
            async with ctx.typing():
                currentpage = 0
                embed = await create_embed("global")
                embed.title = "BH Open Resource Search"
                embed.description = f"Requested by: <@{str(ctx.author.id)}>\nPage: {str(currentpage+1)}\nSorted by: Vouches Descending"
                currentfilter = "vouches"
                pages = constructpages("vouches DESC", "where type = 'Utility'")
                for resource in pages[0]:
                    embed.add_field(name=f"{resource[0]} ({resource[3]})", value=f"Resource ID: {resource[1]}\nResource Type: {resource[2]}", inline=True)
                mainview = view()
                selectedfilter = resourcesearchfilterselect()
                selectedpage = resourcesearchpageselect(pages, currentpage+1)
                if pages.__len__() > 1:
                    mainview.add_item(selectedpage)
                mainview.add_item(selectedfilter)
                mainview.add_item(closebutton())
                originalmessage = await ctx.reply(embed=embed, view=mainview)
            closetask = asyncio.create_task(originalmessage.delete(delay=100))
            await filter(mainview, selectedfilter, selectedpage, closetask, currentpage, currentfilter, pages, "where type = 'Utility'")
        case "guide":
            async with ctx.typing():
                currentpage = 0
                embed = await create_embed("global")
                embed.title = "BH Open Resource Search"
                embed.description = f"Requested by: <@{str(ctx.author.id)}>\nPage: {str(currentpage+1)}\nSorted by: Vouches Descending"
                currentfilter = "vouches"
                pages = constructpages("vouches DESC", "where type = 'Guide'")
                for resource in pages[0]:
                    embed.add_field(name=f"{resource[0]} ({resource[3]})", value=f"Resource ID: {resource[1]}\nResource Type: {resource[2]}", inline=True)
                mainview = view()
                selectedfilter = resourcesearchfilterselect()
                selectedpage = resourcesearchpageselect(pages, currentpage+1)
                if pages.__len__() > 1:
                    mainview.add_item(selectedpage)
                mainview.add_item(selectedfilter)
                mainview.add_item(closebutton())
                originalmessage = await ctx.reply(embed=embed, view=mainview)
            closetask = asyncio.create_task(originalmessage.delete(delay=100))
            await filter(mainview, selectedfilter, selectedpage, closetask, currentpage, currentfilter, pages, "where type = 'Guide'")
        case "building":
            async with ctx.typing():
                currentpage = 0
                embed = await create_embed("global")
                embed.title = "BH Open Resource Search"
                embed.description = f"Requested by: <@{str(ctx.author.id)}>\nPage: {str(currentpage+1)}\nSorted by: Vouches Descending"
                currentfilter = "vouches"
                pages = constructpages("vouches DESC", "where type = 'Building'")
                for resource in pages[0]:
                    embed.add_field(name=f"{resource[0]} ({resource[3]})", value=f"Resource ID: {resource[1]}\nResource Type: {resource[2]}", inline=True)
                mainview = view()
                selectedfilter = resourcesearchfilterselect()
                selectedpage = resourcesearchpageselect(pages, currentpage+1)
                if pages.__len__() > 1:
                    mainview.add_item(selectedpage)
                mainview.add_item(selectedfilter)
                mainview.add_item(closebutton())
                originalmessage = await ctx.reply(embed=embed, view=mainview)
            closetask = asyncio.create_task(originalmessage.delete(delay=100))
            await filter(mainview, selectedfilter, selectedpage, closetask, currentpage, currentfilter, pages, "where type = 'Building'")
        case "anti":
            async with ctx.typing():
                currentpage = 0
                embed = await create_embed("global")
                embed.title = "BH Open Resource Search"
                embed.description = f"Requested by: <@{str(ctx.author.id)}>\nPage: {str(currentpage+1)}\nSorted by: Vouches Descending"
                currentfilter = "vouches"
                pages = constructpages("vouches DESC", "where type = 'Anti Exploit'")
                for resource in pages[0]:
                    embed.add_field(name=f"{resource[0]} ({resource[3]})", value=f"Resource ID: {resource[1]}\nResource Type: {resource[2]}", inline=True)
                mainview = view()
                selectedfilter = resourcesearchfilterselect()
                selectedpage = resourcesearchpageselect(pages, currentpage+1)
                if pages.__len__() > 1:
                    mainview.add_item(selectedpage)
                mainview.add_item(selectedfilter)
                mainview.add_item(closebutton())
                originalmessage = await ctx.reply(embed=embed, view=mainview)
            closetask = asyncio.create_task(originalmessage.delete(delay=100))
            await filter(mainview, selectedfilter, selectedpage, closetask, currentpage, currentfilter, pages, "where type = 'Anti Exploit'")
        case "gfx":
            async with ctx.typing():
                currentpage = 0
                embed = await create_embed("global")
                embed.title = "BH Open Resource Search"
                embed.description = f"Requested by: <@{str(ctx.author.id)}>\nPage: {str(currentpage+1)}\nSorted by: Vouches Descending"
                currentfilter = "vouches"
                pages = constructpages("vouches DESC", "where type = 'GFX'")
                for resource in pages[0]:
                    embed.add_field(name=f"{resource[0]} ({resource[3]})", value=f"Resource ID: {resource[1]}\nResource Type: {resource[2]}", inline=True)
                mainview = view()
                selectedfilter = resourcesearchfilterselect()
                selectedpage = resourcesearchpageselect(pages, currentpage+1)
                if pages.__len__() > 1:
                    mainview.add_item(selectedpage)
                mainview.add_item(selectedfilter)
                mainview.add_item(closebutton())
                originalmessage = await ctx.reply(embed=embed, view=mainview)
            closetask = asyncio.create_task(originalmessage.delete(delay=100))
            await filter(mainview, selectedfilter, selectedpage, closetask, currentpage, currentfilter, pages, "where type = 'GFX'")
        case "mini":
            async with ctx.typing():
                currentpage = 0
                embed = await create_embed("global")
                embed.title = "BH Open Resource Search"
                embed.description = f"Requested by: <@{str(ctx.author.id)}>\nPage: {str(currentpage+1)}\nSorted by: Vouches Descending"
                currentfilter = "vouches"
                pages = constructpages("vouches DESC", "where type = 'Mini Script'")
                for resource in pages[0]:
                    embed.add_field(name=f"{resource[0]} ({resource[3]})", value=f"Resource ID: {resource[1]}\nResource Type: {resource[2]}", inline=True)
                mainview = view()
                selectedfilter = resourcesearchfilterselect()
                selectedpage = resourcesearchpageselect(pages, currentpage+1)
                if pages.__len__() > 1:
                    mainview.add_item(selectedpage)
                mainview.add_item(selectedfilter)
                mainview.add_item(closebutton())
                originalmessage = await ctx.reply(embed=embed, view=mainview)
            closetask = asyncio.create_task(originalmessage.delete(delay=100))
            await filter(mainview, selectedfilter, selectedpage, closetask, currentpage, currentfilter, pages, "where type = 'Mini Script'")
        case _:
            embed = await create_embed("global")
            embed.title = "BH Open Resource Search"
            embed.description = "Uh oh! That isn't a recognized resource type! Please use one of the following:\n```\nsword - Swords\nobjective - Objective\nutility - Utility\nguide - Guide\nbuilding - Building\nanti - Anti Exploit\ngfx - GFX\nmini - Mini Script\n```"
            await ctx.reply(embed=embed, delete_after=20)
            if isinstance(ctx.command, commands.Command):
                ctx.command.reset_cooldown(ctx)
            return

@commands.cooldown(1, 30, commands.BucketType.user)
@dev.command(aliases=["getresource", "fetchresource"])
async def resource(ctx: commands.Context, arg: str=None):
    if arg == None:
        embed = await create_embed("global")
        embed.title = "BH Open Resource"
        embed.description = "Please include a resource ID or resource name!"
        await ctx.reply(embed=embed, delete_after=20)
        return
    cursor = connection.cursor()
    async with ctx.typing():
        if arg.isnumeric() == True:
            cursor.execute("select * from resources where id=?", (int(arg),))
            rows = cursor.fetchall()
            if rows.__len__() >= 1:
                mainview = view()
                embed = await create_embed("global")
                embed.title = rows[0][2]
                embed.description = rows[0][3]
                embed.add_field(name="Creator", value=rows[0][5], inline=False)
                embed.add_field(name="Link", value=rows[0][4], inline=False)
                close = closebutton()
                btn = resourcelinkbutton()
                btn.url = rows[0][4]
                vouch = resourcevouchbutton(rows[0][1])
                mainview.add_item(close)
                mainview.add_item(btn)
                mainview.add_item(vouch)
                await ctx.reply(embed=embed, view=mainview)
                return
            else:
                embed = await create_embed("global")
                embed.title = "BH Open Resource"
                embed.description = "No resource found."
                await ctx.reply(embed=embed, delete_after=20)
                return
        else:
            cursor.execute("select * from resources where name=?", (arg,))
            rows = cursor.fetchall()
            if rows.__len__() >= 1:
                mainview = view()
                embed = await create_embed("global")
                embed.title = rows[0][2]
                embed.description = rows[0][3]
                embed.add_field(name="Creator", value=rows[0][5], inline=False)
                embed.add_field(name="Link", value=rows[0][4], inline=False)
                close = closebutton()
                btn = resourcelinkbutton()
                btn.url = rows[0][4]
                mainview.add_item(close)
                mainview.add_item(btn)
                await ctx.reply(embed=embed, view=mainview)
                return
            else:
                embed = await create_embed("global")
                embed.title = "BH Open Resource"
                embed.description = "No resource found."
                await ctx.reply(embed=embed, delete_after=20)
                return

@bot.group()
async def ro(ctx: commands.Context):
    if ctx.invoked_subcommand == None:
        embed = await create_embed("roblox")
        embed.title = "Invalid Command Syntax"
        embed.description = "Please pass a valid subcommand! Use `b.help ro` for a list of subcommands."
        await ctx.reply(embed=embed, delete_after=30)

# api abooser >:)
@commands.cooldown(1, 60, commands.BucketType.user)
@ro.command()
async def verify(ctx: commands.Context):
    cursor = connection.cursor()
    async with ctx.typing():
        cursor.execute("select * from users where did=?", (ctx.author.id,))
        rows = cursor.fetchall()
        for row in rows:
            embed = await create_embed("roblox")
            embed.title = "Roblox Verification"
            user = await RoClient.get_user(row[1])
            embed.description = f"You're already verified under [{user.name}](https://roblox.com/users/{row[1]}/profile) ({row[1]})!"
            await ctx.reply(embed=embed, delete_after=30)
            return
        originalmessage = None
        if isinstance(ctx.channel, discord.TextChannel) or isinstance(ctx.channel, discord.Thread):
            embed = discord.Embed(title="Loading")
            try:
                originalmessage = await ctx.author.send(embed=embed)
            except discord.Forbidden as e:
                embed = embed = await create_embed("roblox")
                embed.title = "Roblox Verification"
                embed.description = "I was unable to DM you, please make sure your DMs are open for me!"
                embed.set_image(url="https://i.gyazo.com/4a34ad7a3b7daa1da12010c11ee840b5.gif")
                await ctx.reply(embed=embed, delete_after=30)
                return
            embed = await create_embed("roblox")
            embed.title = "Roblox Verification"
            embed.description = "Please check your DMs so I can get you verified!"
            await ctx.reply(embed=embed, delete_after=30)
        else:
            originalmessage = await ctx.author.send(embed=discord.Embed(title="Loading"))
    async with ctx.author.typing():
        async with aiohttp.ClientSession() as WebClient:
            otherids = {}
            global bloxlinkrequests
            global roverrequests
            if bloxlinkrequests < 60:
                result = await WebClient.get(url=f"https://api.blox.link/v1/user/{ctx.author.id}")
                bloxlinkrequests = sum((bloxlinkrequests, 1))
                json = await result.json()
                if json["status"] == "ok":
                    otherids["bloxlink"] = json["primaryAccount"]
            result = await WebClient.get(url=f"https://api.rbxbolt.com/v1/discord/{ctx.author.id}?key=U6PHJoASF8R6S0BcRP5LGaPayVf9u88ld5B")
            if result.content_type == "application/json":
                json = await result.json()
                if "UserId" in json.keys():
                    otherids["rbxbolt"] = json["UserId"]
            if roverrequests < 60:
                result = await WebClient.get(url=f"https://verify.eryn.io/api/user/{ctx.author.id}")
                roverrequests = sum((roverrequests, 1))
                json = await result.json()
                if "UserId" in json.keys():
                    otherids["rover"] = json["UserId"]
            mainview = view(600)
            bloxlink = bloxlinkbutton()
            rbxbolt = rbxboltbutton()
            rover = roverbutton()
            embed = await create_embed("roblox")
            embed.title = "Roblox Verification"
            if "bloxlink" in otherids or "rbxbolt" in otherids or "rover" in otherids:
                embed.description = "We found you verified on another bot(s)! If you would like to use that verification, please press the button corresponding to that bot! If not, press the \"BH\" button!"
                if "bloxlink" in otherids:
                    try:
                        user = await RoClient.get_user(otherids["bloxlink"])
                        embed.description = embed.description + f"\nBloxlink: [{user.name}](https://roblox.com/users/{user.id}/profile) ({user.id})"
                        mainview.add_item(bloxlink)
                    except:
                        pass
                if "rbxbolt" in otherids:
                    try:
                        user = await RoClient.get_user(otherids["rbxbolt"])
                        embed.description = embed.description + f"\nRBXBolt: [{user.name}](https://roblox.com/users/{user.id}/profile) ({user.id})"
                        mainview.add_item(rbxbolt)
                    except:
                        pass
                if "rover" in otherids:
                    try:
                        user = await RoClient.get_user(otherids["rover"])
                        embed.description = embed.description + f"\nRoVer: [{user.name}](https://roblox.com/users/{user.id}/profile) ({user.id})"
                        mainview.add_item(rover)
                    except:
                        pass
                bhbtn = bhbutton()
                mainview.add_item(bhbtn)
                await originalmessage.edit(embed=embed, view=mainview)
                await mainview.wait()
                if bloxlink.pressed == True:
                    embed = await create_embed("roblox")
                    embed.title = "Roblox Verification"
                    embed.description = "Adding user to database.."
                    await originalmessage.edit(embed=embed, view=None)
                    try:
                        cursor.execute("insert into users values (?, ?)", (ctx.author.id, int(otherids["bloxlink"])))
                        user = await RoClient.get_user(otherids["bloxlink"])
                        embed = await create_embed("roblox")
                        embed.title = "Roblox Verification"
                        embed.description = f"You've been successfully verified in the Blade Hub as [{user.name}](https://roblox.com/users/{str(user.id)}/profile)!"
                        await originalmessage.edit(embed=embed)
                        server = await bot.fetch_guild(mainid)
                        jd = await bot.fetch_guild(jdid)
                        verified = server.get_role(verifiedid)
                        jdverified = jd.get_role(jdverifiedid)
                        if isinstance(verified, discord.Role):
                            try:
                                member = await server.fetch_member(ctx.author.id)
                                roles = member.roles
                                roles.append(verified)
                                await member.edit(roles=roles)
                            except discord.Forbidden:
                                pass
                            except discord.NotFound:
                                pass
                        if isinstance(jdverified, discord.Role):
                            try:
                                member = await jd.fetch_member(ctx.author.id)
                                roles = member.roles
                                roles.append(jdverified)
                                await member.edit(roles=roles)
                            except discord.Forbidden:
                                pass
                            except discord.NotFound:
                                pass
                        return
                    except Error as e:
                        logger.debug("Error when adding user to database, traceback in logs.txt")
                        traceback.print_exc(file=open("logs.txt", "a"))
                        embed = await create_embed("roblox")
                        embed.title = "Roblox Verification"
                        embed.description = "Error while adding user to database: " + str(e)
                        return await originalmessage.edit(embed=embed, view=None)
                elif rbxbolt.pressed == True:
                    embed = await create_embed("roblox")
                    embed.title = "Roblox Verification"
                    embed.description = "Adding user to database.."
                    await originalmessage.edit(embed=embed, view=None)
                    try:
                        cursor.execute("insert into users values (?, ?)", (ctx.author.id, int(otherids["rbxbolt"])))
                        user = await RoClient.get_user(otherids["rbxbolt"])
                        embed = await create_embed("roblox")
                        embed.title = "Roblox Verification"
                        embed.description = f"You've been successfully verified in the Blade Hub as [{user.name}](https://roblox.com/users/{str(user.id)}/profile)!"
                        await originalmessage.edit(embed=embed)
                        server = await bot.fetch_guild(mainid)
                        jd = await bot.fetch_guild(jdid)
                        verified = server.get_role(verifiedid)
                        jdverified = jd.get_role(jdverifiedid)
                        if isinstance(verified, discord.Role):
                            try:
                                member = await server.fetch_member(ctx.author.id)
                                roles = member.roles
                                roles.append(verified)
                                await member.edit(roles=roles)
                            except discord.Forbidden:
                                pass
                            except discord.NotFound:
                                pass
                        if isinstance(jdverified, discord.Role):
                            try:
                                member = await jd.fetch_member(ctx.author.id)
                                roles = member.roles
                                roles.append(jdverified)
                                await member.edit(roles=roles)
                            except discord.Forbidden:
                                pass
                            except discord.NotFound:
                                pass
                        return
                    except Error as e:
                        logger.debug("Error when adding user to database, traceback in logs.txt")
                        traceback.print_exc(file=open("logs.txt", "a"))
                        embed = await create_embed("roblox")
                        embed.title = "Roblox Verification"
                        embed.description = "Error while adding user to database: " + str(e)
                        await originalmessage.edit(embed=embed, view=None)
                        return
                elif rover.pressed == True:
                    embed = await create_embed("roblox")
                    embed.title = "Roblox Verification"
                    embed.description = "Adding user to database.."
                    await originalmessage.edit(embed=embed, view=None)
                    try:
                        cursor.execute("insert into users values (?, ?)", (ctx.author.id, int(otherids["rover"])))
                        user = await RoClient.get_user(otherids["rover"])
                        embed = await create_embed("roblox")
                        embed.title = "Roblox Verification"
                        embed.description = f"You've been successfully verified in the Blade Hub as [{user.name}](https://roblox.com/users/{str(user.id)}/profile)!"
                        await originalmessage.edit(embed=embed)
                        server = await bot.fetch_guild(mainid)
                        jd = await bot.fetch_guild(jdid)
                        verified = server.get_role(verifiedid)
                        jdverified = jd.get_role(jdverifiedid)
                        if isinstance(verified, discord.Role):
                            try:
                                member = await server.fetch_member(ctx.author.id)
                                roles = member.roles
                                roles.append(verified)
                                await member.edit(roles=roles)
                            except discord.Forbidden:
                                pass
                            except discord.NotFound:
                                pass
                        if isinstance(jdverified, discord.Role):
                            try:
                                member = await jd.fetch_member(ctx.author.id)
                                roles = member.roles
                                roles.append(jdverified)
                                await member.edit(roles=roles)
                            except discord.Forbidden:
                                pass
                            except discord.NotFound:
                                pass
                        return
                    except Error as e:
                        logger.debug("Error when adding user to database, traceback in logs.txt")
                        traceback.print_exc(file=open("logs.txt", "a"))
                        embed = await create_embed("roblox")
                        embed.title = "Roblox Verification"
                        embed.description = "Error while adding user to database: " + str(e)
                        await originalmessage.edit(embed=embed, view=None)
                        return
                elif bhbtn.pressed == True:
                    us = None
                    async def getuser(failed=False):
                        if failed == False:
                            embed = await create_embed("roblox")
                            embed.title = "Roblox Verification"
                            embed.description = "Please type the name of the user you would like to link your account to!"
                            def mcheck(msg: discord.Message):
                                return msg.author == ctx.author and msg.channel == originalmessage.channel
                            await originalmessage.edit(embed=embed, view=None)
                            message = await bot.wait_for("message", check=mcheck)
                            try:
                                user = await RoClient.get_user_by_username(message.content, expand=True)
                                us = message.content
                                return user
                            except:
                                return await getuser(failed=True)
                        else:
                            embed = await create_embed("roblox")
                            embed.title = "Roblox Verification"
                            embed.description = "Uh oh! We couldn't find that account! Please type the name of the user you would like to link your account to!"
                            def mcheck(msg: discord.Message):
                                return msg.author == ctx.author and msg.channel == originalmessage.channel
                            await originalmessage.edit(embed=embed, view=None)
                            message = await bot.wait_for("message", check=mcheck)
                            try:
                                user = await RoClient.get_user_by_username(message.content, expand=True)
                                us = message.content
                                return user
                            except:
                                return await getuser(failed=True)
                    user = await getuser()
                    mainview = view(600)
                    code = await create_safetext(random.randint(2, 11))
                    async def doverify(user, failed=False):
                        if failed == False:
                            embed = await create_embed("roblox")
                            embed.title = "Roblox Verification"
                            embed.description = f"Please put the following code into your description, and click \"Verify\" when you've done so:\n`{code}`"
                            verifybtn = verifybutton()
                            mainview.clear_items()
                            mainview.add_item(verifybtn)
                            await originalmessage.edit(embed=embed, view=mainview)
                            await mainview.wait()
                            if verifybtn.pressed == True:
                                user = await RoClient.get_user(user.id)
                                if str(user.description) == str(code):
                                    try:
                                        cursor.execute("insert into users values (?, ?)", (ctx.author.id, user.id))
                                        embed = await create_embed("roblox")
                                        embed.title = "Roblox Verification"
                                        embed.description = f"You've been successfully verified in the Blade Hub as [{user.name}](https://roblox.com/users/{str(user.id)}/profile)!"
                                        await originalmessage.edit(embed=embed, view=None)
                                        server = await bot.fetch_guild(mainid)
                                        jd = await bot.fetch_guild(jdid)
                                        verified = server.get_role(verifiedid)
                                        jdverified = jd.get_role(jdverifiedid)
                                        if isinstance(verified, discord.Role):
                                            try:
                                                member = await server.fetch_member(ctx.author.id)
                                                roles = member.roles
                                                roles.append(verified)
                                                await member.edit(roles=roles)
                                            except discord.Forbidden:
                                                pass
                                            except discord.NotFound:
                                                pass
                                        if isinstance(jdverified, discord.Role):
                                            try:
                                                member = await jd.fetch_member(ctx.author.id)
                                                roles = member.roles
                                                roles.append(jdverified)
                                                await member.edit(roles=roles)
                                            except discord.Forbidden:
                                                pass
                                            except discord.NotFound:
                                                pass
                                        return
                                    except:
                                        logger.debug("Error when adding user to database, traceback in logs.txt")
                                        traceback.print_exc(file=open("logs.txt", "a"))
                                        embed = await create_embed("roblox")
                                        embed.title = "Roblox Verification"
                                        embed.description = "Error while adding user to database: " + str(e)
                                        await originalmessage.edit(embed=embed, view=None)
                                        return
                                else:
                                    return await doverify(user, failed=True)
                            else:
                                embed = await create_embed("roblox")
                                embed.title = "Roblox Verification"
                                embed.description = "This prompt has expired! Please run `b.ro verify` to verify!"
                                await originalmessage.edit(embed=embed, view=None)
                                return
                        else:
                            embed = await create_embed("roblox")
                            embed.title = "Roblox Verification"
                            embed.description = f"Uh oh! We didn't see the code as your description! Please put the following code into your description, and click \"Verify\" when you've done so:\n`{str(code)}`"
                            verifybtn = verifybutton()
                            mainview.clear_items()
                            mainview.add_item(verifybtn)
                            await originalmessage.edit(embed=embed, view=mainview)
                            await mainview.wait()
                            if verifybtn.pressed == True:
                                if isinstance(us, str):
                                    if us.isnumeric():
                                        user = await RoClient.get_user(us)
                                    else:
                                        user = await RoClient.get_user_by_username(us, expand=True)
                                    if user.description == code: # type: ignore
                                        try:
                                            cursor.execute("insert into users values (?, ?)", (ctx.author.id, user.id))
                                            embed = await create_embed("roblox")
                                            embed.title = "Roblox Verification"
                                            embed.description = f"You've been successfully verified in the Blade Hub as [{user.name}](https://roblox.com/users/{str(user.id)}/profile)!"
                                            await originalmessage.edit(embed=embed, view=None)
                                            server = await bot.fetch_guild(mainid)
                                            jd = await bot.fetch_guild(jdid)
                                            verified = server.get_role(verifiedid)
                                            jdverified = jd.get_role(jdverifiedid)
                                            if isinstance(verified, discord.Role):
                                                try:
                                                    member = await server.fetch_member(ctx.author.id)
                                                    roles = member.roles
                                                    roles.append(verified)
                                                    await member.edit(roles=roles)
                                                except discord.Forbidden:
                                                    pass
                                                except discord.NotFound:
                                                    pass
                                            if isinstance(jdverified, discord.Role):
                                                try:
                                                    member = await jd.fetch_member(ctx.author.id)
                                                    roles = member.roles
                                                    roles.append(jdverified)
                                                    await member.edit(roles=roles)
                                                except discord.Forbidden:
                                                    pass
                                                except discord.NotFound:
                                                    pass
                                            return
                                        except:
                                            logger.debug("Error when adding user to database, traceback in logs.txt")
                                            traceback.print_exc(file=open("logs.txt", "a"))
                                            embed = await create_embed("roblox")
                                            embed.title = "Roblox Verification"
                                            embed.description = "Error while adding user to database: " + str(e)
                                            await originalmessage.edit(embed=embed, view=None)
                                            return
                                    else:
                                        return await doverify(user, failed=True)
                                else:
                                    raise
                            else:
                                embed = await create_embed("roblox")
                                embed.title = "Roblox Verification"
                                embed.description = "This prompt has expired! Please run `b.ro verify` to verify!"
                                await originalmessage.edit(embed=embed)
                                return
                    await doverify(user)
                else:
                    embed = await create_embed("roblox")
                    embed.title = "Roblox Verification"
                    embed.description = "This prompt has expired! Please run `b.ro verify` to verify!"
                    await originalmessage.edit(embed=embed, view=None)
                    return
            else:
                us = None
                async def getuser(failed=False):
                    if failed == False:
                        embed = await create_embed("roblox")
                        embed.title = "Roblox Verification"
                        embed.description = "Please type the name of the user you would like to link your account to!"
                        def mcheck(msg: discord.Message):
                            return msg.author == ctx.author and msg.channel == originalmessage.channel
                        await originalmessage.edit(embed=embed, view=None)
                        message = await bot.wait_for("message", check=mcheck)
                        try:
                            user = await RoClient.get_user_by_username(message.content, expand=True)
                            us = message.content
                            return user
                        except:
                            return await getuser(failed=True)
                    else:
                        embed = await create_embed("roblox")
                        embed.title = "Roblox Verification"
                        embed.description = "Uh oh! We couldn't find that account! Please type the name of the user you would like to link your account to!"
                        def mcheck(msg: discord.Message):
                            return msg.author == ctx.author and msg.channel == originalmessage.channel
                        await originalmessage.edit(embed=embed, view=None)
                        message = await bot.wait_for("message", check=mcheck)
                        try:
                            user = await RoClient.get_user_by_username(message.content, expand=True)
                            us = message.content
                            return user
                        except:
                            return await getuser(failed=True)
                user = await getuser()
                mainview = view(600)
                code = await create_safetext(random.randint(2, 11))
                async def doverify(user, failed=False):
                    if failed == False:
                        embed = await create_embed("roblox")
                        embed.title = "Roblox Verification"
                        embed.description = f"Please put the following code into your description, and click \"Verify\" when you've done so:\n`{code}`"
                        verifybtn = verifybutton()
                        mainview.clear_items()
                        mainview.add_item(verifybtn)
                        await originalmessage.edit(embed=embed, view=mainview)
                        await mainview.wait()
                        if verifybtn.pressed == True:
                            if isinstance(us, str):
                                if us.isnumeric():
                                    user = await RoClient.get_user(us)
                                else:
                                    user = await RoClient.get_user_by_username(us, expand=True)
                                if user.description == code: # type: ignore
                                    try:
                                        cursor.execute("insert into users values (?, ?)", (ctx.author.id, user.id))
                                        embed = await create_embed("roblox")
                                        embed.title = "Roblox Verification"
                                        embed.description = f"You've been successfully verified in the Blade Hub as [{user.name}](https://roblox.com/users/{str(user.id)}/profile)!"
                                        await originalmessage.edit(embed=embed, view=None)
                                        server = await bot.fetch_guild(mainid)
                                        jd = await bot.fetch_guild(jdid)
                                        verified = server.get_role(verifiedid)
                                        jdverified = jd.get_role(jdverifiedid)
                                        if isinstance(verified, discord.Role):
                                            try:
                                                member = await server.fetch_member(ctx.author.id)
                                                roles = member.roles
                                                roles.append(verified)
                                                await member.edit(roles=roles)
                                            except discord.Forbidden:
                                                pass
                                            except discord.NotFound:
                                                pass
                                        if isinstance(jdverified, discord.Role):
                                            try:
                                                member = await jd.fetch_member(ctx.author.id)
                                                roles = member.roles
                                                roles.append(jdverified)
                                                await member.edit(roles=roles)
                                            except discord.Forbidden:
                                                pass
                                            except discord.NotFound:
                                                pass
                                        return
                                    except:
                                        logger.debug("Error when adding user to database, traceback in logs.txt")
                                        traceback.print_exc(file=open("logs.txt", "a"))
                                        embed = await create_embed("roblox")
                                        embed.title = "Roblox Verification"
                                        embed.description = "Error while adding user to database: " + str(e)
                                        return await originalmessage.edit(embed=embed, view=None)
                                else:
                                    return await doverify(user, failed=True)
                        else:
                            embed = await create_embed("roblox")
                            embed.title = "Roblox Verification"
                            embed.description = "This prompt has expired! Please run `b.ro verify` to verify!"
                            return await originalmessage.edit(embed=embed, view=None)
                    else:
                        embed = await create_embed("roblox")
                        embed.title = "Roblox Verification"
                        embed.description = f"Uh oh! We didn't see the code as your description! Please put the following code into your description, and click \"Verify\" when you've done so:\n`{str(code)}`"
                        verifybtn = verifybutton()
                        mainview.clear_items()
                        mainview.add_item(verifybtn)
                        await originalmessage.edit(embed=embed, view=mainview)
                        await mainview.wait()
                        if verifybtn.pressed == True:
                            if isinstance(us, str):
                                if us.isnumeric():
                                    user = await RoClient.get_user(us)
                                else:
                                    user = await RoClient.get_user_by_username(us, expand=True)
                                if user.description == code: # type: ignore
                                    try:
                                        cursor.execute("insert into users values (?, ?)", (ctx.author.id, user.id))
                                        embed = await create_embed("roblox")
                                        embed.title = "Roblox Verification"
                                        embed.description = f"You've been successfully verified in the Blade Hub as [{user.name}](https://roblox.com/users/{str(user.id)}/profile)!"
                                        await originalmessage.edit(embed=embed, view=None)
                                        server = await bot.fetch_guild(mainid)
                                        jd = await bot.fetch_guild(jdid)
                                        verified = server.get_role(verifiedid)
                                        jdverified = jd.get_role(jdverifiedid)
                                        if isinstance(verified, discord.Role):
                                            try:
                                                member = await server.fetch_member(ctx.author.id)
                                                roles = member.roles
                                                roles.append(verified)
                                                await member.edit(roles=roles)
                                            except discord.Forbidden:
                                                pass
                                            except discord.NotFound:
                                                pass
                                        if isinstance(jdverified, discord.Role):
                                            try:
                                                member = await jd.fetch_member(ctx.author.id)
                                                roles = member.roles
                                                roles.append(jdverified)
                                                await member.edit(roles=roles)
                                            except discord.Forbidden:
                                                pass
                                            except discord.NotFound:
                                                pass
                                        return
                                    except:
                                        logger.debug("Error when adding user to database, traceback in logs.txt")
                                        traceback.print_exc(file=open("logs.txt", "a"))
                                        embed = await create_embed("roblox")
                                        embed.title = "Roblox Verification"
                                        embed.description = "Error while adding user to database: " + str(e)
                                        return await originalmessage.edit(embed=embed, view=None)
                                else:
                                    return await doverify(user, failed=True)
                        else:
                            embed = await create_embed("roblox")
                            embed.title = "Roblox Verification"
                            embed.description = "This prompt has expired! Please run `b.ro verify` to verify!"
                            return await originalmessage.edit(embed=embed)
                await doverify(user)

@commands.cooldown(3, 30, commands.BucketType.user)
@ro.command(aliases=["uinfo", "getuserinfo", "showuserinfo"])
async def userinfo(ctx: commands.Context, arg: str=None):
    cursor = connection.cursor()
    WebClient = aiohttp.ClientSession()
    if arg == None:
        async with ctx.typing():
            cursor.execute("select * from users where did=?", (ctx.author.id,))
            rows = cursor.fetchall()
            if rows.__len__() > 0:
                try:
                    user = await RoClient.get_user(rows[0][1])
                    embed = await create_embed("roblox")
                    embed.title = "User Info"
                    embed.set_thumbnail(url=f"https://www.roblox.com/bust-thumbnail/image?userId={user.id}&width=420&height=420&format=png")
                    embed.add_field(name="Username", value=user.name, inline=True)
                    if user.display_name != user.name:
                        embed.add_field(name="Display Name", value=user.display_name, inline=True)
                    embed.add_field(name="User ID", value=str(user.id), inline=True)
                    embed.add_field(name="Description", value="```" + disnake.utils.escape_markdown(str(user.description)) + "```", inline=False)
                    embed.add_field(name="Created (dd/mm/yyyy)", value=user.created.strftime("%d/%m/%Y"), inline=False)
                    embed.add_field(name="Verified", value=":white_check_mark:", inline=False)
                    embed.add_field(name="Associated Discord Account", value=f"<@{rows[0][0]}>", inline=False)
                    dfp = await WebClient.get(f"https://devforum.roblox.com/u/{user.name.lower()}.json")
                    devforumprofile = await dfp.json()
                    if "user" in devforumprofile:
                        if "trust_level" in devforumprofile["user"]:
                            trust = None
                            if int(devforumprofile["user"]["trust_level"]) == 0:
                                trust = "Visitor"
                            elif int(devforumprofile["user"]["trust_level"]) == 1:
                                trust = "Member"
                            elif int(devforumprofile["user"]["trust_level"]) == 2:
                                trust = "Regular"
                            elif int(devforumprofile["user"]["trust_level"]) == 3:
                                trust = "Top Contributor"
                            elif int(devforumprofile["user"]["trust_level"]) == 4:
                                trust = "Community Editor"
                            elif int(devforumprofile["user"]["trust_level"]) == 5:
                                trust = "Community Sage"
                            else:
                                trust = "None"
                            embed.add_field(name=f"DevForum", value=f"Trust Level: {trust}\nTitle: {str(devforumprofile['user']['title'])}", inline=False)
                    await ctx.reply(embed=embed, delete_after=60)
                    return
                except:
                    embed = await create_embed("roblox")
                    embed.title = "User Info"
                    embed.description = "Uh oh! I was unable to get your user! Is your account deleted?"
                    await ctx.reply(embed=embed, delete_after=20)
                    return
            embed = await create_embed("roblox")
            embed.title = "User Info"
            embed.description = "Please provide a username, user ID, or use `b.ro verify` to verify!"
            await ctx.reply(embed=embed, delete_after=20)
            if isinstance(ctx.command, commands.Command):
                ctx.command.reset_cooldown(ctx)
            return
    if arg.isnumeric() == False:
        async with ctx.typing():
            try:
                user = await RoClient.get_user_by_username(arg, expand=True)
                embed = await create_embed("roblox")
                embed.title = "User Info"
                embed.set_thumbnail(url=f"https://www.roblox.com/bust-thumbnail/image?userId={user.id}&width=420&height=420&format=png")
                embed.add_field(name="Username", value=user.name, inline=True)
                if user.display_name != user.name:
                    embed.add_field(name="Display Name", value=user.display_name, inline=True)
                embed.add_field(name="User ID", value=str(user.id), inline=True)
                embed.add_field(name="Description", value="```" + disnake.utils.escape_mentions(disnake.utils.escape_markdown(str(user.description))) + "```", inline=False) # type: ignore
                embed.add_field(name="Created (dd/mm/yyyy)", value=user.created.strftime("%d/%m/%Y"), inline=False) # type: ignore
                cursor.execute("select * from users where rid=?", (user.id,))
                rows = cursor.fetchall()
                if rows.__len__() > 0:
                    embed.add_field(name="Verified", value=":white_check_mark:", inline=False)
                    embed.add_field(name="Associated Discord Account", value=f"<@{rows[0][0]}>", inline=False)
                else:
                    embed.add_field(name="Verified", value=":x:", inline=False)
                dfp = await WebClient.get(f"https://devforum.roblox.com/u/{arg}.json")
                devforumprofile = await dfp.json()
                if "user" in devforumprofile:
                    if "trust_level" in devforumprofile["user"]:
                        trust = None
                        if int(devforumprofile["user"]["trust_level"]) == 0:
                            trust = "Visitor"
                        elif int(devforumprofile["user"]["trust_level"]) == 1:
                            trust = "Member"
                        elif int(devforumprofile["user"]["trust_level"]) == 2:
                            trust = "Regular"
                        elif int(devforumprofile["user"]["trust_level"]) == 3:
                            trust = "Top Contributor"
                        elif int(devforumprofile["user"]["trust_level"]) == 4:
                            trust = "Community Editor"
                        elif int(devforumprofile["user"]["trust_level"]) == 5:
                            trust = "Community Sage"
                        else:
                            trust = "None"
                        embed.add_field(name=f"DevForum", value=f"Trust Level: {trust}\nTitle: {str(devforumprofile['user']['title'])}", inline=False)
                await ctx.reply(embed=embed, delete_after=60)
                return
            except:
                embed = await create_embed("roblox")
                embed.title = "User Info"
                embed.description = "User not found"
                await ctx.reply(embed=embed, delete_after=20)
                return
    elif arg.isnumeric() == True:
        async with ctx.typing():
            try:
                user = await RoClient.get_user(int(arg))
                embed = await create_embed("roblox")
                embed.title = "User Info"
                embed.set_thumbnail(url=f"https://www.roblox.com/bust-thumbnail/image?userId={user.id}&width=420&height=420&format=png")
                embed.add_field(name="Username", value=user.name, inline=True)
                if user.display_name != user.name:
                    embed.add_field(name="Display Name", value=user.display_name, inline=True)
                embed.add_field(name="User ID", value=str(user.id), inline=True)
                embed.add_field(name="Description", value="```" + disnake.utils.escape_mentions(disnake.utils.escape_markdown(str(user.description))) + "```", inline=False)
                embed.add_field(name="Created (dd/mm/yyyy)", value=user.created.strftime("%d/%m/%Y"), inline=False)
                cursor.execute("select * from users where rid=?", (user.id,))
                rows = cursor.fetchall()
                if rows.__len__() > 0:
                    embed.add_field(name="Verified", value=":white_check_mark:", inline=False)
                    embed.add_field(name="Associated Discord Account", value=f"<@{rows[0][0]}>", inline=False)
                else:
                    embed.add_field(name="Verified", value=":x:", inline=False)
                dfp = await WebClient.get(f"https://devforum.roblox.com/u/{arg}.json")
                devforumprofile = await dfp.json()
                if "user" in devforumprofile:
                    if "trust_level" in devforumprofile["user"]:
                        trust = None
                        if int(devforumprofile["user"]["trust_level"]) == 0:
                            trust = "Visitor"
                        elif int(devforumprofile["user"]["trust_level"]) == 1:
                            trust = "Member"
                        elif int(devforumprofile["user"]["trust_level"]) == 2:
                            trust = "Regular"
                        elif int(devforumprofile["user"]["trust_level"]) == 3:
                            trust = "Top Contributor"
                        elif int(devforumprofile["user"]["trust_level"]) == 4:
                            trust = "Community Editor"
                        elif int(devforumprofile["user"]["trust_level"]) == 5:
                            trust = "Community Sage"
                        else:
                            trust = "None"
                        embed.add_field(name=f"DevForum", value=f"Trust Level: {trust}\nTitle: {str(devforumprofile['user']['title'])}", inline=False)
                await ctx.reply(embed=embed)
            except:
                embed = await create_embed("roblox")
                embed.title = "User Info"
                embed.description = "User not found"
                await ctx.reply(embed=embed, delete_after=20)
                return

@bot.group(invoke_without_command=True)
async def mod(ctx: commands.Context):
    if ctx.invoked_subcommand == None:
        embed = await create_embed("global")
        embed.title = "Invalid Command Syntax"
        embed.description = "Please pass a valid subcommand! Use `b.help mod` for a list of subcommands."
        return await ctx.reply(embed=embed, delete_after=15)

@commands.cooldown(1, 10, commands.BucketType.user)
@mod.command(aliases=["prune", "clearmessages"])
async def purge(ctx: commands.Context, count: int, member: typing.Optional[discord.User]=None):
    raise NotImplementedError()
    if await is_mod(ctx) == False:
        embed = await create_embed("global")
        embed.title = "Lacking Permission"
        embed.description = "You currently lack permission to use this command."
        return await ctx.reply(embed=embed, delete_after=15)
    if not isinstance(ctx.guild, discord.Guild) or ctx.guild.id != mainid or not isinstance(ctx.channel, discord.TextChannel):
        embed = await create_embed("global")
        embed.title = "Incorrect Server"
        embed.description = "This command can only be run in the Blade Hub server."
        return await ctx.reply(embed=embed, delete_after=15)
    if member != None:
        def check(message: discord.Message):
            return message.pinned == False and message.author.id == member.id and message.id != ctx.message.id
        deleted = await ctx.channel.purge(limit=count+1, check=check, bulk=True)
        embed = await create_embed("global")
        embed.title = "BH Purge"
        embed.description = f"Successfully purged {deleted.__len__()} messages by {member.name}#{member.discriminator} ({member.id})!"
        await ctx.send(embed=embed, delete_after=30)
        await ctx.message.delete()
        logs = await bot.fetch_channel(logsid)
        embed = await create_embed("red")
        embed.title = "Messages Purged"
        embed.add_field(name="Count", value=str(deleted.__len__()), inline=False)
        embed.add_field(name="Channel", value=ctx.channel.mention, inline=False)
        embed.add_field(name="By", value=f"{member.name}#{member.discriminator} ({member.id})", inline=False)
        if isinstance(logs, discord.TextChannel):
            await logs.send(embed=embed)
        return
    else:
        def check(message: discord.Message):
            return message.pinned == False and message.id != ctx.message.id
        deleted = await ctx.channel.purge(limit=count+1, check=check, bulk=True)
        embed = await create_embed("global")
        embed.title = "BH Purge"
        embed.description = f"Successfully purged {deleted.__len__()} messages!"
        await ctx.send(embed=embed, delete_after=30)
        await ctx.message.delete()
        logs = await bot.fetch_channel(logsid)
        embed = await create_embed("red")
        embed.title = "Messages Purged"
        embed.add_field(name="Count", value=str(deleted.__len__()), inline=False)
        embed.add_field(name="Channel", value=ctx.channel.mention, inline=False)
        if isinstance(logs, discord.TextChannel):
            await logs.send(embed=embed)
        return

@commands.cooldown(4, 30, commands.BucketType.user)
@mod.command()
async def mute(ctx: commands.Context, *args):
    if await is_mod(ctx) == False:
        embed = await create_embed("global")
        embed.title = "Lacking Permission"
        embed.description = "You currently lack permission to use this command." # shouldve made it mute you for trying
        return await ctx.reply(embed=embed, delete_after=15)
    if not isinstance(ctx.guild, discord.Guild) or ctx.guild.id != mainid or not isinstance(ctx.author, discord.Member):
        embed = await create_embed("global")
        embed.title = "Incorrect Server"
        embed.description = "This command can only be run in the Blade Hub server."
        return await ctx.reply(embed=embed, delete_after=15)
    cursor = connection.cursor()
    match args[0]:
        case "-f":
            raise NotImplementedError()
            reason = ""
            for i, arg in enumerate(args):
                if i > 2:
                    reason = reason + " " + arg
            if reason == "":
                reason = "No reason"
            return await fmute(ctx, args[1], args[2], reason)
        case "-s":
            raise NotImplementedError()
        case _:
            try:
                member = await commands.MemberConverter().convert(ctx, args[0])
            except commands.BadArgument:
                embed = await create_embed("global")
                embed.title = "BH Mute"
                embed.description = "Invalid target argument! Please ensure they are a member of the server and that you didn't mistype anything!"
                return await ctx.reply(embed=embed, delete_after=15)
            if member.top_role > ctx.author.top_role:
                embed = await create_embed("global")
                embed.title = "BH Mute"
                embed.description = "You cannot mute those who have a higher role!"
                return await ctx.reply(embed=embed, delete_after=15)
            try:
                end: datetime.datetime = await parse_duration(args[1], "enddatetime", ctx.message.created_at) # type: ignore
            except ValueError:
                embed = await create_embed("global")
                embed.title = "BH Mute"
                embed.description = "Invalid duration argument! Please ensure that you didn't mistype anything!"
                return await ctx.reply(embed=embed, delete_after=15)
            reason = ""
            for i, arg in enumerate(args):
                if i > 1:
                    reason = reason + " " + arg
            if reason == "":
                reason = "No reason"
            try:
                await member.timeout(duration=end-ctx.message.created_at, reason=f"Muted by: {ctx.author.name}#{ctx.author.discriminator}\n\n{reason}")
            except discord.Forbidden:
                embed = await create_embed("global")
                embed.title = "BH Mute"
                embed.description = "Unable to mute that user!"
                return await ctx.reply(embed=embed)
            logs = await bot.fetch_channel(modlogsid)
            punishmentid = shortuuid.uuid()
            date = datetime.datetime.now()
            enddate = date + (end - ctx.message.created_at)
            embed = await create_log(member, ctx.author, reason, "mute", punishmentid, args[1])
            if isinstance(logs, discord.TextChannel):
                await logs.send(embed=embed)
            cursor.execute("insert into punishments values (?, ?, ?, ?, ?, ?, ?)", (punishmentid, "mute", member.id, ctx.author.id, date.strftime("%d/%M/%Y %H:%M:%S"), enddate.strftime("%d/%M/%Y %H:%M:%S"), reason))
            try:
                embed = await create_embed("global")
                embed.title = "Blade Hub Punishment"
                embed.description = f"You have been muted in Blade Hub for {await parse_duration(args[1], 'string')} for the reason:\n{reason}"
                await member.send(embed=embed)
            except discord.Forbidden:
                pass
            embed = await create_embed("global")
            embed.title = "BH Mute"
            embed.description = f"{member.name}#{member.discriminator} ({member.id}) has successfully been muted!\nPunishment ID: {punishmentid}"
            return await ctx.reply(embed=embed)

async def fmute(ctx: commands.Context, target: discord.Member, duration: str, reason: str="No reason"):
    pass

async def smute(ctx: commands.Context, target: discord.Member, duration: str, reason: str="No reason"):
    pass

@commands.cooldown(1, 30, commands.BucketType.user)
@mod.command()
async def delpunish(ctx: commands.Context, punishmentid: str):
    if await is_mod(ctx) == False:
        embed = await create_embed("global")
        embed.title = "Lacking Permission"
        embed.description = "You currently lack permission to use this command."
        return await ctx.reply(embed=embed, delete_after=15)
    if not isinstance(ctx.guild, discord.Guild) or ctx.guild.id != mainid or not isinstance(ctx.author, discord.Member):
        embed = await create_embed("global")
        embed.title = "Incorrect Server"
        embed.description = "This command can only be run in the Blade Hub server."
        return await ctx.reply(embed=embed, delete_after=15)
    cursor = connection.cursor()
    cursor.execute("select id from punishments where id = ?", (punishmentid,))
    rows = cursor.fetchall()
    if rows.__len__() >= 1:
        cursor.execute("delete from punishments where id = ?", (punishmentid,))
        embed = await create_embed("global")
        embed.title = "BH Delete Punishment"
        embed.description = "Punishment successfully deleted!"
        return await ctx.reply(embed=embed)
    else:
        embed = await create_embed("global")
        embed.title = "BH Delete Punishment"
        embed.description = "Punishment not found."
        return await ctx.reply(embed=embed, delete_after=15)

# this wouldve been really cool. too bad.
@bot.group()
async def clan(ctx: commands.Context):
    if ctx.invoked_subcommand == None:
        embed = await create_embed("global")
        embed.title = "Invalid Command Syntax"
        embed.description = "Please pass a valid subcommand! Use `b.help aff` for a list of subcommands."
        await ctx.reply(embed=embed, delete_after=30)

@commands.cooldown(5, 30, commands.BucketType.user)
@bot.command()
async def help(ctx: commands.Context, module: str=None):
    if module == None:
        embed = await create_embed("global")
        embed.title = "General Commands"
        embed.add_field(name="b.help [module]", value="Displays this message, or displays documentation for the specified module", inline=False)
        embed.add_field(name="b.case [case ID/discord ID/roblox ID/discord name/roblox name]", value="Shows all Low cases containing the given information", inline=False)
        embed.add_field(name="b.check [group ID]", value="Searches the specified group for Lows", inline=False)
        await ctx.reply(embed=embed, delete_after=90)
    else:
        match module:
            case "jp":
                if await is_supervisor(ctx) == True:
                    embed = await create_embed("jd")
                    embed.title = "JP Supervisor Commands"
                    embed.add_field(name="b.jd create", value="Starts a DM prompt to create a JP case", inline=False)
                    embed.add_field(name="b.jd edit [XPLT/DGN] [case ID]", value="Starts a DM prompt to edit a JP case", inline=False)
                    embed.add_field(name="b.jd activate [XPLT/DGN] [case ID]", value="Activates a cleared JP case", inline=False)
                    embed.add_field(name="b.jd clear [XPLT/DGN] [case ID]", value="Clears an active JP case", inline=False)
                    return await ctx.reply(embed=embed, delete_after=90)
                else:
                    embed = await create_embed("jd")
                    embed.title = "JP Supervisor Commands"
                    embed.description = "You do not have permission to view JP Supervisor commands."
                    return await ctx.reply(embed=embed, delete_after=90)
            case "mod":
                if await is_mod(ctx) == True:
                    embed = await create_embed("global")
                    embed.title = "Moderation Commands"
                    embed.add_field(name="b.mod mute [flag, optional] [username/ID/mention] [duration] [reason]", value="Mutes the specified user for the specified duration and reason", inline=False)
                    embed.add_field(name="(UNIMPLEMENTED) b.mod ban [flag, optional] [username/ID/mention] [duration, permanent if blank] [reason]", value="Bans the specified user for the specified duration and reason", inline=False)
                    embed.add_field(name="(UNIMPLEMENTED) b.mod kick [flag, optional] [username/ID/mention] [reason]", value="Kicks the specified user for the specified reason", inline=False)
                    embed.add_field(name="(UNIMPLEMENTED) b.mod warn [flag, optional] [username/ID/mention] [reason]", value="Warns the specified user for the specified reason", inline=False)
                    embed.add_field(name="(UNIMPLEMENTED) b.mod purge [amount of messages] [username/ID/mention, optional]", value="Purges all messages in the invoking channel sent by the specified user, otherwise deletes any message", inline=False)
                    embed.add_field(name="(UNIMPLEMENTED) b.mod logs [username/ID/mention]", value="Grabs and displays the moderation logs for the specified user", inline=False)
                    embed.add_field(name="b.mod rmpunish [punishment ID]", value="Removes the specified punishment", inline=False)
                    embed.add_field(name="(UNIMPLEMENTED) b.mod reason [punishment ID] [reason]", value="Sets the reason of the specified punishment to the specified reason", inline=False)
                    return await ctx.reply(embed=embed, delete_after=90)
                else:
                    embed = await create_embed("global")
                    embed.title = "Moderation Commands"
                    embed.description = "You do not have permission to view Moderation commands."
                    return await ctx.reply(embed=embed, delete_after=90)
            case "ro":
                embed = await create_embed("roblox")
                embed.title = "Roblox Commands"
                embed.add_field(name="b.ro verify", value="Starts a DM prompt to verify your Roblox account", inline=False)
                embed.add_field(name="b.ro userinfo [user ID/username]", value="Gives information about a specified user", inline=False)
                return await ctx.reply(embed=embed, delete_after=90)
            case "dev":
                embed = await create_embed("global")
                embed.title = "Developer Commands"
                embed.add_field(name="b.dev createresource", value="Starts a DM prompt to create an open resource", inline=False)
                embed.add_field(name="b.dev editresource [resource ID]", value="Starts a DM prompt to edit the specified open resource (if created by invoker)", inline=False)
                embed.add_field(name="b.dev deleteresource [resource ID]", value="Deletes the specified open resource (if created by invoker)", inline=False)
                embed.add_field(name="b.dev resources [type]", value="Shows a list of open resources, with the ability to filter", inline=False)
                embed.add_field(name="b.dev resource [resource ID/resource name]", value="Shows a list of open resources, with the ability to filter", inline=False)
                return await ctx.reply(embed=embed, delete_after=90)

if __name__ == "__main__":
    logger.debug("Running bot without launcher")
    bot.run("daves mother") # did you think id give you the token?
