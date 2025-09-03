import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
‎
‎# আপনার বট টোকেন এখানে দিন
‎# আসল টোকেন সরাসরি কোডে না রেখে Environment Variable হিসেবে ব্যবহার করা ভালো
‎# তবে শেখার জন্য আপাতত সরাসরি ব্যবহার করতে পারেন।
‎TOKEN = "7783347864:AAEHo8P7gQ8pyeAsgq8QsF5IKByQgJC3V-Y" # <<<<<<< এখানে আপনার টোকেনটি বসান
‎
‎# /start কমান্ডের জন্য ফাংশন
‎def start(update, context):
‎    """/start কমান্ড দিলে এই ফাংশনটি কাজ করবে"""
‎    update.message.reply_text('হ্যালো! আমি একটি বেসিক টেলিগ্রাম বট। আমাকে কিছু লিখে পাঠান, আমি সেটারই উত্তর দেবো।')
‎
‎# যেকোনো সাধারণ মেসেজের উত্তর দেওয়ার জন্য ফাংশন
‎def echo(update, context):
‎    """ব্যবহারকারীর পাঠানো মেসেজের উত্তর দেয়"""
‎    user_text = update.message.text
‎    update.message.reply_text(user_text)
‎
‎def main():
‎    """বটটি চালু করার মূল ফাংশন"""
‎    # আপডেটার অবজেক্ট তৈরি করা, যা টেলিগ্রাম থেকে আপডেট আনে
‎    updater = Updater(TOKEN, use_context=True)
‎
‎    # ডিসপ্যাচার তৈরি করা, যা বিভিন্ন কমান্ড বা মেসেজকে নির্দিষ্ট ফাংশনের সাথে যুক্ত করে
‎    dp = updater.dispatcher
‎
‎    # একটি কমান্ড হ্যান্ডলার যোগ করা, যা /start কমান্ড পেলে start ফাংশনকে কল করবে
‎    dp.add_handler(CommandHandler("start", start))
‎
‎    # একটি মেসেজ হ্যান্ডলার যোগ করা, যা যেকোনো টেক্সট মেসেজ পেলে echo ফাংশনকে কল করবে
‎    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
‎
‎    # বটটিকে চালু করা (টেলিগ্রাম থেকে আপডেট খোঁজা শুরু করবে)
‎    updater.start_polling()
‎    print("বটটি সফলভাবে চালু হয়েছে এবং মেসেজের জন্য অপেক্ষা করছে...")
‎
‎    # বটটি Ctrl+C দিয়ে বন্ধ না করা পর্যন্ত চলতে থাকবে
‎    updater.idle()
‎
‎if __name__ == '__main__':
‎    main()
‎‎import telegram
‎from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
‎import os
‎
‎# আপনার বট টোকেন এখানে দিন
‎# আসল টোকেন সরাসরি কোডে না রেখে Environment Variable হিসেবে ব্যবহার করা ভালো
‎# তবে শেখার জন্য আপাতত সরাসরি ব্যবহার করতে পারেন।
‎TOKEN = "7783347864:AAEHo8P7gQ8pyeAsgq8QsF5IKByQgJC3V-Y" # <<<<<<< এখানে আপনার টোকেনটি বসান
‎
‎# /start কমান্ডের জন্য ফাংশন
‎def start(update, context):
‎    """/start কমান্ড দিলে এই ফাংশনটি কাজ করবে"""
‎    update.message.reply_text('হ্যালো! আমি একটি বেসিক টেলিগ্রাম বট। আমাকে কিছু লিখে পাঠান, আমি সেটারই উত্তর দেবো।')
‎
‎# যেকোনো সাধারণ মেসেজের উত্তর দেওয়ার জন্য ফাংশন
‎def echo(update, context):
‎    """ব্যবহারকারীর পাঠানো মেসেজের উত্তর দেয়"""
‎    user_text = update.message.text
‎    update.message.reply_text(user_text)
‎
‎def main():
‎    """বটটি চালু করার মূল ফাংশন"""
‎    # আপডেটার অবজেক্ট তৈরি করা, যা টেলিগ্রাম থেকে আপডেট আনে
‎    updater = Updater(TOKEN, use_context=True)
‎
‎    # ডিসপ্যাচার তৈরি করা, যা বিভিন্ন কমান্ড বা মেসেজকে নির্দিষ্ট ফাংশনের সাথে যুক্ত করে
‎    dp = updater.dispatcher
‎
‎    # একটি কমান্ড হ্যান্ডলার যোগ করা, যা /start কমান্ড পেলে start ফাংশনকে কল করবে
‎    dp.add_handler(CommandHandler("start", start))
‎
‎    # একটি মেসেজ হ্যান্ডলার যোগ করা, যা যেকোনো টেক্সট মেসেজ পেলে echo ফাংশনকে কল করবে
‎    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
‎
‎    # বটটিকে চালু করা (টেলিগ্রাম থেকে আপডেট খোঁজা শুরু করবে)
‎    updater.start_polling()
‎    print("বটটি সফলভাবে চালু হয়েছে এবং মেসেজের জন্য অপেক্ষা করছে...")
‎
‎    # বটটি Ctrl+C দিয়ে বন্ধ না করা পর্যন্ত চলতে থাকবে
‎    updater.idle()
‎
‎if __name__ == '__main__':
‎    main()
‎