# 03/08/2021
Shopee มีระบบกันแล้ว ต้องเลื่อนต่อจิ๊กซอว์ เอาไปพัฒนาต่อกันเอาเองนะครับ

# วิธีใช้งาน
- ใช้ chrome เท่านั้น 
    - แล้วไปเช็คเวอร์ที่ chrome://settings/help
    - แล้วกดโหลด ตามเวอร์ชั่น Chrome [Webdriver](https://chromedriver.chromium.org/downloads)
    - แล้วมาวางในโฟนเดอร์เดียวกับไฟล์บอท
- ต้องตั้งที่อยู่ที่จะจัดส่งเป็นที่อยู่เริ่มต้น เพราะไม่มีระบบเลือกให้
- เพิ่มบัตรเครดิตให้เรียบร้อย ต้องมีใบเดียว ถ้ามีใบอื่นลบให้หมดเหลือแค่ใบที่จะใช้
- ความเร็วขึ้นอยู่กับคอมและเน็ต
- ยังไม่รองรับสินค้าที่มีปุ่มให้ลือก เช่น เลือกสี เลือกขนาด
- ยังไม่รองรับของที่ส่งมาจากต่างประเทศ ไม่สามารถกดเลือกวิธีจ่ายเงินได้


# วิธีตั้งค่าไฟล์ config
- username password แนะนำอย่าใช้เป็นเบอร์เพราะต้องรอ OTP
- Url ใส่ลิงค์ของที่จะซื้อ
- DelayLogin สำหรับไว้เผื่อเวลาใส่ OTP ถ้าไม่ติด OTP ก็ใส่ 0 เลย เวลาเปลี่ยนได้เป็นวินาที
- TEST False ปิดการเทส True เปิดการเทส การเทสจะทำทุกอย่างแต่จะไม่กดจ่ายเงิน
