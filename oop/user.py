class User:
    def __init__(self, user_email, user_name, password, current_job_title):
        self.email = user_email
        self.name = user_name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"user_name: {self.name}, user_email: {self.email}, user_job_title: {self.current_job_title}")

