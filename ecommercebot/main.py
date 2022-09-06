from ecommerce.ecommerce import Shopping


with Shopping(teardown=True) as bot:
    bot.get_home_page()
    bot.phones()
    bot.infomation()
