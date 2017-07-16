import telepot

class App:
    """Here it is: this bot's entry point. Create a new app by giving it their
    API code as provided by Telegram and start running it."""
    def __init__(self, api):
        self.bot = telepot.Bot(api)
        self.offset = 0

    def loop(self):
        updates = self.bot.getUpdates(self.offset)

        # Dealing with updates
        for update in updates:
            if 'message' in update:
                self.bot.sendMessage(update['message']['chat']['id'], 'hello!')

           # Taking care of offset
            self.offset = updates[-1]['update_id'] + 1
