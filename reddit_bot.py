import praw
import config
import time
import os

def bot_login():
    print "Loggin in, yeh"
    r = praw.Reddit(username = config.username,
                            password = config.password,
                            client_id = config.client_id,
                            client_secret = config.client_secret,
                            user_agent = "karl pilkingbot v0.1")
    print "Alrite, logged in"

    return r

def run_bot(r, comm_replies):
    print "Fetching 50 comments"

    for comment in r.subreddit('NewBootGoofin').comments(limit=50):
        if "glass houses" in comment.body and comment.id not in comm_replies and not comment.author != r.user.me():
            print "string with \"glass houses\" found in comment " + comment.id
            comment.reply("People who live in glass houses hafta answer tha door.")
            print "Replied to comment " + comment.id

            comm_replies.append(comment.id)

            with open ("comm_replies.txt", "a") as f:
                f.write(comment.id + "\n")

    print "Resting for 10 secs"
    time.sleep(10)

def get_saved_comments():
    if not os.path.isfile("comm_replies.txt"):
        comm_replies = []
    else:
        with open("comm_replies.txt", "r") as f:
            comm_replies = f.read()
            comm_replies = comm_replies.split("\n")
            comm_replies = filter(None, comm_replies)

    return comm_replies

r = bot_login()
comm_replies = get_saved_comments()
print comm_replies

while True:
    run_bot(r, comm_replies)
