from apscheduler.schedulers.blocking import BlockingScheduler
from app.parser.codeforces_parser import update_problems
from app.database import Base, engine

def main():
    Base.metadata.create_all(bind=engine)
    scheduler = BlockingScheduler()
    scheduler.add_job(update_problems, "interval", hours=1)
    update_problems()
    scheduler.start()

if __name__ == "__main__":
    main()
