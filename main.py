# UserInfo bot
# GitHub: https://github.com/Kourva/UserInfoBot


# Imports
import telebot


# Import config
with open("conf.py") as data:
    exec(data.read())

# Define bot
bot = telebot.TeleBot(config["token"])


# Class that creates a member with all needed stuff
class User:
    def __init__(self, message):
        # takes user info from message
        self.firstname = message.from_user.first_name
        self.lastname = message.from_user.last_name
        self.username = message.from_user.username
        self.chatid = message.from_user.id

    def whoami(self):
        # returns user info as string
        temp = config["whoami"].format(
            self.firstname, self.lastname, self.username, self.chatid
        )
        return temp


# Start command
@bot.message_handler(commands=["start"])
def start_command(message):
    bot.reply_to(message, "Привет, Send any message to get your info")


# All messages
@bot.message_handler(func=lambda _: True)
def all_messages(message):
    user = User(message)
    bot.reply_to(message, user.whoami(), parse_mode="MarkdownV2")


if __name__ == "__main__":
    # Run the bot in infinity mode
    bot.infinity_polling()