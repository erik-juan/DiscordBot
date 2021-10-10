cd ~/discord_bot
docker rmi -f mahkumazahn/discord_bot
docker build -t mahkumazahn/discord_bot .
docker run --rm --env-file .env -v ~/logs/discord_bot:/logs mahkumazahn/discord_bot