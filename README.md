# TheMuezzin
Variables זה קובץ אם כל המשתנים לדוגמה


יש את main.py שהוא עד קאפקא הוא מדליק את
    -Loader.py שהוא מקבל קישור לקובץ ומחזיר מערך של כל הקבצים 
 ואז הוא עובר על כל קובץ בנפרד ו
  -מוציא את המטא_דאטא (ExtractingMetadata)
 -הופך את הכול לjson
 -שולח הכול לקאפקא(Produce)

mastar.py שהוא מהקאפקא מעדכן את מונגו ואלסטיכ
-Consumer מאזין לקאפקא
-SendingToMongoAndElastic שהוא קובץ של כל מה שמונגו ואלסטיכ צריכים
הוא מגדיר את משקל הקובץ כid
שהוא שולח למונגו (MongoDAL.py) את הבינארי(STT.py) ואת הID
 ושולח לאלסטיכ(Elasticsearch_dal.py) את המטא-דאטא

update_text.py 
מושך מאלסטיכ את כל הIDS ואז עובר עליהם בלולאה 
שולף לפי ID את ה ה file_path ומוציא את המלל של הקובץ(STT)
ומעדכן באלסטיכ

main_3.py
מושך מאלסטיכ את כל הIDS ואז עובר עליהם בלולאה 
שולף לפי הID את הטקסט ומחשב רמת מסוכנות (Calculations.py)
האחוזים נחשבים לפי כמה מילים לא טובות יש מתוך כל המלל(כשהרשימה היותר מסוכנת נחשבת ככפול מילים)
ואם יש לו יותר מחצי מהמילים שברשימה מוסיף לו אחוזים לפי באיזה רשימה זה
(החישוב שם צריך תיקון לא הספקתי) 
אם יש לו אפ' מילה אחד מהרשימה הראשונה אז זה כבר מוגדר כמסוכן או אם יש לו יותר מ40 אחוז מסך המלל הכללי
רמת סיכון חושב שאם זה מוגדר כמסוכן ויש לו יותר מ40 אחוז או שיש לו יותר מ60 אחוז זה high
יותר מ10 זה medium
פחות מ10 הוא none



Variables is a file if all the variables for example

There is main.py which is up to Kafka it turns on
-Loader.py which receives a link to a file and returns an array of all the files
Then it goes through each file separately and
-Extracts the metadata (ExtractingMetadata)
-Converts everything to json
-Sends everything to Kafka (Produce)

mastar.py which is from Kafka updates Mongo and Elastic
-Consumer listens to Kafka
-SendingToMongoAndElastic which is a file of everything Mongo and Elastic need

It defines the file weight as id

It sends the binary (STT.py) and the ID to Mongo (MongoDAL.py)
and sends the metadata to Elastic (Elasticsearch_dal.py)

update_text.py
Pulls all the IDS from Elastic and then loops through them
Pulls out the file_path by ID and outputs the text of The file (STT)
and updates in Elastic

main_3.py
pulls all the IDS from Elastic and then loops through them
pulls out the text by ID and calculates the level of danger (Calculations.py)
The percentages are calculated according to how many bad words there are in the entire text (with the most dangerous list considered a duplicate of words)
and if it has more than half of the words in the list, it adds a percentage to it according to which list it is
(the calculation there needs to be corrected, I didn't have time)
If it has one word from the first list then it is already defined as dangerous or if it has more than 40 percent of the total text
Risk level I think if it is defined as dangerous and has more than 40 percent or has more than 60 percent it is high
More than 10 is medium
Less than 10 is none