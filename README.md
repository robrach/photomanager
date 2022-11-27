# photomanager - REST API project in Django

EXAMPLES OF REQUESTS USING POSTMAN:

__1) POST new photo from local file__ 

![image](https://user-images.githubusercontent.com/76916353/204165517-538a7ecc-7bf8-45ab-a809-48e7bf135c23.png)

__2) POST new photo from external API__

![image](https://user-images.githubusercontent.com/76916353/204165522-efa2be06-f814-495f-b577-66c0a6bb90b9.png)

__3) POST new photo from JSON file__

![image](https://user-images.githubusercontent.com/76916353/204165643-84157ba7-1c03-49f1-b548-cfcb90307440.png)

__4) GET all photos__

![image](https://user-images.githubusercontent.com/76916353/204165655-64a9d075-dd2a-4030-b36e-03bfc5c868e9.png)

__5) GET photo with defined id=3__

![image](https://user-images.githubusercontent.com/76916353/204165674-54e588ef-0085-4503-b4dc-9dfb22c90400.png)

__6) PUT photo with defined id=3 (example of changing the title from "et qui rerum" into "NEW EDITED TITLE")__

![image](https://user-images.githubusercontent.com/76916353/204165699-bac77891-6cf3-4c5a-b65d-9060c23b5871.png)

__7) DELETE photo with defined id=3__

![image](https://user-images.githubusercontent.com/76916353/204165720-c7ca1d69-4ca9-4619-978a-e338cdb343c6.png)

__9) Tests (they are written in /photomanager/manager/tests.py)__

run in terminal from /photomanager: _python manage.py test_

![image](https://user-images.githubusercontent.com/76916353/204165745-05e0be77-58ed-44a3-8dde-40c8f0a5c245.png)

__10) CLI script for import photos from external API or from JSON file.__

run in terminal from /photomanager/manager: _python cli_script.py_

__10a) Import from external API:__
![image](https://user-images.githubusercontent.com/76916353/204165777-349f7edf-f19b-45ad-a075-5336aaab03c2.png)

__10b) Import from JSON file:__
![image](https://user-images.githubusercontent.com/76916353/204165795-7250d555-0d47-41d7-aa0e-13434377394d.png)









