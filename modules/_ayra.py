# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.


from . import Button

REPOMSG = """
◈ **ᴀᴜʀᴏʀᴀ ꭙ͢ ᴜsᴇʀʙᴏᴛ** ◈
"""

RP_BUTTONS = [
    [Button.url("Channel", "https://t.me/Kamarsnow")],
]

AYSTRING = """🎇 **Thanks for Deploying ᴀᴜʀᴏʀᴀ ꭙ͢ ᴜsᴇʀʙᴏᴛ!**

• Here, are the Some Basic stuff from, where you can Know, about its Usage."""

"""
@ayra_cmd(
    pattern="repo$",
    manager=True,
)
async def repify(e):
    try:
        q = await e.client.inline_query(asst.me.username, "")
        await q[0].click(e.chat_id)
        return await e.delete()
    except (
        ChatSendInlineForbiddenError,
        ChatSendMediaForbiddenError,
        BotMethodInvalidError,
    ):
        pass
    except Exception as er:
        LOGS.info(f"Error while repo command : {str(er)}")
    await e.eor(REPOMSG)


@ayra_cmd(pattern="ayra$")
async def useAyra(rs):
    button = Button.inline("Start >>", "initft_2")
    msg = await asst.send_message(
        LOG_CHANNEL,
        AYSTRING,
        file="https://graph.org/file/a51b51ca8a7cc5327fd42.jpg",
        buttons=button,
    )
    if not (rs.chat_id == LOG_CHANNEL and rs.client._bot):
        await eor(rs, f"**[Click Here]({msg.message_link})**")
"""
