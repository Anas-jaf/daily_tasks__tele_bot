# daily_tasks__tele_bot
telegram bot for daily tasks that you set up by yourself

قبل تشغيل الملف و تشغيل المشروع على السيرفر يجب ان تنفذ هذا الامر :-

```
chmod +x add_cron_job.sh
dir= "$(pwd)"
(crontab -l ; echo "0 0 * * * $dir/add_cron_job.sh") | crontab -
```



https://github.com/Anas-jaf/daily_diary_document

https://github.com/Anas-jaf/daily_tasks__tele_bot