This project create by 6810110510 นายศิรสิทธิ์ ศุภสาร

โค้ดชุดนี้ใช้เทคนิค Asynchronous I/O และมีจุดประสงค์หลักเพื่อดึงข้อมูลจากเว็บไซต์ (API) จำนวนหลายๆ ครั้งแบบพร้อมๆ กัน เพื่อประหยัดเวลา
(โปรแกรมจะไม่ต้องเสียเวลา จากการรอให้การดึงข้อมูลครั้งที่ 1 เสร็จก่อน ถึงจะเริ่มดึงครั้งที่ 2 )
โดย Code หลักมีสี่ส่วนคือ
1.ส่วน import
import asyncio
=> นำเข้า asyncio ที่เป็นไลบรารีมาตรฐานของ Python ที่ใช้จัดการการทำงานแบบ Asynchronous และดูแลระบบศูนย์กลางที่เรียกว่า Event Loop
import aiohttp
=> นำเข้า aiohttp  ที่เป็นไลบรารีเสริม  สำหรับจัดการ HTTP Request เช่น การ GET/POST ข้อมูล ซึ่งถูกออกแบบมาให้ทำงานแบบ Async โดยเฉพาะ 
import time
=> นำเข้า time เพื่อใช้สำหรับจับเวลาตั้งแต่เริ่มจนจบโปรแกรม

2.ส่วนฟังก์ชันย่อยสำหรับดึงข้อมูล
async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()
=>async def จะให้ว่ามีการใส่คำว่า async ไว้หน้าฟังก์ชัน เป็นการบอก Python ว่านี่คือฟังก์ชันที่สามารถหยุดรอและสลับไปให้งานอื่นทำก่อนได้
=>async with session.get(url) คือทำการส่งคำสั่ง HTTP GET ไปที่ URL นั้นๆ การใช้ async with จะช่วยให้ระบบจัดการเปิดและปิดการเชื่อมต่อให้ โดยอัตโนมัติอย่างปลอดภัย
=> await response.text() จะเห็นว่ามีคำว่า await หมายความว่า ระหว่างที่กำลังรอเซิร์ฟเวอร์ตอบกลับข้อมูลมา โปรแกรมจะหยุดการทำงานของฟังก์ชันนี้ชั่วคราว แล้วคืนคิวให้ระบบ เพื่อนำเอาเวลาไปรันงานอื่นก่อน ถ้ารับข้อมูลเสร็จแล้ว ก็จะกลับมารันต่อ

3.ส่วนฟังก์ชันหลัก
async def get_data_async(num):
    url = "http://localhost:5000/api/data"   
    async with aiohttp.ClientSession() as session:
        # เตรียมงาน
        tasks = [fetch_url(session, url) for _ in range(num)]
        # สั่งรันพร้อมกัน
        await asyncio.gather(*tasks)
        
4.ส่วนการรันโปรแกรมและจับเวลา
=> สำหรับจัดการหลายๆ Request
=> aiohttp.ClientSession() เป็นการสร้างกล่องสำหรับการเชื่อมต่อ ซึ่งการสร้าง Session เดียวแล้วแชร์ให้ทุกๆ Request ใช้ร่วมกัน จะทำงานได้เร็วและประหยัดทรัพยากรเครื่องมากกว่าการสร้างการเชื่อมต่อใหม่ทุกครั้ง
=> tasks = [...] มีใช้ List Comprehension เพื่อสร้างรายการของงานจำนวน 10 งานเตรียมเอาไว้ ตามตัวแปร num
=> await asyncio.gather(*tasks) คำสั่ง gather จะเอางานทั้ง 10 งานที่เตรียมไว้ใน List นำเข้าไปรันใน Event Loop พร้อมๆ กัน และจะ awaitจนกว่าทั้ง 10 งานนั้นจะทำงานเสร็จสมบูรณ์ทั้งหมด จึงจะไปบรรทัดถัดไป

4.ส่วน
start = time.time()
asyncio.run(get_data_async(10))
end = time.time()
print(f"Time taken (Asyncio): {end - start:.4f} seconds")

=> time.time() เป็นคำสั่งเก็บเวลาเริ่มต้นและสิ้นสุดเอาไว้ลบกัน เพื่อหาว่าโปรแกรมใช้เวลาไปกี่วินาที
=> asyncio.run(...) ทำหน้าที่เป็นจุดเริ่มต้นของระบบ asyn มันจะไปสร้าง Event Loop ขึ้นมา รันฟังก์ชัน get_data_async(10) จนเสร็จ แล้วก็ทำลาย Event Loop ทิ้ง