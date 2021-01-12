import json
import time
import datetime
import asyncio
import pyupbit
# 분할 모듈
import KeyModule
import UpbitModule
import FileControl


# init
upbit = KeyModule.get_upbit_key()
settingJson = FileControl.open_json_file("json/upbit_setting.json")
helpJson = FileControl.open_json_file("json/help.json")



# 함수 정의
async def main_loop():
    while True:
        print("test")
        await asyncio.sleep(1)


async def coroutine_trends(settingJson):
    pass
    #for trends in settingJson["trend"]:


if __name__ == "__main__":
    # start
    UpbitModule.get_ticker_krw_base()

    #이벤트 루프
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_loop())
    loop.close()
