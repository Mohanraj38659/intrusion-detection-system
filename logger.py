import datetime

class Logger:
    @staticmethod
    def log(event):
        with open("intrusion_log.txt", "a") as log_file:
            log_file.write(f"{datetime.datetime.now()} - {event}\n")
        print(event)  # Print to console as well
