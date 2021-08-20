const mineflayer = require('mineflayer')
const { Webhook } = require('discord-webhook-node');
require('dotenv').config()
const hook = new Webhook(process.env.WEBHOOK);
const bot = mineflayer.createBot({
    host: 'localhost', // minecraft server ip
    username: 'bot1', // minecraft username
})
bot.on('chat', async (username, message) => {
    hook.setUsername(username);
    await hook.setAvatar("https://www.mc-heads.net/avatar/" + username);
    await hook.send(message);
})
