import re

async def card_pattern(_,__,message):
        num = re.findall(r"^[a-zA-Z0-9]{6}_card$",message.text)
        if num:
            return True
        return False  

async def dp_photo(_,__,message):
        num = re.findall(r"^[0-9]{1,3}px_x=[0-9]{1,5}_y=[0-9]{1,5}$",message.text)
        if num:
            return True
        return False  

async def name_text(_,__,message):
      num=re.findall(r"^\w+_[RBI]_\d{1,3}_\d{1,5}$",message.text)
      if num:
            return True
      return False

async def responses(_,__,message):
      num=re.findall(r"^\d+_res$",message.text)
      if num:
            return True
      return False

