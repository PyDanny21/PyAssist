from instabot import Bot
bot=Bot()
bot.login(username='',password='')
bot.follow('kojo forex')
bot.upload_photo('directory',caption='I love myself')
bot.unfollow('kojo forex')
bot.send_message('',['username1','username2'])
followers=bot.get_user_followers('username of a user')
for follower in followers:
    print(bot.get_user_info(follower))
following=bot.get_user_following('userrname')
for Following in following:
    print(bot.get_user_info(Following))