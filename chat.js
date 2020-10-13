const tmi = require('tmi.js');


const opts = {
  identity: {
    username: 'maestro',
    password: 'oauth:l34hqfxwon74xgi9fdazr0dn0kjvoa'
  },
  channels: [
    'ourchestra_bot'
  ]
};
const client = new tmi.client(opts);

client.on('message', onMessageHandler);
client.on('connected', onConnectedHandler);

client.connect();

function onMessageHandler (target, context, msg, self) {
  if (self) { return; }

  const commandName = msg.trim();

  // If the command is known, let's execute it
  if (commandName === '!oi') {
    client.say(target, 'pau no cu de quem ta lendo.');
    console.log('* Executed ${commandName} command');
  } else {
    console.log('* Unknown command ${commandName}');
  }
}

function onConnectedHandler (addr, port) {
  console.log('* Connected to ${addr}:${port}');
}