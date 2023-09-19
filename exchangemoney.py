import apiexchangemoney
import discord
from discord.ext import commands
from discord import app_commands
import json
import mysql.connector
from datetime import datetime

# เรียกใช้ฟังก์ชั่น listcountry() เพื่อรับรายการสกุลเงิน
cc = apiexchangemoney.listcheckcountry()

for listcountry in cc:
    
    print(listcountry) 
 