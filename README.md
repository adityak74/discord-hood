# Slack-hood

[![Make Release](https://github.com/adityak74/slack-hood/actions/workflows/bump-version-release.yml/badge.svg)](https://github.com/adityak74/slack-hood/actions/workflows/bump-version-release.yml)

### Slack bot to monitor your Robinhood portfolio

#### Environment Variables

```
ROBINHOOD_USERNAME=username
ROBINHOOD_PASSWORD=password
DISCORD_BOT_TOKEN=create a bot app and get token
DISCORD_STOCK_CHANNEL_ID=copy channel id by right click channel and copy id
```

#### Connect bot to server

1. Create a server and a bot account using https://discord.com/developers
2. Go to Oauth2 -> URL Generator -> Select Bot and Admin permission and copy the link generated.
3. Open this Link in New Tab and Select the Server and add the bot.


#### Run the app

```make run```


#### Test the app

```make test```
