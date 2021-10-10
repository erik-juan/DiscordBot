cd ~/discord_bot
docker stop discord_bot
docker rmi -f mahkumazahn/discord_bot
docker build -t mahkumazahn/discord_bot .
docker run -d --rm --env-file .env -v ~/logs/discord_bot:/logs --name discord_bot mahkumazahn/discord_bot