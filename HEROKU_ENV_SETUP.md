# Heroku Environment Variables Setup for Admin Bot

## 🚨 IMPORTANT: Environment Variables Required

The admin bot needs the following environment variables to be set on Heroku:

### Required Environment Variables:

1. **ADMIN_BOT_TOKEN** - Your admin bot token
   - Value: `8185697878:AAEQTzsCj_q0AIoBS90AQUDg6AAX6GDkaEQ`

2. **MAIN_BOT_TOKEN** - Main bot token (to send messages to users)
   - Value: `5598756315:AAEn-zTSdHL3H88DoxTI1sVP28x38h0ltbc`

3. **ADMIN_USER_ID** - Your Telegram user ID
   - Value: `41107472`

4. **ADMIN_TELEGRAM_ID** - Your Telegram user ID (same as above)
   - Value: `41107472`

## 🔧 How to Set Environment Variables on Heroku:

### Method 1: Heroku Dashboard (Web Interface)

1. Go to your Heroku dashboard
2. Select your admin bot app
3. Go to **Settings** tab
4. Scroll down to **Config Vars** section
5. Click **Reveal Config Vars**
6. Add each environment variable:

```
ADMIN_BOT_TOKEN = 8185697878:AAEQTzsCj_q0AIoBS90AQUDg6AAX6GDkaEQ
MAIN_BOT_TOKEN = 5598756315:AAEn-zTSdHL3H88DoxTI1sVP28x38h0ltbc
ADMIN_USER_ID = 41107472
ADMIN_TELEGRAM_ID = 41107472
```

### Method 2: Heroku CLI (if you have it installed)

```bash
heroku config:set ADMIN_BOT_TOKEN=8185697878:AAEQTzsCj_q0AIoBS90AQUDg6AAX6GDkaEQ --app your-admin-bot-app-name
heroku config:set MAIN_BOT_TOKEN=5598756315:AAEn-zTSdHL3H88DoxTI1sVP28x38h0ltbc --app your-admin-bot-app-name
heroku config:set ADMIN_USER_ID=41107472 --app your-admin-bot-app-name
heroku config:set ADMIN_TELEGRAM_ID=41107472 --app your-admin-bot-app-name
```

## 🔍 Verification:

After setting the environment variables:

1. **Restart the admin bot** on Heroku
2. **Check the logs** to ensure no "MAIN_BOT_TOKEN not found" errors
3. **Test the donation confirmation flow**:
   - User confirms donation in main bot
   - Admin receives notification in admin bot
   - Admin clicks "✅ Подтвердить донат"
   - User should receive confirmation message in main bot (not admin bot)

## 🐛 Troubleshooting:

### Issue: Admin bot receives confirmation message instead of user
**Solution**: Make sure `MAIN_BOT_TOKEN` is set correctly

### Issue: "MAIN_BOT_TOKEN not found" error
**Solution**: Verify the environment variable is set in Heroku config vars

### Issue: Messages not reaching users
**Solution**: Check that `MAIN_BOT_TOKEN` matches the main bot's token exactly

## 📋 Environment Variables Summary:

| Variable | Purpose | Value |
|----------|---------|-------|
| `ADMIN_BOT_TOKEN` | Admin bot's own token | `8185697878:AAEQTzsCj_q0AIoBS90AQUDg6AAX6GDkaEQ` |
| `MAIN_BOT_TOKEN` | Main bot token (to send messages to users) | `5598756315:AAEn-zTSdHL3H88DoxTI1sVP28x38h0ltbc` |
| `ADMIN_USER_ID` | Your Telegram user ID | `41107472` |
| `ADMIN_TELEGRAM_ID` | Your Telegram user ID (same as above) | `41107472` |

## ✅ After Setup:

1. The admin bot will be able to send messages to users via the main bot
2. Donation confirmations will reach the correct user
3. The setup process will start automatically after confirmation
4. All admin notifications will work properly

**Remember to restart the admin bot after setting the environment variables!**


