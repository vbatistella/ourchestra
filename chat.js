const tmi = require('tmi.js');
var express = require('express');

/*********************************/
// Twitch Communication
/*********************************/

// Constants for bot
const opts = {
  identity: {
    username: 'maestro',
    password: 'oauth:l34hqfxwon74xgi9fdazr0dn0kjvoa'
  },
  channels: [
    'ourchestra_bot'
  ]
};

// Connect on twtich
const client = new tmi.client(opts);
client.on('message', onMessageHandler);
client.on('connected', onConnectedHandler);
client.connect();

// Data array
var data = [];

// Message Handler
function onMessageHandler (target, context, msg, self) {
  if (self) { return; }

  const commandName = msg.trim();

  // Commands
  switch (commandName) {
    case '!oi':
      client.say(target, 'pau no cu de quem ta lendo.');
      console.log('* Executed !oi command');
      data.push("oi");
      break;
    case '!kill':
      client.say(target, 'why tho?');
      console.log('* Executed !kill command');
      break;
  }
}

function onConnectedHandler (addr, port) {
  console.log('* Connected');
}

/*********************************/
// Python Communication
/*********************************/
var app = express();
var port = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.send(data)
  data = []
})
app.listen(port);