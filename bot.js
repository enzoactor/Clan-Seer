const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
    console.log('I am ready!');
});

client.on('message', message => {
    if (message.content === 'ping') {
    	message.reply('pong');
  	}
});

// THIS  MUST  BE  THIS  WAY
client.login(process.env.NTMxMzEyMzM3MjAyNzA4NDgw.DxMI9Q.WZq0u9yabk89zMEVwRxKGd4BK9o);

#client.run('NTMxMzEyMzM3MjAyNzA4NDgw.DxMI9Q.WZq0u9yabk89zMEVwRxKGd4BK9o')
