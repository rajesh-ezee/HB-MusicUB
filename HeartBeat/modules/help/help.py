import asyncio

from pyrogram import Client, enums, filters
from pyrogram.types import Message

from HeartBeat import app, CMD_HELP
from HeartBeat.helper.PyroHelpers import ReplyCheck
from HeartBeat.helper.utility import split_list


async def edit_or_reply(message: Message, *args, **kwargs) -> Message:
    xyz = (
        message.edit_text
        if bool(message.from_user and message.from_user.is_self or message.outgoing)
        else (message.reply_to_message or message).reply_text
    )
    return await xyz(*args, **kwargs)


@Client.on_message(filters.command(["hlp", "helpme"], ".") & filters.me)
async def module_help(client: Client, message: Message):
    cmd = message.command
    help_arg = ""
    bot_username = (await app.get_me()).username
    if len(cmd) > 1:
        help_arg = " ".join(cmd[1:])
    elif not message.reply_to_message and len(cmd) == 1:
        await message.edit("ʜʙ-ꜰᴀᴍ ᴄᴏᴍɪɴɢ..😈")
        try:
            nice = await client.get_inline_bot_results(bot=bot_username, query="helper")
            await asyncio.gather(
                message.delete(),
                client.send_inline_bot_result(
                    message.chat.id, nice.query_id, nice.results[0].id
                ),
            )
        except BaseException as e:
            print(f"{e}")
            # Build clean HTML list of modules
            modules = sorted(CMD_HELP.keys())
            rows = ""
            for pair in split_list(modules, 2):
                left = pair[0]
                right = pair[1] if len(pair) > 1 else ""
                rows += f"<blockquote>• <b>{left}</b>{' — <b>'+right+'</b>' if right else ''}</blockquote>\n"

            xx = await client.send_message(
                message.chat.id,
                f"<b>💥 HEART-BEAT MODULES 💥</b>\n\n{rows}\n<blockquote>• @HeartBeat_Fam × @HeartBeat_Offi •</blockquote>",
                reply_to_message_id=ReplyCheck(message),
                parse_mode=enums.ParseMode.HTML
            )
            await xx.reply(
                f"<b>Usage:</b> <code>.help broadcast</code> <b>To View Module Information</b>",
                parse_mode=enums.ParseMode.HTML
            )
            return

    if help_arg:
        if help_arg in CMD_HELP:
            commands: dict = CMD_HELP[help_arg]
            this_command = f"<blockquote>──「 <b>Help For {str(help_arg).upper()}</b> 」──</blockquote>\n"
            for x in commands:
                this_command += (
                    f"<blockquote>• <b>Command:</b> <code>.{str(x)}</code><br>"
                    f"• <b>Function:</b> <code>{str(commands[x])}</code></blockquote>\n"
                )
            this_command += "<blockquote>© @HeartBeat_Fam</blockquote>"
            await edit_or_reply(
                message, this_command, parse_mode=enums.ParseMode.HTML
            )
        else:
            await edit_or_reply(
                message,
                f"<code>{help_arg}</code> <b>Not a Valid Module Name.</b>",
                parse_mode=enums.ParseMode.HTML
            )


@Client.on_message(filters.command(["plugins", "modules", "help"], ".") & filters.me)
async def module_helper(client: Client, message: Message):
    cmd = message.command
    help_arg = ""
    if len(cmd) > 1:
        help_arg = " ".join(cmd[1:])
    elif message.reply_to_message and len(cmd) == 1:
        help_arg = message.reply_to_message.text
    elif not message.reply_to_message and len(cmd) == 1:
        modules = sorted(CMD_HELP.keys())
        rows = ""
        for pair in split_list(modules, 2):
            left = pair[0]
            right = pair[1] if len(pair) > 1 else ""
            rows += f"<blockquote>• <b>{left}</b>{' — <b>'+right+'</b>' if right else ''}</blockquote>\n"

        await edit_or_reply(
            message,
            f"<b>𝐇ᴇᴀʀᴛ𝐁ᴇᴀᴛ 𝐏ʟᴜɢɪɴ𝐬</b>\n\n{rows}\n<blockquote>• @HeartBeat_Fam × @HeartBeat_Offi •</blockquote>",
            parse_mode=enums.ParseMode.HTML
        )
        await message.reply(
            f"<b>Usage:</b> <code>.help broadcast</code> <b>To View Module details</b>",
            parse_mode=enums.ParseMode.HTML
        )

    if help_arg:
        if help_arg in CMD_HELP:
            commands: dict = CMD_HELP[help_arg]
            this_command = f"<blockquote>──「 <b>Help For {str(help_arg).upper()}</b> 」──</blockquote>\n"
            for x in commands:
                this_command += (
                    f"<blockquote>• <b>Command:</b> <code>.{str(x)}</code><br>"
                    f"• <b>Function:</b> <code>{str(commands[x])}</code></blockquote>\n"
                )
            this_command += "<blockquote>© @HeartBeat_Fam</blockquote>"
            await edit_or_reply(
                message, this_command, parse_mode=enums.ParseMode.HTML
            )
        else:
            await edit_or_reply(
                message,
                f"<code>{help_arg}</code> <b>Not a Valid Module Name.</b>",
                parse_mode=enums.ParseMode.HTML
            )


def add_command_help(module_name, commands):
    if module_name in CMD_HELP.keys():
        command_dict = CMD_HELP[module_name]
    else:
        command_dict = {}

    for x in commands:
        for y in x:
            if y is not x:
                command_dict[x[0]] = x[1]

    CMD_HELP[module_name] = command_dict
