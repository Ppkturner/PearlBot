# The Pearl song bot. Written by me, 07/10/17

import praw
import pdb
import os
import time # This is to prevent the comment limit (1 comment per second)
import re

from regex import findPer

# The wonderful author of this fabulous bot.
creatorString = "^(*I am a beautiful bot, and I was made by*) [^(*Gandalf_the_Gangsta.*)](https://www.reddit.com/user/Gandalf_the_Gangsta) ^(*Message them for more info, suggestions, or concerns. You can also*) [^(*opt-out*)](https://www.reddit.com/message/compose/?to=__ImPearlfecTron__&subject=Opt-out&message=stop) ^(*, but that would hurt my feelings.*)"

# URLs; may need to put these into an actual data structure at some point
itsOverIsntItURL 		= "https://www.youtube.com/watch?v=5T5rCSmduaY"
strongInTheRealWayURL 	= "https://www.youtube.com/watch?v=MIqnsNphhvU"
doItForHerURL 			= "https://www.youtube.com/watch?v=4yG8caPPY1Y"

# for the subreddit rate limit
# current working submission; finished replying, working on comments.
submissionQueue = []

# Completely finished submissions.
posts_replied_to = []

# completely finished comments.
comments_replied_to = []

# users that opted out :(
opted_out_users = []

# Each reply type is put into a pseudo switch statement
replyTypes = {	"ItsOver" 				: 0,
				"StrongInTheRealWay" 	: 1,
				"DoItForHer" 			: 2}
				
def replaceWithPearl (string):
	
	outputString = string
	
	print (outputString)
	
	if string.find('pur') != -1:
		
		if string.find('pur') + 3 >= len(string):
		
			outputString = outputString.replace('pur', '**pearl**')
		
		elif not string[string.find('pur') + 3] in ['a', 'e', 'i', 'o', 'u']:
	
			outputString = outputString.replace('pur', '**pearl**')
	
	if string.find('per') != -1:
		
		if string.find('per') + 3 >= len(string):
			
			outputString = outputString.replace('per', '**pearl**')
		
		elif not string[string.find('per') + 3] in ['a', 'e', 'i', 'o', 'u']:
	
			outputString = outputString.replace('per', '**pearl**')
	
	return outputString

# Function for submission replies for this bot 
def submissionReply( submission, replyType ):
	if replyType in replyTypes:
		if replyTypes[replyType] == 0:
			submission.reply("[Isn't it? Isn't it over?](" + 
			itsOverIsntItURL + 
			")\n *** \n" + 
			creatorString)
			
		elif replyTypes[replyType] == 1:
			submission.reply(	"[I can show you how to be strong, in the real way.](" +
								strongInTheRealWayURL +
								")\n *** \n" +
								creatorString)
			
		elif replyTypes[replyType] == 2:
			submission.reply(	"[You do it for her, and you would do it again.](" +
								doItForHerURL +
								")\n *** \n" +
								creatorString)
	
	print("Bot replying to: ", submission.title)

def commentReply (comment, replyType):
	if replyType in replyTypes:
		if replyTypes[replyType] == 0:
			comment.reply("[Isn't it? Isn't it over?](" + 
			itsOverIsntItURL + 
			")\n *** \n" + 
			creatorString)
			
		elif replyTypes[replyType] == 1:
			comment.reply(	"[I can show you how to be strong, in the real way.](" +
								strongInTheRealWayURL +
								")\n *** \n" +
								creatorString)
			
		elif replyTypes[replyType] == 2:
			comment.reply(	"[You do it for her, and you would do it again.](" +
								doItForHerURL +
								")\n *** \n" +
								creatorString)
	
	print("Bot replying to comment\n")

def runPearlBot_CommentsOnly():
	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []
	else:
		with open("comments_replied_to.txt", "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")
			comments_replied_to = list(filter(None, comments_replied_to))
	
	if not os.path.isfile("opted_out_users.txt"):
		opted_out_users = []
	else:
		with open("opted_out_users.txt", "r") as f:
			opted_out_users = f.read()
			opted_out_users = opted_out_users.split("\n")
			opted_out_users = list(filter(None, opted_out_users))
	
	# Getting a reddit instance
	reddit = praw.Reddit('PearlBot1')

	# Getting the Subreddit Instance
	# Test Subreddit: GandalfsBotTest
	
	subreddit = reddit.subreddit("stevenuniverse")
	
	for item in reddit.inbox.unread(limit=None):

		if isinstance(item, praw.models.Message):
			
			print( "Message " + item.id + " being processed...")
			
			if item.subject == "Opt-out" and item.body == 'stop':
			
				print("User " + item.author.name + " wants to opt out.")
				opted_out_users.append(item.author.name)
				item.mark_read()
	
	with open(r'opted_out_users.txt', 'w') as f:
		for user in opted_out_users:
			f.write(user + '\n')
	
	for comment in subreddit.stream.comments():
		if comment.submission in subreddit.hot(limit=25):
			
			print("It's a hot comment. Reply to it.\n")
			
			# printing out the submission the comment belongs to.
			print("Submission Title: ", comment.submission.title)
			print("Submission Text: ", comment.submission.selftext)
			print("Submission Score: ", comment.submission.score)
			print("__________________________\n")
			
			if comment.id not in comments_replied_to and comment.author != '__ImPearlfecTron__' and comment.author.name not in opted_out_users:
					try:
						if re.search("it's over", comment.body, re.IGNORECASE):
							print ("It's over, Isn't it?\n")
							print("\tComment Body: ", comment.body)
							print("\tComment ID: ", comment.id)
							print("\t__________________________\n")
							commentReply(comment, "ItsOver")
						elif re.search("its over", comment.body, re.IGNORECASE):
							print ("It's over, Isn't it?\n")
							print("\tComment Body: ", comment.body)
							print("\tComment ID: ", comment.id)
							print("\t__________________________\n")
							commentReply(comment, "ItsOver")
						elif re.search("in the real way", comment.body, re.IGNORECASE):
							print ("Strong in the Real Way!\n")
							print("\tComment Body: ", comment.body)
							print("\tComment ID: ", comment.id)
							print("\t__________________________\n")
							commentReply(comment, "StrongInTheRealWay")
						elif re.search("do it for her", comment.body, re.IGNORECASE):
							print("Do it for her!\n")
							print("\tComment Body: ", comment.body)
							print("\tComment ID: ", comment.id)
							print("\t__________________________\n")
							commentReply(comment, "DoItForHer")
						elif re.search('per', comment.body, re.IGNORECASE) or re.search('pur', comment.body, re.IGNORECASE):
							print("Replacing 'per' an 'pur' with 'pearl'\n")
							print("\tComment Body: ", comment.body)
							print("\tComment ID: ", comment.id)
							print("\t__________________________\n")
							
							output = findPer(comment.body)
							
							if output != comment.body:
								comment.reply(	output +
										"\n *** \n" +
										creatorString)
							
						comments_replied_to.append(comment.id)
						
						print("Writing processed comments...")

						with open("comments_replied_to.txt", "w") as f:
							for comment_id in comments_replied_to:
								f.write(comment_id + '\n')
					
					except praw.exceptions.APIException as e:
						with open("comments_replied_to.txt", "w") as f:
							for comment_id in comments_replied_to:
								f.write(comment_id + '\n')
						raise e
			else:
				print("Writing processed comments...")
				with open("comments_replied_to.txt", "w") as f:
					for comment_id in comments_replied_to:
						f.write(comment_id + '\n')

		
# Running of the code here
while(1):
	try:
		runPearlBot_CommentsOnly()
	except praw.exceptions.APIException as e:
		#if posting too much, catch here and wait.
		
		print(e.error_type, "\n")
		
		print (e.message + "\n")
		
		minutesToWait = [int(s) for s in e.message.split() if s.isdigit()]
		
		units = "minutes"
				
		if re.search("minutes", e.message, re.IGNORECASE):
			print ("Waiting " + str(minutesToWait[0]) + " " + units + "..." )
			time.sleep(60 * minutesToWait[0])
			
		elif re.search("minute", e.message, re.IGNORECASE):
			print ("Waiting " + str(minutesToWait[0]) + " " + units + "..." )
			time.sleep(60)
		
		elif re.search("seconds", e.message, re.IGNORECASE):
			units = "seconds"
			print ("Waiting " + str(minutesToWait[0]) + " " + units + "..." )
			time.sleep(minutesToWait[0])
		
		elif re.search("second", e.message, re.IGNORECASE):
			units = "second"
			print ("Waiting " + str(minutesToWait[0]) + " " + units + "..." )
			time.sleep(1)	
	
	#except praw.exceptions.ResponseException as e:
	#	print(e.error_type + '\n')
	#	print(e.message + '\n')
		
	except KeyboardInterrupt:
		print("Pearlbot shutting down...")
		break

'''
def runPearlBot():
	if not os.path.isfile("posts_replied_to.txt"):
			posts_replied_to = []
	else:
		with open("posts_replied_to.txt", "r") as f:
			posts_replied_to = f.read()
			posts_replied_to = posts_replied_to.split("\n")
			posts_replied_to = list(filter(None, posts_replied_to))

			
	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []
	else:
		with open("comments_replied_to.txt", "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")
			comments_replied_to = list(filter(None, comments_replied_to))
			
	# Getting a reddit instance
	reddit = praw.Reddit('PearlBot')

	# Getting the Subreddit Instance
	subreddit = reddit.subreddit("GandalfsBotTest")

	# A test for the hottest posts
	for submission in subreddit.hot(limit=25):		
		if submission.id not in posts_replied_to:
			
			# printing out the submission we jsut replied to.
			print("Title: ", submission.title)
			print("Text: ", submission.selftext)
			print("Score: ", submission.score)
			print("__________________________\n")
		
			# if we are in the submission queue, we are still using the submission, but have already finished replying to it if we want to.
			if submission.id not in submissionQueue:			
				
				# make the reply
				if re.search("it's over", submission.title, re.IGNORECASE):
					submissionReply(submission, "ItsOver")
				elif re.search("its over", submission.title, re.IGNORECASE):
					submissionReply(submission, "ItsOver")
				elif re.search("in the real way", submission.title, re.IGNORECASE):
					submissionReply(submission, "StrongInTheRealWay")
				elif re.search("do it for her", submission.title, re.IGNORECASE):
					submissionReply(submission, "DoItForHer")
				
				#limit of one post per second
				time.sleep(600)
				
				submissionQueue.append(submission.id)
				print("Submission ID " + submission.id + "has been replied to. Adding to queue...\n")
			
			for comment in submission.comments.list():
				if comment.id not in comments_replied_to:
					print("Comment Body: ", comment.body)
					print("Comment ID: ", comment.id)
					print("__________________________\n")
					
					
					if re.search("it's over", comment.body, re.IGNORECASE):
						commentReply(submission, "ItsOver")
					elif re.search("its over", comment.body, re.IGNORECASE):
						commentReply(comment, "ItsOver")
					elif re.search("in the real way", comment.body, re.IGNORECASE):
						commentReply(comment, "StrongInTheRealWay")
					elif re.search("do it for her", comment.body, re.IGNORECASE):
						commentReply(comment, "DoItForHer")
					
					
					comments_replied_to.append(comment.id)
			
			# Write all comments under a single submission when we're done with them
			with open("comments_replied_to.txt", "w") as f:
				for comment_id in comments_replied_to:
					f.write(comment_id + '\n')
					
				#time.sleep(600)
			
			posts_replied_to.append(submission.id)
			
			# Done with the submission, now removing from the queue.
			if submission.id in submissionQueue:
				submissionQueue.remove(submission.id)
			
	with open("posts_replied_to.txt", "w") as f: 
		for post_id in posts_replied_to:
			f.write(post_id + '\n')
'''