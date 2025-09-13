มาถึง ก็พิมพ์
venv\Scripts\activate.bat
pip install -r requirements.txt

fastapi ใช้ยิง api สื่อสารกันระหว่าง front-end กับ back-end เวลาจะใช้ให้พิมพ์ว่า
(ก่อนใช้ก็เปิด venv ก่อน)
uvicorn main:app --reload
พอพิมพ์เสร็จมันจะมีลิงค์ให้คลิ๊ก ให้กด Ctrl+clickซ้าย
แล้วก็ให้พิมพ์ตรงด้านบนของเว็ปที่มันเด้งขึ้นมาว่า /docs มันก็จะเข้าหน้าที่มี get put pose ที่เราใส่ไว้ในmain

ตัว front เวลาจะเปิด ก็เปิด venv ก่อนแล้วก็ cd front\website แล้วก็ npm run dev