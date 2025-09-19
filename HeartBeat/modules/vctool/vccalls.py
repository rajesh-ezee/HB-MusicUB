from ... import app
from pyrogram import filters
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputPeerChannel, InputPeerChat

async def edit_or_reply(message: Message, *args, **kwargs) -> Message:
    apa = (
        message.edit_text
        if bool(message.from_user and message.from_user.is_self or message.outgoing)
        else (message.reply_to_message or message).reply_text
    )
    return await apa(*args, **kwargs)

eor = edit_or_reply

async def get_vc_call(client, message):
    chat_id = message.chat.id
    chat_peer = await client.resolve_peer(chat_id)

    if isinstance(chat_peer, InputPeerChannel):
        full_chat = (await client.invoke(GetFullChannel(channel=chat_peer))).full_chat
    elif isinstance(chat_peer, InputPeerChat):
        full_chat = (await client.invoke(GetFullChat(chat_id=chat_peer.chat_id))).full_chat
    else:
        return False

    return full_chat.call if full_chat else False


@Client.on_message(filters.command("startvc", ".") & filters.me)
async def start_vc(client, message):
    chat_id = message.chat.id
    aux = await eor(message, "**🔄 Processing...**")

    try:
        vc_call = await get_vc_call(client, message)
        if vc_call:
            return await aux.edit("**🤖 VC Already Active❗**")

        peer = await client.resolve_peer(chat_id)
        await client.invoke(
            CreateGroupCall(
                peer=peer,
                random_id=client.rnd_id() // 9000000000,
            )
        )
        return await aux.edit("**✅ VC Started Successfully!**")
    except Exception as e:
        print(f"[Start VC Error] {e}")
        await aux.edit("**❌ Failed to Start VC.**")


@Client.on_message(filters.command("endvc", ".") & filters.me)
async def stop_vc(client, message):
    aux = await eor(message, "**🔄 Processing...**")
    try:
        vc_call = await get_vc_call(client, message)
        if not vc_call:
            return await aux.edit("**🤖 VC Not Started Yet❗**")

        await client.invoke(DiscardGroupCall(call=vc_call))
        return await aux.edit("**✅ VC Ended Successfully!**")
    except Exception as e:
        print(f"[Stop VC Error] {e}")
        await aux.edit("**❌ Failed to End VC.**")


@Client.on_message(filters.command("restartvc", ".") & filters.me)
async def restart_vc(client, message):
    chat_id = message.chat.id
    aux = await eor(message, "**🔄 Restarting VC...**")

    try:
        vc_call = await get_vc_call(client, message)
        if vc_call:
            await client.invoke(DiscardGroupCall(call=vc_call))
            await aux.edit("**✅ VC Ended. Restarting...**")

        peer = await client.resolve_peer(chat_id)
        await client.invoke(
            CreateGroupCall(
                peer=peer,
                random_id=client.rnd_id() // 9000000000,
            )
        )
        return await aux.edit("**✅ VC Restarted Successfully!**")
    except Exception as e:
        print(f"[Restart VC Error] {e}")
        await aux.edit("**❌ Failed to Restart VC.**")


__NAME__ = "Vᴄ"
__MENU__ = """
**🔊 Voice Chat Controls:**

`.svc` - Start VC in the current chat  
`.dvc` / `.evc` - End VC in the current chat  
`.rvc` - Restart VC in the current chat  
"""
