"""
Name: Abuse Plugin for Sopel IRC bot.
Version: 0.1.0
Create Date: 01-31-2016 16:02:03 PST
Creator: Christopher Hubbard
Contact: guyverix@yahoo.com
Summary: Verbally abuse users from a list of predefined abuses.
"""

from sopel.module import commands
import random
import os.path
import string

@commands('abuse')
def abuse(bot, trigger):
  """
  We are going to verbally abuse people!  
  In channel: abuse <victim>  ( You will be the abuser FYI )
  Or private message: abuse <victim> <#channel> ( A random user will abuse them for you. )
  """

  if not os.path.isfile(bot.config.abuse.abuse_file):
    bot.say('There is no fucking abuse file found!  Check your configuration dipshit.')
    return

  file=bot.config.abuse.abuse_file
  try:
    abuses=open(str(file)).read().splitlines()
  except IOError:
    bot.say('Cannot find or read the fucking abuse file: ' + file)
    return
  except TypeError:
    bot.say('Something is messed up in the config and I could not get a list' + file)
    return

  randomAbuse=random.choice(abuses)
  # bot.say('DEBUG: ' + randomAbuse)

  # We now have our abuse that we are going to use.  NOW we have to format our abuse to make sense.
  # If an arg was given, now is the time to see if it is a user in the channel.
  # if so we are going to abuse them in the channel.
  # However if we cannot parse, or the user does not exist default
  # back to abusing the person who screwed up!  Heheheh!
  # If there are no args, and said in a channel, trigger.sender is the CHANNEL, and trigger.nick is the sender..
  # trigger.group(2) is all args from the user!

  if trigger.group(2):
    #bot.msg(trigger.nick, 'DEBUG: '+ trigger.group(2))
    if trigger.sender.startswith('#'):
      users = bot.privileges[trigger.sender]
      #bot.msg(trigger.nick, 'DEBUG: building dictionary of users in the channel')
      for nick in users:
        #bot.msg(trigger.nick, 'DEBUG: nick '+ nick + " trigger.group(2) is " + trigger.group(2))
        if nick == trigger.group(2):
          #bot.msg(trigger.nick, "DEBUG found user " + nick)
          # bot.say('DEBUG: ' + finalRandomAbuse)
          finalRandomAbuse = string.replace(randomAbuse, 'VICTIM', nick)
          bot.say(trigger.nick + " " + finalRandomAbuse)
          return

      # It appears we did NOT find a match, so abuse the person who screwed up!
      bot.msg(trigger.nick, "We could not match " + trigger.group(2) + " to a userid in " + trigger.sender)
      # bot.msg(trigger.nick, "We could not match " + trigger.group(2) + " to a userid in " + trigger.sender)
      # bot.say("DEBUG found user " + nick)
      # bot.say('DEBUG: ' + finalRandomAbuse)
      
      finalRandomAbuse = string.replace(randomAbuse, 'VICTIM', trigger.nick)
      bot.say('Sopel ' + finalRandomAbuse)

    else:
      #bot.msg(trigger.nick, "DEBUG: I have no idea what channel to abuse the person on")
      #bot.msg(trigger.nick, "DEBUG: " + trigger.sender +" " + trigger.group(2))
      channelDest=trigger.group(2).split()[1]
      if channelDest.startswith('#'):
        users = bot.privileges[channelDest]
        # bot.msg(trigger.nick, channelDest + " looks like a valid channel")
        victim = trigger.group(2).split()[0]
        randAbuser = random.choice(users.keys())
        finalRandomAbuse = string.replace(randomAbuse, 'VICTIM', victim)
        bot.msg(channelDest, randAbuser + " " + finalRandomAbuse)
      else:
        bot.msg(trigger.nick, "I cannot figure out where to abuse the victim at")
  else:
    # bot.say('DEBUG: getting user list for channel')
    users = bot.privileges[trigger.sender]
    # test=str(users)
    # bot.say('DEBUG:' + test)
    victim = random.choice(users.keys())
    randAbuser = random.choice(users.keys())
    finalRandomAbuse = string.replace(randomAbuse, 'VICTIM', victim)
    # Random acts of violence from randAbuser to victim
    bot.say(randAbuser + " " + finalRandomAbuse)

@commands('add_abuse')
def add_abuse(bot, trigger):
  """
  Append a given string to the abuse file.
  It is critical that you use the keyword VICTIM where the userid will be shown.
  Remember to NOT use complete sentences.  A userid will be appended to the front of the abuse.
  EXAMPLE: hits their VICTIM over the head with a trout!
  """

  if not os.path.isfile(bot.config.abuse.abuse_file):
    bot.say('There is no abuse file found.  Check configuration.')
    return

  file=bot.config.abuse.abuse_file
  bot.say('Attempting to add ' + trigger.group(2) + ' to the abuse file')

  try:
    abuse=open(str(file),'a+')
    abuse.write(trigger.group(2) + '\n')
    abuse.close()
  except IOError:
    bot.say('Cannot find or read abuse file: ' + file)
    return
  bot.say('Added ' + trigger.group(2) + ' to the abuse file')

