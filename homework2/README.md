For homework 2, I used ChatGPT to help me generate the following:
- base.html black bars and layout
    - Lines 6 - 26 OpenAI. (2023). ChatGPT (Mar 14 version). [Online Chat Interface].
- helped on polishing a view function such as seat_booking_view 
    - Lines 31 - 53 OpenAI. (2023). ChatGPT (Mar 14 version). [Online Chat Interface].

Setup Instructions
Clone the Repository

bash
Copy
git clone https://github.com/YourUsername/YourRepoName.git
cd YourRepoName
Create and Activate a Virtual Environment

bash
Copy
python3 -m venv homework2
source homework2/bin/activate  
# or: myenv\Scripts\activate (Windows)
Install Dependencies

bash
Copy
pip install -r requirements.txt
If you don’t have a requirements.txt, you can install manually:

bash
Copy
pip install django djangorestframework
Set Up Environment Variables (Optional)

Apply Migrations

bash
Copy
python manage.py makemigrations
python manage.py migrate

bash
Copy
python manage.py createsuperuser
Running the Server
Start the Django development server:

bash
Copy
python manage.py runserver 0.0.0.0:3000