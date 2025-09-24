#!/usr/bin/env python3
"""
Test script to check if admin bot is running and can receive messages
"""

import os
import asyncio
import logging
from telegram import Bot

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def test_admin_bot_connection():
    """Test if admin bot is running and can receive messages"""
    
    # Get bot token from environment
    bot_token = os.getenv('ADMIN_BOT_TOKEN')
    if not bot_token:
        logger.error("ADMIN_BOT_TOKEN not found in environment variables")
        return False
    
    try:
        # Create bot instance
        bot = Bot(token=bot_token)
        
        # Get bot info
        bot_info = await bot.get_me()
        logger.info(f"Admin bot info: {bot_info.username} ({bot_info.first_name})")
        
        # Test sending a message to admin
        admin_user_id = os.getenv('ADMIN_USER_ID', '41107472')
        
        test_message = """🔧 Admin Bot Connection Test

✅ Admin bot is running and can send messages
✅ Connection to Telegram API is working
✅ Ready to receive donation confirmation requests

If you see this message, the admin bot is working correctly!"""
        
        await bot.send_message(
            chat_id=int(admin_user_id),
            text=test_message
        )
        
        logger.info("✅ Test message sent successfully to admin")
        return True
        
    except Exception as e:
        logger.error(f"❌ Error testing admin bot connection: {e}")
        return False

async def main():
    """Main test function"""
    logger.info("🧪 Testing admin bot connection...")
    
    success = await test_admin_bot_connection()
    
    if success:
        logger.info("✅ Admin bot connection test PASSED")
    else:
        logger.info("❌ Admin bot connection test FAILED")
    
    return success

if __name__ == "__main__":
    asyncio.run(main())


