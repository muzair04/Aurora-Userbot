FROM theteamultroid/ultroid:main

COPY installer.sh .

RUN bash installer.sh

# changing workdir
WORKDIR "/root/muzair04"

# start the bot.
CMD ["bash", "start"]
