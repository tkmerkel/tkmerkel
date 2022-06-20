import pandas as pd
import praw
import datetime
import pytz
import smtplib
import ssl

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     password='',
                     user_agent='',
                     username='')

output_df = pd.DataFrame()

tz = pytz.timezone('America/New_York')

print('Sorting through DD from:')

for submission in reddit.subreddit('wallstreetbets').new(limit=1000):
    if submission.link_flair_text == 'DD':
        print(f'{submission.author}')
        utc_dt = datetime.datetime.utcfromtimestamp(submission.created).replace(tzinfo=pytz.utc) - datetime.timedelta(hours=9)
        timestamp = utc_dt.astimezone(tz)
        #timestamp = datetime.datetime.fromtimestamp(submission.created, tz)
        data = {'Date': [timestamp.strftime('%Y-%m-%d %H:%M:%S')],
                'timestamp': [timestamp],
                'Author': [submission.author],
                'Title': [submission.title],
                'Text': [submission.selftext],
                'Score': [submission.score],
                'Upvote Ratio': [submission.upvote_ratio],
                'URL': [submission.url]}

        new_data_df = pd.DataFrame(data, index=None)
        output_df = pd.concat([new_data_df, output_df], sort=True)
        output_df['Composite'] = output_df['Score'] * output_df['Upvote Ratio']
        output_df.sort_values(by=['Composite'], inplace=True, ascending=False)
        output_df = output_df.head(100)

date_1 = output_df['timestamp'].max() - datetime.timedelta(1)
output_df = output_df.loc[output_df['timestamp'] >= date_1]
output_df = output_df.head(10)

message = 'Subject: Your Daily DD From WSB!\n'
num_of_rows = len(output_df.index)

for i in range(num_of_rows):
    message +=  f"\nTitle: {output_df['Title'].iloc[i]} \
    \nAuthor: {output_df['Author'].iloc[i]} \
    \nDate: {output_df['Date'].iloc[i]} \
    \nScore: {output_df['Score'].iloc[i]} \
    \nUpvote Ratio: {output_df['Upvote Ratio'].iloc[i]} \
    \nLink: {output_df['URL'].iloc[i]} \
    \n\n{output_df['Text'].iloc[i]}\n\n"


port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = ""  # Enter sender address
receiver_email = ""  # Enter receiver address
message = message.encode('utf-8')
password = ''
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
