def test_Lock_to_personal_account(app):
    app.Monitoring.delete_txt()
    app.entry_block.autotest() #Проверка Блокировки входа в личный кабинет
