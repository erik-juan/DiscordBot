module.exports = {
    apps: [
      {
        name: 'aws-codedeploy',
        script: './scripts/start-bot.sh',
        interpreter: 'none',
        env: {
          NODE_ENV: 'development',
        },
      },
    ],
}
