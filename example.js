require('dotenv').config()

const YoutubePlaylistMarkdown = require('./index');

let config = {
  GOOGLE_API_KEY: process.env.GOOGLE_API_KEY
};

let ypm = new YoutubePlaylistMarkdown(config);

// const playlistId = 'PLrG78JjvL7hWqX2FW54Ck8UP45fbWQXcu';
// ypm.generatorPlaylist(playlistId);

const channelId = 'UCdoadna9HFHsxXWhafhNvKw';
ypm.generatorAll(channelId);