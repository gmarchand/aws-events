const debug = require('debug')('youtubePlaylistMarkdown');
const fs = require('fs');
const table = require('markdown-table');
const PlaylistSummary = require('youtube-playlist-summary');

let config = {
  GOOGLE_API_KEY: process.env.GOOGLE_API_KEY
};

const getFieldNames = function() {
  return ['title', 'Published At'];
};

const getRow = function (item) {
  let videoTitle = `[${item.title.replace(/\|/g, '-')}](${item.videoUrl})`;
  let publishedAt = item.publishedAt.substr(0, 10);
  return [videoTitle, publishedAt];
};

const generatorPlaylistItemTable = async function (file, playlist) {
  debug('=== generatorPlaylistItemTable ===');
  let tableContent = [];
  playlist.items.forEach(function (item, index) {
    if (index == 0) {
      tableContent.push(getFieldNames());
    }
    tableContent.push(getRow(item));
  });
  file.write(`\n\n#### [${playlist.playlistTitle}](${playlist.playlistUrl}) created by [${playlist.channelTitle}](${playlist.channelUrl})\n\n`);
  file.write(`* video count: ${playlist.items.length} \n\n`);
  file.write(table(tableContent));
  debug(table(tableContent));
};

class PlaylistMarkdown {

  constructor(config) {
    this.config = config;
    debug(config);
    this.ps = new PlaylistSummary(config);
  }

  async generatorPlaylist(playlistId) {
    debug('=== generatorPlaylist ===');
    try {
      let playlist = await this.ps.getPlaylistItems(playlistId);
      let file = fs.createWriteStream(`playlist-${playlistId}.md`);
      generatorPlaylistItemTable(file, playlist);
      file.end();
    } catch (error) {
      throw error;
    }
  }

  async generatorAll(channelId) {
    try {
      debug('=== generatorAll ===');
      let result = await this.ps.getSummary(channelId);
      let file = fs.createWriteStream(`channel-${channelId}.md`);
      file.write(`### [${result.channelTitle}](${result.channelUrl})`);
      result.items.forEach(function (playlist) {
        generatorPlaylistItemTable(file, playlist);
      });
      file.end();
    } catch (error) {
      throw error;
    }
  }
}

module.exports = PlaylistMarkdown;