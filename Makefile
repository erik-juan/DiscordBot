build:
	docker rmi -f mahkumazahn/discord_bot
	docker build -t mahkumazahn/discord_bot .
run:
	docker run --rm --env-file .env -v ~/logs/discord_bot:/logs