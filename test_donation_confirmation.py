#!/usr/bin/env python3
"""
Test script to simulate donation confirmation flow
"""

import os
import asyncio
import logging
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def test_donation_confirmation():
    """Test donation confirmation flow"""
    
    # Get admin bot token (use the one from the logs)
    admin_bot_token = "8185697878:AAEQTzsCj_q0AIoBS90AQUDg6AAX6GDkaEQ"
    main_bot_token = "5598756315:AAEn-zTSdHL3H88DoxTI1sVP28x38h0ltbc"
    admin_user_id = "41107472"
    test_user_id = "41107472"  # Using admin as test user
    
    try:
        # Create bot instances
        admin_bot = Bot(token=admin_bot_token)
        main_bot = Bot(token=main_bot_token)
        
        # Get bot info
        admin_info = await admin_bot.get_me()
        main_info = await main_bot.get_me()
        logger.info(f"Admin bot: {admin_info.username}")
        logger.info(f"Main bot: {main_info.username}")
        
        # Send test donation confirmation request to admin
        test_message = f"""💳 **Новая попытка оплаты**

👤 **Пользователь:** Test User
🆔 **ID:** {test_user_id}
🎯 **Цель:** Test goal for debugging
📋 **План:** Express
💰 **Сумма:** 1000 руб
⏰ **Время:** 2025-09-24 09:19:13

**Подтвердите получение доната:**"""
        
        # Create inline keyboard
        keyboard = [
            [InlineKeyboardButton("✅ Подтвердить донат", callback_data=f"confirm_donation_{test_user_id}")],
            [InlineKeyboardButton("❌ Отклонить донат", callback_data=f"reject_donation_{test_user_id}")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        # Send to admin
        await admin_bot.send_message(
            chat_id=int(admin_user_id),
            text=test_message,
            parse_mode='Markdown',
            reply_markup=reply_markup
        )
        
        logger.info("✅ Test donation confirmation request sent to admin")
        
        # Wait a bit
        await asyncio.sleep(2)
        
        # Send follow-up message
        await admin_bot.send_message(
            chat_id=int(admin_user_id),
            text="🔍 If you see the buttons above, click '✅ Подтвердить донат' to test the flow."
        )
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Error testing donation confirmation: {e}")
        return False

async def main():
    """Main test function"""
    logger.info("🧪 Testing donation confirmation flow...")
    
    success = await test_donation_confirmation()
    
    if success:
        logger.info("✅ Donation confirmation test completed")
    else:
        logger.info("❌ Donation confirmation test failed")
    
    return success

if __name__ == "__main__":
    asyncio.run(main())


