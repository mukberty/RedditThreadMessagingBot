import praw
import subprocess

reddit=praw.Reddit(client_id='',
                   client_secret='',password='',
                   user_agent='',username='')

z= subprocess.check_output(['python3', 'content.py'])
# can also be a string 

url = "commentrthreadurl"
submission = reddit.submission(url=url)
for top_level_comment in submission.comments:
    a = top_level_comment.author
    b =  f'{a}'
    reddit.redditor(b).message('Subject', z)
    
print('Done!')
