import praw
import json
import config

reddit = praw.Reddit(client_id = config.client['client_id'],
                     client_secret = config.client['client_secret'],
                     username = config.client['username'],
                     password = config.client['password'],
                     user_agent = config.client['user_agent'])

subreddit = reddit.subreddit(config.subreddit['name'])

limit = int(config.subreddit['limit'])

#sort by
comments = subreddit.top(limit=limit)
if config.subreddit['sortby'] == 'hot':
    print('hot')
    comments = subreddit.hot(limit=limit)
elif config.subreddit['sortby'] == 'new':
    print('new')
    comments = subreddit.new(limit=limit)
elif config.subreddit['sortby'] == 'controversial':
    print('controversial')
    comments = subreddit.controversial(limit=limit)
elif config.subreddit['sortby'] == 'rising':
    print('rising')
    comments = subreddit.rising(limit=limit)

notduplicate = True

try:
    file = open("reddit-comments.txt", "a+")
    file.close()

    read_file = open("reddit-comments.txt", "r")
    read_lines = read_file.readlines()
    read_file.close()

    file = open("reddit-comments.txt", "a+")

    for sub in comments:
        print(sub.title)
        #checking to not write duplicates
        notduplicate = True
        for line in read_lines:
            check_line = sub.title + "\n"
            if check_line == line:
                notduplicate = False
        if notduplicate == True:
            file.writelines(sub.title + "\n")

    file.close()
except:
    #there might be some comments that are skipped
    pass



